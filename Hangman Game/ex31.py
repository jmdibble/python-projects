print("Welcome to Hangman!")
print("Rules: You have 6 wrong attempts to guess a word from the official list of Scrabble words")

from random import *

with open("SOWPODS.txt", "r") as f:
    lines = f.readlines()

x = randint(0, len(lines))
# print(lines[x]) # DON'T COMMENT THIS LINE IF YOU WANT TO SEE THE WORD FIRST FOR DEBUGGING
y = lines[x]
w = y

length = []
for i in w:
    length.append("_")

print(" ".join(map(str, length)))

letters = []
for i in w:
    letters.append(i)

def game():
    tries = 0
    while tries < 6:
        g = input("Guess a letter: ")
        guess = g.upper()
        for i, j in enumerate(letters):
            if j == guess:
                length[i] = guess
                print(" ".join(map(str, length)))

        if tries == 5:
            print("You've had 6 incorrect attempts out of 6")
            print("Game over")
            break
        if guess in letters:
            print("You've had", tries, "incorrect attempts out of 6")
        if guess not in letters:
            tries += 1
            print("You have had", tries, "incorrect attempts out of 6")
            print("Try again")
            print(" ".join(map(str, length)))

game()