from app.repository.RepositoryAbstract import RepositoryAbstract
from app.connection.ConnectionAbstract import ConnectionAbstract


class RepositoryMusic(RepositoryAbstract):

    def __init__(self, connection: ConnectionAbstract):
        self.sql = connection

    def create(self):
        pass

    def read(self, query: str):
        with self.sql.get_connection() as connection:
            cursor = connection.cursor()
            return cursor.execute(query)

    def update(self):
        pass

    def delete(self):
        pass

