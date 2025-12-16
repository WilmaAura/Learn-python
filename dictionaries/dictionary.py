### DICTIONARY
# Collection of unordered, modifable paired (key: value) data type.

# syntax
empty_dcit = {}
dct = {
    'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4', 
}
print (dct)

# example
person = {
    'first_name': 'Wilma',
    'last_name':'Auraruna Khalif',
    'age':20,
    'country': 'Indonesia',
    'is_married':False,
    'Hobbies':['Read books', 'learning', 'playing games', 'play guitar']
} # the value could be any data types
print(person['first_name'], person['last_name'])
print(person['country'])
print(person['age'])
print(person['is_married'])
print(person['Hobbies'][0]) 
# Adding Items to a Dictionary
dct = {
    'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4', 
} 
dct['key5'] = 'value5'
person['Hobbies'] = 'Watching anime' # replacing all the elements of Hobbies
person['skills']= ('HTML', 'CSS', 'python', 'C++')
print (person)

# modifying items in a dictionary
dct = {
    'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4', 
}
dct ['key1'] = 'value-one'
print (dct)

# Checking keys in a Dictionary
    # We use the 'in' operator
dct = {
    'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4', 
}
print('ley2' in dct) # false
print('key2' in dct) # true

# Removing Key and Value Pairs from a Dictionary
    # pop(key): removes the item with the specified key name
    # popitem(): removes the last item
    # del: removes an item with specified key name
dct = {
    'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4', 
}
dct.pop('key1') # removes the key1 and the value
print (dct)
dct = {
    'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4', 
}
print("\nBefore deleting the dct", dct)
dct.popitem() # removes the last item
print (dct)
del dct['key2']
print (dct)

# changing Dictionary to a list of items
    # The 'items' method changes dictionary to a list of tuples
dct = {
    'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4', 
}
print(dct.items())
del dct

# Copy a Dictionary
dct = {
    'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4', 
}
dct_copy = dct.copy()
print ("Copied dictionary",dct_copy)

# Getting dictionary Keys as a List
    # The keys() method gives us all the keys of a dictionary as a list
dct = {
    'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4', 
}
keys = dct.keys()
print(keys)

# Getting Dictionary Values as a list
dct = {
    'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4', 
}
values = dct.values()
print(values)













