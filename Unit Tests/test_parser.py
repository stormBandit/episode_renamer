from unittest import TestCase
from unittest.mock import patch
from parserClass import Parser


class TestUserInput(TestCase):

    @patch('builtins.input', lambda: 'y')
    def test_find_pattern_safe_to_ignore(self):
        parser = Parser()
        pattern = parser.find_pattern("../Tests/Test Episodes/")
        self.assertIsNotNone(parser.ignore_list)
        self.assertIsNotNone(pattern)

    @patch('builtins.input', lambda: 'n')
    def test_find_pattern_not_safe_to_ignore(self):
        parser = Parser()
        pattern = parser.find_pattern("../Tests/Test Episodes/")
        self.assertEqual(parser.ignore_list.__len__(), 0)
        self.assertIsNone(pattern)