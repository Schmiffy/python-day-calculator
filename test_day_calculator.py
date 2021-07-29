from day_calculator import *
import unittest

class day_calculator(unittest.TestCase):
    def test_date_diff(self):
        self.assertEqual(calculate_diff('2/6/1983', '22/6/1983'),"19")
        self.assertEqual(calculate_diff('4/7/1984', '25/12/1984'),"173")
        #self.assertEqual(calculate_diff('3/1/1989', '3/8/1983'),"2036")