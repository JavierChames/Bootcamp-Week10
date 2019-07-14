# 1 
#help('modules') 
#2
# import email
# import html
# import secrets
#3
#import email
#print(dir(email))
#from email import message_from_bytes

#4
#from random import copy,deepcopy,_keep_alive
#5 from <module> import *



import math

def calcFactorial(x):
    return math.factorial(x)

assert(calcFactorial(5) == 120)

def exponent(x):
    return math.pow(2,x)

print(exponent(3))

def ceiling(x):
    return math.ceil(x)

print(ceiling(3.2))