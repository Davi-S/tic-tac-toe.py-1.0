import contextlib
from os import system
from time import sleep
from math import ceil

class CustomInput:
    def _print_options(self, options:dict) -> None:
        for key, value in options.items():
            print (f'[{key}] - {value}')

    def _error_message(self, error_message):
        sleep(0.3)
        print(f'\n{error_message}\n')
        sleep(1)

    def pick_option(self, options:dict, prompt:str='', return_type:str='key',
                    error_message:str='PICK A VALID OPTION'):
        """input that can return the key or value of the given options

        Args:
            options (dict): the dict with the options to choose
            prompt (str): message shown on prompt. Defalts to "''"
            return_type (str): can be "key" or "value", and references to the dict key, or value.
                                Defaults to 'key'.
            error_message (str): the error message to show if the user input
                                someting out of the options range

        Returns:
            depends on the key and/or value of the given dict and the return_type param
        """
        option = None
        while option not in options.keys():
            print(prompt)
            self._print_options(options)
            with contextlib.suppress(ValueError): # using "contexlib.suppress" intead of "except: pass"
                option = int(input('->'))
            # there is no need to catch value error when trying to transform input in int. 
            # all invalid inputs can be treated with _error_message
            if option not in options.keys():
                self._error_message(error_message)
        return option if return_type == 'key' else options[option]


    def pick_in_range(self, prompt:str='', init_range:int=1, final_range:int=9,
                        error_message:str='PICK A VALID OPTION') -> int:
        """input that acepts only integer in between the given interval. Includes init and final

        Args:
            prompt (str): prompt message. Defalts to "''"
            init_range (int, optional): lower point. Defaults to 1.
            final_range (int, optional): higher point. Defaults to 9.
        """
        option = None
        while option not in range(init_range, final_range + 1):
            try:
                option = int(input(prompt))
            except ValueError:
                self._error_message(error_message)
        return option

    


    def number_to_grid(self, grid:list[list], number:int) -> tuple:
        """return a single number as a x a y axis on the board

        Args:
            number (int): the number that represents a place on a grid.
                            The grid values are counted from up to down, left to right

        Returns:
            tuple: x and y axis
        """
        count = 0
        for line_idx, line in enumerate(grid):
            for column_idx, _ in enumerate(line):
                count +=1
                if count == number:
                    return line_idx, column_idx
