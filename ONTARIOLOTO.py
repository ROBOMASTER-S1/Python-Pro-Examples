import os,time,math,random,winsound
from ont_var import*

def ont_lotto():
    os.system(text_words[4])

    random_num=(
    random.randint(1,9), # index 0 = random_num
    random.randint(10,17), # index 1 = random_num
    random.randint(18,25), # index 2 = random_num
    random.randint(26,33), # index 3 = random_num
    random.randint(34,41), # index 4 = random_num
    random.randint(42,49)  # index 5 = random_num
    )
    
    y=0
    while y<=len(text_words[0]):
        winsound.PlaySound(win_sound[0],winsound.SND_ASYNC)
        print(text_words[0][:y])
        time.sleep(.06)
        os.system(text_fx[0])
        y+=1

    button=input(text_words[0]).lower().strip()

    y=0
    while y<=len(text_words[1]):
        winsound.PlaySound(win_sound[0],winsound.SND_ASYNC)
        print(text_words[1][:y])
        time.sleep(.06)
        os.system(text_fx[0])
        y+=1

    while True:
        winsound.PlaySound(win_sound[1],winsound.SND_ASYNC)
        print(
            f'{text_words[1]}{text_colour[0]}({random_num[0]}) \
({random_num[1]}) ({random_num[2]}) ({random_num[3]}) \
({random_num[4]}) ({random_num[5]})'
            )

        button=input(text_words[2]).lower().strip()

        os.system(text_fx[0])

        if button==(text_fx[1]):
            random_num=(
            random.randint(1,9),
            random.randint(10,17),
            random.randint(18,25),
            random.randint(26,33),
            random.randint(34,41),
            random.randint(42,49)
            )
        elif button==(text_fx[2]):
            break

    y=0
    while y<=len(text_words[3]):
        winsound.PlaySound(win_sound[0],winsound.SND_ASYNC)
        print(text_words[3][:y])
        time.sleep(.06)
        os.system(text_fx[0])
        y+=1

    print(text_words[3])
    time.sleep(3)
    
ont_lotto()
