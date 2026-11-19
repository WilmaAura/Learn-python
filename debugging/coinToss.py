import random
import logging
logging.basicConfig(filename='coinTossLog.txt', level=logging.DEBUG,
format=' %(asctime)s -  %(levelname)s -  %(message)s')

logging.debug('Start of program')

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it')
else:
    print ('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
logging.debug(f'Nilai guess: {guess} (tipe: {type(guess)})')
toss = random.randint(0, 1)
logging.debug(f'Nilai toss: {toss} (tipe: {type(toss)})')