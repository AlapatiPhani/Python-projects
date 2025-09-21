import random

easy_words= ['cat', 'dog', 'fish', 'bird', 'tree']
medium_words= ['python', 'jumble', 'easy', 'difficult', 'answer']
hard_words= ['xylophone', 'quizzical', 'pneumonia', 'rhythm', 'zephyr']

print("Welcome to the Password Guessing Game!")
print("Choose a difficulty level: easy, medium, hard")

level=input("Enter difficulty level: ").lower()
if level=='easy':
    word=random.choice(easy_words)
elif level=='medium':
    word=random.choice(medium_words)
elif level=='hard':
    word=random.choice(hard_words)
else:
    print("Invalid level. Defaulting to easy.")
    word=random.choice(easy_words)

attempts = 0
print("Guess the word!")

while True:
    guess=input("Enter your guess: ").lower()
    attempts += 1
    if guess == word:
        print(f"Congratulations! You've guessed the word '{word}' in {attempts} attempts.")
        break

    hint = ''
    for i in range(len(word)):
        if i < len(guess) and guess[i] == word[i]:
            hint += guess[i]
        else:
            hint += '_'
    print(f"Hint: {hint}") 
print("Game Over.  Thanks for playing!")
