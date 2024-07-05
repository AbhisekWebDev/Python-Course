import random

# Define emojis for rock, paper, and scissors
emojis = ["✊", "📄", "✂️"]

# Get user's choice
user_choice = int(input("Enter choice: 0 for Rock ✊, 1 for Paper 📄, 2 for Scissors ✂️  : "))

# Validate user's choice
if user_choice >= 3 or user_choice < 0:
    print("Invalid input, You lose")
else:
    # Generate computer's choice
    comp_choice = random.randint(0, 2)

    # Display choices with emojis
    print(f"Your choice : {emojis[user_choice]}")
    print(f"Computer's choice : {emojis[comp_choice]}")

    # Determine the result
    if comp_choice == user_choice:
        print("It's a draw")
    elif (user_choice == 0 and comp_choice == 2) or (user_choice == 1 and comp_choice == 0) or (user_choice == 2 and comp_choice == 1):
        print("You win")
    else:
        print("You lose")
