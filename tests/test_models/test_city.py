import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()
        self.city.name = ""

    def test_attributes(self):
        self.assertEqual(self.city.name, "")

    def test_string_representation(self):
        expected_string = "City: "
        self.assertEqual(str(self.city), expected_string)


if __name__ == "__main__":
    unittest.main()
