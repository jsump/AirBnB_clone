import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.place = Place()

    def test_attributes(self):
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_string_representaion(self):
        self.place.name = "New Place"
        self.place.description = "It's a new joint"
        self.place.number_rooms = 2
        self.place.number_bathrooms = 1
        self.place.max_guest = 4
        self.place.price_by_night = 100
        self.place.latitude = 23.8798
        self.place.longitude = 3.97556
        self.place.amenity_ids = ["1", "2", "3"]

        expected_string = ("Place: Name - New Place, "
                           "Description - It's a new joint, "
                           "Number of rooms - 2, "
                           "Number of bathrooms - 1, "
                           "Max Guests - 4, "
                           "Price per night - 100, "
                           "Latitude - 23.8798, "
                           "Longitude - 3.97556, "
                           "Amenity IDs - ['1', '2', '3']")
        self.assertEqual(str(self.place), expected_string)


if __name__ == "__main__":
    unittest.main()
