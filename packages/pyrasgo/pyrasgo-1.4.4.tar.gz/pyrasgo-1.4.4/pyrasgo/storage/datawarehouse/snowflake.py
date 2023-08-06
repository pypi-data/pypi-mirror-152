import logging
from typing import Optional

import pandas as pd
from snowflake import connector as snowflake

from pyrasgo.api.session import Session
from pyrasgo.storage.dataframe import utils as dfutils
from pyrasgo.storage.datawarehouse.base import DataWarehouse, DataWarehouseSession
from pyrasgo.utils import naming


class SnowflakeDataWarehouse(DataWarehouse, Session, metaclass=DataWarehouseSession):
    def __init__(self):
        username = self.profile.get("dwUsername", self.profile.get("snowUsername"))
        if username is None:
            raise EnvironmentError("Your user is missing credentials, please contact Rasgo support.")
        self.username = username
        self.password = self.profile.get("dwPassword", self.profile.get("snowPassword"))
        self.role = self.profile.get("dwRole", self.profile.get("snowRole"))

        organization = self.profile.get("organization")
        self.account = organization.get("account")
        self.database = organization.get("database")
        self.schema = organization.get("schema")
        self.warehouse = organization.get("warehouse")
        if self.role is None:
            self.role = organization.get("role")

    # Temporarily change these to default role
    # Deprecate these when we remove the v1 publish methods that reference them
    @property
    def publisher_role(self) -> str:
        return self.role

    @property
    def reader_role(self) -> str:
        return self.role

    @property
    def user_connection(self) -> snowflake.SnowflakeConnection:
        return snowflake.connect(**self.user_credentials)

    @property
    def user_credentials(self) -> dict:
        return {
            "user": self.username,
            "password": self.password,
            "account": self.account,
            "database": self.database,
            "schema": self.schema,
            "warehouse": self.warehouse,
            "role": self.role,
            "application": "rasgo",
            "session_parameters": {"QUERY_TAG": "rasgo_python_sdk"},
        }

    def execute_query(self, query: str, params: Optional[dict] = None):
        """
        Execute a query on the [cloud] data platform.

        :param query: String to be executed on the data platform
        :param params: Optional parameters
        :return:
        """
        return self.user_connection.cursor().execute(query, params)

    def query_into_dict(self, query: str, params: Optional[dict] = None) -> pd.DataFrame:
        """
        Execute a query on the [cloud] data platform.

        :param query: String to be executed on the data platform
        :param params: Optional parameters
        :return:
        """
        return self.user_connection.cursor(snowflake.DictCursor).execute(query, params).fetchall()

    def query_into_dataframe(self, query: str, params: Optional[dict] = None) -> pd.DataFrame:
        """
        Execute a query on the [cloud] data platform.

        :param query: String to be executed on the data platform
        :param params: Optional parameters
        :return:
        """
        cur = self.user_connection.cursor()
        cur.execute(query, params)
        return cur.fetch_pandas_all()

    def get_source_table(
        self,
        table_name: str,
        database: Optional[str] = None,
        schema: Optional[str] = None,
        record_limit: Optional[int] = None,
    ) -> pd.DataFrame:
        if record_limit is None:
            logging.info(f"Loading all rows from {table_name}...")
        database = database or self.database
        schema = schema or self.schema
        result_set = self.execute_query(
            f"SELECT * FROM {database}.{schema}.{naming._quote_restricted_keywords(table_name)} "
            f"{f'LIMIT {record_limit}' if record_limit else ''}"
        )
        return pd.DataFrame.from_records(
            data=iter(result_set),
            columns=[x[0] for x in result_set.description],
        )

    def get_source_tables(self, database: Optional[str] = None, schema: Optional[str] = None):
        database = database or self.database
        schema = schema or self.schema
        filters = f"WHERE TABLE_SCHEMA='{schema}'"
        result_set = self.execute_query(
            f"SELECT TABLE_NAME, TABLE_CATALOG||'.'||TABLE_SCHEMA||'.'||TABLE_NAME "
            f"AS FQTN, ROW_COUNT, TABLE_OWNER, CREATED, LAST_ALTERED "
            f"FROM {database}.INFORMATION_SCHEMA.TABLES {filters}"
        )
        return pd.DataFrame.from_records(iter(result_set), columns=[x[0] for x in result_set.description])

    def get_source_columns(
        self,
        table: Optional[str] = None,
        database: Optional[str] = None,
        schema: Optional[str] = None,
        data_type: Optional[str] = None,
    ):
        database = database or self.database
        schema = schema or self.schema
        filters = f"WHERE TABLE_SCHEMA='{schema}'"
        filters += f" AND TABLE_NAME='{table}'" if table else ""
        filters += f" AND DATA_TYPE='{data_type}'" if data_type else ""
        result_set = self.execute_query(
            f"SELECT COLUMN_NAME, DATA_TYPE, TABLE_NAME, TABLE_CATALOG||'.'||TABLE_SCHEMA||'.'||TABLE_NAME AS FQTN "
            f"FROM {database}.INFORMATION_SCHEMA.COLUMNS {filters}"
        )
        return pd.DataFrame.from_records(iter(result_set), columns=[x[0] for x in result_set.description])

    def grant_table_ownership(
        self,
        table: str,
        role: str,
        database: Optional[str] = None,
        schema: Optional[str] = None,
    ):
        """
        Grants ownership of a table or FQTN to specified role
        Note: If user role is not the table owner, this will fail
        """
        database = database or self.database
        schema = schema or self.schema
        self.execute_query(
            f"GRANT OWNERSHIP ON {database}.{schema}.{naming._quote_restricted_keywords(table)} "
            f"TO ROLE {role} REVOKE CURRENT GRANTS;"
        )

    def grant_table_access(self, table: str, role: str, database: Optional[str] = None, schema: Optional[str] = None):
        """
        Grants select privilege on a table or FQTN to specified role
        Note: If user role does not have access with grant option, this will fail
        """
        database = database or self.database
        schema = schema or self.schema
        self.execute_query(
            f"GRANT SELECT ON {database}.{schema}.{naming._quote_restricted_keywords(table)} TO ROLE {role};"
        )

    def clone_table(self, existing_table: str, new_table: str, overwrite: bool = False):
        """
        Clones a table or FQTN
        Note: if user role doesn't have select & create access to db + schema + table this will fail
        """
        if overwrite:
            self.execute_query(
                f"CREATE OR REPLACE TABLE {naming._quote_restricted_keywords(new_table)} "
                f"CLONE {naming._quote_restricted_keywords(existing_table)};"
            )
        else:
            self.execute_query(
                f"CREATE TABLE {naming._quote_restricted_keywords(new_table)} "
                f"CLONE {naming._quote_restricted_keywords(existing_table)};"
            )

    def append_to_table(self, from_table: str, into_table: str):
        """
        Inserts data from a table or FTQN into another table or FQTN
        Note: if user role doesn't have select & modify access to db + schema + table this will fail
        """
        self.execute_query(
            f"INSERT INTO {naming._quote_restricted_keywords(into_table)} "
            f"SELECT * FROM {naming._quote_restricted_keywords(from_table)};"
        )

    def _make_table_metadata(self, table: str):
        if table.count(".") > 0:
            table = table.split(".")[-1]
        metadata = {
            "database": self.database,
            "schema": self.schema,
            "table": table,
        }
        return metadata

    def _write_dataframe_to_table(
        self,
        df: pd.DataFrame,
        table_name: str,
        append: bool = False,
    ):
        """
        Note: we will allow users to select from other database, but only to write into org default database
        """
        from snowflake.connector.pandas_tools import write_pandas

        dfutils.cleanse_sql_dataframe(df)
        write_pandas(
            conn=self.user_connection,
            df=df,
            table_name=naming.cleanse_sql_name(table_name),
            quote_identifiers=False,
        )

    def get_schema(
        self,
        fqtn: str,
    ) -> list:
        """
        Return the schema of a table or view

        Params:
        `fqtn`: str:
            Fully-qualified table name (database.schema.table)
        """
        desc_sql = f"DESC TABLE {fqtn}"
        query_response = self.query_into_dict(desc_sql)
        return [(x['name'], x['type']) for x in query_response]
