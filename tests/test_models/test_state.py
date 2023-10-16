import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_statr_initial_vale(self):
        self.assertEqual(self.state.name, "")

    def test_inheritance_from_base_model(self):
        self.assertTrue(issubclass(State, BaseModel))

    def test_attributes_inherited_from_base_model(self):
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_attributes_strings(self):
        self.assertIsInstance(self.state.name, str)


if __name__ == "__main__":
    unittest.main()
