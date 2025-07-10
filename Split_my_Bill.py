print ("Welcome to split my bill")

print("What is the total bill?")
try:
    bill_total= float(input())
except ValueError:
    print("You must enter a valid number")
    bill_total= float(input())


print("How many people are sharing")

try:
    people= int(input())
except ValueError:
    print("You must enter a number")
    people= int(input())

print("What percent tip would you like to leave?")

try:
    tip= int(input())
except ValueError:
    print("You must enter a number")
    tip= int(input())


#percent_decimal = tip/100
#tip_total = bill_total * percent_decimal
#bill_total = bill_total + tip_total

bill_total = bill_total + ((tip/100) * bill_total)

cost_per_person = bill_total/ people

print("total bill including tip is $", bill_total)
print("total cost per person is $", cost_per_person)
