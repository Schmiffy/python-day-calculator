import sys
from datetime import date


# grab the first 2 input parameters and split them
# e.g. python3 python-day-calculator.py 2/6/1983 22/6/1983
start_input = sys.argv[1].split('/')
end_input = sys.argv[2].split('/')


start = date(int(start_input[2]), int(start_input[1]), int(start_input[0]))
end = date(int(end_input[2]), int(end_input[1]), int(end_input[0]))

difference = end - start

print(' There are ' + str(difference.days) + ' day between ' + str(start) + ' and ' + str(end) )
