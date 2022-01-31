import random
from typing import Collection

# Class for colour codes
class color:
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   GREY = '\033[90m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# Open text file to read from
with open("5letters.txt", "r") as file:
    words = []
    for line in file:
        
        # Store every line into a list
        words.append(line)

# Store random word into variable
ran = random.choice(words)[:-1]

# Welcome code
print("-----")
print("Welcome to the word game " + color.BOLD + "Wordle!" + color.END)
print("You have " + color.BOLD + "6" + color.END + " tries to guess the random 5-letter word.")
print(color.GREEN + "Green" + color.END + " means you got the correct letter in the correct spot.")
print(color.YELLOW + "Yellow" + color.END + " means you got a correct letter in the wrong spot.")
print(color.GREY + "Grey" + color.END + " means you got the wrong letter.")


# Initialize variables
guesses=[]
guess=""
guessWord=""
i = 1

# Loop for 6 turns
while i != 7:
    print("-----")

    # Loop if guess is not 5 letters
    while len(guess)!=5:
        print("What is your guess? (Must be 5 letters): ")

        # Store guess in varaible
        guess = input()

        # If guess is not 5 letters
        if (len(guess)!=5):
            print("-----")
            print("Must be a 5 letter word!")
    print("-----")

    # Loop through word
    for x in range(len(guess)):

        # If the letter is in the right spot
        if (guess[x]==ran[x]):
            guessWord = guessWord + (color.GREEN + guess[x] + color.END)
            #print(color.GREEN + guess[x] + color.END, end="")

        # If the letter is in the wrong spot
        elif (guess[x] in ran):
            guessWord = guessWord + (color.YELLOW + guess[x] + color.END)
            #print(color.YELLOW + guess[x] + color.END, end="")

        # If the wrong letter
        else:
            guessWord = guessWord + (color.GREY + guess[x] + color.END)
            #print(color.GREY + guess[x] + color.END, end="")
    
    # Add all letters into list
    guesses.append(guessWord)

    # Print out previous guesses
    for y in guesses:
        print(y)

    # Win check
    if (guess==ran):
        print()
        print(color.BOLD + "Congratulations! You got the word!" + color.END)
        break

    # Add for loop counter
    i += 1

    # Clear previous guess
    guess=""
    guessWord=""

# Out of guesses and loss
if (guess!=ran):
    print()
    print("Unforunately you failed to get the word '" + color.BOLD + ran + color.END + "'.")

print("-----")