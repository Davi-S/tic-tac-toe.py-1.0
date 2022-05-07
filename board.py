from typing import Union
from ui import UI
class TicTacToeBoard():
    def __init__(self, defalt_value:str=' ') -> None:
        self.defalt_value = defalt_value
        self.size = None # used to quick access board size for the CustomInput class
        self.board = None

    def create_board(self, size:int=3) -> None:
        """Assign a new empty board to board instance variable

        Args:
            size (int, optional): size of "x" and "y" axis. Defaults to 3.
        """
        gridline = [self.defalt_value for _ in range(size)]
        self.board = [list(gridline) for _ in range(size)]
        self.size = size

    def is_filled(self) -> bool:
        """check if the board if fully filled"""
        for line in self.board:
            for column in line:
                if column == self.defalt_value:
                    return False
        return True

    def is_marked(self, line:int, column:int) -> bool:
        """checks if a place on the board if already marked

        Args:
            line (int): x axis
            column (int): y axis
        """
        return self.board[line][column] != self.defalt_value

    def place_mark(self, line:int, column:int, mark:str, rewrite:bool=False) -> bool:
        """Place a mark on the board

        Args:
            line (int): x axis
            column (int): y axis
            mark (str): the sign to mark
            rewrite (bool, optional): place a new mark over the actual one. Defaults to False.

        Returns:
            bool: True if the marks was sucessfuly placed. False if the mark could not be placed
        """
        if rewrite or not rewrite and not self.is_marked(line, column):
            self.board[line][column] = mark
            return True
        else:
            return False


    def print_formated_board(self):
        """Print a nice boad on the screen"""
        for idx, line in enumerate(self.board):
            print('\n', str(line).replace('[', '').replace(']', '')\
                                    .replace(',', ' |').replace("'", ''))
            if idx < len(self.board) -1:
                for count, _ in enumerate(line, start=1):
                    print('---', end='')
                    if count < len(line):
                        print('|', end='')
    


    def _check_set(self, seti:set):
        """check if a set has only one item and it is diferent from the board defalt value"""
        return len(seti) == 1 and seti != {self.defalt_value}


    # NOTE the following 3 functions (_check_lines, _check_columns, _check_diagonals)
    # are very simillar to the same function on the "CPU" class in the "cpu_ia.py" file
    def _check_lines_winner(self) -> str:
        """check if all values in any line are the same

        Returns:
            str or bool: the mark that repeats or False if none is repeating
        """
        return next((line[0] for line in self.board if self._check_set(set(line))), self.defalt_value)

    def _check_columns_winner(self) -> str:
        """check if all values in any column are the same

        Returns:
            str or bool: the mark that repeats or False if none is repeating
        """
        for count in range(len(self.board)):
            seti = set()
            for line in self.board:
                seti.add(line[count])
            if self._check_set(seti):
                return line[count]
            
        return self.defalt_value

    def _check_diagonals_winner(self) -> str:
        """check if all values in any diagonal(2) are the same

        Returns:
            str or bool: the mark that repeats or False if none is repeating
        """
        seti = {self.board[idx][idx] for idx, _ in enumerate(self.board)}
        if self._check_set(seti):
            return self.board[0][0]
        
        seti = {self.board[idx][len(self.board) - idx - 1] for idx, _ in enumerate(self.board)}
        if self._check_set(seti):
            return self.board[0][len(self.board)-1]

        return self.defalt_value

    def win_info(self) -> dict:
        """check if there are wins in the board. None that it only return
        one(1) kind of win follwing the hierarchy (line, column and diagonal); ex.:
        tree signs on x=1 axis and 3 signs on y=1 axis will be count as an line win
        
        Returns:
            tuple: [bool, str(winner), str(how the win occoured)]. if bool is False, all other
            values will be None
        """
        wins = {'player': str, 'line': 0, 'column': 0, 'diagonal': 0}

        line = self._check_lines_winner()
        if line != self.defalt_value:
            wins['player'] = line
            wins['line'] += 1

        column = self._check_columns_winner()
        if column != self.defalt_value:
            wins['player'] = column
            wins['column'] += 1

        diagonal = self._check_diagonals_winner()
        if diagonal != self.defalt_value:
            wins['player'] = diagonal
            wins['diagonal'] += 1

        return wins

    def check_win(self) -> True:
        line = self._check_lines_winner()
        column = self._check_columns_winner()
        diagonal = self._check_diagonals_winner()
        
        if line != self.defalt_value or \
            column != self.defalt_value or \
            diagonal != self.defalt_value:
            return True