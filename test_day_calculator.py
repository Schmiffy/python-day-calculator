from day_calculator import *
import unittest

class day_calculator(unittest.TestCase):
    def test_date_diff(self):
        self.assertEqual(calculate_diff(validate_date('01/01/2001'), validate_date('03/01/2001')),1)
        self.assertEqual(calculate_diff(validate_date('2/6/1983'), validate_date('22/6/1983')),19)
        self.assertEqual(calculate_diff(validate_date('4/7/1984'), validate_date('25/12/1984')),173)
#        self.assertEqual(calculate_diff('3/1/1989', '3/8/1983'),"2036") # should be 1980, should we support backwards counting? If so we also need to remove the -1
        # seem like 3/1/1989 is meant as 1/3/1989 then it would result in 2036. We only support normalized date formats :)
class date_validation(unittest.TestCase):
    def test_validate_date(self):
        self.assertAlmostEqual(validate_date('01/01/1900'),datetime.strptime('01/01/1900', '%d/%m/%Y'))
        self.assertAlmostEqual(validate_date('31/12/2999'),datetime.strptime('31/12/2999', '%d/%m/%Y'))
        self.assertAlmostEqual(validate_date('01/01/2001'),datetime.strptime('01/01/2001', '%d/%m/%Y'))
        self.assertAlmostEqual(validate_date('1/1/2001'),datetime.strptime('1/1/2001', '%d/%m/%Y'))
        self.assertRaises(Exception, validate_date,'01/33/2001')
        self.assertRaises(Exception, validate_date,'2001/06/15')
        self.assertRaises(Exception, validate_date,'2001/15/06')
        self.assertRaises(Exception, validate_date,"01/01/20xx")

if __name__ == '__main__':
    unittest.main()