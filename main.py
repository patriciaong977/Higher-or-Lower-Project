#### Imports ####
from os import system, name

### Clear the Screen Function ####
def clear():
    if name == 'nt':  # For windows
        _ = system('cls')
    else: # For Unix and Linux
        _ = system('clear')
