import unittest
from app.DependencyContainer import DependencyContainer
from app.serialize.SerializeJSON import SerializeJSON


class TestSerialize(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.app = DependencyContainer()
        self.config = self.app.config_env()

    def test_get_current_serializer(self):
        current_format = self.config.get("INPUT_FORMAT")
        self.assertEqual(current_format, "JSON")

    def test_instance_serializer(self):
        current_format = self.config.get("INPUT_FORMAT")
        serializer = self.app.serialize_factory()
        self.assertEqual(SerializeJSON, serializer.get_serializer(current_format))
        self.assertEqual(type(serializer.get_serializer(current_format)()), type(SerializeJSON()))

    def test_serialize_json(self):
        current_format = self.config.get("INPUT_FORMAT")
        serializer = self.app.serialize_factory()

        self.assertEqual(SerializeJSON, serializer.get_serializer(current_format))
        self.assertEqual(type(serializer.get_serializer(current_format)()), type(SerializeJSON()))


if __name__ == '__main__':
    unittest.main()
