'''This program is called split my pizza. It will ask the user to input how many slices on the pizza, how many people sharing the pizza then it will ask for total bill and add the delivery cost of the total bill. This will give us a total price to pay and it will output how much slices each person will get, remainder, and how much each person has to pay'''

#Welcome user to program
print ("-----Welcome to split my pizza------")

#Ask user how many slices on the pizza
print("How many slices on the pizza?")

#Create a validation check to insure that the number is a integer
try:
    slices= int(input())
except ValueError:
    print("You must enter a valid number")
    slices= int(input())

#Ask user how many people sharing pizza
print("How many people are sharing pizza")

#Create a validation check to insure that the number is a integer
try:
    people= int(input())
except ValueError:
    print("You must enter a number")
    people= int(input())

#Ask user for the total bill
print("What is the total bill for the pizza?")

#Create a validation check to insure that the number is a number
try:
    bill_total= float(input())
except ValueError:
    print("You must enter a valid number")
    bill_total= float(input())

#Prompt user to enter the delivery fee (tell them to put 0 if nothing)
print("How much was delivery?(0 if no delivery)")

#Create a validation check to insure that the number is a number
try:
    delivery= float(input())
except ValueError:
    print("You must enter a valid number")
    delivery= float(input())

#Calculate total including delivery
bill_total = bill_total + delivery

#Calculate each persons fee
each_person = bill_total/ people

#Calculate each slices by doing integer division
counters_each = slices//people

#Calculate how many slices will remain using modulo
counters_remain= slices % people

#Print how much each person will get and how much will remain
print("Each person will get",counters_each, "Slices each")
print("There will be", counters_remain, "Slices left")

#Print the total and how much each person has to pay
print("\nThe total for the pizza is", bill_total, "each person has to pay", each_person)
