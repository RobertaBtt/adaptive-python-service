import sqlite3
from app.connection.ConnectionAbstract import ConnectionAbstract
from app.configuration.ConfigurationAbstract import ConfigurationAbstract


class ConnectionSQLite(ConnectionAbstract):

    def __init__(self, config: ConfigurationAbstract, section: str):
        self.db_url = config().get(section, "path")

    def get_connection(self) -> ConnectionAbstract:
        try:
            return sqlite3.connect(self.db_url)
        except Exception as e:
            raise e

