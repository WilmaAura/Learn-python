grade = int(input("My score is:"))
print("What grade do i get then?")
if grade >= 80 and grade <= 100:
    print("Congratulations u get an A grade. Good job dear")
elif grade >= 70 and grade <= 79:
    print("Congratulaitons u get a B grade. Try harder next time so u could get an A grade")
elif grade >=60 and grade <= 69:
    print("U should study more dear, u got a C grade")
elif grade >= 50 and grade <= 59:
    print("You must to take remedial ASAP")
else:
    print("For real u got a F grade? You shuold study not just playing games")
