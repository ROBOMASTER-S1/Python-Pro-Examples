import os,time,math
from asc_var import*

def ascii_codes():
    os.system(text_words[4])
    def subroutine1():
        while True:
            os.system(text_features[0])
            print(text_words[0])
            
            try:
                ascii_code=int(input(word_info[0]).strip())
                ascii_code=input(f'\n{text_features[2]}{chr(ascii_code)}\
{text_features[5]} = ASCII code: " {text_features[2]}{ascii_code}\
{text_features[5]} " {word_info[3]}').lower().lower().strip()
                if ascii_code==button[2]:
                    break
                
            except ValueError:
                print(word_info[4])
                time.sleep(2)

    def subroutine2():
        while True:
            os.system(text_features[0])
            print(text_words[1])
            
            try:
                ascii_code=input(word_info[1]).strip()
                ascii_code=input(f'\n{text_features[2]}{ascii_code}\
{text_features[5]} = ASCII code: " {text_features[2]}{ord(ascii_code)}\
{text_features[5]} " {word_info[3]}').lower().strip()
                if ascii_code==button[2]:
                    break
                
            except TypeError:
                print(word_info[5])                
                time.sleep(2)

    while True:
        os.system(text_features[0])
        print(text_words[2])
        
        butt=input(word_info[2]).lower().strip()
        if butt==button[0]:
            subroutine1()
        elif butt==button[1]:
           subroutine2()
           
        else:
            if butt==button[2]:
                os.system(text_features[0])
                print(text_words[3])
                time.sleep(3)
                break
            
ascii_codes()
