from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton
from app.configuration.ConfigurationCONF import ConfigurationCONF
from app.connection.ConnectionSQLite import ConnectionSQLite
from app.repository.RepositoryMusic import RepositoryMusic


class DependencyContainer(DeclarativeContainer):

    config = Singleton(ConfigurationCONF)
    connection = Singleton(ConnectionSQLite, config, "CONNECTION_SQLITE")
    music = Singleton(RepositoryMusic, connection)

