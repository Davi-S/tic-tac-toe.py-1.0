from random import randint
from board import TicTacToeBoard
from typing import Union

class CPU:
    def __init__(self) -> None:
        self.difficulty = None
        self.board = None
        self.board_defalt_value = None

    def _check_near_win(self, listi, action:str):
        if action == 'block':
            return listi.count('x') == 2 and listi.count(self.board_defalt_value) == 1
        
        elif action == 'win':
            return listi.count('o') == 2 and listi.count(self.board_defalt_value) == 1

    def _check_lines(self, action:str) -> Union[tuple[int, int], bool]:
        return next(((line_idx, line.index(' ')) for line_idx, line in enumerate(self.board) if self._check_near_win(line, action)), False) 

    def _check_columns(self, action:str) -> Union[tuple[int, int], bool]:
        for count in range(len(self.board)):
            listi = [line[count] for line in self.board]
            if self._check_near_win(listi, action):
                return listi.index(' '), count
        return False

    def _check_diagonals(self, action:str) -> Union[tuple[int, int], bool]:
        # upper_left to lower_right diagonal
        listi = [self.board[idx][idx] for idx, _ in enumerate(self.board)]
        if self._check_near_win(listi, action):
            return listi.index(' '), listi.index(' ')

        # lower_left to upper_right diagonal
        # not using list comprehention here because need the insert function
        listi.clear()
        for idx, _ in enumerate(self.board):
            listi.insert(0, self.board[idx][len(self.board) - idx - 1])
        if self._check_near_win(listi, action):
            # taking the x and y empty value on the board from the index (only possible because of insert function)
            return abs(listi.index(' ') - 2), listi.index(' ') 

        return False

    
    def _easy(self) -> tuple:
        return randint(0, 2), randint(0, 2)

    def _medium(self) -> tuple:
        if lines := self._check_lines('block'):
            return lines

        if columns := self._check_columns('block'):
            return columns

        if diagonals := self._check_diagonals('block'):
            return diagonals

        return self._easy()
            

    def _hard(self) -> tuple:
        if lines := self._check_lines('win'):
            return lines

        if columns := self._check_columns('win'):
            return columns

        if diagonals := self._check_diagonals('win'):
            return diagonals

        return self._medium()



    def play(self, board:list[list, list, list], board_defalt_value:str) -> tuple:
        self.board = board
        self.board_defalt_value = board_defalt_value
        if self.difficulty == 1:
            return self._easy()

        elif self.difficulty == 2:
            return self._medium()

        elif self.difficulty == 3:
            return self._hard()
