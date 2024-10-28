"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add(6, 8)
        self.assertEqual(res, 14)
        
    def test_subtract_numbers(self):
        res = calc.subtract(10, 5)
        self.assertEqual(res, 5)
        
        