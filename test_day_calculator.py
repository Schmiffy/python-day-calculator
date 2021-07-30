from day_calculator import *
import unittest

class day_calculator(unittest.TestCase):
    def test_date_diff(self):
        self.assertEqual(calculate_diff('01/01/2001', '03/01/2001'),"1")
        self.assertEqual(calculate_diff('2/6/1983', '22/6/1983'),"19")
        self.assertEqual(calculate_diff('4/7/1984', '25/12/1984'),"173")
        #self.assertEqual(calculate_diff('3/1/1989', '3/8/1983'),"2036") # should be 1980, should we support backwards counting? If so we also need to remove the -1

class date_validation(unittest.TestCase):
    def test_validate_date(self):
        self.assertTrue(validate_date('01/01/2001'))



if __name__ == '__main__':
    unittest.main()