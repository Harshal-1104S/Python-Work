score = 0
print("Welcome to JokeMaster!")
print("do you want to hear a joke?")
joke = input()
if joke == "yes":
    print("okay here we go")
print("What is pink and fluffy?")
guess_1=input().lower()
if guess_1 == "pink fluff":
    print("you are correct")
    score = score+1
else:
    print("You are incorrect! The answer is pink fluff")
print(score)
print("What is brown and sticky?")
guess_2=input().lower()
if guess_2 == "a brown stick":
    print("you are correct")
    socre = score+1
elif guess_2 == "brown stick":
    print("you are correct")
    score = score+1
else:
    print("You are incorrect! The answer is a brown stick")
print(score)
print("What is black and white and red all over?")
guess_3=input().lower()
if guess_3 == "a newspaper":
    print("you are correct")
    score =  score+1
elif guess_3 == "newspaper":
    print("you are correct")
    score =  score+1
else:
    print("You are incorrect! The answer is a newspaper")
print(score)





