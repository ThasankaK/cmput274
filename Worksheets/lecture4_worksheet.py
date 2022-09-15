#1 
"""
theCount =0
word = input("Word: ")
if word in ['the', 'The']:
     theCount = theCount + 1
print( "Total count %s" % (theCount) )
"""
#2 
"""
theCount = 0
word = input("Word: ")
targetWords = ['outside', 'today', 'weather', 'raining', 'nice', 'rain', 'snow', 'day', 'winter', 'cold', 'warm', 'snowing', 'out', 'hope', 'boots', 'sunny', 'windy', 'coming', 'perfect', 'need', 'sun']
if word in targetWords:
    theCount = theCount + 1
print("Total count %s" % (theCount))
"""
#2 bonus
notTargetWords = []
targetWords =  ['outside',
'today', 'weather', 'raining', 'nice', 'rain',
'snow', 'day', 'winter', 'cold', 'warm',
'snowing', 'out', 'hope', 'boots', 'sunny',
'windy', 'coming', 'perfect', 'need', 'sun',
'on', 'was', '-40', 'jackets', 'wish', 'fog',
'pretty', 'summer','exit','Exit']
Continue = True
while Continue == True:
    word = input("Word: ") 
    if word not in targetWords:
        notTargetWords.append(word)
    elif word in ['exit', 'Exit']:
        Continue = False 
print(notTargetWords)
#append somehow onto targetwods 


 
# make an empty list and keep adding the inpputs onto that list and then print ot thellist 
