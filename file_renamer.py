#!/usr/bin/python3
import functions
from userInputClass import UserInput
from parserClass import Parser

# print out menu for user
functions.print_main_menu()

# prompt the user for input
# TODO this will be replaced by a file picker
userInput = UserInput()
userInput.nameFile = userInput.get_name_file()
userInput.pathToFiles = userInput.get_path_to_files()

parser = Parser()
parser.find_pattern(userInput.pathToFiles)
# parser.find_delimiter(userInput.pathToFiles)
if parser.ignore_list.__sizeof__() != 0:
    print("ignoreList: " + str(parser.ignore_list))