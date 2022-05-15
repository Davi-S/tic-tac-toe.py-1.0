from ui import UI
from cpu_ia import CPU
from board import TicTacToeBoard
from game import TicTacToeGame


def main():
    board = TicTacToeBoard()
    ui = UI()
    cpu = CPU()
    game = TicTacToeGame(board, ui, cpu)
    game.main()

        
if __name__ == '__main__':
    main()

