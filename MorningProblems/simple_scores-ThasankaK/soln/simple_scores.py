# your solution goes here
num = int(input(""))
phrase = input("")
# grabs input

hashtagCount = phrase.count('#') # counts the number of hashtags in the phrase 
bCount = phrase.count('b') # counts the number of 'b's in the phrase 
if hashtagCount > bCount:
    remainder = hashtagCount - bCount
    newPhrase = "#"*remainder
    # if there is more hashtags than 'b's 
    # subtract them, to get a remainder which is 
    # the number of hashtags left in the phrase
    # same logic for the other elif statement
elif bCount > hashtagCount:
    remainder = bCount - hashtagCount 
    newPhrase = "b"*remainder
elif bCount == hashtagCount:
    newPhrase = bCount - hashtagCount
    # if there are equal, then it will be 0, an empty phrase
print(newPhrase)