from time import sleep
from os import system
from ui import UI

def pick_option(options:dict, command:str, return_type=int) -> int:
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
    option = None
    while option not in range(1, 10):
        try:
            option = int(input(command))
        except ValueError:
            sleep(0.3)
            print('\nPICK A NUMBER IN BETWEEN 1 AND 9\n')
            sleep(1)
    return option



def number_to_grid(number) -> tuple:
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

    

    