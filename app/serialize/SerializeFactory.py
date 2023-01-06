from . import SerializeJSON
from . import SerializeYAML
from . import SerializeXML

# This class is the Abstract Factory for the serializer,
# because the input of the service may differ in the format,
# and this application is ready to adapt to different formats.
#
# Registry / Service container of the Classes that
# can adapt to different data sources or services (XML, JSON, YAML, CSV ecc)


SERVICE_ADAPTERS = dict()


def register():
    """Register a Service Class that can adapt to different data sources"""
    SERVICE_ADAPTERS["JSON"] = SerializeJSON.SerializeJSON
    SERVICE_ADAPTERS["XML"] = SerializeXML.SerializeXML
    SERVICE_ADAPTERS["YAML"] = SerializeYAML.SerializeYAML


class SerializeFactory:

    def __init__(self):
        register()

    def get_service(self, service_type):
        return SERVICE_ADAPTERS[service_type]
