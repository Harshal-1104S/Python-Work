print("welcome to split my pizza!")
print("How many slices are on the pizza?")
slices = int(input())
print("What is the total bill")
try:
    bill_total = float(input())
except ValueError:
    print("You must enter a number")
    bill_total = float(input())
print("How many people are sharing the pizza?")
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
print(f"total bill including tip is {bill_total}")
print(f"Total cost per person is {bill_total//people}")
slices_each = (slices//people)
print(f"Each person gets {slices_each:.2f} slice(s).")
slices_left = (slices%people)
print(f"There are {slices_left} slice(s) remaining.")
