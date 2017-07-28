import sys
import os
import re

#this is the regex help menu for users building a regex
def printRegexHelpMenu():
    print "MUST DEFINE THIS AT A LATER TIME"


#this function, is used to rettrive the regex used for the file names
def getNameFormat(pathToFile):
    regexAccepted = False

    while (regexAccepted == False):
        userRegex = raw_input("\nPlease enter the regex to describe how the files are named (type \"help\" for a regex guide):\n")

        if userRegex.lower() == "help":
            printRegexHelpMenu()
            continue

        try:
            re.compile(userRegex)
            regexAccepted = True
            print "IS VALID"
        except re.error:
            regexAccepted = False          
            print "IS NOT VALID"



#check for proper inputs
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

#get the nameing format for the files 
nameFormat = getNameFormat(sys.argv[2])




