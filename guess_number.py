import random

def start_game():
    print("\nWelcome to the Number Guessing Game!")

    # Difficulty level
    print("Choose difficulty level: Easy / Medium / Hard")
    difficulty = input("Enter difficulty: ").lower()

    if difficulty == "easy":
        max_attempts = 15
    elif difficulty == "medium":
        max_attempts = 10
    elif difficulty == "hard":
        max_attempts = 5
    else:
        print("Invalid input. Defaulting to Medium difficulty.")
        max_attempts = 10

    number = random.randint(1, 100)
    attempts = 0

    while attempts < max_attempts:
        guess = input("\nGuess a number between 1 and 100: ")

        if not guess.isdigit():
            print("❌ Please enter a valid number.")
            continue

        guess = int(guess)

        # Range check
        if guess < 1 or guess > 100:
            print("⚠️ Number out of range! Try a number between 1 and 100.")
            continue

        attempts += 1

        if guess < number:
            print("🔻 Too low! Try again.")
        elif guess > number:
            print("🔺 Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
            break
    else:
        print(f"💥 You've used all {max_attempts} attempts! The number was {number}.")

# Game loop
while True:
    start_game()
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("👋 Thanks for playing! Goodbye.")
        break
