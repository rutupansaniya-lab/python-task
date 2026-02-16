import random

def dice_roll(sides=6):
    """Simulates rolling a dice with a specified number of sides."""
    return random.randint(1, sides)

def get_input():
    """Get valid number of players from user."""
    while True:
        no_of_player = input("Enter number of players: ")
        if no_of_player.isdigit() and int(no_of_player) > 1:
            return int(no_of_player)
        else:
            print("Please enter a valid number of players (greater than 1).")

#  Full game loop
while True:

    no_of_player = get_input()   # input function call here
    player_total = {}

    # Game loop
    while True:
        for i in range(no_of_player):
            player_name = f"Player {i+1}"
            input(f"{player_name}, press Enter to roll the dice...")

            result = dice_roll()
            player_total[player_name] = player_total.get(player_name, 0) + result

            print(
                f"Player {i+1} rolled a {result}. "
                f"Total points: {player_total[player_name]}"
            )

            if player_total[player_name] >= 50:
                print(f"\n Player {i+1} wins with {player_total[player_name]} points!")
                another_game = input("Do you want to play another game? (yes/no): ").strip().lower()
                if another_game == "yes":
                    print("\n Starting a new game...\n")
                    break   # break game loop 
                else:
                    print("Thanks for playing! ")
                    exit()

        