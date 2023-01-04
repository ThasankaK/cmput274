numberofdigits, sumneeded = map(int,input().split())
runningsum = 0
numberofdigitslist = list(range(0,numberofdigits+1))
emptylist = []

while runningsum < sumneeded:
    runningsum = runningsum + max(numberofdigitslist)
    emptylist.append(max(numberofdigitslist))
    numberofdigitslist.remove(max(numberofdigitslist))
if sum(emptylist) > sumneeded:
    emptylist.remove(min(emptylist))
    toaddtoendofthelist = sumneeded - sum(emptylist) 
    emptylist.append(toaddtoendofthelist)

print(len(emptylist))
emptylist.reverse()
# print(' '.join(str(e) for e in emptylist)

