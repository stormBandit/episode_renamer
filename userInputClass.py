#!/usr/bin/python3
import os
import re


class UserInput:
    """Input class for defining methods to work on getting inputs easily from the user"""

    name_scheme_choices = {'1': "Show Name S#.E# Episode Title",
                           '2': "S#.E# Episode Title",
                           '3': "Show Name # X # Episode Title",
                           '4': "# X # Episode Title"}

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

        for i in range(0, names.__len__()):
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
            print("\nPlease enter the file that describes the names for the episodes that you want renamed")
            inputted_value = input()

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
            print("\nPlease input the directory containing the episodes you want renamed")
            inputted_value = input()

            if not os.path.exists(inputted_value):
                print("ERROR: Path to files could not be found. Please try again\n")
            else:
                if os.path.getsize(inputted_value) > 0:
                    return inputted_value
                else:
                    print("ERROR: Directory is empty, please try again\n")

    # get the user's preference on naming scheme
    def get_nameing_scheme(self):

        choice = 0

# TODO this will not accept a character or string.. fix
        while choice not in ['1', '2', '3', '4']:
            print("Please choose one of the following naming schemes for your list of episodes:")
            print("(1): Show Name S#.E# Episode Title")
            print("     ex: Friends S01.E01 Pilot\n")
            print("(2): S#.E# Episode Title")
            print("     ex: S01.E01 Pilot\n")
            print("(3): Show Name # X # Episode Title")
            print("     ex: Friends 01 X 01 Pilot\n")
            print("(4): # X # Episode Title")
            print("     ex: 01 X 01 Pilot\n")
            choice = input()

        return self.name_scheme_choices.get(choice)

    # get the name of the show as input from the user... this is hard to parse and may not even be in the file name
    def get_show_name_from_user(self):
        name = ""
        confirmation = "n"

        while confirmation.lower().strip() != "y":
            name = input("Please enter the name of the show: ")

            print("\nYou have input the name of the show as '" + name + "' is this correct? [y n]")
            confirmation = input("Please double check spelling and capitalization as the name is hard to change later\n")
