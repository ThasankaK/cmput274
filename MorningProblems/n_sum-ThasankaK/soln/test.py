numberofdigits, sumneeded = map(int,input().split())
print(numberofdigits,sumneeded)

numberofdigitslist = list(range(0,numberofdigits+1))
# print(numberofdigitslist)
runningsum = 0
emptylisttousetoadd = []
while runningsum < sumneeded:
    #if sum(emptylisttousetoadd) == sumneeded:
       # runningsum = sumneeded + 1


    if max(numberofdigitslist) + sum(emptylisttousetoadd) == sumneeded:
        runningsum = sumneeded + 1
        emptylisttousetoadd.append(max(numberofdigitslist))
    elif max(numberofdigitslist) + sum(emptylisttousetoadd) > sumneeded:
        emptylisttousetoadd.append(max(numberofdigitslist))

        newmin = min(emptylisttousetoadd) - 2
        emptylisttousetoadd.remove(min(emptylisttousetoadd))
        emptylisttousetoadd.append(newmin)
        runningsum = sumneeded + 1 
    else: 
        emptylisttousetoadd.append(max(numberofdigitslist))
        numberofdigitslist.remove(max(numberofdigitslist))

emptylisttousetoadd.reverse()
print(numberofdigits)
print(emptylisttousetoadd)




