from ui import UI
from cpu_ia import CPU
from board import TicTacToeBoard
from input import CustomInput, number_to_grid
from os import system
from time import sleep

class TicTacToeGame():
    def __init__(self, board:type[TicTacToeBoard], user_interface:type[UI], cpu_ia:type[CPU]) -> None:
        self.board = board
        self.ui = user_interface
        self.cpu = cpu_ia
        self.ci = CustomInput()
        self.player1 = {'player': 'player_1',     'symbol': 'x'}
        self.player2 = {'player': 'undefined', 'symbol': 'o'}
        self.score = None

    def main_menu(self) -> None:
        """Initiates game configs."""
        while True:
            # chosse main menu options
            system("cls")
            menu_option = self.ci.pick_option(self.ui.main_menu_options(), self.ui.main_menu_command())

            if menu_option == 1: # Play option
                # Choose opponent
                system("cls")
                opponent_option = self.ci.pick_option(self.ui.opponent_options(), self.ui.opponent_command())
                self.set_players(opponent_option)

                if opponent_option == 2: # CPU opponent
                    # choose difficulty
                    system("cls")
                    difficulty_option = self.ci.pick_option(self.ui.difficulty_options(), self.ui.difficulty_command())
                    self.set_difficulty(difficulty_option)

                # choose pre_game options
                system("cls")
                print(self.ui.new_game_alert())
                pre_game = self.ci.pick_option(self.ui.pre_game_options(), self.ui.pre_game_command())

                if pre_game == 1: # Start new game
                    self.score = {f'{self.player1["player"]}': 0, f'{self.player2["player"]}': 0} # Start score for new game
                    return

                elif pre_game == 2: # continue game option
                    if self.board.board is None: # no game was initiated yet
                        system("cls")
                        print(self.ui.no_game_in_progress_error())
                        sleep(2)
                        continue
                    return

                elif pre_game == 3: # return option. (user decided not start a game for now)
                    continue

            elif menu_option == 2: # select language option
                # choose language
                system("cls")
                language_option = self.ci.pick_option(self.ui.language_options(), self.ui.language_command(), 'value')
                self.set_language(language_option)
                continue 
            
            elif menu_option == 3: # show rules option
                system("cls")
                print(self.ui.how_to_play())
                input(self.ui.continue_input()) # Show the rules until any input
                continue

            elif menu_option == 4: # exit game
                exit()

    def set_players(self, opponent:int) -> int:
        self.player1['player'] = 'player_1' if opponent == 1 else 'you'
        self.player2['player'] = 'player_2' if opponent == 1 else 'cpu'
        

    def set_language(self, language:str) -> None:
        self.ui.language = language.title()

    def set_difficulty(self, difficulty):
        self.cpu.difficulty = difficulty

    
    def play(self, starter:dict) -> None:
        """The loop for a game in progress. Ends on a win or draw"""
        turn = starter

        while True:
            system("cls")
            self.board.print_formated_board()
            print(self.ui.show_turn(**turn))

            self.player_turn(turn)
            if self.check_end(turn):
                return
            turn = self.change_turn(turn)

            if turn['player'] == 'cpu':
                self.cpu_turn(turn)
                if self.check_end(turn):
                    return
                turn = self.change_turn(turn)

    def player_turn(self, turn:str) -> None:
        """Play in a valid place on the board with player input"""
        while True:
            user_input = self.ci.pick_in_range(self.ui.get_user_input_play(), 1, self.board.size**2)
            line, column = number_to_grid(self.board.size, self.board.size, user_input)
            if self.board.place_mark(line, column, turn['symbol']):
                return
            print(self.ui.not_empty_space_error())

    def cpu_turn(self, turn) -> None:
        """Play in a valid place on the board with cpu choice"""
        while True:
            line, column = self.cpu.play(self.board)
            if self.board.place_mark(line, column, turn['symbol']):
                return

    def change_turn(self, actual_turn:str) -> dict:
        """Change the turn on the game
        
        Returns:
            dict: the dict of the new player turn"""
        return self.player1 if actual_turn == self.player2 else self.player2

    def check_end(self, turn:dict) -> bool:
        """checks if the game has ended and run the due events

        Args:
            turn (dict): The player turn when the game was over

        Returns:
            bool: False if the game has not ended. True if the game has ended
        """
        if self.board.check_win():
            self.win_event(self.board.win_info(), turn)
            return True
        if self.board.is_filled():
            self.draw_event()
            return True
        return False

    def win_event(self, win_info:dict, turn:dict) -> None:
        """Events after a win

        Args:
            win_info (dict): board.win_info return type
            turn (dict): info of the player that won
        """
        system("cls")
        self.board.print_formated_board()
        positions = [key for key, value in win_info.items() if value not in [0, 'x', 'o']]

        print(self.ui.win_message(turn, positions))
        self.score[turn['player']] += 1
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

    
    def main(self) -> None:
        """The main game loop to effectively starts playing"""
        while True:
            self.main_menu()
            self.board.create_board()
            while True:
                self.play(self.player1)
                print('\n' + self.ui.main_menu_alert())
                end = self.ci.pick_option(self.ui.end_options(), self.ui.end_command())
                if end != 1: # not the "play again" choice
                    break
                self.board.create_board()
                continue
            
        
    


    


