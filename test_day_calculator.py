from day_calculator import *
import unittest

class day_calculator(unittest.TestCase):
    def test_date_diff(self):
        self.assertAlmostEqual(calculate_diff("2/6/1983", "22/6/1983"),20)