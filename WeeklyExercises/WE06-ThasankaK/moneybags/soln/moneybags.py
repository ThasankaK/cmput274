members = int(input())
networths = []
for i in range(members):
    i = int(input())
    networths.append(i)
networths.sort()
T = 0
networthNew = networths.copy
if min(networths) >= len(networths):
    N = len(networths)
else:
    for people, money in enumerate(networths):  # returns index and value
        if people <= len(networths) - money:
            j = people
            N = money
        elif (j <= len(networths) - (N+1)):
            T = 1
            N = N + 1
    if T:
        N = N - 1
print(N)
