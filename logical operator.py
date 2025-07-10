total_cost = 0.00
sugar_tax = 0.50
print("Sandwich or Wrap?")
bread_type = input().lower()
print("Meat, Vegetarian or Vegan?")
filling_type = input().lower()
print("Cookie, Crisps, Fruit or None")
pudding = input().lower()
print("Fizzy drink, Water, Juice or None")
drink = input().lower()
print("would you like an extra sauce? Yes or No")
extra_sauce = input().lower()
print("would you like an extra salad? Yes or No")
extra_salad = input().lower()

if bread_type != "sandwich":
    total_cost = 2.00
else:
    total_cost = 3.00

if filling_type == "vegetarian" or filling_type == "vegan":
    total_cost = total_cost + 1.00
else:
    total_cost = total_cost + 1.50

if pudding == "cookie" and drink == "fizzy drink":
    total_cost = total_cost + sugar_tax

if pudding == "none" or drink == "none":
    total_cost = total_cost - 0.50

if extra_sauce == "yes":
    total_cost = total_cost + 0.40

if extra_salad == "yes":
    total_cost = total_cost + 0.80

if extra_sauce == "yes" and extra_salad == "yes":
    total_cost = total_cost + 1.00

print(f"Your total cost is: £{total_cost}")

