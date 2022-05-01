from random import randint

class CPU:
    def __init__(self) -> None:
        self.difficulty = None
    
    def _easy(self) -> tuple:
        return randint(0, 2), randint(0, 2)

    def _medium(self, board) -> tuple:
        pass

    def _hard(self, board) -> tuple:
        pass

    def play(self, board) -> tuple:
        if self.difficulty == 1:
            return self._easy()

        elif self.difficulty == 2:
            return self._medium(board)

        elif self.difficulty == 3:
            return self._hard(board)
