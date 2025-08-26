cat = {
    'name':'Naura',
    'color':'Orange',
    'age':2
}

student = {
    'first_name' : 'Wilma',
    'last_name' : 'Auraruna Khalif',
    'sex' : 'male',
    'marital status': False,
    'country':'Indonesia',
    'city':'Semarang'
}

values= student.values()
print (values)
# Adding new key and values
student['Skills'] = ['Python', 'C++', 'HTML', 'CSS']
print (values)
student['Gf'] = 'Naura'
print (values)

print("\nStudent length:",len(student))
keys = student.keys()
print ("Dictionary keys:", keys)

convert = student.items()
print ("\nChange the dictionary to a list of tuples:",convert)

student.pop('Skills')
print ("After the skills were deleted:",student)

del cat








