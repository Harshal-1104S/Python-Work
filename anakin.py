print("What is your name?")
name = input().lower()
if name == "anakin":
  print("How do you do Anakin!")

elif name == "leia":
    print("The force is with you")

else:
  print(f"Nice name, {name}")
print(f"So {name}, is it hot or cold where you are today?")
weather = input().upper()
if weather == "COLD":
  print("You must be freezing!")
elif weather == "HOT":
  print("Drink plenty of water")
else:
  print("I can't advise you on that type of weather.")
print("Do you like the colour blue?")
likes_blue = input().lower()
if likes_blue == "yes":
  print("I like blue too")

else:
    print("That is a shame I really like blue")

print("What is your favourite food,",name)
favfood = input().lower()

if favfood == "pizza":
    print("That is my favourite food")

elif favfood == "pasta":
    print("I like that food too")

else:
    print("That sounds very good")

print("Have a good day! Bye!")
