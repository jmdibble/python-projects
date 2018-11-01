from __future__ import print_function
## GAME BOARD
# print("Let the games commence! Here's your 3x3 grid")
# def top(r, c):
#     for i in range(0, c):
#         print(" ---", end = "")
#     print("\r")
#
# def board(r, c):
#     for i in range(0, r):
#         for i in range(0, (c+1)):
#             print("|", end = "   ")
#         print("\r")
#         for i in range(0, c):
#            print(" ---", end = "")
#         print("\r")
#
# top(3, 3)
# board(3, 3)

## CHOOSING WHERE TO GO
game = [
    [0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

for sub in game:
    print(*sub)

def oneGo():
    playerOne = input("Player 1, please type your move in co-ordinate form i.e. 'row,column': ")
    pOne = playerOne.split(",")
    pOnex = int(pOne[0])
    pOney = int(pOne[1])
    if game[pOnex - 1][pOney - 1] != "X" and game[pOnex - 1][pOney - 1] != "O":
        game[pOnex - 1][pOney - 1] = "X"
        for sub in game:
            print(*sub)
    else:
        print("Position already taken")
        return oneGo()

def twoGo():
    playerTwo = input("Player 2, please type your move in co-ordinate form i.e. 'row,column': ")
    pTwo = playerTwo.split(",")
    pTwox = int(pTwo[0])
    pTwoy = int(pTwo[1])
    if game[pTwox - 1][pTwoy - 1] != "X" and game[pTwox - 1][pTwoy - 1] != "O":
        game[pTwox - 1][pTwoy - 1] = "O"
        for sub in game:
            print(*sub)
    else:
        print("Position already taken")
        return twoGo()

## FINDING THE WINNER
def win(egg):
    if egg[0][0] == egg[0][1] == egg[0][2] and egg[0][0] != 0:
        print("Winner!")
    elif egg[1][0] == egg[1][1] == egg[1][2] and egg[1][0] != 0:
        print("Winner!")
    elif egg[2][0] == egg[2][1] == egg[2][2] and egg[2][0] != 0:
        print("Winner!")
    elif egg[0][0] == egg[1][0] == egg[2][0] and egg[0][0] != 0:
        print("Winner!")
    elif egg[0][1] == egg[1][1] == egg[2][1] and egg[0][1] != 0:
        print("Winner!")
    elif egg[0][2] == egg[1][2] == egg[2][2] and egg[0][2] != 0:
        print("Winner!")
    elif egg[0][0] == egg[1][1] == egg[2][2] and egg[0][0] != 0:
        print("Winner!")
    elif egg[0][2] == egg[1][1] == egg[2][0] and egg[0][2] != 0:
        print("Winner!")
    else:
        pass

# def isit():
#     if winner == 1:
#         print("Winner!")

## CALLING THE GAME FUNCTIONS
for i in range(4):
    oneGo()
    win(game)
    twoGo()
    win(game)
oneGo()
win(game)