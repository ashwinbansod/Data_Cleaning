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

        suggestions = []
        suggestions = self.spell_dict.suggest(word)

        distance = []
        print(distance)
        print(suggestions)

        retVal = ""
        for suggestedWord in suggestions:
            distance.append(edit_distance(word, suggestedWord))

        print(distance)
        lengthMatched = False

        if min(distance) <= self.max_dist:
            retVal = suggestions[distance.index(min(distance))]

            i = 0
            for ed in distance:
                if ed == min(distance) :
                    if len(word) == len(suggestions[i]) and lengthMatched == False:
                        retVal = suggestions[i]
                        lengthMatched = True
                i += 1
        else :
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
        WordChecker = SpellChecker()
        return WordChecker.replace(word)

print(correct_word("Biomaterial"))
print(correct_word("vizion"))
# print(correct_word("Temporalitiez"))
# print(correct_word("Biopolitics"))