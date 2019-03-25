from datetime import datetime
import unittest
import calculate_charge as calc

class CalculateCharge(unittest.TestCase):
    def test_when_convert_string_to_time_is_passed_valid_am_string_it_returns_correct_time(self):
        time = calc.convert_string_to_time('4:23AM')
        self.assertEqual(time, datetime(year=1900, month=1, day=1, hour=4, minute=23).time())

    def test_when_convert_string_to_time_is_passed_valid_pm_string_it_returns_correct_time(self):
        time = calc.convert_string_to_time('5:01PM')
        self.assertEqual(time, datetime(year=1900, month=1, day=1, hour=17, minute=1).time())

    def test_when_convert_string_to_time_is_passed_invalid_string_it_returns_none(self):
        time = calc.convert_string_to_time('5 : 01 PM')
        self.assertIsNone(time)

    def test_when_is_time_in_legal_range_is_passed_illegal_time_it_returns_false(self):
        self.assertFalse(calc.is_time_in_legal_range(
                             datetime(year=1900, month=1, day=1, hour=5).time()))

    def test_when_is_time_in_legal_range_is_passed_legal_time_it_returns_true(self):
        self.assertTrue(calc.is_time_in_legal_range(
                             datetime(year=1900, month=1, day=1, hour=17).time()))

    def test_when_is_start_time_before_end_time_passed_end_before_start_it_returns_false(self):
        self.assertFalse(calc.is_start_time_before_end_time(
                         datetime(year=1900, month=1, day=1, hour=18).time(),
                         datetime(year=1900, month=1, day=1, hour=17).time()))

    def test_when_is_start_time_before_end_time_passed_start_before_end_it_returns_true(self):
        self.assertTrue(calc.is_start_time_before_end_time(
                         datetime(year=1900, month=1, day=1, hour=17).time(),
                         datetime(year=1900, month=1, day=1, hour=18).time()))

    def test_when_is_start_time_before_end_time_passed_start_pm_end_am_it_returns_true(self):
        self.assertTrue(calc.is_start_time_before_end_time(
                         datetime(year=1900, month=1, day=1, hour=17).time(),
                         datetime(year=1900, month=1, day=1, hour=3).time()))
