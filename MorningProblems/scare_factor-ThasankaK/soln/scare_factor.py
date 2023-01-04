

rooms, movies, scareF = map(int, input().split())
TwoDList = [[]]*rooms

for i in range(rooms):
    TwoDList[i] = input().split()
emptylist1 = []
emptylist2 = []
for c in range(movies): # x
    toop = ''
    for r in range(rooms): # y
        if toop == '':
            toop = int(TwoDList[r][c])
        elif int(TwoDList[r][c]) < toop:
            toop = int(TwoDList[r][c])
    emptylist1.append(toop)  
#print(emptylist1)
emptylist1.sort()
while sum(emptylist1) > scareF:
    emptylist1.pop()
print(len(emptylist1))

    
#print(TwoDList)




    # your solution goes here
#find the min of each list 
