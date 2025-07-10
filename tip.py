print("---Welcome to split my bill---")
print("What is the total bill")
try:
    bill_total = float(input())
except ValueError:
    print("You must enter a number")
    bill_total = float(input())
print("How many people are sharing")
people = int(input())
print("what percent tip would you like to leave?")
try:
    tip_percentage = int(input())
    tip_total = (tip_percentage/100)*bill_total
except ValueError:
    print("You must enter a valid percentage")
    tip_percentage = int(input())
    tip_total = (tip_percentage/100)*bill_total
bill_total = bill_total + tip_total
person_cost = bill_total//people
print(f"total bill including tip is {bill_total}")
print(f"Total cost per person is {person_cost}")
