from board import TicTacToeBoard
from game import TicTacToeGame
from os import system
from ui import UI

def main():
    system("cls")
    ui = UI()
    board = TicTacToeBoard(ui)
    game = TicTacToeGame(board, ui)
    game.main_menu() # Initialize game options
    system("cls")
    game.play()

        
if __name__ == '__main__':
    main()

