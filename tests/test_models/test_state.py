import unittest
from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_attributes(self):
        self.assertEqual(self.state.name, "")

    def test_string_representation(self):
        self.state.name = "Texas"
        self.assertEqual(str(self.state), "State: Texas")


if __name__ == "__main__":
    unittest.main()
