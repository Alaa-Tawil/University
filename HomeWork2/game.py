import random

choices = ['rock', 'paper', 'scissors']


def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice. Please choose again.")


def get_computer_choice():
    return random.choice(choices)


def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "It's a tie!"
    elif (choice1 == 'rock' and choice2 == 'scissors') or \
            (choice1 == 'scissors' and choice2 == 'paper') or \
            (choice1 == 'paper' and choice2 == 'rock'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"


def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    mode = input("Choose mode (1: Player vs Computer, 2: Player vs Player): ")

    player1_score = 0
    player2_score = 0
    rounds_played = 0

    if mode == '1':
        while True:
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            print(f"Computer chose: {computer_choice}")
            result = determine_winner(user_choice, computer_choice)
            print(result)

            rounds_played += 1
            if "Player 1" in result:
                player1_score += 1
            elif "Player 2" in result:
                player2_score += 1

            print(f"Score after round {rounds_played}: Player 1: {player1_score}, Computer: {player2_score}")

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                break

    elif mode == '2':
        while True:
            print("Player 1:")
            player1_choice = get_user_choice()
            print("Player 2:")
            player2_choice = get_user_choice()
            result = determine_winner(player1_choice, player2_choice)
            print(result)

            rounds_played += 1
            if "Player 1" in result:
                player1_score += 1
            elif "Player 2" in result:
                player2_score += 1

            print(f"Score after round {rounds_played}: Player 1: {player1_score}, Player 2: {player2_score}")

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                break

    else:
        print("Invalid mode selected. Please restart the game and choose a valid mode.")
        return

    print(f"\nGame over! You played {rounds_played} rounds.")
    print(f"Player 1 score: {player1_score}")
    if mode == '1':
        print(f"Computer score: {player2_score}")
    else:
        print(f"Player 2 score: {player2_score}")


if __name__ == "__main__":
    play_game()
