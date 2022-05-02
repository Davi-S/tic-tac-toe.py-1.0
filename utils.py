from time import sleep
from typing import Union

def pick_option(options:dict, command:str, return_type=int) -> Union[int, str]:
    """return a int representation of a given dict key. can alse return the dict value

    Args:
        options (dict): the dict with the option to choose
        command (str): imput prompt
        return_type (int or str, optional): int for the key, str for the value. Defaults to int)

    Returns:
        int or str: the key or value of the dict
    """
    option = None
    while option not in options.keys():
        print(command)
        for key, value in options.items():
            print (f'[{key}] - {value}')
        option = input('->')

        if option not in options.keys():
            sleep(0.3)
            print('\nPICK A VALID OPTION\n')
            sleep(1)

    if return_type is int:
        return int(option)
    
    elif return_type is str:
        return str(options[option]).title()


def pick_int(command:str) -> int:
    """Acepts a input in between 1 and 9
    Args:
        command (str): prompt input

    Returns:
        int: the int representaton of the number
    """
    option = None
    while option not in range(1, 10):
        try:
            option = int(input(command))
        except ValueError:
            sleep(0.3)
            print('\nPICK A NUMBER IN BETWEEN 1 AND 9\n')
            sleep(1)
    return option


def number_to_grid(number:int) -> tuple:
    """return a single number as a x a y axis on the board

    Args:
        number (int): the number that represents a place on the board

    Returns:
        tuple: x and y axis
    """
    if number == 7:
        return 0, 0

    elif number == 8:
        return 0, 1

    elif number == 9:
        return 0, 2

    elif number == 4:
        return 1, 0

    elif number == 5:
        return 1, 1

    elif number == 6:
        return 1, 2

    elif number == 1:
        return 2, 0

    elif number == 2:
        return 2, 1

    elif number == 3:
        return 2, 2

    

    