# module: file that containing set of code or functions which can be included to an application
# import the common module such as math, datetime, os, sys, random,statistics, collections, json, re
""" 
 import the common module such as math, 
 datetime, os, 
 sys, random,statistics,
 collections, json, re
"""
import os
import sys #provides functions and variables used to manipulate 
from statistics import * # importing all the statistics modules
import math
import string
from random import random, randint # give random number between 0 and 0.9999
1
#OS
os.mkdir('cok')
# changing the current directory
os.chdir('cok')
# getting current working directory
print(os.getcwd())
# Removing directory
os.chdir('..')
os.rmdir('cok')

# some useful sys commands
print('Max integer size:',sys.maxsize) # to know the largest integer var
print('System path:',sys.path) # to know environment path
print('Python version:',sys.version) # to know the version of python u are using

# statistics 
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print('Mean:',mean(ages))   
print('Median:', median(ages))
print('Mode:', mode(ages)) # the most common value
print('stdev:', stdev(ages)) # standard deviation

# math
print ('pi:', math.pi)
print('Square root',math.sqrt(4))
print(math.pow(2, 3)) # 2^3
print(math.floor(9.81)) # rounding to the lowest
print(math.ceil(9.81)) # rounding to the highest
print(math.log10(100))

# string
print('\n',string.ascii_letters)
print (string.digits)
print (string.punctuation)

# Random
print(random())
print(randint(5,20)) # it returns a random integer number between [5, 20]