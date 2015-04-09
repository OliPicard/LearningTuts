__author__ = 'OliPicard'
import random
import sys
# My tic tac toe program, created after watching JREAM's awesome python tutorial. Thank You Jream!
# Using modified code by Brydon McCluskey, Thank you for the bug fix.

board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]

wins = [[0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 4, 8], [2, 4, 6]]             # Diagonal


def checkline(char, spot1, spot2, spot3):
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
        if char == "X":
            board[spot1] = char
            board[spot2] = char
            board[spot3] = char
            show()
            print("A winner is you.")
            input("Press return to close.")
            sys.exit()

        if char == "o":
            board[spot1] = char
            board[spot2] = char
            board[spot3] = char
            print("You lose. o wins.")
            input("Press return to close.")
            sys.exit()

def checkall(char):
    winning = 0
    for x in range(len(wins)):
        checkline(char, wins[x][0], wins[x][1], wins[x][2]) == True

def show():
    print(board[0], "|", board[1], "|", board[2])
    print("----------")
    print(board[3], "|", board[4], "|", board[5])
    print("----------")
    print(board[6], "|", board[7], "|", board[8])



def game():
    while True:
        print("----Next-Round---")
        _input = input("Choose a number between 0-8 on the grid: ")
        _input = int(_input)
        if board[int(_input)] != 'X' and board[int(_input)] != 'O':
            board[(int(_input))] = 'X'
            checkall("X")
            finding = True
            while finding is True:
                random.seed()
                opponent = random.randint(0,8)
                if board[opponent] != 'O' and board[opponent] != 'X':
                    board[opponent] = 'O'
                    checkall("O")
                    finding = False

            show()
        else:
            print("This spot is taken!")

show()
game()