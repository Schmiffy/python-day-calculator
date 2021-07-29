from datetime import date


start = date(2001, 1, 1)

end = date(2001, 1, 3)

difference = end - start

print(' There are ' + str(difference.days) + ' day between ' + str(start) + ' and ' + str(end) )
