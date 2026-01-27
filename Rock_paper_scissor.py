import random
#if it is tie than keep playing until there is a winner
#let random choice for both players        
#user to press enter to generate player choices
#ask user if they want to play again after a win
class RockPaperScissors:    
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']

    def play(self):
        # game loop
        while True:
            player1_choice = random.choice(self.choices)
            player2_choice = random.choice(self.choices)
            input("Press Enter to generate choices for both players...")
            print(f"Player 1 chooses: {player1_choice}")
            print(f"Player 2 chooses: {player2_choice}")

            if player1_choice == player2_choice:
                print("It's a tie! Let's play again.\n")
                continue
            elif (player1_choice == 'rock' and player2_choice == 'scissors') or \
                 (player1_choice == 'paper' and player2_choice == 'rock') or \
                 (player1_choice == 'scissors' and player2_choice == 'paper'):  
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")

            # another variable to start new game
            new_game = input("Do you want to play again? (yes/no): ").strip().lower()
            if new_game == 'yes':
                self.play()
            elif new_game == 'no':
                print("Thanks for playing!")
                break   
            else:
                break

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play() 

        