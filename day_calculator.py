import sys, os, re
from datetime import *


def main():
    menu()


def calculate_diff(in_date, out_date):
    in_date = date.strftime(in_date, '%d/%m/%Y')
    out_date = date.strftime(out_date, '%d/%m/%Y')
    start_input = list(map(int, in_date.split('/') ))
    end_input = list(map(int, out_date.split('/') ))
    start = date(start_input[2], start_input[1], start_input[0])
    end = date(end_input[2], end_input[1], end_input[0])
    diff = end - start

    #substract one day to give the days in between.
    return diff.days - 1

def menu():
    os.system('clear')
    
    print("Hello")
    print("What would you like to do? Choose number:\n")
    print("1. Calculate date delta")
    print("2. Help me")
    print("0. Quit") 
    choice =  return_input()
    exec_menu(choice)

    return

# menu chooser
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return


def calc_delta():

    # the actual function, grab all the values and return the days
    # trying to catch wrong formats 
    
    print("Enter start date! e.g. 2/6/1983 or 0 to Quit \n")
    try:
        start_date = validate_date(return_input())
    except Exception as e: 
        print('try again:')
        calc_delta()

    print("Enter end date! e.g. 22/6/1983 or 0 to Quit \n")

    try:
        end_date = validate_date(return_input())
    except Exception as e: 
        print('try again:')
        calc_delta()
    
    print('There are ' + str(calculate_diff(start_date, end_date)) + ' days between ' + date.strftime(start_date, '%d/%m/%Y') + ' and ' + date.strftime(end_date,   '%d/%m/%Y') + '\n' )

    calc_delta()
    
    return

def print_help():
    
    print('''
                        _.-;:q=._ 
                      .' j=""^k;:\. 
                     ; .F       ";`Y
                    ,;.J_        ;'j
                  ,-;"^7F       : .F           _________________
                 ,-'-_<.        ;gj. _.,---""''               .'
                ;  _,._`\.     : `T"5,                       ; 
                : `?8w7 `J  ,-'" -^q. `                     ;  
                 \;._ _,=' ;   n58L Y.                     .' 
                   F;";  .' k_ `^'  j'                     ;  
                   J;:: ;     "y:-='                      ;   
                    L;;==      |:;   jT\                  ;
                    L;:;J      J:L  7:;'       _         ; 
                    I;|:.L     |:k J:.' ,  '       .     ;
                    |;J:.|     ;.I F.:      .           : 
                   ;J;:L::     |.| |.J  , '   `    ;    ; 
                 .' J:`J.`.    :.J |. L .    ;         ; 
                ;    L :k:`._ ,',j J; |  ` ,        ; ; 
              .'     I :`=.:."_".'  L J             `.'
            .'       |.:  `"-=-'    |.J              ; 
        _.-'         `: :           ;:;           _ ; 
    _.-'"             J: :         /.;'       ;    ; 
  ='_                  k;.\.    _.;:Y'     ,     .' 
     `"---..__          `Y;."-=';:='     ,      .'
              `""--..__   `"==="'    -        .' 
                       ``""---...__        .-' 
                                   ``""---'
It seems your seeking for help:

This program is to help calculate the days between two dates.
To reach the calucation section press 1 in the main menu.

The date has to be provided in the following format: 
e.g. 01/01/1900, 1/1/2001

If you want to leave this program press 0 anytime during usage of this program.

Press enter to get back to the main menu.

    ''')
    return_input()
    menu()

def exit():
    
    print("Bye!\n")
    sys.exit()

    return

menu_actions = {
    #'main_menu': main_menu,
    '1': calc_delta,
    '2': print_help,
    '0': exit
}

def validate_date(input):
    
    
    try:
        
        return datetime.strptime(input, '%d/%m/%Y')
    except Exception as e:
        print ("Error", e) 
        raise


def return_input():
    ui_input = input(" >>  ")
    
    if ui_input == '0':
        exec_menu('0')
    
    return ui_input

if __name__ == "__main__":
    main()
