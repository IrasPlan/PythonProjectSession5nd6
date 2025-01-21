name = input("What is your name? ")
print("Hello", name)
age = input("How old are you? ")
try:
    #another way to format print is via f-string
    print(f"{name}, you were born in {2024-int(age)}") #the things that you have giving it earlier that is using has to go on {}, when using f""
    #ahsdjah
    #division = int(age) / 0
except ValueError:
    print("Age must be a valid number")
    print(f"The value that you typed was {age}")
    print("please try agian")
    age = input("How old are you? ")
    print(f"{name}, you were born in {2024 - int(age)}")
except ZeroDivisionError:
    print("You can't divide by 0")
except:
    print("I have no idea what else could go wrong")
else: #in case no exception happened
    print("Thank you for being a good gentelman")
finally:
    print("Thanks for playing")