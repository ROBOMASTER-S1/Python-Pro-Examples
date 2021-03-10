text_features=(
    'cls', # index 0 = clear screen
    '\x1b[31m', # index 1 = red
    '\x1b[32m', # index 2 = green
    '\x1b[33m', # index 3 = yellow
    '\x1b[34m', # index 4 = blue
    '\x1b[37m'  # index 5 = red
    )

text_words=(
    f'\n{text_features[3]}ASCII CODE \
NUMERIC VALUE TRANSLATOR\n', # index 0 = text_words

    f'\n{text_features[3]}ASCII CODE \
CHARACTER VALUE TRANSLATOR\n', # index 1 = text_words

    f'\n{text_features[3]}ASCII CODE \
TRANSLATOR', # index 2 = text_words

    f'\n{text_features[3]}Thanks for choosing \
ASCII CODE TRANSLATOR', # index 3 = text_words

    'title ASCII CODE TRANSLATOR' # index 4 = text_words
    )

word_info=(
    f'{text_features[5]}Please type a number, then press \
(Enter) to confirm:{text_features[2]}', # index 0 = word_info

    f'{text_features[5]}Please type a letter key or a number \
key, then press (Enter) to confirm:{text_features[2]}', # index 1 = word_info

    f'\n{text_features[3]}Please choose which ASCII code \
translator you would like to use:\n\n{text_features[5]}Press \
(1) for ASCII code number values.\nPress (2) for ASCII code \
character values.\nPress (Q) to quit.{text_features[2]} ', # index 2 = word_info

    f'\n\n{text_features[3]}Do you wish to continue? Press \
(Enter) or press (Q) to quit:{text_features[2]}', # index 3 = word_info

    f'\n{text_features[1]}This is a Value Error!', # index 4 = word_info

    f'\n{text_features[1]}This is a Type Error!' # index 5 = word_info
    )

button=('1','2','q')
