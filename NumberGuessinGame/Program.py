#Number Game
import random
Name_Input = input("What is Your name player? ")
print("Welcome to the Number Game " + Name_Input)
GameNumber = random.randint(0,100)
Number = -1

while Number != GameNumber:
    User_input = input("What is your number guess? ")
    Number = int(User_input)

    if Number > GameNumber:
        print("Dang" + Name_Input + " number {0} is too High".format(Number))
    elif Number < GameNumber:
        print("Dang" + Name_Input + " number {0} is too Low".format(Number))
    elif Number == GameNumber:
        print("WOW!" + Name_Input + " number {0} was spot on.".format(Number))
        print("Reopen to play again")
    else:
        print("Not a Number try again")



