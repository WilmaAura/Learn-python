def generate_full_name():
    first_name = 'Wilma'
    last_name= 'Auraruna Khalif'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name()

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print("Total 2 numbers:",total)
add_two_numbers()

# Function Returning a Value - Part 1
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings('Wilma'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r **2
    return area
print(area_of_circle(7))

def sum_of_numbers(n):
    total = 0
    for i in range (n+1):
        total+=i
    return total
    print(total)
print(sum_of_numbers(10))
print(sum_of_numbers(100))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;
print("Age:",calculate_age(2025, 2005))

def weight_of_object(mass,gravity):
    weight = str(mass * gravity) + ' N' # The value has to be changed to a string
    return weight
print('Weight of an object in Newtons:', weight_of_object(100, 9.81))

# Passing Arguments with Key and Value  
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    print(full_name)
print(print_fullname(firstname= 'Wilma', lastname='Auraruna Khalif'))

def add_two_numbers (num1,num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2)) 

def print_name(firstname):
    return firstname
print(print_name('Wilma'))

    # Returning a boolean: Example
def is_even(n):
    if n % 2 == 0:
        print('even')
        return True
    return False
print(is_even(10)) # True
print(is_even(7)) # False

def find_even_numbers(n):
    evens = []
    for i in range (n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

# Funciton with Default Parameters
def greetings (name = 'Wilma'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Auraruna Khalif'))

def generate_full_name(first_name = 'Wilma', last_name = 'Auraruna Khalif'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())
print(generate_full_name('David', 'Smith'))

def calculate_age (birth_year, current_year = 2025):
    age = current_year - birth_year
    return age
print('Age:', calculate_age(2005))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity) + ' N'
    return weight
print ('Weight of an object in Newton:',weight_of_object(100))

# Arbitrary Number of Arguments
    # If we dont know the number of arguments we pass to our function
def sum_all_nums (*nums):
    total = 0
    for num in nums:
        total += num
    return total
print('Sum all numbers:',sum_all_nums(1,2,3))

def generate_groups(team, *args):
    print (team)
    for i in args:
        print(i)
print(generate_groups('Team-1', "Wilma", 'Naura','David'))

# Function as a Parameter of Another Function
def square_number (n):
    return n*n
def do_something(f, x):
    return f(x)
print(do_something(square_number,3))

