a = 3 
if a > 0:
    print ("A is a positive number")

if a < 0:
    print ('A is a negative number')
else:
    print ('A is a positive number')

# syntax = elif:
a = 0
print("A is positive") if a >= 0  else print("")

# Nested Conditions
a = 0
if a >0:
    if a %2 == 0:
        print('A is positive and even integer')
    else :
        print('A is a positive number')
elif a == 0:
    print ("A is zero")
else:
    print('A is a none')

# If condition and logical operators
a = 0
if a > 0 and a % 2 == 0:
    print("A is an even and positive integer")
elif a > 0 and a % 2 != 0:
    print('A is a positive integer')
elif a == 0:
    print("A is zero")
else:
    print("A is negative")

# If and Or Logical Operators
user = 'james'
access_level= 3
if user == 'admin' or access_level >= 4:
    print('Access granted')
else:
    print('Access denied')


