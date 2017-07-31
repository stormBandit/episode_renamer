#!/usr/bin/python
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
        except re.error:
            regexAccepted = False          

#this funciton is used to parse the inputted episode guide / file names text
def parseEpisodeGuide(fileNames):
    #read in the lines
    episodes = open(fileNames, "r")
    names = episodes.readlines()
    namesDictionary = {};


    #build the regex to check episode names
    regexp = re.compile(r"[0-9.]+?[a-zA-Z0-9 ]+?")


    #edit the lines to strip away all other text but the name of the episode
    for name in names:
        name.strip("\n")

        if not name:
            print "NULL"
        
        if regexp.search(name):
            result = re.search("(?P<number>[0-9.]*) (?P<title>[a-zA-Z ',]*) *(?P<airDate>[0-9/]*)", name) 
            for i in range(1,3):
                if not result.group(i):
                    print "ERROR: failed to read title name" 
                    sys.exit()

            #append the new key/value to the dict
            namesDictionary[result.group("number")] = result.group("title").rstrip(" ")

    return namesDictionary

#this function searches the given directory for files matching the regex given and replaces the file names with the names given in the name file 
def renameEpisodes(nameFormat, fileNames, directory):
    pattern = re.compile(r"(?P<title>[a-zA-Z0-9 ]*).(?P<seasonEpisode>[a-zA-Z0-9 ]*).(?P<videoType>[0-9]+?p).(?P<junk>[a-zA-Z0-9 ]*).(?P<junk2>[a-zA-Z0-9 -]*).(?P<fileType>[a-zA-Z]*)")

    #load the names of the files from the nameFile
    episodeNames = parseEpisodeGuide(fileNames)

    print episodeNames
    raw_input("DONE")

    #for each episode in the folder, rename it with the corresponding one from the naming file
    for fileName in os.listdir(directory):
        #search for the episode
        result = pattern.search(fileName)
        #check that the search resulted in a find
        if result: 
            for i in range(1,7):
                if result.group(i):
                    print str(i) +" = "+result.group(i) 
            #rename the episode
            number = re.search("s(?P<season>[0-9]{2})e(?P<episode>[0-9]{2})", result.group("seasonEpisode"))
            print "season: " + str(number.group("season")) + " episode " + str(number.group("episode"))

            episodeNum = str(number.group("season")) + "." + str(number.group("episode"))
            #strip 0's from the front
            episodeNum = episodeNum.lstrip("0")

            print "episodeNum = " + episodeNum

            newName = episodeNum + " " + episodeNames[episodeNum]

            print "dir = " + directory
            print "fileName = " + fileName
            print "newName = " + newName

            os.rename(directory + fileName, directory + newName) 

        else:
            print "The regex returned nothing!"

        

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
nameFormat = "0"
#nameFormat = getNameFormat(sys.argv[2])

#search the directory and see if a match for the regex is found, if not report the error
result = renameEpisodes(nameFormat, sys.argv[1], sys.argv[2])

