print("What your first intial?")
intial = input()
print("What is your surname")
surname = input()
print("What is your age?")
try:
    age = int(input())
except ValueError:
    print("You must enter a number!")
    age = int(input())
print("True or False - you like marmite")
likes_marmite = input()
marmite = "True"
decades = float((age/10 ))
print(f"Well hello {intial} {surname}.")
print(f"It is {likes_marmite==marmite} that you like marmite.")
print(f"This is probably because you are {decades} decades old")
