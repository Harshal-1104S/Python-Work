print("Pick either Ostrich, Lion, Fish or Whale")
print("I will attempt to guess your choice")
print("Does the animal live in the water? Y/N")
answer = input().lower()

if answer == "n":
   print("Does the animal have wings? Y/N")
   answer = input().lower()
   if answer == "y":
    print("It must be an Ostrich!")
   else:
    print("It must be a Lion!")
else:
   print("is this animal a mammal? Y/N")
   answer = input().lower()
if answer == "y":
   print("It must be a Whale!")
else:
   print("It must be a fish!")
