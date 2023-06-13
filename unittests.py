import unittest

from boardingpassfinder import test_func

class MyModuleTestCase(unittest.TestCase):


    def testcase_1(self):
        result = test_func(2,4)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()