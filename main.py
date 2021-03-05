

from src.functions import *
from src.board import * 
from src.winner import *
from src.move import *

while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main(board)
    else:
        break