import random
from typing import Collection

class color:
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   GREY = '\033[90m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

textfile = open("5letters.txt", "r")
words = textfile.readlines()

with open("5letters.txt", "r") as file:
    words = []
    for line in file:
        words.append(line)

ran = random.choice(words)[:-1]

guesses=[]

print("-----")
print("Welcome to the word game " + color.BOLD + "Wordle!" + color.END)
print("You have " + color.BOLD + "6" + color.END + " tries to get the random 5-letter word.")
print(color.GREEN + "Green" + color.END + " means you got the letter in the correct spot.")
print(color.YELLOW + "Yellow" + color.END + " means you got a letter in the wrong spot.")
print(color.GREY + "Grey" + color.END + " means the letter is not in the word.")

i = 1
while i != 7:
    print("-----")
    guess = input()
    print("-----")
    guessWord=""
    for x in range(len(guess)):
        if (guess[x]==ran[x]):
            guessWord = guessWord + (color.GREEN + guess[x] + color.END)
            #print(color.GREEN + guess[x] + color.END, end="")
        elif (guess[x] in ran):
            guessWord = guessWord + (color.YELLOW + guess[x] + color.END)
            #print(color.YELLOW + guess[x] + color.END, end="")
        else:
            guessWord = guessWord + (color.GREY + guess[x] + color.END)
            #print(color.GREY + guess[x] + color.END, end="")
    guesses.append(guessWord)

    for y in guesses:
        print(y)

    if (guess==ran):
        print()
        print(color.BOLD + "Congratulations! You got the word!" + color.END)
        break

    i += 1

if (guess!=ran):
    print()
    print("Unforunately you failed to get the word '" + color.BOLD + ran + color.END + "'.")

print("-----")