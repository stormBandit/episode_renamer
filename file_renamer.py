#!/usr/bin/python3
import re
import functions
import os
from userInputClass import UserInput
from parserClass import Parser

# print out menu for user
functions.print_main_menu()

# prompt the user for input
# TODO this will be replaced by a file picker
userInput = UserInput()
#userInput.nameFile = userInput.get_name_file()
#userInput.pathToFiles = userInput.get_path_to_files()
userInput.nameFile = "Tests/episodeNames-01.txt"
userInput.pathToFiles = "Tests/Test Episodes/"

parser = Parser()

# get the name pattern
pattern = parser.find_pattern(userInput.pathToFiles)
if parser.ignore_list.__sizeof__() != 0:
    print("ignoreList: " + str(parser.ignore_list))

# get the file type
file_type = parser.find_file_type(userInput.pathToFiles)
if not file_type:
    print("Fatal Error")
    exit(1)

# get the users preference on naming scheme
name_scheme = userInput.get_nameing_scheme()


# begin renaming process

# get the names in a list
file = open(userInput.nameFile, "r")
names = file.readlines()

# go through the episodes
for fileName in os.listdir(userInput.pathToFiles):
    print(fileName)
    print(re.search(pattern, fileName))


