from src.board import * 
from src.winner import *
from src.move import *





def main(board):
    print("Welcome to the game!")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(IsWinner(board , 'O')):
            playerMove(board)
            printBoard(board)
        else:
            print("sorry you loose!")
            break

        if not(IsWinner(board , 'X')):
            move = computerMove(board)
            if move == 0:
                print(" ")
            else:
                insertLetter('O' , move, board)
                print('computer placed an O on position' , move , ':')
                printBoard(board)
        else:
            print("you win!")
            break




    if isBoardFull(board):
        print("Tie game")
