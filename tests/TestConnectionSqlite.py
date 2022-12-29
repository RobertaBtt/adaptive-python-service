import unittest
from app.connection.ConnectionSQLite import ConnectionSQLite
from app.DependencyContainer import DependencyContainer


class TestConnectionSqlite(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.app = DependencyContainer()
        self.config = self.app.config  # ConfigurationCONF
        self.sql = ConnectionSQLite(self.config, "CONNECTION_SQLITE_TEST")

    def test_connection_works(self):
        self.assertTrue(self.sql.connect())


if __name__ == '__main__':
    unittest.main()
