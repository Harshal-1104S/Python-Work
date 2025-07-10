print("enter a number")
try:
   number1 = int(input())
except ValueError:
    print("you must a number")
    number1 = int(input())

print("enter a number")
try:
   number2 = int(input())
except ValueError:
    print("you must a number")
    number1 = int(input())
print(number1 + number2)
