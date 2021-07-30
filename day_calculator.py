import sys, os, re
from datetime import date


def main():
    # grab the first 2 input parameters and split them
    # e.g. python3 python-day-calculator.py 2/6/1983 22/6/1983
    menu()


def calculate_diff(in_date, out_date):

    start_input = list(map(int, in_date.split('/')))
    end_input = list(map(int, out_date.split('/')))
    start = date(start_input[2], start_input[1], start_input[0])
    end = date(end_input[2], end_input[1], end_input[0])
    diff = end - start

    #substract one day to give the days in between.
    return str(diff.days - 1 )

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

    print("Enter start date! e.g. 2/6/1983 or 0 to Quit \n")
    start_date = validate_date(return_input())

    print("Enter end date! e.g. 22/6/1983 or 0 to Quit \n")
    end_date = validate_date(return_input())
    
    print('There are ' + str(calculate_diff(start_date, end_date)) + ' day between ' + str(start_date) + ' and ' + str(end_date) + '\n' )

    calc_delta()
    
    return

def print_help():
    
    print("Call someone for help")   
    return

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
    
    if re.match(r"[0-9]{1,2}\/[0-1]{0,1}[0-9]{0,1}\/[1-2]{1}[0-9]{3}", input):
        return input
    else :
        print("Date entered in wrong format! e.g. 22/6/1983")
        return



def return_input():
    ui_input = input(" >>  ")
    
    if ui_input == '0':
        exec_menu('0')
    
    return ui_input

if __name__ == "__main__":
    main()
