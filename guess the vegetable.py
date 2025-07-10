print("Pick either Carrot, Broccoli, Peas or Sweetcorn")
print("I will attempt to guess your choice")
print("Is the vegetable green?")
answer = input().lower()

if answer == "yes":
    print("Does it look like a tree?")
    answer = input().lower()
    if answer == "yes":
        print("It is peas!")
    else:
        print("It is broccoli!")
else:
    print("Is the colour orange?")
    answer = input().lower()
    if answer == "yes":
        print("It must be carrot!")
    else:
        print("It is sweetcorn")
