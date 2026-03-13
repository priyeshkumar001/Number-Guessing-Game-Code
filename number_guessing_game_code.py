import random

def number_guessing_game():
    # 1. Generate the random number
    secret_number = random.randint(1, 100)

    # 2. Initialize game variables
    max_guesses = 7
    guesses_taken = 0

    # Game introduction
    print("👋 Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_guesses} attempts to guess it.")

    # 3. Main game loop
    while guesses_taken < max_guesses:
        try:
            # Get the user's guess
            guess = int(input(f"\nAttempt #{guesses_taken + 1}: Enter your guess: "))

            # Check if the guess is within the valid range
            if not (1 <= guess <= 100):
                print("⚠️ Please guess a number between 1 and 100 only.")
                continue # Skip incrementing the guess counter

            guesses_taken += 1

            # 4. Check the guess against the secret number
            if guess < secret_number:
                print("⬇️ Too low! Try a higher number.")
            elif guess > secret_number:
                print("⬆️ Too high! Try a lower number.")
            else:
                # Guessed correctly! Break the loop
                print(f"\n🎉 Congratulations! You guessed the number {secret_number} correctly!")
                print(f"You took {guesses_taken} attempts.")
                return # End the function/game

        except ValueError:
            # Handle non-integer input
            print("🚫 Invalid input. Please enter a whole number.")

    # 5. Handle failure (when loop finishes without a 'return')
    print("\n😞 Game Over! You ran out of attempts.")
    print(f"The number I was thinking of was: {secret_number}")

# Start the game
if __name__ == "__main__":
    number_guessing_game()
