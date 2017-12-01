from unittest import TestCase
from userInputClass import UserInput


class TestUserInput(TestCase):
    def test_has_name_file(self):
        user_input = UserInput()

        user_input.nameFile = "This_is_a_name_file.txt"
        self.assertTrue(user_input.has_name_file())

        user_input.nameFile = ""
        self.assertFalse(user_input.has_name_file())

    def test_has_path_to_files(self):
        user_input = UserInput()

        user_input.pathToFiles = "This/is/a/path/"
        self.assertTrue(user_input.has_path_to_files())

        user_input.pathToFiles = ""
        self.assertFalse(user_input.has_path_to_files())

#    def test_get_user_input(self):
#        self.fail()
