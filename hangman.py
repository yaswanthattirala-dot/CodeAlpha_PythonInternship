import random

words = ["python", "intern", "codealpha", "hangman", "project"]
word = random.choice(words)
guessed = []
attempts = 6

while attempts > 0:
    display = ''.join([char if char in guessed else '_' for char in word])
    print("Word:", display)
    guess = input("Guess a letter: ").lower()

    if guess in word:
        guessed.append(guess)
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

    if all(char in guessed for char in word):
        print("You won!")
        break
else:
    print("You lost! The word was:", word)
