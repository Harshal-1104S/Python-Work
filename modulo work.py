'''this program will ask the user for input for 2 numbers if both numbers are even it will print
that both numbers are even. If they are not it will print atleast one of them in not even '''

#Prompt user to enter num
print("Enter in number 1: ")

#Create validation check to make sure they input correct num
try:
    num1 = int(input())
except ValueError:
    print("You must enter a number")
    num1 = int(input())

#Prompt user to enter num
print("Enter in number 2: ")

#Create validation check to make sure they input correct num
try:
    num2 = int(input())
except ValueError:
    print("You must enter a number")
    num2 = int(input())

#Check if both numbers are odd
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even")

#If not then print atleast one number is odd
else:
    print("Atleast one number is odd")
