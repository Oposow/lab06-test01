import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    def test_fun(self):

        weekday = calculate(2016, 2, 29)
        self.assertEqual(weekday, 0)
        weekday = calculate(2017, 3, 15)
        self.assertEqual(weekday, 2)
        weekday = calculate(2015, 2, 29)
        self.assertEqual(weekday, None)
        weekday = calculate(2016, 2, 30)
        self.assertEqual(weekday, None)
        weekday = calculate(2016, -2, 30)
        self.assertEqual(weekday, None)

        badArgsList = [
            ["--year", "2001", "--month", "-1", "--day", "3"],
            ["--year", "2001", "--monh", "1", "--day", "3"],
            ["--year", "2001", "--month", "1", "--day", "38"]
        ]

        for arg in badArgsList:
            retcode = main(arg)
            self.assertNotEqual(retcode, 0)


if __name__ == '__main__':
	unittest.main()
