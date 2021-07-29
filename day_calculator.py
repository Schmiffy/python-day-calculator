import sys
from datetime import date


def main():
    # grab the first 2 input parameters and split them
    # e.g. python3 python-day-calculator.py 2/6/1983 22/6/1983

    in_date = sys.argv[1]
    out_date = sys.argv[2]
    print(' There are ' + str(calculate_diff(in_date, out_date)) + ' day between ' + str(in_date) + ' and ' + str(out_date) )


def calculate_diff(in_date, out_date):

    start_input = list(map(int, in_date.split('/')))
    end_input = list(map(int, out_date.split('/')))
    start = date(start_input[2], start_input[1], start_input[0])
    end = date(end_input[2], end_input[1], end_input[0])
    diff = end - start

    #substract one day to give the days in between.
    return str(diff.days - 1 )




if __name__ == "__main__":
    main()
