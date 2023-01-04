"""
--------------------------------------------
Name: Thasanka Kandage
SID: 1716597
CCID: thasanka
AnonID: 1000324813
CMPUT 274, Fall 2022

Assessment: Weekly Assignment 3
--------------------------------------------

FREQ TEMPLATE: ADD YOUR INFORMATION TO ABOVE

You must determine how to structure your solution.
Create your functions here and call them from under
if __name__ == "__main__"!
"""
import sys
# import sys to be able to use  command line functions


def openFile():
    # makes a function to error check command line input and opens the textfile
    if len(sys.argv) < 2:
        print("Too few arguments. Usage: python3 freq.py <input_file_name>")
    if len(sys.argv) > 2:
        print("Too many arguments. Usage: python3 freq.py <input_file_name>")
    if len(sys.argv) == 2:
        inputFile = open(sys.argv[1], "r")
        # sys.argv is a list where the first element is the code file
        # and second is the text file
    return inputFile
    # return the variable inputFile to the "__main__" space


def readFile(inputFile):
    # creates a function to reflect the words in the textfile
    # and how many times they are repeated
    allWords = inputFile.read().split()
    # finds all the words in the file
    # then split them into a comma seperated list
    wordAmount = len(allWords)
    wordDict = {}
    # initiates an empty dictionary
    for word in allWords:
        # for every value in allWords, and using that specific value
        if word in wordDict:
            # if that value is already INSIDE wordDict
            wordDict[word] += 1
            # give it an incrementing value of 1
        else:
            wordDict[word] = 1
            # if its THE FIRST TIME that value is called/used TURN
            # that word into a KEY in the empty dictionary
            # and Assign it a value of 1
    return wordDict, wordAmount
    # returns the values of wordDict and wordAmount


def makeOutput(wordDict, wordAmount):
    # creates a function using values wordDict and wordAmount as input values
    wordsSorted = sorted(wordDict)
    # sorts the   wordDict KEYS into a LIST in lexiographical order
    with open(sys.argv[1] + ".out", 'w') as outFile:
        # opens a file with the name of the inputfile + "out"
        for keys in wordsSorted:
            # loop by every element in the ordered list(the keys)
            # then use their values
            wordValues = str(wordDict[keys])
            # makes a variable which is the values of the keys
            wordFreq = str(round(int(wordDict[keys])/wordAmount, 3))
            # makes a variable which is the frequency of the words
            outFile.write(keys + " " + wordValues + " " + wordFreq + "\n")
            # print the key and then a space
            # then print the value of the two variables
            # for every instance of the loop
            # because the looping is used by the SORTED list
            # it will loop in lexicographical order and therefore
            # use the keys(words) in lexicographical order
    return


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to
    # this exercise, so you should call your code from here.
    f = openFile()
    words, wordAmount = readFile(f)
    makeOutput(words, wordAmount)
    pass
