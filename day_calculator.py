import sys, os
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
    choice = input(" >>  ")
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
    
    print("Enter start date! e.g. 2/6/1983 \n")
    start_date = input(" >>  ")

    if start_date == '0':
        exec_menu('0')

    
    print("Enter end date! e.g. 22/6/1983 \n")
    end_date = input(" >>  ")
    
    print(' There are ' + str(calculate_diff(start_date, end_date)) + ' day between ' + str(start_date) + ' and ' + str(end_date) + '\n' )
    print("enter new start date or 0 to Quit")
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


if __name__ == "__main__":
    main()
