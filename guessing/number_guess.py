import random
print ("Hi, Welcome to the Number Guessing Game. \nYou have 7 changces to guess the number. Let's start!")

low = int(input("Input the lower bound: "))
high = int(input("Enter the upper Bound: "))

print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's start!" )

num = random.randint(low, high)
ch = 7
gc = 0

while gc < ch:
    gc +=1
    guess = int(input('Enter your guess: '))

    if guess == num: 
        print(f'Correct the number is {num}. You guessed it in {gc} attempts.')
        break
    elif gc >= ch and guess != num:
        print('Sorry! The number was {num}. Better luck next time.')
    elif guess > num:
        print ('Too high! Try a lower number.')
    elif guess < num:
        print ('Too low! Try a higher number.')