class TicTacToeBoard():
    def __init__(self, defalt_value:str=' ') -> None:
        self.defalt_value = defalt_value
        self.board = list(self.create_board(self.defalt_value))

    def create_board(self, defalt_value:str, size:int=3):
        gridline = [defalt_value for _ in range(size)]
        return [list(gridline) for _ in range(size)]

    def is_filled(self):
        for line in self.board:
            for column in line:
                if column == self.defalt_value:
                    return False
        return True

    def is_marked(self, line:int, column:int):
        return self.board[line][column] == self.defalt_value

    def place_mark(self, line:int, column:int, mark:str):
        self.board[line][column] = mark


    def print_formated_board(self):
        for idx, line in enumerate(self.board):
            print('\n', str(line).replace('[', '').replace(']', '').replace(',', ' |').replace("'", ''))
            if idx < len(self.board) -1:
                for count, _ in enumerate(line, start=1):
                    print('---', end='')
                    if count < len(line):
                        print('|', end='')
    


    def _check_set(self, seti:set):
        return len(seti) == 1 and seti != {self.defalt_value}

    def _check_lines(self) -> str:
        return next((line[0] for line in self.board if self._check_set(set(line))), self.defalt_value)

    def _check_columns(self) -> str:
        for count in range(len(self.board)):
            seti = set()
            for line in self.board:
                seti.add(line[count])
            if self._check_set(seti):
                return line[count]
                
        return self.defalt_value

    def _check_diagonals(self) -> str:
        seti = {self.board[idx][idx] for idx, _ in enumerate(self.board)}
        if self._check_set(seti):
            return self.board[0][0]
        
        seti = {self.board[idx][len(self.board) - idx - 1] for idx, _ in enumerate(self.board)}
        if self._check_set(seti):
            return self.board[0][len(self.board)-1]

        return self.defalt_value

    def check_win(self) -> tuple:
        line = self._check_lines()
        column = self._check_columns()
        diagonal = self._check_diagonals()

        if line != self.defalt_value:
            return True, line, 'Line'
        
        if column != self.defalt_value:
            return True, column, 'Column'

        if diagonal != self.defalt_value:
            return True, diagonal, 'Diagonal'

        return False, None, None