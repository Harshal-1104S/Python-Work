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
likes_blue = input().upper()
if likes_blue == "YES":
  print("I like blue too")
else:
  print("That's a shame because I really like blue")
print("who is your favourite basketball player?")
favourite_basketball_player = input().lower()
if favourite_basketball_player == "lebron james":
  print("he is the goat")
elif favourite_basketball_player == "micheal jordan":
  print("He is elite")
else:
  print("That's an unpopular opinion but still a very good player")
  print("Have a good day! Bye!")
