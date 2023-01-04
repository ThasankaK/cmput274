# Good luck on this morning problem!

length, tank, numberofstations, refueling = map(int,input().split())
baselength = length 
templength = length
listofstations = list(map(int,input().split()))
gasstops = 0
newlist = []
listofstations.reverse()
travel = length - tank
gasstationreached = 0
#copyofliststations = listofstations

x = listofstations.copy()
while travel > 0:
    while gasstationreached < numberofstations - 1 and x[gasstationreached+1] >= (travel):
        gasstationreached += 1
    travel = x[gasstationreached] - tank
    gasstationreached += 1
    gasstops += 1



#if (length - tank) < min(x):
 #   gasstops = gasstops + 1

time = refueling*gasstops+baselength

print(time)
