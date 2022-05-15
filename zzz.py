from typing import Union
from timeit import timeit
class CPU:
    def __init__(self) -> None:
        self.board = [['x', 'x', 'o'],['o', 'o', 'x'],['', 'x', 'o']]
        self.defalt_value = ' '
        self.size = 3

    def check_near_win(self, position:list, player:str) -> bool:
        return position.count(player) == (self.size - 1)\
            and position.count(self.defalt_value) == 1

    def small(self, action:str='x') -> Union[tuple[int], bool]:
        return next(((line_idx, line.index(' ')) for line_idx, line in enumerate(self.board) if self.check_near_win(line, action)), False) 

    def big(self, action:str='x') -> Union[tuple[int], bool]:
        for line_idx, line in enumerate(self.board):
            if self.check_near_win(line, action):
                return line_idx, line.index(' ')
        return False

small_code = timeit(CPU().small, number=100000)
big_code = timeit(CPU().big, number=100000)
fast = min(small_code, big_code)
slow = max(small_code, big_code)
print(f'small: {small_code}\nbig: {big_code}')
print('\n')
if fast == small_code:
    print('faster: small')
else:
    print('faster: big')