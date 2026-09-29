import random


def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    print("=" * 40)
    print("   WELCOME TO ROCK-PAPER-SCISSORS GAME   ")
    print("=" * 40)
    print("Instructions:")
    print(" - Type 'rock', 'paper', or 'scissors' to make your choice.")
    print(" - Rock beats Scissors | Scissors beats Paper | Paper beats Rock")

    while True:
        print("\n" + "-" * 35)

        # User Input
        user_choice = (
            input("Enter your choice (rock/paper/scissors): ").strip().lower()
        )

        if user_choice not in choices:
            print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
            continue

        # Computer Selection
        computer_choice = random.choice(choices)

        # Display Choices
        print(f"\nYour choice    : {user_choice.capitalize()}")
        print(f"Computer choice: {computer_choice.capitalize()}")

        # Game Logic & Display Result
        if user_choice == computer_choice:
            print("Result         : It's a Tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "scissors" and computer_choice == "paper")
            or (user_choice == "paper" and computer_choice == "rock")
        ):
            print("Result         : You Win! 🎉")
            user_score += 1
        else:
            print("Result         : Computer Wins! 🤖")
            computer_score += 1

        # Score Tracking
        print(f"\n--- SCORE BOARD ---")
        print(f"User: {user_score} | Computer: {computer_score}")

        # Play Again
        play_again = (
            input("\nDo you want to play another round? (yes/no): ")
            .strip()
            .lower()
        )
        if play_again not in ("yes", "y"):
            print("\n" + "=" * 40)
            print("         FINAL SCOREBOARD         ")
            print(f"   User: {user_score}   |   Computer: {computer_score}")
            print("=" * 40)
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    rock_paper_scissors()
