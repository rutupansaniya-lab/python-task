import random
def generate_random_number(start=1, end=100):
    """Generate a random number between start and end (inclusive)."""
    return random.randint(start, end)
def check_guess(guess, target):
    """Check if the guess is lower, higher, or equal to the target number."""
    if guess < target:
        return "lower"
    elif guess > target:
        return "higher"
    else:
        return "correct"
def main():
    print("Welcome to the Number Guessing Game!")
    target_number = generate_random_number()
    attempts = 0
    while True:
        try:
            user_guess = int(input("Enter your guess (1-100): "))
            attempts += 1
            result = check_guess(user_guess, target_number)
            if result == "correct":
                print(f"Congratulations! You've guessed the number {target_number} in {attempts} attempts.")
                break
            else:
                print(f"Your guess is too {result}. Try again.")
        except ValueError:
            print("Please enter a valid integer.")
if __name__ == "__main__":
    main()