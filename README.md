# CodeAlpha_HangmanGame 🎮

A classic, console-based **Hangman Game** built with Python using only standard libraries. Developed as part of the **CodeAlpha Python Programming Internship**.

---

## 📌 Project Overview

**CodeAlpha_HangmanGame** is an interactive, text-based terminal game where the player tries to guess a secret word one letter at a time within a limited number of attempts (6 incorrect guesses maximum). The game features dynamic ASCII art gallows, input validation, guess history tracking, masked word display, and a replay system.

---

## 🚀 Features

- **Predefined Word List**: Contains a curated list of exactly 5 words related to programming and challenges.
- **Random Word Selection**: Leverages Python's `random` module to select a word each round.
- **Dynamic ASCII Gallows**: Displays 7 progressive visual stages of the hangman figure as incorrect guesses occur.
- **Masked Word Display**: Unguessed letters remain hidden as underscores (`_`), revealing letters as they are correctly identified.
- **Guessed Letters Tracking**: Shows an alphabetically sorted list of all guessed letters to assist the player.
- **Duplicate Guess Prevention**: Detects repeated letter guesses without penalizing player attempts.
- **Input Validation**: Validates user input to accept only single alphabetic characters (`A-Z`), gracefully handling numbers, symbols, spaces, and multi-character strings.
- **Attempt Countdown**: Clearly tracks and displays remaining incorrect attempts (out of 6).
- **Clear Game End Conditions**: Displays bold victory (`WIN`) and defeat (`GAME OVER`) messages along with the revealed secret word.
- **Replay Feature**: Gives the player the option to start a new game round without restarting the program.
- **Clean & Modular Code**: Structured using functions with comprehensive docstrings and beginner-friendly comments.

---

## 🛠️ Technologies Used

- **Language**: Python 3 (Python 3.6+ recommended)
- **Built-in Modules**:
  - `random` (for `random.choice()` word selection)
- **External Dependencies**: None (Zero third-party installations required)

---

## 📥 How to Install and Run

### Prerequisites
Make sure Python 3 is installed on your system. You can verify your Python version by running:
```bash
python --version
```
*(or `python3 --version` on Linux/macOS)*

### Installation & Execution

1. **Clone or Download the Repository**:
   ```bash
   git clone https://github.com/your-username/CodeAlpha_HangmanGame.git
   cd CodeAlpha_HangmanGame
   ```

2. **Run the Game**:
   ```bash
   python hangman.py
   ```
   *(or `python3 hangman.py`)*

---

## 🎲 How the Game Works

1. The game randomly chooses a secret word from a predefined list of 5 words.
2. The player is presented with a blank gallows and the word masked with underscores (`_ _ _ _ _ _`).
3. On each turn:
   - The player enters a single letter guess.
   - If the letter is in the secret word, its occurrences are revealed.
   - If the letter is NOT in the secret word, an incorrect attempt is deducted and the hangman gallows advances.
4. **Win Condition**: The player successfully guesses all the letters before using up 6 incorrect guesses.
5. **Loss Condition**: The player accumulates 6 incorrect guesses and the hangman figure is fully drawn.
6. The secret word is revealed, and the player is prompted whether they want to play another round (`y/n`).

---

## 🖥️ Sample Output

### 1. Game Start & Correct Guess
```text
=======================================================
   WELCOME TO CODEALPHA HANGMAN GAME
   Created for CodeAlpha Python Internship
=======================================================
Rules:
 - Guess one letter at a time.
 - You can make up to 6 incorrect guesses.
 - Guess all letters to win before the hangman is complete!


=============================================
        LET'S PLAY HANGMAN!
=============================================
Hint: The secret word has 6 letters.

       +---+
       |   |
           |
           |
           |
           |
    =========
    
---------------------------------------------
Word: _ _ _ _ _ _
---------------------------------------------
Guessed letters: [ None yet ]
Remaining incorrect attempts: 6 / 6
---------------------------------------------
Enter a letter: p

>> Good job! 'P' is in the word!
```

### 2. Incorrect Guess & ASCII Update
```text
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    
---------------------------------------------
Word: p _ _ _ _ _
---------------------------------------------
Guessed letters: [ a, p ]
Remaining incorrect attempts: 5 / 6
---------------------------------------------
>> Sorry! 'A' is NOT in the word.
>> You have 5 attempts left.
```

### 3. Victory Screen
```text
       +---+
       |   |
           |
           |
           |
           |
    =========
    
*********************************************
  CONGRATULATIONS! YOU WON! 🎉
  The secret word was: PYTHON
*********************************************

Do you want to play again? (y/n): 
```

### 4. Game Over Screen
```text
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  GAME OVER! YOU RAN OUT OF ATTEMPTS. 💀
  The secret word was: HANGMAN
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Do you want to play again? (y/n): 
```

---

## 🧠 Learning Concepts

This project showcases core Python programming fundamentals:
- **Control Flow**: `while` loops, `for` loops, `if-elif-else` conditional branching.
- **Functions & Modularity**: Breaking code into clean, reusable functions with single responsibilities.
- **Data Structures**: Lists for words and stages, sets for tracking unique letter guesses.
- **String Manipulation**: String casing (`.lower()`, `.upper()`), stripping whitespace (`.strip()`), joining strings (`.join()`).
- **Input Validation**: Safe handling of user inputs using `.isalpha()` and length checks.
- **Standard Library**: Utilizing Python's built-in `random` module.
- **Clean Code & Documentation**: Comprehensive docstrings and comments adhering to PEP 8 standards.

---

## 📂 Project Structure

```text
CodeAlpha_HangmanGame/
│
├── hangman.py          # Main Python script containing the Hangman game logic
├── README.md           # Documentation, installation, and game rules
└── requirements.txt    # Project requirements and Python environment notes
```

---

## 💼 Internship Task Information

- **Organization**: [CodeAlpha](https://www.codealpha.tech/)
- **Domain**: Python Programming Internship
- **Task**: Hangman Game (Task 1)
- **Project Name**: `CodeAlpha_HangmanGame`
