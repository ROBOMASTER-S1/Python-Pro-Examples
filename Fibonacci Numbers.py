import os,math,random,time,winsound
from fib_var import*

os.system(f'title Fibonacci Natural Number Sequence')

def Fib_Num():
    winsound.PlaySound(sounds[0],winsound.SND_ASYNC)
    
    for i in range(25):
        print('\n',' '*i,text_words[0])
        time.sleep(.25)
        os.system('cls')
        
    num1=0
    num2=1
    fib=[num1,num2]

    while True:
        num3=num1+num2
        fib.append(num3)
        num1=num2        
        num2=num3
        clock=(time.asctime())

        print('\n',' '*25,text_words[0],text_words[1],text_words[2])
        
        print(f'\nFibonacci Natural Number Sequence: {text_colours[2]}\
{num1} {text_colours[5]}+ {text_colours[2]}{num2}{text_colours[5]} = \
({text_colours[0]}{num1+num3}{text_colours[5]}){text_colours[5]}\n\n\
Fibonacci Natural Numbers: "{text_colours[0]}{num1+num3:,}\
{text_colours[5]} "\n\n{text_colours[0]}Date & Time:\n\n{clock}')
        
        winsound.PlaySound(sounds[1],winsound.SND_ALIAS)
        os.system('cls')
        
Fib_Num()
