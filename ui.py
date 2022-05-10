class UI:
    """Every string on the game must be taken from here
    """
    def __init__(self) -> None:
        self.language = 'English'

    def select_language_options(self):
        return {1: 'ENGLISH', 2: 'PORTUGUES'}

    def select_game_command(self):
        returns = {'English': 'SELECT LANGUAGE',
                    'Portugues': 'SELECIONAR IDIOMA'}
        
        return returns[self.language]

    def main_menu_options(self):
        returns = {'English': {1: 'PLAY', 2:'SELECT LANGUAGE', 3: 'HOW TO PLAY', 4:'EXIT'},
                    'Portugues': {1: 'JOGAR', 2:'SELECIONAR IDIOMA',3: 'COMO JOGAR', 4:'SAIR'}}

        return returns[self.language]
    
    def main_menu_command(self):
        returns = {'English': 'MENU OPTIONS',
                    'Portugues': 'MENU DE OPÇÕES'}

        return returns[self.language]

    def pre_game_options(self):
        returns = {'English': {1: 'START NEW GAME', 2:'CONTINUE', 3: 'RETURN'},
                    'Portugues': {1: 'COMEÇAR NOVO JOGO', 2: 'CONTINUAR', 3: 'VOLTAR'}}
                
        return returns[self.language]
    
    def pre_game_command(self):
        returns = {'English': 'WHAT DO YOU WANT?',
                    'Portugues': 'O QUE VOCÊ DESEJA?'}
                
        return returns[self.language]

    def select_opponent_options(self):
        returns = {'English': {1: 'LOCAL MULTIPLAYER', 2: 'CPU'},
                    'Portugues': {1: 'MULTI JOGADOR LOCAL ', 2: 'COMPUTADOR'}}

        return returns[self.language]
    
    def select_opponent_command(self):
        returns = {'English': 'PICK YOUR OPPONENT',
                    'Portugues': 'SELECIONE SEU OPONENTE'}

        return returns[self.language]

    def select_difficulty_options(self):
        returns = {'English': {1: 'EASY', 2: 'MEDIUM', 3: 'HARD', 4: 'IMPOSIBLE'},
                    'Portugues': {1: 'FACIL', 2: 'MEDIO', 3: 'DIFICIL',4: 'IMPOSSÍVEL'}}

        return returns[self.language]
    
    def select_difficulty_command(self):
        returns = {'English': 'PICK YOUR DIFFICULTY',
                    'Portugues': 'SELECIONE SUA DIFICULDADE'}

        return returns[self.language]

    def show_turn(self, turn):
        returns = {'English': f'player {turn} turn!',
                    'Portugues': f'Vez do jogador {turn}'}

        return returns[self.language]

    def get_user_input_play(self):
        returns = {'English': 'PLACE MARK ON:\n',
                    'Portugues': 'COLOCAR MARCA NO:\n'}

        return returns[self.language]

    def win_message(self, winner:str, positions:list):
        # making list nice to print
        position = str(positions).replace('[', '').replace(']', '').replace("'", '').replace(',', ' and')
        returns = {'English': f'PLAYER {winner} WON THE GAME ON THE {position.upper()}!',
                    'Portugues': f'JOGADO {winner} GANHOU O JOGO NA POSIÇÃO {position.upper()}!'}

        return returns[self.language]

    def draw_message(self):
        returns = {'English': 'THE GAME ENDED UP ON A DRAW!',
                    'Portugues': 'O JOGO TEMINOU UM UM EMPATE!'}

        return returns[self.language]

    def positions(self, position):
        returns = {'English': {'diagonal': 'diagonal', 'line': 'line', 'column': 'column'},
                    'Portugues': {'diagonal': 'diagonal', 'line': 'linha', 'column': 'coluna'}}

        return returns[self.language][position]


    def how_to_play(self):
        returns = {'English': 'You will play as the "x", and your opponent as the "o".\n\nIn your turn, enter the position you want to play:\nThe number 1 indicates the upper left corner; the 2, the upper middle and so on.\n\nThe first player completing 3 signs on either horizontal, vertical or diagonal first wins.\n\nGOOD LUCK!',
                    'Portugues': 'Você irá jogar como o "x", e o seu oponente como o "o".\n\nNa sua vez, digite a posição que deseja jogar:\nO número 1 indica o canto superior esquerdo; o 2, o meio superior e assim por diante.\n\nO primeiro jogador a conpletar 3 de sinais em qualquer horizontal, vertical ou diagonal primeiro vence.\n\nBOA SORTE!'}

        return returns[self.language]

    def end_options(self):
        returns = {'English': {1: 'PLAY AGAIN', 2: 'MAIN MENU'},
                    'Portugues': {1: 'JOGAR NOVAMENTE', 2: 'MENU INICIAL'}}

        return returns[self.language]
    
    def end_command(self):
        returns = {'English': 'GAME IS OVER. WHAT DO YOU WANT?',
                    'Portugues': 'O JOGO ACABOU. O QUE VOCÊ DESEJA?'}

        return returns[self.language]

    def no_game_in_progress_error(self):
        returns = {'English': 'YOU MUST HAVE A GAME IN PROGRESS TO CONTINUE',
                    'Portugues': 'VOCÊ PRECISA TER UM JOGO EM ANDAMENTO PARA CONTINUAR'}

        return returns[self.language]

    def empty_space(self):
        returns = {'English': 'PICK A EMPTY SPACE',
                    'Portugues': 'ESCOLHA UM LUGAR VAZIO'}

        return returns[self.language]   

    def continue_input(self):
        returns = {'English': 'PRESS ENTER TO CONTINUE',
                    'Portugues': 'APERTE ENTER PARA CONTINUAR'}

        return returns[self.language]

    def main_menu_alert(self):
        returns = {'English': 'your score will be saved if you retun to the main menu',
                    'Portugues': 'seu placar será salvo se você voltar para o menu inicial'}

        return returns[self.language]

    def new_game_alert(self):
        returns = {'English': 'the score will be reset if you start a new game',
                    'Portugues': 'o placa irá ser reiniciado se você começar um novo jogo'}

        return returns[self.language]