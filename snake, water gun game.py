'''
Game Rules
Snake drinks water → Snake wins.
Water douses gun → Water wins.
Gun kills snake → Gun wins.
Same choice → Draw.
'''
import random                                                      # imports the random module used to generate random choices for the computer. 

def get_computer_choice():                                         # this is a function get_computer_choice().
    return random.choice (['snake', 'water', 'gun'])               # it returns a random choice from a list

def determine_winner(user,computer):                               # this is a function determine_winner() it takes two parameters (user,computer)
    if user == computer:
        return "draw"                                              # it return "draw" if both user & computer choose same
        
    elif(user == "snake" and computer == "water") or\
        (user == "water" and computer == "gun") or\
        (user == "gun" and computer == "snake"):
        return "user"                                               # if any of these are true, the function returns "user"
    
    else:
        return "computer"                                          # if its not a draw and the user didn't win, then it return computer win
        
def play_game():                                                   # it defines the main function play_game() and displays welcome messages
    print("welcome to the game")
    print("enter your choice: snake, water, gun")
    
user_choice = input("enter your choice: ").lower()                 # it ask the user to type their choice
if user_choice not in ['snake', 'water', 'gun']:
    print("invalid choice, please choise snake, water, gun")       # if the user type wrong then it prints this line

computer_choice = get_computer_choice()
print(f"computer choice: {computer_choice}")

result = determine_winner(user_choice, computer_choice)

if result == "user":                                               # Prints the final outcome based on the result
    print("you win")
    
elif result == "computer":
    print("computer win")
    
else:
    print("draw")
    
play_game                                                         # it calls the play_game() function to start the game