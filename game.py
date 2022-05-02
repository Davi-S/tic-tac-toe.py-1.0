from time import sleep
from board import TicTacToeBoard
from utils import pick_option, number_to_grid, pick_int
from random import randint
from ui import UI
from cpu_ia import CPU

class TicTacToeGame():
    def __init__(self, board:type[TicTacToeBoard], user_interface:type[UI], cpu_ia:type[CPU]) -> None:
        self.cpu = cpu_ia
        self.ui = user_interface
        self.board = board
        self.opponent = None
        self.turn = 'x' # TODO change the marks, so the player can pick whatever he wants
                        # change also in the cpu_ia.py file
        
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
                print(self.ui.how_to_play())
                sleep(1)
                continue

            elif menu_option == 4:
                exit()

    def select_language(self):
        self.ui.language = pick_option(self.ui.select_language_options(), self.ui.select_game_command(), str)

    def pick_opponent(self):
        opponent_option = pick_option(self.ui.select_opponent_options(), self.ui.select_opponent_command())
        self.opponent = 'player2' if opponent_option == 1 else 'cpu'
        return opponent_option

    def pick_difficulty(self):
        self.cpu.difficulty = pick_option(self.ui.select_difficulty_options(), self.ui.select_difficulty_command())

    def change_turn(self):
        self.turn = 'x' if self.turn == 'o' else 'o'

    def player_turn(self):
        while True:
            line, column = number_to_grid(pick_int(self.ui.get_user_input_play()))
            if self.board.place_mark(line, column, self.turn):
                return

    def cpu_turn(self):
        while True:
            line, column = self.cpu.play(self.board.board, self.board.defalt_value)
            if self.board.place_mark(line, column, self.turn):
                self.change_turn()
                break
    
    def win_event(self):
        self.board.print_formated_board()
        print(self.ui.win_message(self.board.check_win()[1], self.board.check_win()[2]))

    def draw_event(self):
        self.board.print_formated_board()
        print(self.ui.draw_message())

    def play(self):
        self.board.create_board()
        while True:
            self.board.print_formated_board()
            print(self.ui.show_turn(self.turn))

            # colect and mark the player option
            self.player_turn()
            self.change_turn()

            if self.board.check_win()[0]:
                self.win_event()
                return
            if self.board.is_filled():
                self.draw_event()
                return

            if self.turn == 'o' and self.opponent == 'cpu':
                self.cpu_turn()

            if self.board.check_win()[0]:
                self.win_event()
                return
            if self.board.is_filled():
                self.draw_event()
                return


    def main(self):
        while True:
            self.main_menu()
            while True:
                self.play()
                end = pick_option(self.ui.end_options(), self.ui.end_command())
                if end == 1:
                    continue

                else:
                    break
            
        
    


    


