#!/usr/bin/env python3
import unittest
from rearange import rearange_name


class TestRearange(unittest.TestCase):
    def test_basic(self):
        testcase = "Sorwar, Alam"
        expected = "Alam Sorwar"
        self.assertEqual(rearange_name(testcase), expected)

    def test_empty(self):
        testcase =" "
        expected = " "
        self.assertEqual(rearange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Hopper, Makger G."
        expected = "Makger G. Hopper"

        self.assertEqual(rearange_name(testcase), expected)

    def test_single_name(self):
        testcase = "Hopper"
        expected = "Hopper"

        self.assertEqual(rearange_name(testcase), expected)



if __name__ == '__main__':
    unittest.main()
