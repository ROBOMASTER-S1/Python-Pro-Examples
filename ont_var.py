text_colour=(
    '\x1b[31m', # index 0 = red
    '\x1b[32m', # index 1 = green
    '\x1b[33m', # index 2 = yellow
    '\x1b[34m', # index 3 = blue
    '\x1b[35m', # index 4 = purple
    '\x1b[36m', # index 5 = cyan
    '\x1b[37m'  # index 6 = white
    )

text_words=(
    f'\n{text_colour[1]}Welcome to ONTARIO LOTTO 6/49 \
RANDOM NUMBER GENERATOR. Good Luck!\n\nPress \
(Enter) to activate the ONTARIO LOTTO 6/49 RANDOM \
NUMBER GENERATOR:', # index 0 = text_words

    f'\n{text_colour[1]}ONTARIO LOTTO 6/49 RANDOM \
NUMBER GENERATOR is activated.\n\nONTARIO LOTTO \
6/49 RANDOM NUMBER GENERATOR SEQUENCE:', # index 1 = text_words

    f'\n{text_colour[2]}Press (N) then press (Enter) to \
randomly pick a different set of Ontario Lotto 6/49 \
numbers.\n\nPress (Q) then press (Enter) to quit:\
{text_colour[1]}', # index 2 = text_words

    f'\n{text_colour[1]}Thanks for playing ONTARIO \
LOTTO 6/49 RANDOM NUMBER GENERATOR. Good \
Luck!', # index 3 = text_words

    'title ONTARIO LOTTO 6/49 RANDOM NUMBER \
GENERATOR' # index 4 = text_words
    )

win_sound='TYPE','Windows Notify Messaging'

text_fx=('cls','n','q') # clear screen, n = random number button, q = quit
