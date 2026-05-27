import random

# Step 1: Create word list
words = ["apple", "mango", "grape", "tiger", "table"]

# Step 2: Choose random word
secret_word = random.choice(words)

# Step 3: Create hidden word
guessed_word = []

for letter in secret_word:
    guessed_word.append("_")

# Step 4: Set chances
wrong_guesses = 6

print("Welcome to Hangman Game!")

# Step 5: Start game loop
while wrong_guesses > 0:

    # Show current word
    print("\nWord:", " ".join(guessed_word))

    # Ask user for letter
    guess = input("Enter a letter: ")

    # Check correct guess
    if guess in secret_word:

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess

        print("Correct guess!")

    else:
        wrong_guesses -= 1
        print("Wrong guess!")
        print("Chances left:", wrong_guesses)

    # Check win
    if "_" not in guessed_word:
        print("\nYou Win!")
        print("The word was:", secret_word)
        break

# Lose condition
if wrong_guesses == 0:
    print("\nYou Lose!")
    print("The word was:", secret_word)