import random

words = [
    "apple",
    "banana",
    "elephant",
    "computer",
    "knowledge",
    "creativity",
    "adventure",
    "thunderstorm",
    "basketball",
    "universe",
    "whisper",
    "mystery",
    "sunshine",
    "friendship",
    "chocolate",
    "volcano",
    "dragonfly",
    "moonlight",
    "rainbow",
    "symphony"
]

stages = [
    '''
      😀
    ''',
    '''
      😐
    ''',
    '''
      😕
    ''',
    '''
      😟
    ''',
    '''
      😦
    ''',
    '''
      😧
    ''',
    '''
      😵
    '''
]

lives = 6

# generating random words from the words list
chosen_word = random.choice(words)
print(chosen_word)

# generating blank dashes as long as the chosen word
display = []

for letter in range(len(chosen_word)):
    display += '_'
print(display)


# taking user input and compareing that letter to the guessed word one by one
game_over = False

while not game_over:
    guessed_letter = input("Guess a letter : ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            print("You guessed it right ⭐")
            display[position] = guessed_letter
            print(display)
    
    if guessed_letter not in chosen_word:
        lives -= 1
        print(f"Wrong guess. You have {lives} lives left.")
        print(stages[6 - lives])  # Display the current hangman stage
        if lives == 0:
            game_over = True
            print("You Lose!")
    
    if '_' not in display:
        game_over = True
        print("You Win! ⭐⭐⭐")
    