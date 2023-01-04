listofstations = list(map(int,input().split()))
y = len(listofstations.copy()) + 1
print(y)
x = range(y)
listofstations.copy().append('0')
print(listofstations.copy())
print(x)