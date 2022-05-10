from itertools import product
from math import inf
from random import randint
from typing import Union
from board import TicTacToeBoard

class CPU:
    def __init__(self) -> None:
        self.board = None
        self.difficulty = None

    def play(self, board_instance:type[TicTacToeBoard]) -> tuple:
        """call the cpu play on the given board acording to the difficulty

        Args:
            board (list): the board for the cpu bases his moves
            board_defalt_value (str): the sign that represents a empty place on the board

        Returns:
            tuple: x and y axis to mark on the board
        """
        self.board = board_instance
        if self.difficulty == 1:
            return CPUeasy().play() # random plays

        elif self.difficulty == 2:
            return CPUmedium().play(self) # block wins whenever possible, else calls easy play

        elif self.difficulty == 3:
            return CPUhard().play(self) # wins whenever possible, else calls medium play

        elif self.difficulty == 4:
            return CPUimpossible().play(self) # minmax algorithm. NEVER LOSES

    def _check_near_win(self, listi:list, action:str) -> bool:
        """checks if a player is almost winning (2 equal signs and a defalt sign(indicates a empty place))

        Args:
            listi (list): the list with the signs on a line, column or diagonal
            action (str): if "block", checks if the player 'x' if winnin; if "win", checks
            fo the 'o' player

        Returns:
            bool: if there is a near win
        """
        if action == 'block':
            return listi.count('x') == 2 and listi.count(self.board.defalt_value) == 1
        
        elif action == 'win':
            return listi.count('o') == 2 and listi.count(self.board.defalt_value) == 1
    
    # NOTE the following 3 functions (_check_lines, _check_columns, _check_diagonals)
    # are very simillar to the same function on the "TicTacToeBoard" class in the "board.py" file
    def _check_lines(self, action:str) -> Union[tuple[int, int], bool]:
        return next(((line_idx, line.index(' ')) for line_idx, line in enumerate(self.board.board) if self._check_near_win(line, action)), False) 

    def _check_columns(self, action:str) -> Union[tuple[int, int], bool]:
        for count in range(len(self.board.board)):
            listi = [line[count] for line in self.board.board]
            if self._check_near_win(listi, action):
                return listi.index(' '), count
        return False

    def _check_diagonals(self, action:str) -> Union[tuple[int, int], bool]:
        # upper_left to lower_right diagonal
        listi = [self.board.board[idx][idx] for idx, _ in enumerate(self.board.board)]
        if self._check_near_win(listi, action):
            return listi.index(' '), listi.index(' ')

        # lower_left to upper_right diagonal
        # not using list comprehention here because need the insert function
        listi.clear()
        for idx, _ in enumerate(self.board.board):
            listi.insert(0, self.board.board[idx][len(self.board.board) - idx - 1])
        if self._check_near_win(listi, action):
            # taking the x and y empty value on the board from the index (only possible because of insert function)
            return abs(listi.index(' ') - 2), listi.index(' ') 

        return False


class CPUeasy():
    def play(self) -> tuple:
        """A randon play
        
        Returns:
            tuple: x and y axis to mark on the board
        """
        return randint(0, 2), randint(0, 2)


class CPUmedium():
    def play(self, cpu) -> tuple:
        """Always block the opponent win if possible. else: randon play
        
        Returns:
            tuple: x and y axis to mark on the board
        """
        if lines := cpu._check_lines('block'):
            return lines

        if columns := cpu._check_columns('block'):
            return columns

        if diagonals := cpu._check_diagonals('block'):
            return diagonals

        return CPUeasy().play()


class CPUhard():
    def play(self, cpu) -> tuple:
        """Always win if opponent. else, block the opponent win. else: random play
        
        Returns:
            tuple: x and y axis to mark on the board
        """
        if lines := cpu._check_lines('win'):
            return lines

        if columns := cpu._check_columns('win'):
            return columns

        if diagonals := cpu._check_diagonals('win'):
            return diagonals

        return CPUmedium().play()


class CPUimpossible(): # TODO understand why it works
    def minimax(self, board:type[TicTacToeBoard], actual_player):
        """MINMAX algorithm recurses every possible move and them choses the best and fast way to win

        Args:
            board (type[TicTacToeBoard]): the board
            actual_player (_type_): the player that will make the turn

        Returns:
            dict: dict with position and score. position means the best place on the board (grid)
        """
        next_player = 'o' if actual_player == 'x' else 'x'

        if board.win_info()['player'] == next_player:
            return {'position': None,
                    'score': 1 * (board.empty_spaces() + 1) if next_player == 'o' else -1 * (
                        board.empty_spaces() + 1)}

        
        elif board.is_filled(): # draw
            return {'position': None, 'score': 0}


        if actual_player == 'o':
            best = {'position': None, 'score': -inf}
        else:
            best = {'position': None, 'score': inf}

        for line, column in product(range(board.size), range(board.size)): # itertools replace nested for loops
            if not board.is_marked(line, column):
                board.place_mark(line, column, actual_player)
                # print(board.print_formated_board())
                simulated_score = self.minimax(board, next_player)

                # undo move
                board.place_mark(line, column, board.defalt_value, True)
                simulated_score['position'] = line, column

                if actual_player == 'o' and simulated_score['score'] > best['score'] \
                    or actual_player != 'o' and simulated_score['score'] < best['score']:
                    best = simulated_score
        return best


    def play(self, cpu:type[CPU]):
        return self.minimax(cpu.board, 'o')['position']

