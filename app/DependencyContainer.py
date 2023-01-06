from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton
from app.configuration.ConfigurationCONF import ConfigurationCONF
from app.configuration.ConfigurationENV import ConfigurationENV
from app.connection.ConnectionSQLite import ConnectionSQLite
from app.repository.RepositoryMusic import RepositoryMusic
from app.service.ServiceMusic import ServiceMusic
from app.serialize.SerializeFactory import SerializeFactory


class DependencyContainer(DeclarativeContainer):

    config_conf = Singleton(ConfigurationCONF)
    config_env = Singleton(ConfigurationENV)
    connection = Singleton(ConnectionSQLite, config_conf, "CONNECTION_SQLITE")
    music_repository = Singleton(RepositoryMusic, connection)
    service = Singleton(ServiceMusic, config_conf, music_repository)
    serialize_factory = Singleton(SerializeFactory)


