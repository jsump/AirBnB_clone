import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_user_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_attributes_update(self):
        user = User()
        user.email = "test@example.com"
        user.password = "password123abc"
        user.first_name = "Jane"
        user.last_name = "Smith"

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123abc")
        self.assertEqual(user.first_name, "Jane")
        self.assertEqual(user.last_name, "Smith")


if __name__ == "__main__":
    unittest.main()
