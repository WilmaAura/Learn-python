# 1. empty list
empty = list()
print (empty)

# 2. declare a list with more than 5 items
ages = [29, 49, 13, 5, 19]

# 3. find the length
print (len (ages))

# 4. get the first, mid, and the last item of the list
firstAges = ages [0]
print ("First age of the list:", firstAges)
midAges=ages[2]
print ("The mid age of the list:",midAges)
lastAges = ages[-1]
print("The last age of the list:", lastAges)

# 5.  declare a list called mixed_data_types, put your (name, age, height, major)
mixed_data_types = ["Wilma Auraruna Khalif", 20, 175, "Computer Science"]

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. print the list
print("\n")
print (mixed_data_types)
print (it_companies)

# 8. Print the number of companies in the list
n = len (it_companies)
print ("The number of companies in the list:", n)

# 9. print the first, middle and last company
mid = n //2
if n % 2 == 0:
    it_companies[mid -1]
else :
    it_companies[mid]

print ("The first company:", it_companies[0])
print ("The middle company of the list:", it_companies[mid])
print ("The last company of the list:", it_companies[-1])

# 10. Print the list after modifying one of the companies
it_companies = ["Facebook is shit", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print (it_companies)

# 11. Add an IT company to it_companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.append("IT")
print (it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.insert(mid, "IT") # the difference between insert and append is, if append it only add item at the last, so u can't add item in the middle.
print (it_companies)

# 13. Change one of the it_companies names to uppercase
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies[0].upper())

    # Convert all items
uppercased = [company.upper() for company in it_companies]
    # "company" is the loop variable representing each element
    # "in" means: take each element from the list "it_companies" one by one and put into the variable company
print (uppercased)

# 14. join the it_companies with a stinrg "#;"
newString = ["#;"]
joining = it_companies + newString
print (joining)

# 15. Check if the element on a certain list
print ("#;" in joining)

# 16. sort the list using sort()
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.sort()
print (it_companies)

# 17. Reverse the list in descending order using reverse ()
it_companies.reverse()
print (it_companies)

# 18. Slice out the first 3 companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print ("The first 3 companies:", it_companies[0:3])

# 19. slice out the last 3 companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print ("The first 3 companies:", it_companies[-3:])

# 20. Slice out the middle IT company 
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print ("The first 3 companies:", it_companies[3:])

# 21. Remove the first IT company from the list
it_companies.remove("Facebook")
print(it_companies)

# 22. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 23. Destroy the IT companies list
del it_companies

# 24. Join the following list
front_end = ["HTML" , "CSS", "JS", 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
fullStack= front_end + back_end
print(fullStack)

# 25 Copy the joined list and assign it to a variable full_stack
# them imsert Python, SQL after Redux 
full_stack = fullStack.copy()
print (full_stack)
redux_index = full_stack.index("Redux")
full_stack.insert(redux_index+1, "Python") # insert is only 2 statements
full_stack.insert(redux_index+2, "SQL")
print(full_stack) 




