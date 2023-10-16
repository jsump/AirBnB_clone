import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_aminity_initial_value(self):
        self.assertEqual(self.amenity.name, "")

    def test_inheritance_from_base_model(self):
        self.assertTrue(issubclass(Amenity, BaseModel))
    
    def test_attributes_inherited_from_base_model(self):
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_attributes_strings(self):
        self.assertIsInstance(self.amenity.name, str)


if __name__ == "__main__":
    unittest.main()
