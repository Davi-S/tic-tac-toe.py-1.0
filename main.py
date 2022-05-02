from ui import UI
from cpu_ia import CPU
from board import TicTacToeBoard
from game import TicTacToeGame
from os import system


def main():
    system("cls")
    ui = UI()
    cpu = CPU()
    board = TicTacToeBoard(ui)
    game = TicTacToeGame(board, ui, cpu)
    game.main()

        
if __name__ == '__main__':
    main()

