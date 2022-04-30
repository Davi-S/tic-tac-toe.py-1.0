from board import TicTacToeBoard
from utils import pick_option, pick_int, number_to_grid
from random import randint

class TicTacToeGame():
    def __init__(self, board:type[TicTacToeBoard]) -> None:
        self.board = board
        self.player1 = 'x'
        self.player2 = 'o'
        self.turn = self.player1
        self.difficulty = None
        self.language = 'English'
        

    def select_language(self):
        self.language = pick_option({'1': 'ENGLISH', '2': 'PORTUGUESE'}, 'SELECT LANGUAGE', str)

    def pick_opponent(self):
        opponent = pick_option({'1': 'LOCAL MULTIPLAYER', '2': 'CPU'}, 'PICK YOUR OPPONENT')

    def pick_difficulty(self):
        self.difficulty = pick_option({'1': 'EASY', '2': 'MEDIUM', '3': 'HARD'}, 'PICK YOUR DIFFICULTY')

    def change_turn(self):
        self.turn = self.player1 if self.turn == self.player2 else self.player2
    
    


