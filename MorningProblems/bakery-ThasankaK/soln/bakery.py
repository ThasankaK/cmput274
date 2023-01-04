recipes, ovenSize, tempRange = map(int, input().split())
temp = list(map(int,input().split()))
temp.sort()
tempRange = 2*tempRange
if ovenSize == 1:
    time = recipes
    print(time)
else:
    time = 0
    n = 0
    while n < recipes: 
        count = 0 #
        for placeholder, tempValues in enumerate(temp[n:ovenSize+n]):
            if tempValues in range(temp[n], temp[n] + tempRange + 1):
                count += 1
        time += 1
        n += count
    print(time)
