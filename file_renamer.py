#!/usr/bin/python3
import functions
from userInputClass import UserInput
from parserClass import Parser
from renamerClass import Renamer

userInput = UserInput()
parser = Parser()
renamer = Renamer()

# print out menu for user
functions.print_main_menu()

# prompt the user for input
# TODO this will be replaced by a file picker

# TODO remove this, this is for testing purposes
# userInput.nameFile = userInput.get_name_file()
# userInput.pathToFiles = userInput.get_path_to_files()
userInput.nameFile = "Tests/episodeNames-01.txt"
userInput.pathToFiles = "Tests/Test Episodes/"

# get the name pattern
renamer.pattern = parser.find_pattern(userInput.pathToFiles)
if parser.ignore_list.__sizeof__() != 0:
    print("Files that will not be renamed: " + str(parser.ignore_list))

# get the file type
renamer.file_type = parser.find_file_type(userInput.pathToFiles)
if not renamer.file_type:
    print("Fatal Error")
    exit(1)

# get the users preference on naming scheme
renamer.name_scheme = userInput.get_nameing_scheme()

# get the name of the show
renamer.show_name = userInput.get_show_name_from_user()

renamer.rename_episodes(userInput, parser)
