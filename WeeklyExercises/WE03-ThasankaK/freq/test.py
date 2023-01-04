from pdb import line_prefix
import sys # import sys to be able to use  command line functions
if len(sys.argv) < 2:
    print("Too few arguments. Usage: python3 freq.py <input_file_name>")
if len(sys.argv) > 2: 
    print("Too many arguments. Usage: python3 freq.py <input_file_name>")

if len(sys.argv) == 2:
    inputFile = open(sys.argv[1], "r")
    allWords = inputFile.read().split() # finds all the words in the file, then splits them into a comma seperated lists
    emptydict = {} # initiates an empty dictionary 
    for word in allWords: # for every value in allWords, and using that specific value
        if word in emptydict: # if that value is INSIDE emptydict, ASSIGN THAT VALUE AS A KEY into the dictionary and give it an incrementing value
            emptydict[word] += 1
        else:
            emptydict[word] = 1 # if its THE FIRST TIME that value is INSIDE the empty dictionary,  ASSIGN A 




    emptydictSorted = sorted(emptydict) # sorts the  emptydict KEYS into a LIST in lexiographical order
    with open(sys.argv[1] + ".out", 'w') as outFile:
        for keys in emptydictSorted: # loop by every element in the ordered list(the keys) and using their values, then 
            outFile.write(keys + " " + str(emptydict[keys]) + " " + str(round((emptydict[keys]/len(allWords)),3)) + "\n" ) # first off print the key and 
                                                # then a space, then find the VALUE associated with the key and turn it into a string to be
                                                # concatenated and the another space and then
                                                # divide the value of the keys by the total number of keys( all the words) and round that
                                                # value to 3 decimal places and turn the value into a string to be concatenated
                                                # because the looping is used by the SORTED list it will loop in lexiographical order 

    #for i in emptydict:
    #   print(emptydict.keys())

    #i want to make a for loop that contains the line
    #   print(key + value + frequency for every word)