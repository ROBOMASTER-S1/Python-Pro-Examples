text_colour=(
    '\x1b[31m', # index 0 = red
    '\x1b[32m', # index 1 = green
    '\x1b[33m', # index 2 = yellow
    '\x1b[34m', # index 3 = blue
    '\x1b[37m'  # index 4 = white
    )

win_sound=(
    'Windows Notify System Generic', # index 0 = win_sound
    'Windows Background', # index 1 = win_sound
    'Windows Notify Email','BUZZ' # index 2 = win_sound
    )

text_words=(
    f'\n{text_colour[2]}FANTASTIQUE {text_colour[1]}\
PLASTIQUE {text_colour[2]}Easy {text_colour[1]}Mix \
{text_colour[2]}Converter', # index 0 = text_words

    f'\n{text_colour[4]}Liquid Acrylic Mix: 8.oz = (1) Cup', # index 1 = text_words

    f'\nLiquid Acrylic Mix: 4.oz = One Half Cup', # index 2 = text_words

    f'\nGlow Powder Pigment: 28.349523 Grams = (1) \
Ounce', # index 3 = text_words

    f'\nGlow Powder Pigment: 14.1747615 Grams = One \
Half Ounce', # index 4 = text_words

    f'\nLiquid Acrylic Mix and Glow Powder Pigment Ratios: \
(4 = Parts LAM) to (1 = Part GPP)', # index 5 = text_words

    f'\n1.0 Ounce = 28.349523 Grams or 28.35 Grams.' # index 6 = text_words
    )

text_info=(
    f'\n{text_colour[2]}Please Enter Ounce Amount:\
{text_colour[1]}', # index 0 = text_info

    f'\n{text_colour[4]}Press (Enter) to convert again or press (Q) \
to quit.{text_colour[1]}', # index 1 = text_info

    f'\n{text_colour[2]}Thanks for measuring with FANTASTIQUE \
PLASTIQUE Easy Mix Converter', # index 2 = text_info

    f'\n{text_colour[0]}ERROR! Input numbers only please.', # index 3 = text_info

    'title FANTASTIQUE PLASTIQUE Easy Mix Converter' # index 4 = text_info
    )

text_works=('cls','q') # clear screen, q = quit

ounce1=float()
ounce0=float()
grams0=float(28.349523)
grams1=round(28.349523,2)
