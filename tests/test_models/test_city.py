import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_city_initial_value(self):
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_inheritance_from_base_model(self):
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes_inherited_from_base_model(self):
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_attributes_atrings(self):
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)


if __name__ == "__main__":
    unittest.main()
