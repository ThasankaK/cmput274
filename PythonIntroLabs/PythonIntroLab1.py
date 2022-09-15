# print("Hello World!")

#--------------------------------------------------
# Change these variables to design your own scarf!
# Add a comment describing what each variable does.
#--------------------------------------------------

# this variable...
colours = ['#', '|', 'T', 'V']

# this variable...
colour_length = 5

# this variable...
pattern_length = 25

# this variable...
pattern_width = 10

#--------------------------------------------------
# Don't change anything below this line!
#--------------------------------------------------
"""
print("Here is your scarf:\n")
for pos in range(int(pattern_width * pattern_length)):
    print( colours[ int ((pos)/colour_length) % len(colours)], end="")
    if (pos % pattern_width) == pattern_width-1:
        print("")
"""
# Transformations
"""
# These two variables store x and y coordinates
x = 1
y = 1
# PERFORM TRANSFORMATIONS HERE
# Reflect the point over the y- axis
x = -x
# Shift the point up by 2
y = y + 2 
# Shift the point left by 6.5
x = x - 6.5
# Vertically stretch the point by a factor of y
y = y*y
# Print the result
print (x)
print (y)
"""
