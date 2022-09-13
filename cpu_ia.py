from itertools import product
from math import inf
from random import randint
from typing import Union
from board import TicTacToeBoard

class CPU:
    def __init__(self) -> None:
        self.board:type[TicTacToeBoard] = None
        self.difficulty:int = 1
        self.cpu_symbol:str = None
        self.player1_symbol:str = None

    def play(self) -> tuple:
        if self.difficulty == 1:
            return self.easy_play()

        elif self.difficulty == 2:
            return self.medium_play()

        elif self.difficulty == 3:
            return self.hard_play()
            
        elif self.difficulty == 4:
            return self.impossible_play()

    @staticmethod
    def easy_play() -> tuple:
        return randint(0, 2), randint(0, 2)

    def medium_play(self) -> tuple:
        """Always block the opponent if possible. else, randon play
        
        Returns:
            tuple: x and y axis to mark on the board
        """
        if lines := self.check_lines(self.player1_symbol):
            return lines

        if columns := self.check_columns(self.player1_symbol):
            return columns

        if diagonals := self.check_diagonals(self.player1_symbol):
            return diagonals

        return self.easy_play()

    def hard_play(self) -> tuple:
        """Always win if possible. else, block the opponent win. else, random play
        
        Returns:
            tuple: x and y axis to mark on the board
        """
        if lines := self.check_lines(self.cpu_symbol):
            return lines

        if columns := self.check_columns(self.cpu_symbol):
            return columns

        if diagonals := self.check_diagonals(self.cpu_symbol):
            return diagonals

        return self.medium_play()

    def impossible_play(self):
        return self.minimax(self.cpu_symbol)['position']

    def check_near_win(self, position:list, player:str) -> bool:
        """checks if a player is almost winning.
        Only one space empty, and only the player symbol on the sequence

        Args:
            position (list): the list with the signs on a line, column or diagonal
            player (str): the player to check if its winning

        Returns:
            bool: True if the player is almost winnin. else, False
        """
        return (position.count(player) == (self.board.size - 1)\
            and position.count(self.board.defalt_value) == 1)
    

    # NOTE the following 3 functions (_check_lines, _check_columns, _check_diagonals)
    # are very simillar to the same function on the "TicTacToeBoard" class in the "board.py" file
    def check_lines(self, player:str) -> Union[tuple[int, int], bool]:
        """return the empty space (x and y axis)
        if the given player is almost winning on any line of the board

        Args:
            player (str): the player to check if is almost winning

        Returns:
            Union[tuple[int, int], bool]: the x and y axis. or false is the player is not winning
        """
        for line_idx, line in enumerate(self.board.board): # sourcery skip: use-next
            if self.check_near_win(line, player):
                return line_idx, line.index(self.board.defalt_value)
        return False

    def check_columns(self, player:str) -> Union[tuple[int, int], bool]:
        """return the empty space (x and y axis)
        if the given player is almost winning on any column of the board

        Args:
            player (str): the player to check if is almost winning

        Returns:
            Union[tuple[int, int], bool]: the x and y axis. or false is the player is not winning
        """
        for column in range(self.board.size):
            listi = [line[column] for line in self.board.board]

            if self.check_near_win(listi, player):
                return listi.index(self.board.defalt_value), column

        return False

    def check_diagonals(self, player:str) -> Union[tuple[int, int], bool]:
        """return the empty space (x and y axis)
        if the given player is almost winning on any column of the board

        Args:
            player (str): the player to check if is almost winning

        Returns:
            Union[tuple[int, int], bool]: the x and y axis. or false is the player is not winning
        """
        # upper_left to lower_right diagonal
        listi = [self.board.board[idx][idx] for idx, _ in enumerate(self.board.board)]
        if self.check_near_win(listi, player):
            return listi.index(self.board.defalt_value), listi.index(self.board.defalt_value)

        # lower_left to upper_right diagonal
        listi.clear()
        # not using list comprehention here because need the insert function
        for idx, _ in enumerate(self.board.board):
            listi.insert(0, self.board.board[idx][len(self.board.board) - idx - 1])
        if self.check_near_win(listi, player):
            # taking the x and y empty value on the board from the index (only possible because of insert function)
            return abs(listi.index(self.board.defalt_value) - 2), listi.index(self.board.defalt_value) 

        return False

    def minimax(self, actual_player): # TODO understand why it works
        """MINMAX algorithm recurses every possible move and them choses the best and fast way to win

        Args:
            actual_player (_type_): the player that will make the turn

        Returns:
            dict: dict with position and score. position means the best place on the board (grid)
        """
        next_player = self.cpu_symbol if actual_player == self.player1_symbol else self.player1_symbol

        if self.board.win_info()['player'] == next_player:
            return {'position': None,
                    'score': 1 * (self.board.empty_spaces() + 1) if next_player == self.cpu_symbol
                            else -1 * (self.board.empty_spaces() + 1)}

        elif self.board.is_filled(): # draw
            return {'position': None, 'score': 0}


        if actual_player == self.cpu_symbol:
            best = {'position': None, 'score': -inf}
        else:
            best = {'position': None, 'score': inf}

        for line, column in product(range(self.board.size), range(self.board.size)): # itertools replace nested for loops
            if not self.board.is_marked(line, column):
                self.board.place_mark(line, column, actual_player)
                # print(board.print_formated_board())
                simulated_score = self.minimax(next_player)

                # undo move
                self.board.place_mark(line, column, self.board.defalt_value, True)
                simulated_score['position'] = line, column

                if actual_player == self.cpu_symbol and simulated_score['score'] > best['score'] \
                        or actual_player != self.cpu_symbol and simulated_score['score'] < best['score']:
                    best = simulated_score
        return best






