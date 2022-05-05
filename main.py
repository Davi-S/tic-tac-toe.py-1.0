from ui import UI
from cpu_ia import CPU
from board import TicTacToeBoard
from game import TicTacToeGame


def main():
    ui = UI()
    cpu = CPU()
    board = TicTacToeBoard(ui)
    game = TicTacToeGame(board, ui, cpu)
    game.main()

        
if __name__ == '__main__':
    main()

