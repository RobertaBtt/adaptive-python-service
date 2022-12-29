from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton
from app.configuration.ConfigurationCONF import ConfigurationCONF
from app.connection.ConnectionSQLite import ConnectionSQLite


class DependencyContainer(DeclarativeContainer):

    config = Singleton(ConfigurationCONF)
    sql = Singleton(ConnectionSQLite, config, "CONNECTION_SQLITE")

    try:
        print(config().get("APP", "name"))
    except KeyError as ex:
        print(ex)

