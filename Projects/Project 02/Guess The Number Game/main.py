import random
import sys
print("Welcome to the Guessing Game!")
print("I'm guessing a number between 1 and 100.")

value = random.randint(1,100)


userLevel = input("Choose a difficulty. Type 'easy' or 'hard': ")
userAttempts = 0
if userLevel == 'easy':
  userAttempts = 10  
elif userLevel == 'hard':
  userAttempts = 5 
else:
    print("You have entered an invalid input. Bye!")
    sys.exit()
while userAttempts > 0:  
  print(f"You have {userAttempts} attempts remaining to guess the number.")
  user_guessed = int(input("Make a guess: "))
  if user_guessed == value:
    print(f"You got it! The answer was {value}.")
    userAttempts = -1    
  elif user_guessed > value:
    print("Too high.\nGuess again.")
    userAttempts -= 1
  elif user_guessed < value:
    print("Too low.\nGuess again.")
    userAttempts -= 1

if userAttempts == 0:
  print("You've run out of guesses, you lose.")
  print(f"The secret number is {value}.")
