import random
words = ["python", "eugene", "computer", "hangman", "challenge"]
#where you can choose a random word
secret_word = random.choice(words)
wrong_guesses = []
guesses = []
#used to create a list of dashes for the word
current_display = ["-" for _ in secret_word]

# hint 
hint = secret_word[0] 
current_display[0] = hint  # to update the current hint



MAX_WRONG_GUESSES = 6

print("Welcome to Hangman!")
print(f"Hint: The first letter of the word is '{hint}'.\n")

while len(wrong_guesses) < MAX_WRONG_GUESSES and "-" in current_display:
    print(" ".join(current_display))

    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    if guess in guesses:
        print("You already guessed that letter.")
        continue

    guesses.append(guess)
#cheking if guess is there
    if guess in secret_word:
        # Updating the current display with the guessed letter
        for i, letter in enumerate(secret_word):
            if letter == guess:
                current_display[i] = guess
    else:
        wrong_guesses.append(guess)
        print(f"Incorrect guess. You have {MAX_WRONG_GUESSES - len(wrong_guesses)} guesses left.")

# the game is over
if len(wrong_guesses) == MAX_WRONG_GUESSES:
    
    print("You lost! The word was:", secret_word)
else:
    print("Congratulations! You guessed the word:", secret_word)
