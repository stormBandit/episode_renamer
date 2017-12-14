#!/usr/bin/python3
import sys
import os
import re


# Print main menu for introduction to the program
def print_main_menu():
    print("\n\nWelcome to the episode renamer")
    print("a program used to rename those pesky episodes with weird names like 'Friends-S01E01.alan.1080p.HD.mkv'")
    print("\nThis program will accept a file describing the name of the episodes, and a folder holding the episodes you"
          " want renamed")
    print("\nIMPORTANT: the file holding the episode names needs to be formatted correctly, following these rules:")
    print("     1. Each episode name need to be on a new line")
    print("     2. The lines must prefix with #.## format indicating what season and episode the name corresponds with"
          "         ex. 1.01 -> season 1, episode 1\n\n")
    # TODO ad rules as needed

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
            print("NULL")
        
        if regexp.search(name):
            result = re.search("(?P<number>[0-9.]*) (?P<title>[a-zA-Z ',]*) *(?P<airDate>[0-9/]*)", name) 
            for i in range(1,3):
                if not result.group(i):
                    print("ERROR: failed to read title name" )
                    sys.exit()

            #append the new key/value to the dict
            namesDictionary[result.group("number")] = result.group("title").rstrip(" ")

    return namesDictionary


# this function searches the given directory for files matching the regex given and replaces the file names with the
# names given in the name file
def renameEpisodes(nameFormat, fileNames, directory):
    pattern = re.compile(r"(?P<title>[a-zA-Z0-9 ]*).(?P<seasonEpisode>[a-zA-Z0-9 ]*).(?P<videoType>[0-9]+?p).(?P<junk>[a-zA-Z0-9 ]*).(?P<junk2>[a-zA-Z0-9 -]*).(?P<fileType>[a-zA-Z]*)")

    #load the names of the files from the nameFile
    episodeNames = parseEpisodeGuide(fileNames)

    #for each episode in the folder, rename it with the corresponding one from the naming file
    for fileName in os.listdir(directory):
        #search for the episode
        result = pattern.search(fileName)
        #check that the search resulted in a find
        if result: 
            for i in range(1,7):
                if not result.group(i):
                    print("ERROR: a rogue file name was found, continuing would be dangerous")
                    sys.exit()

            #rename the episode
            number = re.search("s(?P<season>[0-9]{2})e(?P<episode>[0-9]{2})", result.group("seasonEpisode"))
            episodeNum = str(number.group("season")) + "." + str(number.group("episode"))
            #strip 0's from the front
            episodeNum = episodeNum.lstrip("0")

            newName = episodeNum + " " + episodeNames[episodeNum]

            os.rename(directory + fileName, directory + newName) 

        else:
            print("The regex returned nothing!")
            return -1

    return 1

