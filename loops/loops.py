# syntax
count = 0
while count < 5:
    print(count)
    count += 1
# print from 0 to 4
else:
    print(count) # whhen it false it will print out the condition that is no longer true

# Break and Continue - Part 1
    # Break: Stop the loop

# Example
print("\nLoop break")
count = 0
while count < 5:
    print(count)
    count += 1
    if count ==3:
        break # when it reaches 3 it stops

    # Continue: skip the current iteration and continue with the next iteration
print ('\nLoop Continue')
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print (count)
    count +=1

# For loop
    # syntax 
print("\nFor loop:")
numbers = [0, 1,2,3,4,5]
for number in numbers:
    print(number)
print('Word iteration')
language = 'python'
for letter in language:
    print(letter)
print('different method')
for i in range(len(language)):
    print(language[i])  

    # Loops in dictionary
print('\nPerson dictionary loop')
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
print('key:')
for key in person:
    print(key)
print('\nvalue:')
for value in person:
    print(value)
print('\nKey and value:')
for key, value in person.items():
    print(key,':',value)

    # Loops in set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print('\nLoops for set:')
for company in it_companies:
    print(company)