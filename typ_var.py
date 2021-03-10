text_colours=(
    '\x1b[31m', # index 0 = red
    '\x1b[32m', # index 1 = green
    '\x1b[33m', # index 2 = yellow
    '\x1b[34m', # index 3 = blue
    '\x1b[35m', # index 4 = purple
    '\x1b[36m', # index 5 = cyan
    '\x1b[37m'  # index 6 = white
    )

sounds=('TYPE')

text_words=(
    f'\n{text_colours[2]}Welcome to the Typewriter \
Game.\n\n{text_colours[1]} Type a sentence and I \
will retype whatever you type.\n\n{text_colours[3]}\
To begin, simply type a sentence or sentences,\nthen \
press (Enter) and I will retype whatever you type.\n\n\
{text_colours[0]}Press (F) to make the letters type \
forward/default.\nPress (R) to make the letters type \
reverse.\nPress (B) to make the letters type back\
wards.\nPress (Q) to quit.', # index 0 = text_words

    f'\n\n{text_colours[2]}Type sentence here: \
{text_colours[1]}', # index 1 = text_words

    f'\n{text_colours[3]}Press (Enter) to type again or\npress any \
one of the options above:{text_colours[0]}', # index 2 = text_words

    f'\n{text_colours[3]}Thanks for playing Typewriter \
Game.', # index 3 = text_words
    )

os_features=('cls','title Typewriter Game')

button=('f','r','b','q')
