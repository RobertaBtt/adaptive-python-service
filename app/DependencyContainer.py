from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton
from app.configuration.ConfigurationCONF import ConfigurationCONF
from app.connection.ConnectionSQLite import ConnectionSQLite
from app.repository.RepositoryMusic import RepositoryMusic
from app.service.ServiceMusic import ServiceMusic


class DependencyContainer(DeclarativeContainer):

    config = Singleton(ConfigurationCONF)
    connection = Singleton(ConnectionSQLite, config, "CONNECTION_SQLITE")
    music_repository = Singleton(RepositoryMusic, connection)
    service = Singleton(ServiceMusic, config, music_repository)

