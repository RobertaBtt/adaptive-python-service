import sqlite3
from app.connection.ConnectionAbstract import ConnectionAbstract
from app.configuration.ConfigurationAbstract import ConfigurationAbstract


class ConnectionSQLite(ConnectionAbstract):

    def __init__(self, config: ConfigurationAbstract, section: str):
        self.db_url = config().get(section, "path")
        self.sqlite_connection = None

    def connect(self) -> bool:
        try:
            self.sqlite_connection = sqlite3.connect(self.db_url)
            return True
        except Exception as e:
            print(e)
            return False

    def disconnect(self) -> bool:
        pass
