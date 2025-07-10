#getting a gym membership
print("Welcome to LA Fitness!") #welcomes the user
name = input("What is your name: ") #input name
try:
    age = int(input("how old are you: ")) #input age
except ValueError: #validation check
    contact = int(input("What is your phone number: ")) #input phone number
email = input("what is your email address: ") #input email
phone = input("what is your home adress: ") #input home adress
health = input("do you have any medical conditions: ") #input medical conditions
emergency = int(input("Please put down an emergency contact number: ")) #input number
goals = input("What are you fitness goals: ") #input goals you want to accomplish
improvement = input("What body parts do you want to strengthen?: ")
print("would you like a basic membership which costs $150 for 4 months or a premium membership which costs $200 for 8 months: ") #description of each option
membership_type = input("Enter membership type (Basic/Premium): ") #choice between the two options
input("now lets proceed to the payment, how would you like to pay? (only card): ") #input payment type
print("loading....")
try: #validation check
    int(input("enter your pin: ")) #input your pin
except ValueError:
    print("payment successful") #payment went through
print(f"Thank you for registering {name}!") #you are now a member
print("Name:", name)
print("Membership Type:", membership_type)
