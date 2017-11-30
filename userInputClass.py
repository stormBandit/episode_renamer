#!/usr/bin/python
import sys
import os

class UserInput:
    'Input class for defining methods to work on getting inputs easily from the user'

    def __init__(self):
        self.nameFile = "" #this is a txt that holds the desired names of the files wanted to rename
        self.pathToFiles = "" #this is a path to the directory of files we want to rename
        self.hasNameFile = False
        self.hasPathToFiles = False

    def hasNameFile(self):
        return self.hasNameFile

    def hasPathToFiles(self):
        return self.hasPathToFiles

    def getUserInput(self, inputDesired):
        success = False

        while success is not True:
            print inputDesired
            inputtedValue = raw_input()
            print "inputtedValue: " + inputtedValue
            if not os.path.exists(inputtedValue):
                print "ERROR: Path to files could not be found. Please try again\n"
            else:
                success = True
                break

        return inputtedValue
            
    

"""prompt the user for input"""
userInput = UserInput()
self.nameFile = userInput.getUserInput("Please enter the file that describes the names for the files you want renamed")

if (len(sys.argv) != 3) :
    print "You must pass in a names file for the renaming scheme and a path to the directory of file you want renamed"
    print "Example:"
    print "     ./episode_renamer [names-File] [/Path/To/Files}"    
    sys.exit()
if not os.path.exists(sys.argv[1]):
    print "ERROR: names file does not exist"
    sys.exit()
if not  os.path.exists(sys.argv[2]):
    print "ERROR: Path to files is not valid"
    sys.exit()
if os.listdir(sys.argv[2]) == []:
    print "ERROR: The directory given is empty"
    sys.exit()

