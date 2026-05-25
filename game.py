import random
import time


def loading_animation():
    print("Initializing Guess The Number", end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="")
    print("\n")


def play_game():
    print("=" * 45)
    print("        WELCOME TO GUESS THE NUMBER")
    print("=" * 45)

    player_name = input("Enter your name: ").strip()

    print(f"\nHello, {player_name}!")
    print("I have selected a random number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.\n")

    secret_number = random.randint(1, 100)
    attempts = 0

    start_time = time.time()

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.\n")
                continue

            if guess < secret_number:
                print("Too low! Try a higher number.\n")

            elif guess > secret_number:
                print("Too high! Try a lower number.\n")

            else:
                end_time = time.time()
                total_time = round(end_time - start_time, 2)

                print("\n" + "=" * 45)
                print("            CONGRATULATIONS!")
                print("=" * 45)
                print(f"You guessed the correct number: {secret_number}")
                print(f"Total Attempts : {attempts}")
                print(f"Time Taken     : {total_time} seconds")

                if attempts <= 5:
                    print("Performance    : Excellent")
                elif attempts <= 10:
                    print("Performance    : Good")
                else:
                    print("Performance    : Keep Practicing")

                print("=" * 45)
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.\n")


def main():
    loading_animation()

    while True:
        play_game()

        choice = input("\nDo you want to play again? (yes/no): ").lower()

        if choice != "yes":
            print("\nThank you for playing!")
            print("Goodbye!")
            break

        print("\nRestarting Game...\n")
        time.sleep(1)


if __name__ == "__main__":
    main()