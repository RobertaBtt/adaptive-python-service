from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton
from app.configuration.ConfigurationCONF import ConfigurationCONF


class DependencyContainer(DeclarativeContainer):
    config = Singleton(ConfigurationCONF)

    try:
        print(config().get("APP", "name"))
    except KeyError as ex:
        print(ex)

