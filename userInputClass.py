#!/usr/bin/python3
import os
import re


class UserInput:
    """Input class for defining methods to work on getting inputs easily from the user"""

    def __init__(self):
        self.nameFile = ""      # this is a txt that holds the desired names of the files wanted to rename
        self.pathToFiles = ""   # this is a path to the directory of files we want to rename

    def has_name_file(self):
        return True if self.nameFile != "" else False

    def has_path_to_files(self):
        return True if self.pathToFiles != "" else False

    # check the formatting of the names file
    def check_name_file_formatting(self, name_file):
        # read in the lines
        episodes = open(name_file, "r")
        names = episodes.readlines()

        regexp = re.compile(r"[0-9]{1,2}[.][0-9]{1,2}[a-zA-Z0-9 ]+?")

        for i in range(0, names.__sizeof__()):
            line = names.__getitem__(i)
            result = re.search(regexp, line)
            if not result:
                print("\n\nERROR in formatting of names file\nline number " + str(
                    i) + ": '" + line + "'\ndoes not match the proper formatting\n")
                return False

        return True

    # TODO replace with a file picker eventually
    def get_name_file(self):

        while True:
            print("Please enter the file that describes the names for the episodes that you want renamed")
            inputted_value = input()
            print("inputtedValue: " + inputted_value)
            if not os.path.isfile(inputted_value):
                print("ERROR: The file does not exist. Please try again\n")
            else:
                if os.path.getsize(inputted_value) > 0:
                    if self.check_name_file_formatting(inputted_value):
                        return inputted_value
                else:
                    print("ERROR: File is empty, please try again\n")

    # TODO replace with a file picker eventually
    def get_path_to_files(self):

        while True:
            print("Please input the directory containing the episodes you want renamed")
            inputted_value = input()
            print("inputtedValue: " + inputted_value)
            if not os.path.exists(inputted_value):
                print("ERROR: Path to files could not be found. Please try again\n")
            else:
                if os.path.getsize(inputted_value) > 0:
                    return inputted_value
                else:
                    print("ERROR: Directory is empty, please try again\n")


