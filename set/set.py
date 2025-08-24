# set is collection of items
# Set is unordered and un-indexed distinct elements

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
len(st)
print (st)
print ("Does set st containt item3?", "ite3" in st)

# Adding items to a set
st.add("item5")
print(st)
    # Adding multiple items using update ()
st.update(['item7', 'item8', 'item9'])
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'} # tuple
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits.update(vegetables)
print(fruits)

# Removing items 
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
print (st)

# pop item
st = {'item1', 'item2', 'item3', 'item4'}
st.pop()
print(st)

# clearing items in a set
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
print (st)

# Deleting a set
st = {'item1', 'item2', 'item3', 'item4'}
del st
    # print (st) = Error

# converting list to set
lst = ['item1', 'item2', 'item3', 'item4']
st = set(lst)
print (st)

# joining Sets
    # Union this method returns a new set
st1 = {'item1', 'item2', 'item3', 'item4'} 
st2 = {'item5', 'item6', 'item7', 'item8'} 
st3 = st1.union(st2)
print(st3)
    # update the sets
st1 = {'item1', 'item2', 'item3', 'item4'} 
st2 = {'item5', 'item6', 'item7', 'item8'} 
st1.update(st2) # st2 elements are added to st1

# finding intersections Items
    # Intersection: a set of items which are in both sets
st1 = {'item1', 'item2', 'item3', 'item4'} 
st2 = {'item1', 'item5'}
intersection = st1.intersection(st2)
print (intersection)

# checking Subset and Super Set
    # Subset: issubset()
    # Super set: issuperset
st1 = {'item1','item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print (st2.issubset(st1)) # check if all elements of st2 are inside st1 
print (st1.issuperset(st2)) # check if st1 contains all elements of st2 

num1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }
num2 = {5,6,7,8,9,10}
print (num2.issubset(num1))
print (num1.issubset(num2))
print (num1.issuperset(num2))

# Checking the difference between two sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print (st2.difference(st1))
print (st1.difference(st2)) # st1 bedanya dari st2 apa? It says like that

whole_numbers = {1,2,3,4,5,6,7,8,9,10}
even_nubers= {0,2,4,6,8,10}
whole_numbers.difference(even_nubers) # {1,3,5,7,9}

python = {'p','y','t','h','o','n'}
dragon = {'d','r','a','g','o','n'}
print (python.difference(dragon))
print (dragon.difference(python))
print (dragon.difference(dragon))

# joining Sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print (st2.isdisjoint(st1)) # check if both sets have same element
print (st1.isdisjoint(st2))

even_numbers = {0,2,4,6,8}
odd_numbers = {1,3,5,7,9}
print (even_numbers.isdisjoint(odd_numbers)) # true: there is no same element







