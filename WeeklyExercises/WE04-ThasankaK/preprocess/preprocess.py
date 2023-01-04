"""
--------------------------------------------
Name: Thasanka Kandage
SID: 1716597
CCID: thasanka
AnonID: 1000324813
CMPUT 274, Fall 2022
Assessment: Assignment 4 Preprocessor
--------------------------------------------
TEMPLATE: ADD YOUR INFORMATION TO ABOVE
You must determine how to structure your solution.
Create your functions here and call them from under
if __name__ == "__main__"!
"""
import sys
Stop_Words = [
    "i", "me", "my", "myself", "we", "our",
    "ours", "ourselves", "you", "your",
    "yours", "yourself", "yourselves", "he",
    "him", "his", "himself", "she", "her",
    "hers", "herself", "it", "its", "itself",
    "they", "them", "their", "theirs",
    "themselves", "what", "which", "who",
    "whom", "this", "that", "these", "those",
    "am", "is", "are", "was", "were", "be",
    "been", "being", "have", "has", "had",
    "having", "do", "does", "did", "doing",
    "a", "an", "the", "and", "but", "if",
    "or", "because", "as", "until", "while",
    "of", "at", "by", "for", "with",
    "about", "against", "between", "into",
    "through", "during", "before", "after",
    "above", "below", "to", "from", "up",
    "down", "in", "out", "on", "off", "over",
    "under", "again", "further", "then",
    "once", "here", "there", "when", "where",
    "why", "how", "all", "any", "both",
    "each", "few", "more", "most", "other",
    "some", "such", "no", "nor", "not",
    "only", "own", "same", "so", "than",
    "too", "very", "s", "t", "can", "will",
    "just", "don", "should", "now",
    " "]
mode = ''
rawSentence = input()
a = ".,?!;:'-_()[]"".../|*@#$%^&"
Puncutation_and_Symbols = [*a]
Numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
b = "abcdefghijklmnopqrstuvwxyz"
Alphabet = [*b]
lcSentence = rawSentence.lower()
loopingSentence = lcSentence


def Mode():
    if len(sys.argv) < 1:
        print("Too few arguments. Usage: python3 preprocess.py <command>")
        value = 1
        return value
    if len(sys.argv) > 2:
        print("Too many arguments. Usage: python3 preprocess.py <command>")
        value = 1
        return value
    if len(sys.argv) == 2:
        if sys.argv[1] == "keep-digits":
            keepDigits(loopingSentence)
        elif sys.argv[1] == "keep-stops":
            keepStops(loopingSentence)
        elif sys.argv[1] == "keep-symbols":
            keepSymbols(lcSentence)
        else:
            print("Mode Error. Modes: “keep-digits/stops/symbols")
    if len(sys.argv) == 1:
        removeAll(loopingSentence)


def keepDigits(loopingSentence):
    for i in Puncutation_and_Symbols:
        loopingSentence = loopingSentence.replace(i, '')
    sentenceList = loopingSentence.split()
    noStopsSentence = []
    for k in sentenceList:
        if k not in Stop_Words:
            noStopsSentence.append(k)
    completedString = ' '.join(noStopsSentence)
    return print(completedString)


def keepStops(loopingSentence):
    for i in Puncutation_and_Symbols:
        loopingSentence = loopingSentence.replace(i, '')
    sentenceList = loopingSentence.split()
    newSentence = []
    for i in sentenceList:
        if any(char.isdigit() for char in i):
            # makes a for loop every character in the string i, using that
            # specific character, if ATLEAST ONE CHARACTER
            # IS A DIGIT, the any() function results in TRUE
            t = ''.join([x for x in i if not x.isdigit()])
            # for x in i (a string) -ITERATES THROUGH THE STRING -
            # if x (a character in a string)
            # is NOT a digit, append THAT character to the the variable t
            if len(t) == 0:
                newSentence.append(i)
                # this means that t was acutally a number
                # and when ran thru the above line, reduces it to an empty
                # space, therefore append the element that was used
            else:
                newSentence.append(t)
        else:
            newSentence.append(i)
    completedString = ' '.join(newSentence)
    return print(completedString)


def keepSymbols(lcSentence):
    sentenceList = lcSentence.split()
    newSentence = []
    for i in sentenceList:
        if any(char.isdigit() for char in i):
            # makes a for loop every character in the string i, using that
            # specific character, if ATLEAST ONE CHARACTER
            # IS A DIGIT, the any() function results in TRUE
            t = ''.join([x for x in i if not x.isdigit()])
            # for x in i (a string) -ITERATES THROUGH THE STRING -
            # if x (a character in a string)
            # is NOT a digit, append THAT character to the the variable t
            if len(t) == 0:
                newSentence.append(i)
            else:
                newSentence.append(t)
        else:
            newSentence.append(i)
    noStopsSentence = []
    for k in newSentence:
        if k not in Stop_Words:
            noStopsSentence.append(k)
    completedString = ' '.join(noStopsSentence)
    return print(completedString)


def removeAll(loopingSentence):
    print(loopingSentence)
    for i in Puncutation_and_Symbols:
        loopingSentence = loopingSentence.replace(i, '')
    sentenceList = loopingSentence.split()
    newSentence = []
    for i in sentenceList:
        if any(char.isdigit() for char in i):
            # makes a for loop every character in the string i, using that
            # specific character, if ATLEAST ONE CHARACTER
            # IS A DIGIT, the any() function results in TRUE
            t = ''.join([x for x in i if not x.isdigit()])
            # for x in i (a string) -ITERATES THROUGH THE STRING -
            # if x (a character in a string)
            # is NOT a digit, append THAT character to the the variable t
            if len(t) == 0:
                newSentence.append(i)
            else:
                newSentence.append(t)
        else:
            newSentence.append(i)
    noStopsSentence = []
    for k in newSentence:
        if k not in Stop_Words:
            noStopsSentence.append(k)
    completedString = ' '.join(noStopsSentence)
    return print(completedString)


Mode()
if mode == "keep-digits":
    keepDigits(loopingSentence)
if mode == "keep-stops":
    keepStops(loopingSentence)
if mode == "keep-symbols":
    keepSymbols(lcSentence)
# Global List
if __name__ == "__main__":

    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 preprocess.py". This is directly relevant
    # to this exercise, so you should call your code from here.
    pass