#!/usr/bin/python3
import sys
import os
import re
import functions
from userInputClass import UserInput

# print out menu for user
functions.print_main_menu()

# prompt the user for input
# TODO this will be replaced by a file picker
userInput = UserInput()
userInput.nameFile = userInput.get_user_input("Please enter the file that describes the names for the episodes that you"
                                              " want renamed")
print("testing format: "+str(functions.check_name_file_formatting(userInput.nameFile)))

userInput.pathToFiles = userInput.get_user_input("Please input the directory containing the episodes you want renamed")

print("Check: \nhasNameFile: "+str(userInput.has_name_file())+"\nhasPathToFiles: "+str(userInput.has_path_to_files()))

# check the formatting for file names and path to the episodes
#functions.check_name_file_formatting(userInput.nameFile)

# get the nameing format for the files
# nameFormat = "0"
# nameFormat = getNameFormat(sys.argv[2])

# search the directory and see if a match for the regex is found, if not report the error

# result = renameEpisodes(nameFormat, sys.argv[1], sys.argv[2])
# if result == 1:
#    print "Success!"
# else:
#    print "Failure!"

