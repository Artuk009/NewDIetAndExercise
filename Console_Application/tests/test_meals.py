import unittest
from unittest.mock import patch
from diet_db import meals as m


class MyTestCase(unittest.TestCase):
    @patch('builtins.input', return_value="1")
    def test_set_breakfast(self, mock_input):
        self.assertEqual(m.set_meal(), "Breakfast")

    @patch('builtins.input', return_value="2")
    def test_set_lunch(self, mock_input):
        self.assertEqual(m.set_meal(), "Lunch")

    @patch('builtins.input', return_value="3")
    def test_set_dinner(self, mock_input):
        self.assertEqual(m.set_meal(), "Dinner")

    @patch('builtins.input', return_value="4")
    def test_set_snack(self, mock_input):
        self.assertEqual(m.set_meal(), "Post-Workout")


if __name__ == '__main__':
    unittest.main()
