import sys
from datetime import date


def main():
    # grab the first 2 input parameters and split them
    # e.g. python3 python-day-calculator.py 2/6/1983 22/6/1983
    
    in_date = sys.argv[1]
    out_date = sys.argv[2]
    print(' There are ' + str(calculate_diff(in_date, out_date)) + ' day between ' + str(in_date) + ' and ' + str(out_date) )


def calculate_diff(in_date, out_date):

    start_input = in_date.split('/')
    end_input = out_date.split('/')
    start = date(int(start_input[2]), int(start_input[1]), int(start_input[0]))
    end = date(int(end_input[2]), int(end_input[1]), int(end_input[0]))
    return end - start




if __name__ == "__main__":
    main()
