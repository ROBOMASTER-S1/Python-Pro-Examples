import os,time,math;from math import*
from maj_var import*

def stan_cal():
    while True:
        try:
            os.system(text_features[0])
            num1=float(input(f'{text_words[1]}{text_words[12]}').lower().strip())

            os.system(text_features[0])
            oper=input(f'{text_words[1]}\n\n{text_features[2]}{num1}\
{text_words[13]}').lower().strip()

            if oper==operator[0]:
                os.system(text_features[0])
                num2=float(input(f'{text_words[1]}\n\n{text_features[2]}\
{num1} {operator[0]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f'{text_words[1]}\n\n{text_features[2]}{num1} \
{operator[0]} {num2} = {text_features[5]}" {float(num1+num2)} \
"\n{text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break
            elif oper==operator[1]:

                os.system(text_features[0])
                num2=float(input(f'{text_words[1]}\n\n{text_features[2]}\
{num1} {operator[1]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f'{text_words[1]}\n\n{text_features[2]}{num1} \
{operator[1]} {num2} = {text_features[5]}" {float(num1-num2)} \
"\n{text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break
            elif oper==operator[2]:

                os.system(text_features[0])
                num2=float(input(f'{text_words[1]}\n\n{text_features[2]}\
{num1} {operator[2]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f'{text_words[1]}\n\n{text_features[2]}{num1} \
{operator[2]} {num2} = {text_features[5]}" {float(num1*num2)} \
"\n{text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break
            elif oper==operator[3]:

                os.system(text_features[0])
                num2=float(input(f'{text_words[1]}\n\n{text_features[2]}\
{num1} {operator[3]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f'{text_words[1]}\n\n{text_features[2]}{num1} \
{operator[3]} {num2} = {text_features[5]}" {float(num1/num2)} \
"\n{text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

        except ZeroDivisionError:
            os.system(text_features[0])
            print(f'{text_words[1]}{text_words[16]}')
            time.sleep(2)

        except ValueError:
            os.system(text_features[0])
            print(f'{text_words[1]}{text_words[17]}')
            time.sleep(2)

def bin_cal():
    while True:
        try:
            os.system(text_features[0])
            num1=int(input(f'{text_words[2]}{text_words[12]}').lower().strip())

            os.system(text_features[0])
            oper=input(f'{text_words[2]}\n\n{text_features[2]}{bin(num1)}\
{text_words[13]}').lower().strip()

            if oper==operator[0]:
                os.system(text_features[0])
                num2=int(input(f'{text_words[2]}\n\n{text_features[2]}\
{bin(num1)} {operator[0]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f'{text_words[2]}\n\n{text_features[2]}{bin(num1)} \
{operator[0]} {bin(num2)} = {text_features[5]}" {bin(num1+num2)} " \
{text_features[2]}= {text_features[5]}" {int(num1+num2)} " \
\n{text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

            elif oper==operator[1]:
                os.system(text_features[0])
                num2=int(input(f'{text_words[2]}\n\n{text_features[2]}\
{bin(num1)} {operator[1]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f'{text_words[2]}\n\n{text_features[2]}{bin(num1)} \
{operator[1]} {bin(num2)} = {text_features[5]}" {bin(num1-num2)} " \
{text_features[2]}= {text_features[5]}" {int(num1-num2)} \
" \n{text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

            elif oper==operator[2]:
                os.system(text_features[0])
                num2=int(input(f'{text_words[2]}\n\n{text_features[2]}\
{bin(num1)} {operator[2]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f'{text_words[2]}\n\n{text_features[2]}{bin(num1)} \
{operator[2]} {bin(num2)} = {text_features[5]}" {bin(num1*num2)} " \
{text_features[2]}= {text_features[5]}" {int(num1*num2)} \
" \n{text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

            elif oper==operator[3]:
                os.system(text_features[0])
                num2=int(input(f'{text_words[2]}\n\n{text_features[2]}\
{bin(num1)} {operator[3]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f'{text_words[2]}\n\n{text_features[2]}\
{bin(num1)} {operator[3]} {bin(num2)} = {text_features[5]}" \
{bin(int(num1/num2))} " {text_features[2]}= {text_features[5]}" \
{int(num1/num2)} " \n{text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

        except ZeroDivisionError:
            os.system(text_features[0])
            print(f'{text_words[2]}{text_words[16]}')
            time.sleep(2)

        except ValueError:
            os.system(text_features[0])
            print(f'{text_words[1]}{text_words[17]}')
            time.sleep(2)

def oct_cal():
    while True:
        try:
            os.system(text_features[0])
            num1=int(input(f'{text_words[3]}{text_words[12]}').lower().strip())

            os.system(text_features[0])
            oper=input(f'{text_words[3]}\n\n{text_features[2]}\
{oct(num1)} {text_words[13]}').lower().strip()

            if oper==operator[0]:
                os.system(text_features[0])
                num2=int(input(f'{text_words[3]}\n\n{text_features[2]}\
{oct(num1)} {operator[0]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f'{text_words[3]}\n\n{text_features[2]}\
{oct(num1)} {operator[0]} {oct(num2)} = {text_features[5]}" \
{oct(num1+num2)} " {text_features[2]}= {text_features[5]}" \
{int(num1+num2)} " \n {text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

            elif oper==operator[1]:
                os.system(text_features[0])
                num2=int(input(f'{text_words[3]}\n\n{text_features[2]}\
{oct(num1)} {operator[1]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f'{text_words[3]}\n\n{text_features[2]}\
{oct(num1)} {operator[1]} {oct(num2)} = {text_features[5]}" \
{oct(num1-num2)} " {text_features[2]}= {text_features[5]}" \
{int(num1-num2)} " \n {text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

            elif oper==operator[2]:
                os.system(text_features[0])
                num2=int(input(f'{text_words[3]}\n\n{text_features[2]}\
{oct(num1)} {operator[2]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f'{text_words[3]}\n\n{text_features[2]}\
{oct(num1)} {operator[2]} {oct(num2)} = {text_features[5]}" \
{oct(num1*num2)} " {text_features[2]}= {text_features[5]}" \
{int(num1*num2)} " \n{text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

            elif oper==operator[3]:
                os.system(text_features[0])
                num2=int(input(f'{text_words[3]}\n\n{text_features[2]}\
{oct(num1)} {operator[3]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f'{text_words[3]}\n\n{text_features[2]}\
{oct(num1)} {operator[3]} {oct(num2)} = {text_features[5]}" \
{oct(int(num1/num2))} " {text_features[2]}= {text_features[5]}" \
{int(num1/num2)} " \n{text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

        except ZeroDivisionError:
            os.system(text_features[0])
            print(f'{text_words[3]}{text_words[16]}')
            time.sleep(2)

        except ValueError:
            os.system(text_features[0])
            print(f'{text_words[3]}{text_words[17]}')
            time.sleep(2)

def hex_cal():
    while True:
        try:
            os.system(text_features[0])
            num1=int(input(f'{text_words[4]}{text_words[12]}').lower().strip())

            os.system(text_features[0])
            oper=input(f'{text_words[4]}\n\n{text_features[2]}\
{hex(num1)} {text_words[13]}').lower().strip()

            if oper==operator[0]:
                os.system(text_features[0])
                num2=int(input(f'{text_words[4]}\n\n{text_features[2]}\
{hex(num1)} {operator[0]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f'{text_words[4]}\n\n{text_features[2]}\
{hex(num1)} {operator[0]} {hex(num2)} = {text_features[5]}" \
{hex(num1+num2)} " {text_features[2]}= {text_features[5]}" \
{int(num1+num2)} " \n{text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

            elif oper==operator[1]:
                os.system(text_features[0])
                num2=int(input(f'{text_words[4]}\n\n{text_features[2]}\
{hex(num1)} {operator[1]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f'{text_words[4]}\n\n{text_features[2]}\
{hex(num1)} {operator[1]} {hex(num2)} = {text_features[5]}" \
{hex(num1-num2)} " {text_features[2]}= {text_features[5]}" \
{int(num1-num2)} " \n{text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

            elif oper==operator[2]:
                os.system(text_features[0])
                num2=int(input(f'{text_words[4]}\n\n{text_features[2]}\
{hex(num1)} {operator[2]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f'{text_words[4]}\n\n{text_features[2]}\
{hex(num1)} {operator[2]} {hex(num2)} = {text_features[5]}" \
{hex(num1*num2)} " {text_features[2]}= {text_features[5]}" \
{int(num1*num2)} " \n{text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break
                
            elif oper==operator[3]:
                os.system(text_features[0])
                num2=int(input(f'{text_words[4]}\n\n{text_features[2]}\
{hex(num1)} {operator[3]}{text_words[14]}').lower().strip())

                os.system(text_features[0])
                but=input(f'{text_words[4]}\n\n{text_features[2]}\
{hex(num1)} {operator[3]} {hex(num2)} = {text_features[5]}" \
{hex(int(num1/num2))} " {text_features[2]}= {text_features[5]}" \
{int(num1/num2)} " \n{text_words[18]}').lower().strip()

                if but==('\r'):
                    continue
                elif but==button[7]:
                    break

        except ZeroDivisionError:
            os.system(text_features[0])
            print(f'{text_words[4]}{text_words[16]}')
            time.sleep(2)

        except ValueError:
            os.system(text_features[0])
            print(f'{text_words[4]}{text_words[17]}')
            time.sleep(2)

def bin_trans():
    while True:
        try:
            os.system(text_features[0])
            num_trans=int(input(f'{text_words[8]}{text_words[11]}').lower().strip())

            os.system(text_features[0])
            but=input(f'{text_words[8]}\n\n{text_features[2]}\
{num_trans} = {text_features[5]} " {bin(num_trans)} \
"\n{text_words[18]}').lower().strip()

            if but==('\r'):
                continue
            elif but==button[7]:
                break

        except ValueError:
            os.system(text_features[0])
            print(f'{text_words[8]}{text_words[17]}')
            time.sleep(2)

def oct_trans():
    while True:
        try:
            os.system(text_features[0])
            num_trans=int(input(f'{text_words[9]}{text_words[11]}').lower().strip())

            os.system(text_features[0])
            but=input(f'{text_words[9]}\n\n{text_features[2]}\
{num_trans} = {text_features[5]} " {oct(num_trans)} \
"\n{text_words[18]}').lower().strip()

            if but==('\r'):
                continue
            elif but==button[7]:
                break

        except ValueError:
            os.system(text_features[0])
            print(f'{text_words[9]}{text_words[17]}')
            time.sleep(2)

def hex_trans():
    while True:
        try:
            os.system(text_features[0])
            num_trans=int(input(f'{text_words[10]}{text_words[11]}').lower().strip())

            os.system(text_features[0])
            but=input(f'{text_words[10]}\n\n{text_features[2]}\
{num_trans} = {text_features[5]} " {hex(num_trans)} \
"\n{text_words[18]}').lower().strip()

            if but==('\r'):
                continue
            elif but==button[7]:
                break

        except ValueError:
            os.system(text_features[0])
            print(f'{text_words[10]}{text_words[17]}')
            time.sleep(2)

def maj_cal():
    os.system(text_features[6])
    while True:
        os.system(text_features[0])
        choice=input(text_words[0]).lower().strip()

        if choice==button[0]:
            stan_cal()
            pass
        elif choice==button[1]:
            bin_cal()
            pass
        elif choice==button[2]:
            oct_cal()
            pass
        elif choice==button[3]:
            hex_cal()
            pass
        elif choice==button[4]:
            bin_trans()
            pass
        elif choice==button[5]:
            oct_trans()
            pass
        elif choice==button[6]:
            hex_trans()
            pass
        elif choice==button[7]:
            os.system(text_features[0])
            print(text_words[19])
            time.sleep(3)
            break

maj_cal()
