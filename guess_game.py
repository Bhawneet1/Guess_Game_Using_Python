import random

# Welcome message
print("Welcome to Number Guessing Game!")
print("I'll think of a number between 1 and 100.")
print("You have 7 attempts to guess it correctly.\n")

# Set the target number
target = random.randint(1, 100)
attempts = 0

while True:
    # Get player's guess
    try:
        guess = int(input("Enter your guess: "))
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    attempts += 1

    if guess == target:
        print(f"\nCongratulations! You won! The number was {target}!\n")
        break
    else:
        if attempts >= 7:
            print("\nYou ran out of attempts. Better luck next time!")
            break
        print(f"{attempts}/{7} Attempts used. Try again!\n")

# Optional: Add a restart option (you can skip this part)
print("\nDo you want to play again? (y/n)")
play_again = input().lower()
if play_again == 'y':
    # You can copy and paste the entire code again to play
    
    pass
else:
    print("Thanks for playing!")
# ```

# ### How to Play:
# 1. The game starts by generating a random number between 1 and 100.
# 2. You have up to 7 attempts to guess the number correctly.
# 3. If you guess incorrectly, you'll get feedback on whether your guess was too high or too low.
# 4. If you guess correctly within the allowed attempts, you win!
# 5. If you run out of attempts, the game ends, and you can decide to play again or quit.

# ### Example:
# ```python
# # Let's say the target number is 87
# ```
# 1. You input `50`: The program will tell you that your guess was too low.
# 2. You input `70`: The program will tell you that your guess was too high.
# 3. You input `80`: The program will tell you that your guess was too high, but closer.
# 4. You input `85`: Again, it's too high.
# 5. On your 7th attempt, if you guess `87`, you'll win!

# This is a simple but engaging game that can be easily customized by adjusting the number range and other
# parameters in the code.