# Read in the input
x1, y1 = input('coordinate1(x,y): ').split()
x2, y2 = input('coordinate2(x.y): ').split()
x3, y3 =input('coordinate3(x,y): ').split()
# Solve the probelm
if x1 == x2 or x1 == x3: 
    if x1 == x2:
        x4 = x3
    else:
        x4 = x2 
else:
    x4 = x1
if y1 == y2 or y1 == y3:
    if y1 == y2:
        y4 = y3
    else:
        y4 = y2
else:
    y4 = y1
# Output the result
print(x4,y4)
