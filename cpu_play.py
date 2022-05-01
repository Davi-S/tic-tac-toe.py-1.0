from board import TicTacToeBoard
from random import randint
class CPU_play:
    def __init__(self, board:type[TicTacToeBoard]) -> None:
        self.board = board
    
    def easy_play(self):
        return randint(0, 2), randint(0, 2)
