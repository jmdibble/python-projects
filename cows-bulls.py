import random

generate = random.sample(range(0, 9), 4)

user = [int(x) for x in str(input("Type your 4 digit number: "))]

goes = 1

while goes != 0:
    ordered = [i for i, j in zip(generate, user) if i == j]
    bulls = int(len(ordered))
    if bulls == 4:
        print("Winner! 4 bulls!")
        break
    elif bulls == 3:
        print("3 bulls")
    elif bulls == 2:
        print("2 bulls")
    elif bulls == 1:
        print("1 bull")
    else:
        print("0 bulls")

    unordered = []
    for i in generate:
        if i in user:
            unordered.append(i)

    cows = int(len(unordered) - len(ordered))
    if cows == 4:
        print("4 cows")
    elif cows == 3:
        print("3 cows")
    elif cows == 2:
        print("2 cows")
    elif cows == 1:
        print("1 cow")
    else:
        print("0 cows")
    goes = 0

    user = [int(x) for x in str(input("Try again. Type your 4 digit number: "))]

    goes = 1