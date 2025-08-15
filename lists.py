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




