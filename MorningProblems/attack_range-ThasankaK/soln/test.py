import random
n, m = map(int,input().split())
enemyList1 = list(map(int,input().split()))
classList1 = list(map(int,input().split()))
if max(classList1) > max(enemyList1):
    for i in range(0,m):
        if min(classList1) < max(enemyList1):
            classList1.remove(min(classList1))
        elif min(classList1) == max(enemyList1):
            classList1.remove(min(classList1))
    print(min(classList1))
else:
    print('-1')
"""
enemyList = []
classList =[]
for i in range(0,n):
    l = random.randint(1,10000)
    enemyList.append(l
print(enemyList)
for j in range(0,m):
    a = random.randint(1,10000)
    classList.append(a)
print(classList)
"""