"""
    This script outputs a CSV file with a decimal value from [1-1000] and the smallest base in which the number
    is a palindrome with the headers:
        "decimal", "smallest base in which the number is a palindrome"
    For each decimal N>2, it is a palindrome for base N-1. i.e. 20 is a palindrome in base 19 (11).
    For N = 1 or 2, smallest base would be base 2 and 3 respectively
"""
import csv


class Palindrome:
    def __init__(self, file: str):
        self.csv_file = file

    def print_palindrome_bases(self, start: int, end: int):
        """
        Outputs a CSV file where the first column represents the integer values between start and end and
        the second column represents the smallest base in which the integer value is a palindrome
        :param start: Integer to start from
        :param end: Integer to end with
        :return:
        """
        with open(self.csv_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['decimal', 'smallest base in which the number is a palindrome'])
            for i in range(start, end + 1):
                writer.writerow([str(i), str(self.get_smallest_palindrome_base(i))])

    def get_smallest_palindrome_base(self, number: int):
        """
        Returns the smallest base where the number is a palindrome
        :param number: Number to find the smallest base palindrome
        :return: The smallest base where the number is a palindrome
        """
        if number in [1, 2]:
            return number + 1
        for base, base_value in enumerate(self.get_base_values(number)):
            if self.is_palindrome(base_value):
                return base + 2  # Start from base 2
        return number - 1

    def get_base_values(self, number: int):
        """
        Generate arrays that represent the digits for the number in bases 2 - (Number - 1)
        :param number: Number to generate base arrays for
        :return: An array of integers where each index is a digit within the value in the base
        """
        for b in range(2, number - 1):
            temp = number
            digits = []
            while temp:
                digits.append(int(temp % b))
                temp //= b
            yield digits[::-1]
        yield [1, 1]

    def is_palindrome(self, number_digit_array):
        """
        Returns true if the given string is a palindrome
        :param number_digit_array: an integer array where each index is a digit for the number
        :return: True if the array is equal to its reverse and False otherwise
        """
        return number_digit_array == number_digit_array[::-1]


if __name__ == '__main__':
    palindrome = Palindrome('palindromes.csv')
    palindrome.print_palindrome_bases(1, 1000)
