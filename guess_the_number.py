import random

# Select difficulty
level = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nChoose a "
              "difficulty. Type 'easy' or 'hard: ").lower()


# function that reduce the number of trial after each guess
def deduct_attempt(attempt):
    if attempt != 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
    else:
        print("You've run out of guesses, you lose!")
        print(f"The answer is {pc_guess}.")

# function if the number guess is greater than the actual number
def greater(attempt):
    print('Too high.\nGuess again.')
    deduct_attempt(attempt)

# function if the number guess is smaller than the actual number
def lower(attempt):
    print('Too low.\nGuess again.')
    deduct_attempt(attempt)


# Random number generator
pc_guess = random.randint(0, 100)

# conditional statement
if level == 'easy':
    num_attempt = 10
    print(f'You have {num_attempt} attempts remaining to guess the number.')
    while num_attempt > 0:
        num_attempt -= 1 # The num of attempt is reduced by 1 after each round.
        my_guess = int(input("Make a guess: ")) # Guess again
        if my_guess > pc_guess:
            greater(num_attempt)
        elif my_guess == pc_guess:
            print(f"You got it! The answer was {my_guess}.")
            break
        else:
            lower(num_attempt)
else:
    num_attempt = 5
    print(f'You have {num_attempt} attempts remaining to guess the number.')
    while num_attempt > 0:
        num_attempt -= 1
        my_guess = int(input("Make a guess: "))
        if my_guess > pc_guess:
            greater(num_attempt)
        elif my_guess == pc_guess:
            print(f"You got it! The answer was {my_guess}.")
            break
        else:
            lower(num_attempt)
