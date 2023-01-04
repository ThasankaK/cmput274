# Good luck!
days = int(input())
profits = list(map(int,input().split()))
newlist = []
runningMin = 4310784138974138974138974138758075505050523780
for i in range(days): # looping from 0 to n days
    if runningMin > profits[i]: # a check to reduce the amount of times it is double looped
        runningMin = profits[i] # a way to keep changing the minimum
        for j in range(i,days,1): # subtract a number from i to n from i
            newlist.append(profits[j]-profits[i]) # store the values 
if profits[-1] == min(profits): # if the min is at the end, there cannot be any stock bought
    print('0')
else:
    print(max(newlist)) # print max of the new list