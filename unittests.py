import unittest

from boardingpassfinder import decode_seat_number_from_boarding_pass, find_seat_from_scanned_boarding_pass

filename = "testdata.txt"

class MyModuleTestCase(unittest.TestCase):
    """
    Test case class for boardingpassfinder.
    """
    # Test Scenarios are derived from the examples.
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
        """
        Test finding the missing seat number from a list of scanned boarding pass data.
        """

        test_set = set()
        # Copying the test Data for Boarding Passes into a Set.
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                test_set.add(line)

        result = find_seat_from_scanned_boarding_pass(test_set)
        self.assertEqual(result, 640)

if __name__ == '__main__':
    unittest.main()