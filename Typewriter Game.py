import os,time,winsound
from typ_var import*
# type_intro

def type_intro():
    os.system(os_features[1])
    length=0
    while length<=len(text_words[0]):
        winsound.PlaySound(sounds,winsound.SND_ASYNC)
        print(text_words[0][:length])
        time.sleep(.05)
        os.system(os_features[0])
        length+=1

# forward type

    while True:
        os.system(os_features[0])
        letters=input(text_words[0]+text_words[1]).strip()
        if letters==button[0]:
            forward_type()
            break
        elif letters==button[1]:
            reverse_type()
            break
        elif letters==button[2]:
            backward_type()
            break
        elif letters==button[3]:
            breakout()
            break

        length=0
        while length<=len(letters):
            winsound.PlaySound(sounds,winsound.SND_ASYNC)
            time.sleep(.05)
            os.system(os_features[0])
            print(text_words[0]+text_words[1]+letters[:length])
            length+=1
            
        letters=input(text_words[2]).strip()
        if letters==button[0]:
            forward_type()
            break
        elif letters==button[1]:
            reverse_type()
            break
        elif letters==button[2]:
            backward_type()
            break
        elif letters==button[3]:
            breakout()
            break
        
def forward_type():
    while True:
        os.system(os_features[0])
        letters=input(text_words[0]+text_words[1]).strip()
        if letters==button[0]:
            forward_type()
            break
        elif letters==button[1]:
            reverse_type()
            break
        elif letters==button[2]:
            backward_type()
            break
        elif letters==button[3]:
            breakout()
            break

        length=0
        while length<=len(letters):
            winsound.PlaySound(sounds,winsound.SND_ASYNC)
            time.sleep(.05)
            os.system(os_features[0])
            print(text_words[0]+text_words[1]+letters[:length])
            length+=1
            
        letters=input(text_words[2]).strip()
        if letters==button[0]:
            forward_type()
            break
        elif letters==button[1]:
            reverse_type()
            break
        elif letters==button[2]:
            backward_type()
            break
        elif letters==button[3]:
            breakout()
            break            

def reverse_type():
    while True:
        os.system(os_features[0])
        letters=input(text_words[0]+text_words[1]).strip()
        if letters==button[0]:
            forward_type()
            break
        elif letters==button[1]:
            reverse_type()
            break
        elif letters==button[2]:
            backward_type()
            break
        elif letters==button[3]:
            breakout()
            break

        length=0
        while length<=len(letters):
            winsound.PlaySound(sounds,winsound.SND_ASYNC)
            time.sleep(.05)
            os.system(os_features[0])
            print(text_words[0]+text_words[1]+letters[length:])
            length+=1
            
        letters=input(text_words[2]).strip()
        if letters==button[0]:
            forward_type()
            break
        elif letters==button[1]:
            reverse_type()
            break
        elif letters==button[2]:
            backward_type()
            break
        elif letters==button[3]:
            breakout()
            break

def backward_type():
    while True:
        os.system(os_features[0])
        letters=input(text_words[0]+text_words[1]).strip()
        if letters==button[0]:
            forward_type()
            break
        elif letters==button[1]:
            reverse_type()
            break
        elif letters==button[2]:
            backward_type()
            break
        elif letters==button[3]:
            breakout()
            break

        length=0
        while length<=len(letters):
            winsound.PlaySound(sounds,winsound.SND_ASYNC)
            time.sleep(.05)
            os.system(os_features[0])
            print(text_words[0]+text_words[1]+letters[length::-1])
            length+=1
            
        letters=input(text_words[2]).strip()
        if letters==button[0]:
            forward_type()
            break
        elif letters==button[1]:
            reverse_type()
            break
        elif letters==button[2]:
            backward_type()
            break
        elif letters==button[3]:
            breakout()
            break
        
def breakout():
    os.system(os_features[1])
    length=0
    while length<=len(text_words[3]):
        winsound.PlaySound(sounds,winsound.SND_ASYNC)
        print(text_words[3][:length])
        time.sleep(.05)
        os.system(os_features[0])
        length+=1
   
    print(text_words[3][:length])
    time.sleep(3)

def type_game():
    type_intro()
    
type_game()
