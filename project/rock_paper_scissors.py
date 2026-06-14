# Rock, Paper, Scissors Game

# A simple command-line Rock, Paper, Scissors game built with Python. The player competes against the computer, 
# which makes random choices each round.


            # Features

#           User-friendly command-line interface
#           Input validation to prevent invalid choices
#           Random computer moves
#           Winner determination based on game rules
#           Option to play multiple rounds


        #Game Rules

#           Stone beats Scissors
#           Scissors beats Paper
#           Paper beats Stone
#           If both players choose the same option, the game ends in a tie


        #Example Gameplay


#           Welcome to Rock, Paper, Scissors Game!
#           Enter your choice (stone, paper, scissors): stone
#           You chose: stone
#           Computer chose: scissors
#           You win!
#           Do you want to play again? (yes/no): yes 


        # Functions


#           get_user_choice()
#           Prompts the user to enter a valid choice and validates the input.

#           get_computer_choice()
#           Randomly selects one of the available choices: stone, paper, or scissors.
#           determine_winner(user_choice, computer_choice)
#           Determines the winner based on the game rules and returns the result.




        #Created as a beginner-friendly Python project to practice:

#Functions
#Loops
#Conditional statements
#User input handling
#Random module usage


        #Future Improvements


#           Add score tracking
#           Add a graphical user interface (GUI)
#           Support Rock-Paper-Scissors-Lizard-Spock
#           Store game history
#           Add multiplayer mode



#           Author:- Aakash kumar


import random
def get_user_choice():
    user_input = input("Enter your choice (stone, paper, scissors): ")
    while user_input not in ["stone", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        user_input = input("Enter your choice (stone, paper, scissors): ")
    return user_input
def get_computer_choice():
    choices = ["stone", "paper", "scissors"]
    return random.choice(choices)
def determine_winner(user_choice , computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "stone" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "stone") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

print("Welcome to Rock, Paper, Scissors Game!")
while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for playing! Goodbye!")
        break
