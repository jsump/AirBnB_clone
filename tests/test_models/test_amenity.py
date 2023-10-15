import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_attributes(self):
        self.assertEqual(self.amenity.name, "")

    def test_string_representation(self):
        self.amenity.name = "Water"
        self.assertEqual(str(self.amenity), "Amenity: Water")


if __name__ == "__main__":
    unittest.main()
