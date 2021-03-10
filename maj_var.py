text_features=(
    'cls', # index 0 = clear screen
    '\x1b[31m', # index 1 = red
    '\x1b[32m', # index 2 = green
    '\x1b[33m', # index 3 = yellow
    '\x1b[34m', # index 4 = blue
    '\x1b[37m', # index 5 = white
    'title Majestic Calculator' # index 6 = window title
    )

text_words=(
    f'\n{text_features[3]}Majestic Calculator\n\n{text_features [5]}\
Press (1) for Standard Decimal Base 10 Calculator\nPress \
(2) for Binary Base 2 Calculator\nPress (3) for Octal Base 8 \
Calculator\nPress (4) for Hexadecimal Base 16 Calculator\n\n\
{text_features[3]}(BIN) (OCT) (HEX) Number Translator\n\n\
{text_features[5]}Press (5) for Binary Base 2 Number Translator\n\
Press (6) for Octal Base 8 Number Translator\nPress (7) for \
Hexadecimal Base 16 Number Translator\n\nPress (Q) to quit\n\n\
{text_features[1]}READY:{text_features[5]}', # index 0 = text_words

    f'\n{text_features[3]}Majestic Calculator\n\nStandard Decimal \
Base 10 Calculator', # index 1 = text_words

    f'\n{text_features[3]}Majestic Calculator\n\nBinary Base 2 \
Calculator', # index 2 = text_words

    f'\n{text_features[3]}Majestic Calculator\n\nOctal Base 8 \
Calculator', # index 3 = text_words

    f'\n{text_features[3]}Majestic Calculator\n\nHexadecimal \
Base 16 Calculator', # index 4 = text_words

    f'\n{text_features[3]}Majestic Calculator\n\nBinary Base 2 \
Number Translator', # index 5 = text_words

    f'\n{text_features[3]}Majestic Calculator\n\nOctal Base 8 \
Number Translator', # index 6 = text_words

    f'\n{text_features[3]}Majestic Calculator\n\nHexadecimal \
Base 16 Number Translator', # index 7 = text_words

    f'\n{text_features[3]}Majestic Calculator\n\nBinary Base 2 \
Translator', # index 8 = text_words

    f'\n{text_features[3]}Majestic Calculator\n\nOctal Base 8 \
Translator', # index 9 = text_words

    f'\n{text_features[3]}Majestic Calculator\n\nHexadecimal \
Base 16 Translator', # index 10 = text_words

    f'\n\n{text_features[5]}Please enter a decimal base 10 \
number:{text_features[2]}', # index 11 = text_words

    f'\n\n{text_features[5]}Enter First Number:\
{text_features[2]}', # index 12 = text_words

    f'\n\n{text_features[5]}Enter (+) (-) (*) (/) Operator:\
    {text_features[2]}', # index 13 = text_words

    f'\n\n{text_features[5]}Enter Second Number:\
    {text_features[2]}', # index 14 = text_words

    f'\n{text_features[3]}Majestic Calculator\n\n\
    {text_features[1]}Invalid operator!', # index 15 = text_words

    f'\n\n{text_features[1]}ERROR! {text_features[3]}\
    Cannot divide by zero.', # index 16 = text_words

    f'\n\n{text_features[1]}ERROR!', # index 17 = text_words

    f'\n{text_features[5]}Do you wish to continue? Press \
(Enter) or press (Q) to quit:', # index 18 = text_words

    f'\n{text_features[3]}Thanks for choosing Majestic \
Calculator' # index 19 = text_words
    )

operator=(
    chr(43),chr(45),chr(42),chr(47) # math operators in ASCII codes
    )

button=('1','2','3','4','5','6','7','q') # button choices, q = quit
