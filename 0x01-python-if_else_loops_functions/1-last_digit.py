#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDig = abs(number) % 10
if (lastDig > 5):
    str = "is greater than 5"
elif (lastDig == 0):
    str = "is zero"
elif (lastDig < 6):
    str = "is less than 6 and not 0"

print(f"Last digit of {number} is {lastDig} and {str}")
