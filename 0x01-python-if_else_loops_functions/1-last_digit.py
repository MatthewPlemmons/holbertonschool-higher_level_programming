#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
negative = False
if number < 0:
    number *= -1
    negative = True
n = number % 10
if negative:
    number *= -1
    n *= -1
print("Last digit of {} is {} and is ".format(number, n), end="")
if n > 5:
    print("greater than 5")
elif n == 0:
    print("0")
else:
    print("less than 6 and not 0")
