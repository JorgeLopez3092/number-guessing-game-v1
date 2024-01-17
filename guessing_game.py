"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import the random module.
import random
# Create the start_game function.
def start_game(high_score):
# Write your code inside this function.\
    #   When the program starts, we want to:
    #   ------------------------------------
    #   1. Display an intro/welcome message to the player.
    # Determine the high score message
    if high_score == float('inf'):
        high_score_message = "Set the high score!"
    else:
        high_score_message = f"Current High Score to Beat: {high_score} Guesses"
    print(f"""
    🌟🚀🌟 WELCOME TO THE ULTIMATE GUESSING GAME! 🌟🚀🌟

    🔮 "Can You Outsmart the Machine? Predict the Number, Claim the Glory!" 🔮

    🎯 Ready... Set... Guess! 🎯
    💥 {high_score_message} 💥
    """)
    #   2. Store a random number as the answer/solution.
    low_range = 1
    high_range = 21
    number_to_guess = random.randrange(low_range, high_range)
    guess_count = 0
    user_guess = None
    has_error = False
    #   3. Continuously prompt the player for a guess.
    while user_guess != number_to_guess:
        try:
            if user_guess is None and has_error == False:
                user_guess = int(input(f"Guess a number between {low_range} and {high_range - 1}\n> "))
            elif user_guess is None:
                user_guess = int(input("> "))
            else:
                if user_guess > number_to_guess:
                    user_guess = int(input("WRONG! It's lower! Try again:\n> ")) if guess_count <= 1 else int(input("WRONG AGAIN! It's lower! Try again:\n> "))
                elif user_guess < number_to_guess:
                    user_guess = int(input("WRONG! It's higher! Try again:\n> ")) if guess_count <= 1 else int(input("WRONG AGAIN! It's higher! Try again:\n> "))
            if user_guess < low_range or user_guess > high_range:
                print(f"""
    🚨👽 WHOOPS! OUT OF BOUNDS! 👽🚨
    
    Your guess must be between {low_range} and {high_range - 1}.
    Try channeling your psychic powers within the right range! 🧙‍♂️
    """)
                has_error = True
                user_guess = None
                continue
            guess_count += 1

        except ValueError:
            print("""
    🚨👾 ERROR! 👾🚨
    The Oracle speaks only in numbers! 🧙‍♂️
    Please enter a valid number to continue your quest.""")
            has_error = True
    # 4. Once the guess is correct, stop looping, inform the user they "Got it"
    if guess_count == 1:
        print("""
    🌠🥇🌠 UNBELIEVABLE! FIRST TRY VICTORY! 🌠🥇🌠

    You're a True Guessing Wizard! 🧙‍♂️
    You nailed it on the first attempt! Are you psychic? 🤯

    🏆 A Legend is Born! 🏆
    """)
    elif guess_count < 5:
        print(f"""
    🎉👍 GREAT JOB! You Guessed It within {guess_count} tries! 🎉👍

    Not bad at all! You've got some serious guessing skills. 👀

    🌟 Ready to beat your own record? Give it another go! 🌟
    """)
    else:
        print(f"""
    🎈🔍 FINALLY! You Did It after {guess_count} tries! 🎈🔍

    Persistence pays off! You cracked the code after a few tries. 💪

    💡 Think you can do it faster? Try again to prove it! 💡
    """)
    new_high_score = guess_count if guess_count < high_score else high_score
    play_again = input("\nDo you want to play again? (y/n): ").lower().strip()
    if play_again == "y":
        print("\nStarting a new game!")
        start_game(new_high_score)
    else:
        print("\n🌌 The portal closes and the machine powers down...")

#      and show how many attempts it took them to get the correct number.
#   5. Let the player know the game is ending, or something that indicates the game is over.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.
start_game(float('inf'))