import unittest
from datetime import datetime, timedelta
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_attributes(self):
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_init_with_kwargs(self):
        instance_dict = {
                'id': '123',
                'created_at': '2023-10-12T10:00:00.000000',
                'updated_at': '2023-10-12T10:30:00.000000',
                'name': 'Example',
                'age': 25
        }
        instance = BaseModel(**instance_dict)

        self.assertEqual(instance.id, '123')
        self.assertEqual(instance.name, 'Example')
        self.assertEqual(instance.age, 25)

        self.assertEqual(instance.created_at.year, 2023)
        self.assertEqual(instance.created_at.month, 10)
        self.assertEqual(instance.created_at.day, 12)
        self.assertEqual(instance.created_at.hour, 10)
        self.assertEqual(instance.created_at.minute, 0)
        self.assertEqual(instance.created_at.second, 0)
        self.assertEqual(instance.created_at.microsecond, 0)

        self.assertEqual(instance.updated_at.year, 2023)
        self.assertEqual(instance.updated_at.month, 10)
        self.assertEqual(instance.updated_at.day, 12)
        self.assertEqual(instance.updated_at.hour, 10)
        self.assertEqual(instance.updated_at.minute, 30)
        self.assertEqual(instance.updated_at.second, 0)
        self.assertEqual(instance.updated_at.microsecond, 0)

    def test_init_without_kwargs(self):
        instance = BaseModel()

        self.assertIsNotNone(instance.id)
        self.assertIsInstance(instance.created_at, datetime)

    def test_str_method(self):
        expected_output = (
                f"[BaseModel] ({self.base_model.id}) "
                f"{self.base_model.__dict__}"
        )
        self.assertEqual(str(self.base_model), expected_output)

    def test_save_method(self):
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        expected_dict = {
                'id': self.base_model.id,
                '__class__': 'BaseModel',
                'created_at': self.base_model.created_at.isoformat(),
                'updated_at': self.base_model.updated_at.isoformat()
        }
        self.assertDictEqual(self.base_model.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
