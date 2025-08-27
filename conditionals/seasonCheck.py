season = input("Check season by the months:").lower() # This is how to program read the input is lowercase

if season == "September" or season == "October" or season == "November":
    print("The season is Autumn")
elif season == "December" or season == "January" or season == "February":
    print("The season is Winter")
elif season == "March" or season == "April" or season == "May":
    print("The season is Sprint")
else:
    print("The season is Summer")
