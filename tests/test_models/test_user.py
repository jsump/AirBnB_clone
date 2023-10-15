import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_email_initial_value(self):
        self.assertEqual(self.user.email, "")

    def test_password_initial_value(self):
        self.assertEqual(self.user.password, "")

    def test_first_name_initial_value(self):
        self.assertEqual(self.user.first_name, "")
    
    def test_last_name_initial_value(self):
        self.assertEqual(self.user.last_name, "")

    def test_inheritance_from_base_model(self):
        self.assertTrue(issubclass(User, BaseModel))
       
    def test_user_attributes_inherited_from_base_model(self):
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))


    def test_user_attributes_are_strings(self):
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)


if __name__ == "__main__":
    unittest.main()
