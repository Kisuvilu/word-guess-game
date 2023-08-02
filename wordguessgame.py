# Kibo FPWP Final Project
# Put your final project code in this file for submission
# Add the names of the authors, a brief description, and link to your video in the file called 'readme.md'
# Then, you can remove these instruction comments
import random
#print a welcome message for our player
print("........Welcome to my word guess game........\nHint: African country names.")
print()
#the user is asked to enter the name first
name = input("What is your name? ")
print(f"Good Luck!{name}")
# lets store the variable words in a list called words
words = ['kenya', 'nigeria','southafrica', 'egypt', 'ghana', 'uganda','morocco', 'rwanda',]
# function will that choose one random word from this list of words
word = random.choice(words)
print("Guess the character ")
guesses = " "
# any number of turns can be used here
turns = 8
# use loop to determine number of guesses
while turns > 0:
  failed = 0
  #all the character from the input word taking one at a time
  for character in word:
    # comparing that character with character in guesses
    if character in guesses:
      print(character, end = " ")
    else:
      print("_")
      # for every fail 1 will be added in failure
      failed += 1
  if failed == 0:
    # user will win the game if failure is 0 and 'you win'
    print("You win")
    # this print the correct word
    print(f"The word is:{word}")
    break
    # if user has input the wrong character then it will ask the user to enter another character
  print()
  guess = input("guess a character: ").lower()
  guesses += guess
    # check input with the character will be stored in guesses
    # check input with the character in word
  if guess not in word:
    turns -= 1
      # if character does not match the word then 'wrong' will be given as output
    print("wrong")
      # this will print the number of turns left for the user
    print(f"you have, {turns},more guesses")

    if turns == 0:
      print("You loose")
