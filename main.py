import random

print(f"You are welcome to 'rock paper scissors' game. Enjoy it while it lasts")
print(f"----------------------------------------------------------------------")

while True:
    choices = ["rock", "paper", "scissors"]
    cpu = random.choice(choices)
    player = None

    while player not in choices:
        player = input(f"rock, paper, or  scissors?: ").lower()
        
        if player not in choices:
            print("Error, try again!")
            
        elif player == cpu:
            print(f"Player:",player, f"Cpu:",cpu)
            print(f"it's a tie!")
    
        elif player == "rock":
            if cpu == "paper":
                print(f"Player:", player, f"Cpu:", cpu)
                print(f"You lose!")
            if cpu == "scissors":
                print(f"Player:", player, f"Cpu:", cpu)
                print(f"You win!")
                
        elif player == "paper":
            if cpu == "scissors":
                print(f"Player:", player, f"Cpu:", cpu)
                print(f"You lose!")
            if cpu == "rock":
                print(f"Player:", player, f"Cpu:", cpu)
                print(f"You win!")
                
        elif player == "scissor":
            if cpu == "paper":
                print(f"Player:", (player), f"Cpu:", (cpu))
                print(f"You win!")
            if cpu == "rock":
                print(f"Player:", player, f"Cpu:", cpu)
                print(f"You lose!")

    print()
    play_again = input("Play again? (yes/no):").lower()
    
    if play_again != "yes":
        break

print(f"Game over!")