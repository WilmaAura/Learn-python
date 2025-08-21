## tuple is unchangeable list
# syntax
tpl = ("banana", "apple", "pineapple")
print ("Tuple:", tpl)
# example
fruits = ("banana", "apple", "pineapple")
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print (last_index)
print (last_fruit)
# Slicing tuples
# Range of positive indexes
tpl = ("item1", "item2", "item3","item4")
print ("All item:", tpl[0:4])
print ("All item asswell:", tpl[0:])
print ("Doesn't include the last item:", tpl[0:3])
# range of negative indexes
# ("banana", "orange", "mango", "lemon")
#     -4        -3        -2       -1
tpl = ("item1", "item2", "item3", "item4")
first_item = tpl[-4]
print (first_item)
print ("All item by slicing them with negative indexes:", tpl[-4:])


