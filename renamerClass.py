import re
import os
from userInputClass import UserInput


class Renamer:
    """Class for the functionality of actually renaming the episodes"""

    def __init__(self):
        self.pattern = ""       # valid pattern for the episodes to be renamed
        self.name_scheme = ""   # string describing the scheme that the user has chosen to style the names after
        self.show_name = ""     # the name of the tv show being renamed
        self.file_type = ""     # the file type for the episode video files

    def renameEpisodes(self, userInput, parser):
        # get the names in a list
        file = open(userInput.nameFile, "r")
        new_names = file.readlines()

        # go through the episodes
        for fileName in os.listdir(userInput.pathToFiles):
            if parser.ignore_list.__contains__(fileName):
                continue

            print("\nfilename: " + fileName)

            regex = re.compile(self.pattern)
            result = regex.search(fileName)
            if not result:
                exit(1)

            # get season and episode numbers
            season_number = re.search('\d+', result.group("Season")).group(0)
            episode_number = re.search('\d+', result.group("Episode")).group(0)

            print("Season: " + str(season_number))
            print("Episode: " + str(episode_number))

            print(self.name_scheme)
