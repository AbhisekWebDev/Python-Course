import random

random_num = random.randint(1,50)

print(random_num)

def guess_game(options):
    guess_num = int(input("Make a guess : "))

    if guess_num == random_num:
        print(f"You guessed it right, the number was : {random_num}")
        return True
    else:
        if options > 0:
            print(f"Guess again, you have {options} guesses left")
        else:
            print("You are out of guesses")
        return False

print("I have chosen a number b/w 1 to 20 \n Now you should guess the number which i have chosen")

level = input("Choose the difficulty level : type 'E' for easy or 'H' for hard : ").lower()

if level == 'e':
    options = 10
elif level == 'h':
    options = 5
else:
    print("Invalid input. Starting game in easy mode.")
    options = 10

for i in range(options - 1, -1, -1):
    if guess_game(i):
        break
