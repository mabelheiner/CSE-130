# 1. Name: 
#    Mabel Heiner
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    This program is the classic "High Low" game. The user picks a max number. The computer
#    picks a random number between the max number and 1. The user guesses the computer's 
#    number. The computer responds if the user is too low or too high. If the number is 
#    guessed, the program will display the number of guesses and the guess history and end.
# 4. What was the hardest part? Be as specific as possible.
#    The hardest part of this assignment was figuring out the while loop and how to display
#    the tabbed responses of "Too low" and "Too high"
# 5. How long did it take for you to complete the assignment?
#    -total time in hours including reading the assignment and submitting the program-  
#    This assignment took me 2 hours. That is divided in 45 minutes programming, 30 minutes 
#    of video, 15 minutes of optimizing, and 30 minutes of video recording and submittal.

import random

def main():
  # Game introduction.
  print('This is the "guess a number" game.')
  print("You try to guess a random number in the smallest number of attempts.")

  # Prompt the user for how difficult the game will be. Ask for an integer.
  value_max = int(input("Pick a positive integer: "))
  # Generate a random number between 1 and the chosen value.
  value_random = random.randint(1, value_max)

  # Give the user instructions as to what he or she will be doing.
  print(f"Guess a number between 1 and {value_max}.")

  # Initialize the sentinal and the array of guesses.
  guessed = []

  num = None
  guess = 0
  # Play the guessing game.
  while num != value_random:

    # Prompt the user for a number.
    num = int(input())

    # Store the number in an array so it can be displayed later.
    guessed.append(num)
    guess += 1

    # Make a decision: was the guess too high, too low, or just right.

    if num < value_random:
      print("\tToo low!")
    if num > value_random:
      print("\tToo high!")

# Give the user a report: How many guesses and what the guesses where.
  print(f"You were able to find the number in {guess} guesses.")
  print("The numbers you guessed were: ", guessed)

if __name__ == "__main__":
  main()