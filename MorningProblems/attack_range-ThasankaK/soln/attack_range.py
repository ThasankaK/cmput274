# your solution goes here
# n, m = map(int,input().split())
# enemyList1 = list(map(int,input().split()))
# classList1 = list(map(int,input().split()))
# if max(classList1) > max(enemyList1):
#     for i in range(0,m):
#         if min(classList1) < max(enemyList1):
#             classList1.remove(min(classList1))
#         elif min(classList1) == max(enemyList1):
#             classList1.remove(min(classList1))
#     print(min(classList1))
# else:
#     print('-1')
n, m = map(int,input().split())
enemyList1 = list(map(int,input().split()))
classList1 = list(map(int,input().split()))
if max(classList1) > max(enemyList1):
    newlist = []
    x = max(enemyList1)
    for i in classList1:
        if i > x:
            newlist.append(i)
    print(min(newlist))
else:
    print('-1')
