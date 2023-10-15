import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.test_file_path = "test_file.json"
        open(self.test_file_path, "w").close()

        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.test_file_path

        self.base_model_instance = BaseModel()
        self.user_instance = User()

    def tearDown(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_save_and_reload(self):
        self.base_model_instance.save()
        self.storage.reload()
        loaded_objects = self.storage.all()
        loaded_model = loaded_objects.get(
                "BaseModel.{}".format(self.base_model_instance.id))
        self.assertIsInstance(loaded_model, BaseModel)
        self.assertEqual(loaded_model.id, self.base_model_instance.id)

        self.user_instance.save()
        self.storage.reload()
        loaded_objects = self.storage.all()
        loaded_user = loaded_objects.get(
                "User.{}".format(self.user_instance.id))
        self.assertIsInstance(loaded_user, User)
        self.assertEqual(loaded_user.id, self.user_instance.id)

    def test_new_method(self):
        model = BaseModel()

        self.storage.new(model)

        self.assertIn("BaseModel.{}".format(model.id),
                      self.storage.all())

    def test_all_method(self):
        model = BaseModel()

        self.storage.new(model)

        all_objects = self.storage.all()

        self.assertIsInstance(all_objects, dict)

        self.assertIn("BaseModel.{}".format(model.id), all_objects)

    def test_save_method(self):
        model = BaseModel()

        self.storage.new(model)

        self.storage.save()

        with open(self.test_file_path, "r") as f:
            data = json.load(f)

        self.assertIn("BaseModel.{}".format(model.id), data)

    def test_reload_method_file_exists(self):
        os.remove(self.test_file_path)
        self.storage.reload()

        self.assertGreater(len(self.storage.all()), 0)


if __name__ == "__main__":
    unittest.main()
