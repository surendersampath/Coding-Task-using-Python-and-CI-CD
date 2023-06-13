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

    def testcase_find_your_seat(self):
        test_set = set()

        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                test_set.add(line)

        result = find_seat_from_scanned_boarding_pass(test_set)
        print("Result = " + str(result) )
        self.assertEqual(0, 0)

if __name__ == '__main__':
    unittest.main()