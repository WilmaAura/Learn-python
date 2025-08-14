# Arithmatic Operations in Python
# Integers

print ("Addition:", 8+9)
print ("Substraction:", 8-9)
print ("Multiplication:", 8*9)
print ("Division:", 8/9)
print ("Division:", 9//8) # without floating numbers
print ("Modulus:", 9%8) 
print ("Exponential:", 3**3) # it means 3 * 3 * 3
print ("\n")
# Floating Numbers
print ('Eleven digits of PI:', 3.1415926535)
print ("Floating number, gravity:", 9.81)
print ("\n")
# Declaring the variable first
a = 8
b = 4

total = a + b
diff = a - b
product = a * b
division = a / b
floorDivision= a // b
remainder = a % b 
exponential = a ** b

print ("total:" , total)
print ("diff:" , diff)
print ("product:" , product)
print ("division:" , division)
print ("remainder:" , remainder)
print ("Flor Division:" , floorDivision)
print ("exponential:" , exponential)

# Calculating area of circle
radius = 10
circleArea= 3.14 * radius ** 2
print ("Area of circle:", circleArea) 

# Calculating area of a ractangle
length = 20
width = 10
rectangleArea = length * width
print ("Area of rectangle", rectangleArea)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print ("Weight of an object:", weight, "N")

print ("")
print (3 < 2)
print (3 > 2)
print (3 >= 2)
print (2 < 3)
print (3 == 2)
print (3 != 2)
print (len('mango') == len ('avocado')) # counts the number of characters in "mango" and "avocado"
print (len('mango') == len ('mango')) # counts the number of characters in "mango"
print (len('mango') < len ('mango')) 

# Boolean comparison
print ("True == True: ", True == True)
print ("True == False: ", True == False)
print ("False == False: ", False == False)
print ("True and False: ", True and False)
print ("True or False: ", True or False)

# Another way comparison
print ("1 is 1", 1 is 1)
print ("1 is not 2", 1 is not 2)
print ("W in Wilma", 'W' in "Wilma")
print ("N in Wilma", 'N' in "Wilma")
print ("coding", 'coding' in "coding is fun cok")
print ("4 is 2 ** 2", 4 is 2 ** 2)
print ("4 is 8/2", 4.0 is 8/2)

print ("")
print (3 > 2 and 4 > 3) # both of them is true
print (3 > 2 and 3 < 3) # the second statement is false
print (3 > 2 or 3 < 2) # one of them is true 
print (3 < 2 or 3 <= 2) # all of them is false
print (not 3 > 2) # 
print (not True)
print (not False) # its like (-1 * -1) = 1
print (not not True)
print (not not False)