import random
def Dice_Roll(sides=6):
    """Simulates rolling a dice with a specified number of sides.

    Args:
        sides (int): The number of sides on the dice. Default is 6.

    Returns:
        int: A random integer between 1 and the number of sides, inclusive.
    """
    return random.randint(1, sides)
# roll dice till one of the player get total 50 points
Total_of_player={}
while True:
    no_of_player=input("Enter number of players: ")
    if no_of_player.isdigit() and int(no_of_player)>1:
        break
    else:
        print("Please enter a valid number of players (greater than 1).")   
# Game loop for not exiting till one player reaches 50 points
while True: 
    # Iterate through each player
    for i in range(int(no_of_player)):
        # Prompt the player to roll the dice
        input(f"Player {i+1}, press Enter to roll the dice...")
        result = Dice_Roll()
        # Update the player's total score
        Total_of_player[f"Player {i+1}"] = Total_of_player.get(f"Player {i+1}", 0) + result                             
        print(f"Player {i+1} rolled a {result}. Total points: {Total_of_player[f'Player {i+1}']}")
        # Check if the player has reached or exceeded 50 points
        if Total_of_player[f"Player {i+1}"] >= 50:
            print(f"Player {i+1} wins with {Total_of_player[f'Player {i+1}']} points!")
            another_game=input("Do you want to play another game? (yes/no): ").strip().lower()
            if another_game == 'yes':
                Total_of_player.clear()
                break
            else:
                print("Thanks for playing!")
                exit()        
