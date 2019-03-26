from datetime import datetime
import unittest
import calculate_charge as calc

def get_time(hour):
    '''Convenience function to make tests cleaner.'''
    return datetime(year=1900, month=1, day=1, hour=hour).time()

class CalculateCharge(unittest.TestCase):
    def test_when_convert_string_to_time_is_passed_valid_am_string_it_returns_correct_time(self):
        time = calc.convert_string_to_time('4:00AM')
        self.assertEqual(time, get_time(hour=4))

    def test_when_convert_string_to_time_is_passed_valid_pm_string_it_returns_correct_time(self):
        time = calc.convert_string_to_time('5:00PM')
        self.assertEqual(time, get_time(17))

    def test_when_convert_string_to_time_is_passed_invalid_string_it_returns_none(self):
        time = calc.convert_string_to_time('5 : 01 PM')
        self.assertIsNone(time)

    def test_when_is_time_in_legal_range_is_passed_illegal_time_it_returns_false(self):
        self.assertFalse(calc.is_time_in_legal_range(get_time(5)))

    def test_when_is_time_in_legal_range_is_passed_legal_time_it_returns_true(self):
        self.assertTrue(calc.is_time_in_legal_range(get_time(17)))

    def test_when_is_start_time_before_end_time_passed_end_before_start_it_returns_false(self):
        self.assertFalse(calc.is_start_time_before_end_time(get_time(18), get_time(17)))

    def test_when_is_start_time_before_end_time_passed_start_before_end_it_returns_true(self):
        self.assertTrue(calc.is_start_time_before_end_time(get_time(17), get_time(18)))

    def test_when_is_start_time_before_end_time_passed_start_pm_end_am_it_returns_true(self):
        self.assertTrue(calc.is_start_time_before_end_time(get_time(17), get_time(3)))

    def test_when_calculate_sitting_hours_before_time_passed_time_at_start_it_returns_0(self):
        self.assertEqual(calc.calculate_sitting_hours_before_time(
            get_time(17), get_time(3), get_time(17)), 0)

    def test_when_calculate_sitting_hours_before_time_passed_pm_time_it_returns_hours(self):
        self.assertEqual(calc.calculate_sitting_hours_before_time(
            get_time(17), get_time(23), get_time(22)), 5)

    def test_when_calculate_sitting_hours_before_time_passed_start_pm_cutoff_am_time_it_returns_hours(self):
        self.assertEqual(calc.calculate_sitting_hours_before_time(
            get_time(17), get_time(3), get_time(2)), 9)
