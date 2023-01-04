numOfDigits, sumneeded = map(int,input().split())
runSum = 0
numOfDigitsList = list(range(0,numOfDigits+1))
numOfDigitsList.reverse()
emptylist = []

while runSum < sumneeded:
    runSum = runSum + (numOfDigitsList[0])
    emptylist.append((numOfDigitsList[0]))
    numOfDigitsList.remove((numOfDigitsList[0]))

if sum(emptylist) > sumneeded:
    emptylist.remove(min(emptylist))
    final = sumneeded - sum(emptylist) 
    emptylist.append(final)

print(len(emptylist))
emptylist.reverse()
print(' '.join(str(i) for i in emptylist))