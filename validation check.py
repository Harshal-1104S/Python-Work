print("what is your first initial")
initial = input()
print("what is your surname")
surname = input()
print("what is your age")
age = int(input())
print("true or false - you like marmite")
likes_marmite = input()
marmite = "true"
decades = float((age/10))
print(f"well hello {initial}{surname}.")
print(f"It is {likes_marmite==marmite} that you like marmite.")
print(f"this is probably because you are {decades} decades old")

