# How to create a List
# using list built-in function
empty_list = list()
print (len(empty_list))

# using square brackets, []
# lst = []
fruits = ["banana", 'orange', 'mango']
vegatables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
animal_products = ['milk', 'meat', 'butter', 'yoghurt']
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# paint the lists and its length
print ("Fruits:", fruits)
print ("Number of fruits:", len(fruits))
print ("Vegetables:", vegatables)
print ("Number of vegetables:", len(vegatables))
print ("Animal products", animal_products)
print ("Number of animal products", len(animal_products))
print ('\n')
# Accessing List Items Using Positive Indexing
fruits = ["banana", 'orange', 'mango', 'lemon']
print (fruits[0])
print (fruits[1])
# Last index
last_index = len(fruits) - 1
print (fruits[-1])
print ("last index of the character: ", last_index)
first_fruit = fruits[-4]
print(first_fruit)
print (fruits[-3])
print (fruits[-1])

# Unpacking list item
lst = ['item1', 'item2','item3','item4','item5']
first_item, second_item, third_item, *rest = lst
print (first_item)
print (second_item)
print (third_item)
print (*rest) # take all the leftover values from the iterable and pack them into this variable as a list

# Slicing items
fruits = ["banana", 'orange', 'mango', 'lemon']
all_fruits= fruits[0:4]
print (all_fruits)
print (fruits[1:3])
print (fruits[-2:])
print (len(fruits))

# append
fruits = ["banana", 'orange', 'mango', 'lemon']
fruits.append("apple")
print (fruits)
fruits.append("lime")
print (fruits)

# remove
fruits = ["banana", 'orange', 'mango', 'lemon']
fruits.remove("banana")
print(fruits)
# fruits.remove("coba") : ERROR

# pop -> removing elements from the queue
print ("\nPopping:")
fruits = ["banana", 'orange', 'mango', 'lemon']
fruits.pop()
print (fruits)

fruits.pop(0)
print(fruits)

# del 
fruits = ["banana", 'orange', 'mango', 'lemon']
del fruits [0]
print (fruits)

del fruits [2]
print (fruits)

# clear
fruits = ["banana", 'orange', 'mango', 'lemon']
fruits.clear()
print ("\nclearing list:")
print(fruits)

# copying a list
fruits = ["banana", 'orange', 'mango', 'lemon', "cok"]
fruits_copy = fruits.copy()
print (fruits_copy)

# join
positive_numbers=[1,2,3,4,5]
zero = [0]
negative_numbers=[-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print ("\njoining some of lists: ")
print (integers)

# join with extend
print ("\nJoin with extend:")
num1 = [1,2,3]
num2 = [4,5]
num1.extend(num2)
print("Numbers:", num1)

positive_numbers=[1,2,3,4,5]
zero = [0]
negative_numbers=[-5,-4,-3,-2,-1]
negative_numbers.extend(positive_numbers)
negative_numbers.extend(zero)
print (negative_numbers)






