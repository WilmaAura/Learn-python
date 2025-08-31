# syntax
count = 0
while count < 5:
    print(count)
    count += 1
# print from 0 to 4
else:
    print(count) # whhn it false it will print out the condition that is no longer true

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

# break and continue - part 2
    # Example
print('\nBreak and continue part 2')
numbers = (0,1,2,3,4,5)
for i in numbers:
    print(i)
    if i == 3:
        break

    # continue is to skip some of the steps
print('\ncontinue loop')
numbers = (0,1,2,3,4,5)
for i in numbers:
    if i == 3:
        continue
    print(i)

# The Range Function
print('\nThe Range Function:')
lst = list(range(11))
print(lst)
st = set(range(1, 11)) # two arguments indicate start and end of sequence
print(st)

lst = list(range(0,11,2)) # last number is determine the multiple
print(lst)
lst2 = list(range(0,11,3))
print(lst2)
st = set(range(0,11,2))
print(st)

# range (start, end, step)
for number in range(11):
    print(number) # prints 0 to 10, not including 11

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
print('\nSkill that he has:')
for key in person:
    if key == 'skills':
        for i in person['skills']:
            print(i)

    # For Else
for i in range (11):
    print(i)
else:
    print("The loops stops at:",i)

    # pass statement
for i in range(6):
    pass