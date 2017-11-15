import unittest
import csv
import os
from palindrome import Palindrome


class PalindromeTestCase(unittest.TestCase):
    csv_file = 'testing.csv'

    def setUp(self):
        self.Palindrome = Palindrome(self.csv_file)

    def tearDown(self):
        if os.path.isfile(self.csv_file):
            os.remove(self.csv_file)

    def test_smallest_base_values_special(self):
        # Test that the special case of integers 1 and 2 return the correct result
        self.assertEqual(2, self.Palindrome.get_smallest_palindrome_base(1))
        self.assertEqual(3, self.Palindrome.get_smallest_palindrome_base(2))

    def test_smallest_base_values_small_numbers(self):
        # Test that the smaller values return the correct result
        self.assertEqual(2, self.Palindrome.get_smallest_palindrome_base(3))
        self.assertEqual(3, self.Palindrome.get_smallest_palindrome_base(4))
        self.assertEqual(2, self.Palindrome.get_smallest_palindrome_base(5))
        self.assertEqual(5, self.Palindrome.get_smallest_palindrome_base(6))
        self.assertEqual(2, self.Palindrome.get_smallest_palindrome_base(7))
        self.assertEqual(3, self.Palindrome.get_smallest_palindrome_base(8))
        self.assertEqual(2, self.Palindrome.get_smallest_palindrome_base(9))
        self.assertEqual(3, self.Palindrome.get_smallest_palindrome_base(10))

    def test_smallest_base_values_large_numbers(self):
        # Test that some of the larger values return the correct result
        self.assertEqual(2, self.Palindrome.get_smallest_palindrome_base(15))
        self.assertEqual(5, self.Palindrome.get_smallest_palindrome_base(18))
        self.assertEqual(18, self.Palindrome.get_smallest_palindrome_base(19))
        self.assertEqual(3, self.Palindrome.get_smallest_palindrome_base(20))

    def test_base_values(self):
        # Test that the given integer is represented in the base values appropriately from base 2 to base N - 1
        def base_array_equality_check(number, ans_array):
            for i, value in enumerate(self.Palindrome.get_base_values(number)):
                self.assertEqual(ans_array[i], value)

        ans_array = [[1, 1]]
        base_array_equality_check(3, ans_array)
        ans_array = [[1, 0, 0], [1, 1]]
        base_array_equality_check(4, ans_array)
        ans_array = [[1, 0, 1], [1, 2], [1, 1]]
        base_array_equality_check(5, ans_array)
        ans_array = [[1, 1, 0], [2, 0], [1, 2], [1, 1]]
        base_array_equality_check(6, ans_array)
        ans_array = [[1, 1, 1], [2, 1], [1, 3], [1, 2], [1, 1]]
        base_array_equality_check(7, ans_array)
        ans_array = [[1, 0, 0, 0], [2, 2], [2, 0], [1, 3], [1, 2], [1, 1]]
        base_array_equality_check(8, ans_array)
        ans_array = [[1, 0, 0, 1], [1, 0, 0], [2, 1], [1, 4], [1, 3], [1, 2], [1, 1]]
        base_array_equality_check(9, ans_array)
        ans_array = [[1, 0, 1, 0], [1, 0, 1], [2, 2], [2, 0], [1, 4], [1, 3], [1, 2], [1, 1]]
        base_array_equality_check(10, ans_array)

    def test_is_palindrome(self):
        # Test that the is_palindrome function works appropriately
        self.assertTrue(self.Palindrome.is_palindrome([1, 1]))
        self.assertTrue(self.Palindrome.is_palindrome([1, 2, 1]))
        self.assertTrue(self.Palindrome.is_palindrome([2, 2]))
        self.assertFalse(self.Palindrome.is_palindrome([1, 0]))
        self.assertFalse(self.Palindrome.is_palindrome([1, 2]))

    def test_print_file(self):
        # Test that the print_palindrome_bases actually creates a file
        self.Palindrome.print_palindrome_bases(1, 20)
        self.assertTrue(os.path.isfile(self.csv_file))

    def test_print_out(self):
        # Test that the print_palindrome_bases function outputs a file with values and that the values are correct
        self.Palindrome.print_palindrome_bases(1, 20)
        ans_array = [
            ["decimal", "smallest base in which the number is a palindrome"],
            [1, 2],     [2, 3],     [3, 2],     [4, 3],     [5, 2],
            [6, 5],     [7, 2],     [8, 3],     [9, 2],     [10, 3],
            [11, 10],   [12, 5],    [13, 3],    [14, 6],    [15, 2],
            [16, 3],    [17, 2],    [18, 5],    [19, 18],   [20, 3]]

        with open(self.csv_file, 'r') as csvfile:
            csv_dict = [row for row in csv.DictReader(csvfile)]
            self.assertNotEqual(0, len(csv_dict))

            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                self.assertEquals(ans_array[i], row)


if __name__ == '__main__':
    unittest.main()
