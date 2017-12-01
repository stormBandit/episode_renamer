#!/usr/bin/python3
import os


class UserInput:
    """Input class for defining methods to work on getting inputs easily from the user"""

    def __init__(self):
        self.nameFile = ""      # this is a txt that holds the desired names of the files wanted to rename
        self.pathToFiles = ""   # this is a path to the directory of files we want to rename

    def has_name_file(self):
        return True if self.nameFile != "" else False

    def has_path_to_files(self):
        return True if self.pathToFiles != "" else False

    def get_user_input(self, input_desired):

        while True:
            print(input_desired)
            inputted_value = input()
            print("inputtedValue: " + inputted_value)
            if not os.path.exists(inputted_value):
                print("ERROR: Path to files could not be found. Please try again\n")
            else:
                if os.path.getsize(inputted_value) > 0:
                    return inputted_value
                else:
                    print("ERROR: File or Directory inputted was empty, please try again\n")
