import random

comp_wins = 0
player_wins = 0

def Choose_Option():
    user_choice = input("Choose Rock, Paper or Scissors: ")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"
    else:
        print("I don't understand, try again.")
        Choose_Option()
    return user_choice

def Computer_Option():
    comp_choice = random.choice(['r','p','s'])
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice


while True:
    print("")
    
    user_choice = Choose_Option()
    comp_choice = Computer_Option()

    print("")
    
    if user_choice == "r":
        if comp_choice == "r":
            print("Player (Rock) : CPU (Rock). You tied.")
        
        elif comp_choice == "p":
            print("Player (Rock) : CPU (Paper). You lose.")
            comp_wins += 1
            
        elif comp_choice == "s":
            print("Player (Rock) : CPU (Scissors). You win.")
            player_wins += 1

    elif user_choice == "p":
        if comp_choice == "r":
            print("Player (Paper) : CPU (Rock). You win.")
            player_wins += 1
        
        elif comp_choice == "p":
            print("Player (Paper) : CPU (Paper). You tied.")
            
            
        elif comp_choice == "s":
            print("Player (Paper) : CPU (Scissors). You lose.")
            comp_wins += 1

    elif user_choice == "s":
        if comp_choice == "r":
            print("Player (Scissors) : CPU (Rock). You lose.")
            comp_wins += 1
        
        elif comp_choice == "p":
            print("Player (Scissors) : CPU (Paper). You win.")
            player_wins += 1
            
        elif comp_choice == "s":
            print("Player (Scissors) : CPU (Scissors). You tied.")

    print("")
    print("Player wins: " + str(player_wins))
    print("Computer wins: " + str(comp_wins))
    print("")
    
    user_choice = input("Do you want to play again? (yes/no) ")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break