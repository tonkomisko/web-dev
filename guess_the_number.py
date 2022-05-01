#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo
from replit import clear


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5




def set_num_of_turns():
  difficulty_chosen = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if difficulty_chosen == 'easy':
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS



def compare_guess(user_guess, random_number, turns):
  if user_guess > random_number:
    print("Too high...")
    return turns -1
  elif user_guess < random_number:
    print("Too low...")
    return turns -1
  else:
    print(f"You've guessed the number. The random number is {random_number}. You WIN.")


def play_game():
  
  print(logo)
  
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  random_number = random.randint(1,100)
  user_guess = 0
  print(f"Psst, the correct answer is {random_number}")
  
  turns_left = set_num_of_turns()
  print(f"You have {turns_left} attempts remaining to guess the number.")
  
  
  while user_guess != random_number:
    # print(f"You have {turns} turns left")
    user_guess = int(input("Make a guess: "))
    
    turns_left = compare_guess(user_guess, random_number, turns_left)
    # print(turns_left)
    if turns_left == 0:
      print("You've run out of guesses.")
      return
    elif user_guess != random_number:
      print(f"You have {turns_left} turns left")
    
  
while input("Do you want to play a number guessing game? Yes 'y' or No 'n': ") == "y":
  clear()  
  play_game()