import random

randomNumber = random.randint(1, 100)

numberOfTries = 0

# print(randomNumber, numberOfTries)

# loop through numberOfTries
while numberOfTries <= 10:
    print(f"Number of tries: {10-numberOfTries}")
    guessNumber = (input("Guess the number: "))
    print("Type 'quit' to finish")

    if guessNumber == randomNumber:
        print("You found it!")
        break
    elif guessNumber == "quit": break
    # else: print("Please input applicable number!")
     
    print("Wrong number")
    numberOfTries+=1
    again = input("Wanna play again? Y/N ")
    if again.lower() in ["n"]: break
        

if numberOfTries > 10: print("You have used all your tries. You lost!!!")