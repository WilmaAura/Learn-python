import random  

secret_number = random.randint(1,20)

print('I am thinking of a number between 1 and 20.')

# Ask player to guess 6 times
for guesses_taken in range (1, 7):
    print('Take a guess.')
    guess = int(input('>'))

    if guess < secret_number:
        print("Ur guess is too low")
    elif guess > secret_number:
        print("Ur guess is too high")
    else:
        break # This condition is the correct guess!

if guess == secret_number:
    print("Good boy! It's " + str(guess))
else:
    print("Nope. The number was" + str(secret_number))