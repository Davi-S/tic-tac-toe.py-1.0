from board import TicTacToeBoard
from utils import pick_option, number_to_grid, pick_int
from random import randint
from ui import UI

class TicTacToeGame():
    def __init__(self, board:type[TicTacToeBoard], user_interface:type[UI]) -> None:
        self.ui = user_interface
        self.board = board
        self.opponent = None
        self.turn = 'x'
        self.difficulty = None
        
    def main_menu(self):
        while True:
            menu_option = pick_option(self.ui.main_menu_options(), self.ui.main_menu_command())
            
            if menu_option == 1:
                opponent = self.pick_opponent()
                if opponent == 2:
                    self.pick_difficulty()

                pre_game = pick_option(self.ui.pre_game_options(), self.ui.pre_game_command())
                if pre_game == 1:
                    return 
                elif pre_game == 2: 
                    continue

            elif menu_option == 2:
                self.select_language()
                continue 

            elif menu_option == 3:
                exit()

    def select_language(self):
        self.ui.language = pick_option(self.ui.select_language_options(), self.ui.select_game_command(), str)

    def pick_opponent(self):
        opponent = pick_option(self.ui.select_opponent_options(), self.ui.select_opponent_command())
        self.opponent = 'player2' if opponent == 1 else 'cpu'

    def pick_difficulty(self):
        self.difficulty = pick_option(self.ui.select_difficulty_options(), self.ui.select_difficulty_command())

    def change_turn(self):
        self.turn = 'x' if self.turn == 'o' else 'o'


    def play(self):
        while True:
            self.board.print_formated_board()

            print(self.ui.show_turn(self.turn))
            # colect and mark the player option
            while True:
                line, column = number_to_grid(pick_int(self.ui.get_user_input_play()))
                if self.board.place_mark(line, column, self.turn):
                    break
            self.change_turn()

            if self.board.check_win()[0]:
                self.board.print_formated_board()
                print(self.ui.win_message(self.board.check_win()[1], self.board.check_win()[2]))
                break
            
            if self.board.is_filled():
                self.board.print_formated_board()
                print(self.ui.draw_message())
                break

            if self.turn == 'o' and self.opponent == 'cpu':
                while True:
                    line, column = randint(0, 2), randint(0, 2)
                    if self.board.place_mark(line, column, self.turn):
                        self.change_turn()
                        break
            
            
            if self.board.check_win()[0]:
                self.board.print_formated_board()
                break
            
            if self.board.is_filled():
                self.board.print_formated_board()
                break

        
    


    


