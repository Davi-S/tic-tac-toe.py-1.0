from board import TicTacToeBoard
from game import TicTacToeGame
from os import system
from utils import pick_option, pick_int, number_to_grid
from random import randint

def main_menu(game:type[TicTacToeGame]):
    while True:
        menu_option = pick_option({'1': 'PLAY', '2':'SELECT LANGUAGE', '3':'EXIT'}, 'MENU OPTIONS')
        
        if menu_option == 1:

            opponent = game.pick_opponent()
            if opponent == 2:
                game.pick_difficulty()

            pre_game = pick_option({'1': 'START', '2': 'RETURN'}, 'GAME') 
            if pre_game == 1:
                return 
        
            elif pre_game == 2: 
                continue

        elif menu_option == 2:
            game.select_language()
            continue 

        elif menu_option == 3:
            exit()
    

def main():
    system("cls")
    board = TicTacToeBoard()
    game = TicTacToeGame(board)
    main_menu(game) # Initialize game options
    system("cls")

    for _ in range(8):
        board.print_formated_board()
        print(f'player {game.turn.upper()} time')

        while True:
            line, column = number_to_grid(pick_int('PLACE MARK ON:\n'))
            if board.is_marked(line, column):
                break
            print('escolha um lugar vazio')
            
        board.place_mark(line, column, game.turn)
        game.change_turn()
        if board.check_win()[0]:
            print(f'{board.check_win()[1]} won the game on {board.check_win()[2]}')
            board.print_formated_board()
            break


        
if __name__ == '__main__':
    main()

