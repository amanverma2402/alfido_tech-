#-----------------------------------------
# number number_guessing_game
#-----------------------------------------
import random
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    random_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print(" Invalid input. Please enter a number between 1 and 100.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < random_number:
            print(" Too Low! Try again.")
        elif guess > random_number:
            print(" Too High! Try again.")
        else:
            print(f" Correct! The number was {random_number}.")
            print(f" You guessed it in {attempts} attempts!")
            break

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        number_guessing_game()
    else:
        print("Thanks for playing! Goodbye! 👋")

# Run the game
if __name__ == "__main__":
    number_guessing_game()

