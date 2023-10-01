#importing the random function
import random

# List of words
word_list = ["apple", "banana", "cherry", "orange", "strawberry"]
#main game loop
def main_game_loop():
    selected_word = random.choice(word_list)
    guessed_letters = []
    max_attempts = 6
    incorrect_attempts = 0

    print("Welcome to Hangman!")

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in selected_word:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            incorrect_attempts += 1

        print("Word: ", display_word(selected_word, guessed_letters))
        display_hangman(incorrect_attempts)

        if display_word(selected_word, guessed_letters) == selected_word:
            print("Congratulations! You win!")
            break

        if incorrect_attempts >= max_attempts:
            print("You lose. The word was", selected_word)
            break

# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Function to display the hangman
def display_hangman(incorrect_attempts):
    stages = [
        """
          --------
          |      |
          |      
          |     
          |     
          |     
          -
        """,
        """
          --------
          |      |
          |      O
          |     
          |     
          |     
          -
        """,
        """
          --------
          |      |
          |      O
          |      |
          |     
          |     
          -
        """,
        """
          --------
          |      |
          |      O
          |     /|
          |     
          |     
          -
        """,
        """
          --------
          |      |
          |      O
          |     /|\ 
          |     
          |     
          -
        """,
        """
          --------
          |      |
          |      O
          |     /|\ 
          |     / 
          |     
          -
        """,
        """
          --------
          |      |
          |      O
          |     /|\ 
          |     / \ 
          |     
          -
        """
    ]
#if the length of the incorrect attempts is bigger than the stages, the game ends
    if incorrect_attempts < len(stages):
        print(stages[incorrect_attempts])
    else:
        print("Game over!")


if __name__ == "__main__":
    while True:
        main_game_loop()
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break
