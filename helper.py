from string import printable
from random import randint
from random import choice


bad_chars = ["'", '"', printable[-1], printable[-2], printable[-3],
    printable[-4], printable[-5], printable[-6]
]
color = {'HEADER': '\x1b[95m', 'OKBLUE': '\x1b[94m',
         'OKCYAN': '\x1b[96m', 'OKGREEN': '\x1b[92m',
         'WARNING': '\x1b[93m', 'FAIL': '\x1b[91m',
         'ENDC': '\x1b[0m', 'BOLD': '\x1b[1m',
         'UNDERLINE': '\x1b[4m'
        }

def password_generator():
    '''Returns a password'''
    length = randint(13, 20)
    password = ''
    
    for _ in range(length):
        letter = choice(printable)

        if letter not in bad_chars:
            password += letter

    return password # When adding this feature to the program make sure that returned 
                    #stuff is copied to the clip board