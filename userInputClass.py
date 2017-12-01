#!/usr/bin/python3
import sys
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


# prompt the user for input
# TODO this will be replaced by a file picker

userInput = UserInput()
userInput.nameFile = userInput.get_user_input("Please enter the file that describes the names for the episodes that you"
                                              " want renamed")
userInput.pathToFiles = userInput.get_user_input("Please input the directory containing the episodes you want renamed")

print("Check: \nhasNameFile: "+str(userInput.has_name_file())+"\nhasPathToFiles: "+str(userInput.has_path_to_files()))
