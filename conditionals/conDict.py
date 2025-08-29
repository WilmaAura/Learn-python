person={
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
skills = person['skills']
if 'skills' in person:
    skills = person['skills']
    middle = len(person['skills'])//2
    print("There is skills key in the person dictionary`")
    print(person['skills'][middle])
else:
    print ('none')
if 'Python' in skills:
   print("There is python in skills key") 

if 'JavaScript' in skills and 'React' in skills:
    print('He is front end developer')

if 'Node' in skills and 'MongoDB' in skills and 'Python' in skills:
     print("He is backend developer")

if 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('He is fullstack developer')











