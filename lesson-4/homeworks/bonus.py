import random

# initial values
userPoints = 0
pcPoints = 0

# R-Rock, P-Paper, S-Scissors
choices = ["R", "P", "S"]



while userPoints <5 and pcPoints <5:
    pcChoice = random.choice(choices)
    actualChoice = random.choice(choices)
    print(actualChoice)

    print("Rock, Paper or Scissors? R/P/S")
    userChoice = input("Input: ")

    # checks if user inputted blank or not
    if userChoice.strip() == "":
        print("Please input R/P/S")
    else:

        # checks choices
        if userChoice == pcChoice and userChoice == actualChoice:
            print("Both of you found right!")
            userPoints+=1
            pcPoints+=1
            print(f"You: {userPoints} \nComputer: {pcPoints}")

        elif userChoice==actualChoice and pcChoice != actualChoice:
            print("You found it right!")
            print(f"Computer's choice: {pcChoice}")
            userPoints+=1
            print(f"You: {userPoints} \nComputer: {pcPoints}")

        elif pcChoice == actualChoice and userChoice != actualChoice:
            print("Computer found it right!")
            print(f"Your choice: {userChoice}")
            pcPoints+=1
            print(f"You: {userPoints} \nComputer: {pcPoints}")

        elif userChoice != actualChoice and pcChoice != actualChoice: 
            print("Both of you didn't find it!")
            print(f"You: {userPoints} \nComputer: {pcPoints}")
    
    # identify the winner
    if userPoints == 5: print("YOU WON!!!"); break
    elif pcPoints == 5: print("COMPUTER WON!!!"); break
    