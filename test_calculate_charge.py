from datetime import datetime
import unittest
import calculate_charge as calc

class CalculateCharge(unittest.TestCase):
    def test_when_convert_string_to_time_is_passed_valid_string_it_returns_correct_time(self):
        time = calc.convert_string_to_time('5:01PM')
        self.assertEqual(time, datetime(year=1900, month=1, day=1, hour=17, minute=1).time())
