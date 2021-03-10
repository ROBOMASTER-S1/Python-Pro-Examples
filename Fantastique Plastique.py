import os,time,math,winsound
from fan_var import*

def fan_plast():
    os.system(text_info[4])
    while True:
        os.system(text_works[0])
        winsound.PlaySound(win_sound[0],winsound.SND_ASYNC)
        
        for i in text_words:
            print(i)
            
        try:
            ounce0=float(input(text_info[0]).lower().strip())
            os.system(text_works[0])
            for i in text_words:
                print(i)
                
            winsound.PlaySound(win_sound[1],winsound.SND_ASYNC)
            
            print(f'\n{text_colour[2]}{ounce0} Ounce = {text_colour[1]}\
{ounce0*grams0} {text_colour[2]}Grams or {text_colour[1]}\
{ounce0*grams1} {text_colour[2]}Grams.')
            
            button=input(text_info[1]).lower().strip()
            if button==(''):
                continue
            elif button==(text_works[1]):
                os.system(text_works[0])
                winsound.PlaySound(win_sound[2],winsound.SND_ASYNC)
                print(text_info[2])
                time.sleep(3)
                break
            
        except ValueError:
            os.system(text_works[0])
            
            for i in text_words:
                print(i)
                
            winsound.PlaySound(win_sound[3],winsound.SND_ASYNC)
            
            print(text_info[3])
            
            time.sleep(2)
            
fan_plast()
