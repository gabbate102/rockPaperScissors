# rockPaperScissors.py
# author: Giovanni Abbate
# version 1.1

# import random and time modules
import random
import time

# constants for possible results
TIE = 0
COMP_WIN = -1
USER_WIN = 1

# define main()
def main():
    # print welcome message
    print("Welcome to Rock Paper Scissors!\nPlay against the CPU\n" +
          "----------------------------------------")

    # create hands list to hold possible hands
    hands = ["rock", "paper", "scissors"]

    play = "yes"
    while play == "yes" or play == "y":   
        try:
            userInput = input("Please choose rock, paper, or scissors: ")
            usrHand = hands.index(userInput.lower())
        
            # create random number between 0-3 and assign to cpuHand
            cpuHand = random.randint(0, 2)
            print("Computer chose:", hands[cpuHand] , "\n")
            # call the sleep function to add delay to game
            time.sleep(1)
            # call the compare function to get the result
            compare(usrHand, cpuHand)

            # ask the user if they would like to play again
            play = input("-----------------\n" + "Play again? yes/no: ").lower()
            print("-----------------")
        except ValueError:
            print("Invalid choice. Please only enter rock, paper, or scissors.")
    return

# define compare()
def compare(usrHand, cpuHand):
    # create dictionary of winning pairs for usr
    usrWin = {0:2, 2:1, 1:0}
    
    # check if tie
    if usrHand == cpuHand:
        print("It's a tie!")
    # check if user won    
    elif (usrHand, cpuHand) in usrWin.items():
        print("You won!")
    # check if computer won
    else:
       print("You lost!")
    return

# call main()
main()
