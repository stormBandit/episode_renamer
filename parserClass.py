#!/usr/bin/python3
import re
import os


class Parser:
    """The parser class is used to parse the episodes and the file for converting the names"""

    # hardcoded patterns list to search for
    patterns = [
        '(?P<Season>S[0-9]{1,2}).*(?P<Episode>E[0-9]{1,3})'     # 'S[0-9]{1,2}.*E[0-9]{1,3}'
    ]

    fileTypePattern = "\.[a-zA-z]{1,}$"

    def __init__(self):
        self.ignore_list = list()
        self.episode_guide_file = ""
        self.episodes_folder = ""
        self.delimiter = ""
        self.num_chunks = 0

    # TODO make this more robust, in a more systematic way not so brute force
    # TODO wrap this stuff in try-catch blocks for safety
    def find_pattern(self, episode_folder):
        num_files = len(os.listdir(episode_folder))
        num_matches = 0
        for pattern in self.patterns:
            for fileName in os.listdir(episode_folder):
                if re.search(pattern, fileName):
                    num_matches += 1
                else:
                    print("Found a file that does not conform to the pattern: " + fileName)
                    print("Is is safe to ignore this file when renaming ? [y n]")
                    choice = input()
                    if choice.lower().strip() == "y":
                        self.ignore_list.append(fileName)
                    else:
                        print("File will not be ignored, continuing search for proper pattern")
                        continue

                if num_matches == (num_files - len(self.ignore_list)):
                    print("Pattern '" + pattern + "' matches all files in directory")
                    return pattern

        # TODO don't just give up like this...
        print("Unable to find a pattern that suits all files... sorry")

    # TODO what if not all the files are the same file type???
    # grab the file type for the episodes
    def find_file_type(self, episode_folder):
        regex = re.compile(self.fileTypePattern)

        file_type = ""

        for fileName in os.listdir(episode_folder):
            print(fileName)
            result = regex.search(fileName)
            if not result:
                print("A file caused the regex to fail: " + fileName)
                # TODO lets make this not a fatal error
                return None

            if file_type == "":
                file_type = result.group(0)
            elif file_type == result.group(0) or self.ignore_list.__contains__(fileName):
                continue
            else:
                print("There is a file that has a different extension then all the others " + fileName)
                # TODO lets make this not a fatal error
                return None

        return file_type

    def parse_episode_names(self, episode_name_file):
        file = open(episode_name_file, "r")
        episode_names = file.readlines()
        for name in episode_names:
            print(name)

    # TODO want to make this process automatic
    def get_delimiter_from_user(self):
        print("\nIn order to make this work we need some more information from you, the user")
        while True:
            print("\nPlease insert the delimiter used in the episode names: ")
            delimiter = input()
            if delimiter.__len__() > 1 or delimiter.isalpha() or delimiter.isnumeric():
                print("ERROR: delimiter cannot be numeric, alpha, or larger than 1 character")

    # TODO the automated version of the demlimeter problem
    # delimiters should be non-numeric, non-alpha symbls
    # ie: . _
    def find_delimiter(self, episodes_folder):

        for fileName in os.listdir(episodes_folder):
            print("fileName: "+fileName)
            for char in fileName:
                print("char: "+char)
