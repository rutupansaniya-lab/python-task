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
    Total_of_player = {}

    # Game loop
    while True:
        for i in range(no_of_player):
            input(f"Player {i+1}, press Enter to roll the dice...")

            result = dice_roll()
            Total_of_player[f"Player {i+1}"] = Total_of_player.get(f"Player {i+1}", 0) + result

            print(
                f"Player {i+1} rolled a {result}. "
                f"Total points: {Total_of_player[f'Player {i+1}']}"
            )

            if Total_of_player[f"Player {i+1}"] >= 50:
                print(f"\n Player {i+1} wins with {Total_of_player[f'Player {i+1}']} points!")

                another_game = input("Do you want to play another game? (yes/no): ").strip().lower()
                if another_game == "yes":
                    print("\n Starting a new game...\n")
                    break   # break game loop → ask players again
                else:
                    print("Thanks for playing! ")
                    exit()

        