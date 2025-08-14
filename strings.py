# multiline_string
multiline = """rorrrrrrrr
rorrrrrr
rorrrrrr
Meow
Meow
Meow
"""
print (multiline)

# String Concatenation = rangkaian string
first_name = "Wilma"
last_name = "Auraruna Khalif"
space = " "
print (first_name + space + last_name)

language = 'Python'
a, b, c, d, e, f = language
print (a)
print (b)
print (c)
print (d)
print (e)
print (f)

print ("")

# Accessing characters in strings by index
language = 'Python'
first_letter= language[0]
print (first_letter)
second_letter = language[1]
print (second_letter)
last_index = len (language) - 1
last_letter = language[last_index]
print ("Last letter:", last_letter)
elementLanguage= len (language)
print ("Number of elements language: ",elementLanguage)

# If we want to start from the right, use negative index. -1 is the last index
language = "python"
last_letter = language [-1]
print ("Print array from the rigth:", last_letter)
secondLast = language [-2]
print ("Print array second last:", secondLast)
print ("")

# Slicing
print ("Slicing:")
language = 'python'
first_three = language [0:3] # starts at zero index and up to 3 but not include 3
print (first_three)
print ("Jumlah element language:", len (language))
trying = language [2:] # its not include the first 2 letter
print (trying)
coba2 = language [-2:] # its only the last 2 letter
print (coba2)
print ("")

# Skipping character while spliting python strings
language = 'python'
pto = language [0:6:2] # [start : stop : step]
# start with 0 index
# stop -> go up to index 6 or all of them included
# step = 2 -> take every 2nd character
print(pto)
ph = language [0:6:3]
print (ph)

# Escape sequence
print ("")
print ("ESCAPE SEQUENCE:")
print ("I hope every one enjoying the python challange. \nDo you?") # Line break
print ("Days\t| Topics\t| Exercises |")
print ("Day 1\t3\t5")
print ("Day 2\t3\t5")
print ("Day 3\t3\t5")
print ("Day 4\t3\t5")
print ("This is a back slash symbol")

# count index array
print ("")
arr = [1, 2, 3, 4]
jumlahIndex = len (arr)
print (arr)
print (*arr)
print ("Jumlah index array: ", jumlahIndex)

## String Methods
# capitalize(): Converts the first word to Capital Letter
challange = "thirty days of python"
print(challange.capitalize()) # Thirty

#endwith(): Checks if a string ends with a specified ending
challange = "thirty days of python"
print (challange.endswith("n"))
print (challange.endswith("kyah"))

# expandtabs(): Replaces tab



