from datetime import datetime
import unittest
import calculate_charge as calc

def get_time(hour):
    '''Convenience function to make tests cleaner.'''
    return datetime(year=1900, month=1, day=1, hour=hour).time()

class TestConvertStringToTime(unittest.TestCase):
    def test_when_convert_string_to_time_is_passed_valid_am_string_it_returns_correct_time(self):
        time = calc.convert_string_to_time('4:00AM')
        self.assertEqual(time, get_time(hour=4))

    def test_when_convert_string_to_time_is_passed_valid_pm_string_it_returns_correct_time(self):
        time = calc.convert_string_to_time('5:00PM')
        self.assertEqual(time, get_time(17))

    def test_when_convert_string_to_time_is_passed_invalid_string_it_returns_none(self):
        time = calc.convert_string_to_time('5 : 01 PM')
        self.assertIsNone(time)

class TestIsTimeInLegalRange(unittest.TestCase):
    def test_when_is_time_in_legal_range_is_passed_illegal_time_it_returns_false(self):
        self.assertFalse(calc.is_time_in_legal_range(get_time(5)))

    def test_when_is_time_in_legal_range_is_passed_legal_time_it_returns_true(self):
        self.assertTrue(calc.is_time_in_legal_range(get_time(17)))

class TestIsStartTimeBeforeEndTime(unittest.TestCase):
    def test_when_is_start_time_before_end_time_passed_end_before_start_it_returns_false(self):
        self.assertFalse(calc.is_start_time_before_end_time(get_time(18), get_time(17)))

    def test_when_is_start_time_before_end_time_passed_start_before_end_it_returns_true(self):
        self.assertTrue(calc.is_start_time_before_end_time(get_time(17), get_time(18)))

    def test_when_is_start_time_before_end_time_passed_start_pm_end_am_it_returns_true(self):
        self.assertTrue(calc.is_start_time_before_end_time(get_time(17), get_time(3)))

    def test_when_is_start_time_before_end_time_passed_start_am_end_pm_it_returns_false(self):
        self.assertFalse(calc.is_start_time_before_end_time(get_time(3), get_time(18)))

class TestCalcHours(unittest.TestCase):
    def test_when_calc_hours_passed_time_at_start_it_returns_0(self):
        self.assertEqual(calc.calc_hours(get_time(17), get_time(3), get_time(17)), 0)

    def test_when_calc_hours_passed_pm_start_pm_end_pm_cutoff_it_returns_hours(self):
        self.assertEqual(calc.calc_hours(get_time(17), get_time(23), get_time(22)), 5)

    def test_when_calc_hours_passed_pm_start_am_end_am_cutoff_it_returns_hours(self):
        self.assertEqual(calc.calc_hours(get_time(17), get_time(3), get_time(2)), 9)

    def test_when_calc_hours_passed_pm_end_pm_start_am_cutoff_it_returns_hours(self):
        self.assertEqual(calc.calc_hours(get_time(17), get_time(21), get_time(2)), 4)

    def test_when_calc_hours_passed_am_end_am_start_am_cutoff_it_returns_hours(self):
        self.assertEqual(calc.calc_hours(get_time(1), get_time(4), get_time(3)), 2)

    def test_when_calc_hours_passed_pm_start_am_end_pm_cutoff_it_returns_hours(self):
        self.assertEqual(calc.calc_hours(get_time(17), get_time(3), get_time(19)), 2)

    def test_when_calc_hours_passed_am_start_am_end_pm_cutoff_it_returns_hours(self):
        self.assertEqual(calc.calc_hours(get_time(2), get_time(4), get_time(19)), 0)

    def test_when_calc_hours_passed_am_start_pm_end_pm_cutoff_it_returns_hours(self):
        self.assertIsNone(calc.calc_hours(get_time(2), get_time(18), get_time(19)))

    def test_when_calc_hours_passed_am_start_pm_end_am_cutoff_it_returns_hours(self):
        self.assertIsNone(calc.calc_hours(get_time(2), get_time(18), get_time(1)))

class TestGetFamilyRates(unittest.TestCase):
    def test_when_get_family_rates_passed_invalid_it_returns_none(self):
        self.assertIsNone(calc.get_family_rates('D'))

    def test_when_get_family_rates_passed_a_it_returns_not_none(self):
        self.assertIsNotNone(calc.get_family_rates('A'))

    def test_when_get_family_rates_passed_b_it_returns_not_none(self):
        self.assertIsNotNone(calc.get_family_rates('b'))

    def test_when_get_family_rates_passed_c_it_returns_not_none(self):
        self.assertIsNotNone(calc.get_family_rates('C'))

class TestCalcPay(unittest.TestCase):
    def test_when_calc_pay_passed_invalid_time_it_returns_none(self):
        self.assertIsNone(calc.calc_pay('5:00', '5:00PM', 'A'))

    def test_when_calc_pay_passed_end_before_start_it_returns_none(self):
        self.assertIsNone(calc.calc_pay('6:00PM', '5:00PM', 'A'))

    def test_when_calc_pay_passed_invalid_time_range_it_returns_none(self):
        self.assertIsNone(calc.calc_pay('4:00PM', '5:00PM', 'A'))

    def test_when_calc_pay_passed_same_start_end_it_returns_0(self):
        self.assertEqual(calc.calc_pay('5:00PM', '5:00PM', 'A'), 0)

    def test_when_calc_pay_passed_invalid_family_it_returns_none(self):
        self.assertIsNone(calc.calc_pay('4:00PM', '5:00PM', 'D'))

    def test_when_calc_pay_passed_5_to_6_fam_a_it_returns_15(self):
        self.assertEqual(calc.calc_pay('5:00PM', '6:00PM', 'A'), 15)
