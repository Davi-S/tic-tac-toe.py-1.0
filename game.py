from typing import Union
from ui import UI
from cpu_ia import CPU
from board import TicTacToeBoard
from utils import pick_option, number_to_grid, pick_int
from os import system

class TicTacToeGame():
    def __init__(self, board:type[TicTacToeBoard], user_interface:type[UI], cpu_ia:type[CPU]) -> None:
        self.cpu = cpu_ia
        self.ui = user_interface
        self.board = board
        self.opponent = None
        
    def main_menu(self) -> None:
        """Initiates most game configs. Must always come before self.main()
        """
        while True:
            system("cls")
            menu_option = pick_option(self.ui.main_menu_options(), self.ui.main_menu_command())
            
            if menu_option == 1: # Play option
                system("cls")
                opponent = self.pick_opponent()

                if opponent == 2: # If the pponent is the cpu
                    system("cls")
                    self.pick_difficulty()

                system("cls")
                print(self.ui.new_game_alert())
                pre_game = pick_option(self.ui.pre_game_options(), self.ui.pre_game_command())
                if pre_game == 1:
                    # Start placar for new game
                    self.score = {'x': 0, 'o': 0}
                    system("cls")
                    return

                elif pre_game == 2: # continue game option
                    if self.board.board is None:
                        system("cls")
                        print(self.ui.no_game_in_progress_error())
                        continue
                    system("cls")
                    return

                elif pre_game == 3: # return option
                    continue

            elif menu_option == 2:
                system("cls")
                self.select_language()
                continue 
            
            elif menu_option == 3:
                print(self.ui.how_to_play())
                # Show the rules until any input
                input(self.ui.continue_input())
                continue

            elif menu_option == 4:
                exit()

    def select_language(self) -> None:
        self.ui.language = pick_option(self.ui.select_language_options(), self.ui.select_game_command(), str)

    def pick_opponent(self) -> int:
        opponent_option = pick_option(self.ui.select_opponent_options(), self.ui.select_opponent_command())
        self.opponent = 'player2' if opponent_option == 1 else 'cpu'
        return opponent_option

    def pick_difficulty(self):
        self.cpu.difficulty = pick_option(self.ui.select_difficulty_options(), self.ui.select_difficulty_command())

    def change_turn(self) -> None:
        self.turn = 'x' if self.turn == 'o' else 'o'

    def player_turn(self) -> None:
        """Play in a valid place on the board with player input
        """
        while True:
            line, column = number_to_grid(pick_int(self.ui.get_user_input_play()))
            if self.board.place_mark(line, column, self.turn):
                return
            print(self.ui.empty_space())

    def cpu_turn(self) -> None:
        """Play in a valid place on the board with cpu choice
        """
        while True:
            line, column = self.cpu.play(self.board.board, self.board.defalt_value)
            if self.board.place_mark(line, column, self.turn):
                self.change_turn()
                break
    
    def win_event(self, win_info:Union(list, tuple)) -> None:
        """Events after a win

        Args:
            win_info (list or tuple): [bool, str(winner), str(how the win occoured)].
                                      if bool is false, all the other values must be None
        """
        system("cls")
        self.board.print_formated_board()
        print(self.ui.win_message(win_info[1], win_info[2]))
        self.score[win_info[1]] += 1
        # print the score
        for key, value in self.score.items():
            print(f'{key}: {value}')

    def draw_event(self) -> None:
        """Events after a draw
        """
        system("cls")
        self.board.print_formated_board()
        print(self.ui.draw_message())
        # print the score
        for key, value in self.score.items():
            print(f'{key}: {value}')


    def play(self) -> None:
        """The loop for a game in progress. Ends on a win or draw
        """
        # player x must always start. if not, all functions that handle cpu throws must
        # also changes to handle the new sign ('x' or 'o') assignment 
        self.turn = 'x'

        while True:
            system("cls")
            self.board.print_formated_board()
            print(self.ui.show_turn(self.turn))

            # colect and mark the player option
            self.player_turn()
            self.change_turn()

            if self.board.check_win()[0]:
                self.win_event(self.board.check_win())
                return
            if self.board.is_filled():
                self.draw_event()
                return

            if self.turn == 'o' and self.opponent == 'cpu':
                self.cpu_turn()

            if self.board.check_win()[0]:
                self.win_event(self.board.check_win())
                return
            if self.board.is_filled():
                self.draw_event()
                return


    def main(self) -> None:
        """The main game loop. Handle the main menu loop and play loop
        """
        while True:
            self.main_menu()
            self.board.create_board()
            while True:
                self.play()
                print('\n' + self.ui.main_menu_alert())
                end = pick_option(self.ui.end_options(), self.ui.end_command())
                if end != 1: # not the "play again" choice
                    break
                self.board.create_board()
                continue
            
        
    


    


