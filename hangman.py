"""
=============================================================================
Project Name : CodeAlpha_HangmanGame
Internship   : CodeAlpha Python Programming Internship
Task         : Hangman Game
Description  : A console-based Hangman game built with Python standard library.
=============================================================================
"""

import random

# Predefined list of exactly 5 words as specified in the project requirements
WORD_LIST = [
    "python",
    "developer",
    "internship",
    "hangman",
    "challenge"
]

# ASCII art representing the 7 stages of Hangman (0 to 6 incorrect guesses)
HANGMAN_STAGES = [
    # Stage 0: 6 attempts left (0 incorrect guesses)
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    # Stage 1: 5 attempts left (1 incorrect guess)
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    # Stage 2: 4 attempts left (2 incorrect guesses)
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    # Stage 3: 3 attempts left (3 incorrect guesses)
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    # Stage 4: 2 attempts left (4 incorrect guesses)
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    # Stage 5: 1 attempt left (5 incorrect guesses)
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    # Stage 6: 0 attempts left (6 incorrect guesses - Game Over)
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# Maximum allowed incorrect attempts
MAX_INCORRECT_GUESSES = 6


def get_random_word(word_list):
    """
    Selects and returns a random word from the provided word list.
    
    Parameters:
        word_list (list): List of candidate words.
        
    Returns:
        str: A randomly chosen word in lowercase.
    """
    return random.choice(word_list).lower()


def display_hangman(incorrect_count):
    """
    Displays the ASCII hangman figure corresponding to the number of incorrect guesses.
    
    Parameters:
        incorrect_count (int): Number of incorrect guesses made so far (0 to 6).
    """
    print(HANGMAN_STAGES[incorrect_count])


def get_masked_word(secret_word, guessed_letters):
    """
    Constructs the masked word string where unguessed letters are hidden as underscores.
    
    Parameters:
        secret_word (str): The target secret word.
        guessed_letters (set): Set of letters guessed by the player.
        
    Returns:
        str: Space-separated representation of the word with letters and underscores.
    """
    display_chars = [
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    ]
    return " ".join(display_chars)


def display_game_state(secret_word, guessed_letters, incorrect_count):
    """
    Prints the complete status of the game including hangman art, masked word,
    guessed letters list, and remaining attempts.
    
    Parameters:
        secret_word (str): The target secret word.
        guessed_letters (set): Set of letters guessed by the player.
        incorrect_count (int): Number of incorrect guesses made so far.
    """
    display_hangman(incorrect_count)
    
    remaining_attempts = MAX_INCORRECT_GUESSES - incorrect_count
    
    print("-" * 45)
    print(f"Word: {get_masked_word(secret_word, guessed_letters)}")
    print("-" * 45)
    
    # Show sorted list of already guessed letters
    if guessed_letters:
        sorted_guesses = ", ".join(sorted(guessed_letters))
        print(f"Guessed letters: [ {sorted_guesses} ]")
    else:
        print("Guessed letters: [ None yet ]")
        
    print(f"Remaining incorrect attempts: {remaining_attempts} / {MAX_INCORRECT_GUESSES}")
    print("-" * 45)


def get_valid_guess(guessed_letters):
    """
    Prompts the user for a letter guess and validates the input.
    Ensures input is a single alphabetic character that has not been guessed yet.
    
    Parameters:
        guessed_letters (set): Set of letters already guessed by the player.
        
    Returns:
        str: A single valid, lowercase alphabetic letter.
    """
    while True:
        user_input = input("Enter a letter: ").strip().lower()
        
        # Check if input is exactly one alphabetic character
        if len(user_input) != 1 or not user_input.isalpha():
            print(">> Invalid input! Please enter a single alphabetic character (A-Z).")
            continue
            
        # Check if the letter was already guessed
        if user_input in guessed_letters:
            print(f">> You already guessed '{user_input.upper()}'. Please choose a different letter.")
            continue
            
        return user_input


def play_hangman():
    """
    Executes a single round of the Hangman game from start to finish.
    Tracks player guesses, updates game state, and determines win/loss outcome.
    """
    secret_word = get_random_word(WORD_LIST)
    guessed_letters = set()
    incorrect_guesses = 0
    
    print("\n" + "=" * 45)
    print("        LET'S PLAY HANGMAN!")
    print("=" * 45)
    print("Hint: The secret word has", len(secret_word), "letters.")
    
    # Main game loop for the round
    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        display_game_state(secret_word, guessed_letters, incorrect_guesses)
        
        # Prompt user for valid guess
        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)
        
        # Check if the guess is in the secret word
        if guess in secret_word:
            print(f"\n>> Good job! '{guess.upper()}' is in the word!")
            
            # Check if all unique letters in the secret word have been guessed
            if all(letter in guessed_letters for letter in secret_word):
                display_hangman(incorrect_guesses)
                print("\n" + "*" * 45)
                print(f"  CONGRATULATIONS! YOU WON! 🎉")
                print(f"  The secret word was: {secret_word.upper()}")
                print("*" * 45)
                return
        else:
            incorrect_guesses += 1
            remaining = MAX_INCORRECT_GUESSES - incorrect_guesses
            print(f"\n>> Sorry! '{guess.upper()}' is NOT in the word.")
            if remaining > 0:
                print(f">> You have {remaining} attempt{'s' if remaining != 1 else ''} left.")
    
    # If loop ends, maximum incorrect guesses were reached
    display_hangman(incorrect_guesses)
    print("\n" + "!" * 45)
    print("  GAME OVER! YOU RAN OUT OF ATTEMPTS. 💀")
    print(f"  The secret word was: {secret_word.upper()}")
    print("!" * 45)


def main():
    """
    Main entry point of the program.
    Welcomes the player, runs game rounds, and manages replay requests.
    """
    print("=" * 55)
    print("   WELCOME TO CODEALPHA HANGMAN GAME")
    print("   Created for CodeAlpha Python Internship")
    print("=" * 55)
    print(f"Rules:")
    print(f" - Guess one letter at a time.")
    print(f" - You can make up to {MAX_INCORRECT_GUESSES} incorrect guesses.")
    print(f" - Guess all letters to win before the hangman is complete!\n")
    
    # Replay loop
    while True:
        play_hangman()
        
        # Prompt player to play again
        while True:
            play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
            if play_again in ['y', 'yes']:
                print("\nStarting a new game...")
                break
            elif play_again in ['n', 'no']:
                print("\n" + "=" * 55)
                print(" Thank you for playing CodeAlpha Hangman! Goodbye! 👋")
                print("=" * 55)
                return
            else:
                print(">> Invalid choice! Please type 'y' for YES or 'n' for NO.")


if __name__ == "__main__":
    main()
