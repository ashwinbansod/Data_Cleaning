# Author: Ashwin Bansod
# Description : This file reads the raw data file cleans the data
#               and formats it as per requirement.

import collections
import nltk
import enchant
from nltk.metrics import edit_distance


# Spell checker and corrector
class SpellChecker(object):
    def __init__(self, dict_name='en_US', max_dist=2):
        self.spell_dict = enchant.Dict(dict_name)
        self.max_dist = 2

    def replace(self, word):
        if self.spell_dict.check(word):
            return word

        distance = []
        suggestions = []
        suggestions = self.spell_dict.suggest(word)

        retVal = ""
        for suggestedWord in suggestions:
            distance.append(edit_distance(word, suggestedWord))

        if min(distance) <= self.max_dist:
            retVal = suggestions[distance.index(min(distance))]

            i = 0
            for ed in distance:
                if ed == min(distance) :
                    if len(word) == len(suggestions[i]):
                        retVal = suggestions[i]
                        break
                i += 1
        else:
            retVal = word

        return retVal


# This function checks the correctness of the word
# and outputs the corrected version of the word.
def correct_word(word):
    if word == '&':
        return "and"
    elif word == 'intro' or word == 'Intro':
        return "Introduction"
    elif word == 'temporalitiez':
        return "temporalities"
    else:
        wordChecker = SpellChecker()
        return wordChecker.replace(word)


# This function extracts the lastname
def GetLastName(name):
    if ',' in name:
        n = name.split(',')[0]
    elif ' ' in name:
        n = name.split(' ')[-1]
    elif '.' in name:
        n = name.split('.')[-1]
    else:
        n = name
    return n


# __MAIN__FUNCTION__
# It creates a map of the professor and courses,
# cleans the data for the courses and writes it to output file
uic = {}
tokens = []
courseset = set()
dotcounter = 0

# The input file which is to be cleaned
f = open('class.txt', 'r')

for line in f:
    lines = line.split("\n")[0]
    # Get the Last Name of Professor
    name = GetLastName(lines.split('-', 1)[0].strip()).title()

    # Get the course list, append the to list if professor is already existing
    courses = lines.split('-', 1)[1].strip()
    if name in uic:
        allcourses = str(uic[name]) + "|" + courses
        del uic[name]
    else:
        allcourses = str(courses)

    # Sort the course list and clean the course data
    # For this, first tokenize the course, get the correct
    # word using enchant library, then combine the tokens and
    # add to the course list.
    coursearr = allcourses.split("|")
    coursesInOrder = ""
    for temp in coursearr:
        tokens.clear()
        tokens = nltk.word_tokenize(temp)

        i = 0
        for word in tokens:
            if (word.isalpha()) or word == '&':
                tokens[i] = correct_word(word.lower())

            # Capitalize first word of the courses
            if i == 0:
                tokens[i] = tokens[i].title()

            i += 1

        for word in tokens:
            if word == ".":
                continue
            else:
                coursesInOrder += word
                coursesInOrder += " "

        coursesInOrder = coursesInOrder.strip()
        coursesInOrder += "|"

        # Logic to print dots to show processing is in progress
        print(".", end="", flush=True)
        dotcounter += 1
        if dotcounter == 100:
            dotcounter = 0
            print()

    coursesInOrder = coursesInOrder[:-1]

    # sort the coursers after adding to set. so as to remove the duplicates
    courseset.clear()
    for element in coursesInOrder.split("|"):
        courseset.add(element)
    coursearr = ""
    coursearr = "|".join(courseset)
    coursesInOrder = ""
    coursesInOrder = "|".join(sorted(coursearr.split("|")))

    # Add the course list of the professor.
    uic[name] = str(coursesInOrder)

# Use OrderedDict to sort the dict as per professor name.
O_UIC = collections.OrderedDict(sorted(uic.items()))

# Open output file
of = open('cleaned.txt', 'w')

# Write data into output file.
for k in O_UIC:
    of.write(str(k) + " - " + O_UIC[k] + "\n")
