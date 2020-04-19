# This program picks a random number for the user to guess correctly.
# 19 April 2020
# CTI-110 P5HW1 - Random Number
# Devorick Johnson

# Get menu option from the user.
choice = input('Enter choice(1/2): ')

# Display of Menu options.
print('-----MENU-----')
print('1.Play Game')
print('2.Exit')

# Get result for each of the menu selection options.
if choice == '1':
    print('Guess a number (between 1 and 100): ')

if choice == '2':
    print('Program Terminated')

# Initialize program fuction.
import random

# Display name of the game.
print('Number guessing game')

# Calculate the random number to guess.
number = random.randint(1, 100)

chances = 0

# Get veriable for each user input.
while chances < 5:
    guess = int(input())

    if guess == number:

        print('Congratulation You Won!!')
        break

    elif guess < number:
        print('Your guess was too low: Guess a number higher than', guess)

    else:
        print('Your guess was too high: Guess a number lower than', guess)

    chances += 1

if not chances < 5:
    print('You Lose! The number is', number)
