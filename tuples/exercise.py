# create an empty tuple
tuple = ()
print (tuple)
# create tuple containing name
siblings = ("Dyan", "Dinda", "Wilma")
# join it
parent = ("Sutanto", "Sri Wahyuni")
family = parent + siblings
print (family)
# how many siblings
n = len(siblings)
print(n)
## Exercises: Level 2
# Unpack siblings and parents from family_members 
fruits = ("Apple", "Manggo", "Pineapple")
vegetables = ("Onion", "Carots", "Cauliflower")
animal_products = ("meat", "chicken", "rabbit")
food_stuff = fruits + vegetables + animal_products
print(food_stuff)
# Slice out the middle item compz
mid = len(food_stuff) // 2
print (food_stuff[mid])

# Slice out the first three items 
first_three=food_stuff[0:3]
print(first_three)
last_three= food_stuff[-3:]
print(last_three)

# delete completely the tuple
del food_stuff

# Check if an item exists in tuple
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Swedan")
print ("Estonie" in nordic_countries)
print ("Iceland" in nordic_countries)



