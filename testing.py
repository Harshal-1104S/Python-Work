import random

print("Pick a number from 1-2")
num = int(input())
random_num = random.randint(1, 2)

if random_num == num:
    print("You got it!")
else:
    print("Try again.")
