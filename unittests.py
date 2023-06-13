import unittest

from boardingpassfinder import test_func

class MyModuleTestCase(unittest.TestCase):

    def testcase_seatnumber_1(self):
        result = decode_seat_number_from_boarding_pass("BFFFBBFRRR")
        self.assertEqual(result, 567)

    def testcase_seatnumber_2(self):
        result = decode_seat_number_from_boarding_pass("FFFBBBFRRR")
        self.assertEqual(result, 119)

    def testcase_seatnumber_3(self):
        result = decode_seat_number_from_boarding_pass("BBFFBBFRLL")
        self.assertEqual(result, 820)

    def testcase_seatnumber_4(self):
        result = decode_seat_number_from_boarding_pass("FBFBBFFRLR")
        self.assertEqual(result, 357)

if __name__ == '__main__':
    unittest.main()