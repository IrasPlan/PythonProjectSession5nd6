# form random import choice


# virtual bartender
drinks = ["vodka", "wiskey", "gin", "tequila", "rum", "rakia", "sake"]
print("Welcome to la Irish Irish")
name = input("I am the virtual bartender, how do I call you? ")
try:
    age = input(f"How old are you, {name}? ")
    age = int(age) #try to convert to a number
    legal = False
    if age >= 21:
        legal = True
    elif age < 16:
        legal = False
    else:
        country = input(f"Where are you from, {name}? ")
        if age >= 21:
            legal = True
        elif age < 21 and country == "USA":
            legal = False
        elif age >= 18 and country != "USA":
            legal = True
        elif age >= 16 and country == "Luxemburg":
            legal = True
    if age > 120 or age < 5:
        print(f"Please do not lie to the virtual bartender {name}")
    if legal:
        print(f"Congratulations {name}, you are allowed to drink")
        print(f"Here is a list of drinks for you: {drinks}")
    else:
        print(f"Dear {name}, I am not allowed to serve you a drink")
except ValueError:
    print("Please give a valid age")