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

    def create_new_name(self, new_names, season_number, episode_number):
        new_name = ""
        pattern = season_number.strip("0") + "\." + episode_number

        print("pattern: " + pattern)

        for name in new_names:
            # found the right name for this episode, rename the episode
            if re.search(pattern, name):
                new_name = self.name_scheme
                episode_name = name.split(None, 1)

                print("episodeName: " + episode_name)

                # replace with the show name
                if self.name_scheme.__contains__("Show Name"):
                    re.sub('Show Name', self.show_name, new_name)

                    print("1. new_name: " + new_name)

                # replace the S#.E#
                if self.name_scheme.__contains__("S#.E#"):
                    re.sub('S#', season_number, new_name)
                    re.sub('E#', episode_number, new_name)

                    print("2. new_name: " + new_name)

                # replace the S# X E#
                if self.name_scheme.__contains__("S# X E#"):
                    re.sub('S#', season_number, new_name)
                    re.sub('E#', episode_number, new_name)

                    print("3. new_name: " + new_name)

                #replace the 'Episde Title'
                re.sub('Episode Title', episode_name, new_name)



        return new_name

    def rename_episodes(self, userInput, parser):
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

            new_name = self.create_new_name(new_names, season_number, episode_number)
