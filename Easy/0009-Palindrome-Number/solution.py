"""
LeetCode Problem: 9. Palindrome Number
Difficulty: Easy
Language: Python
Approach: Reversing Half of the Integer (Mathematical Logarithmic Simulation)
Concepts Used: Math, Modulo Arithmetic, Half-Number Reversal

Time Complexity: O(log10(N))
Space Complexity: O(1)

Author: Suraj Sawant
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        Determines whether an integer is a palindrome without converting to string.

        Args:
            x (int): Input integer.

        Returns:
            bool: True if x is a palindrome, False otherwise.
        """

        # Guard Clause: Negative numbers can never be palindromes due to leading '-' sign.
        # Numbers ending in 0 (except 0 itself) can never be palindromes because leading digits cannot be 0.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Accumulator holding the reversed digits of the second half of the number.
        reversed_half = 0

        # Loop until we have processed half of the digits.
        # When x <= reversed_half, we have reached or passed the middle digit position.
        while x > reversed_half:
            # Extract rightmost digit using modulo 10.
            digit = x % 10
            # Push digit onto reversed_half accumulator.
            reversed_half = reversed_half * 10 + digit
            # Drop rightmost digit from x using integer division.
            x = x // 10

        # For numbers with an even count of digits: x == reversed_half (e.g. 1221 -> x=12, reversed_half=12).
        # For numbers with an odd count of digits: x == reversed_half // 10 (e.g. 12321 -> x=12, reversed_half=123, middle digit '3' discarded).
        return x == reversed_half or x == reversed_half // 10

"""
Algorithm Used: Reversing Half of the Integer
Key Concepts: Base-10 Digit Extraction, Half-Way Symmetry Verification, Constant Memory
Time Complexity: O(log10(N)) - Iterates through half of the total decimal digits
Space Complexity: O(1) - Uses constant auxiliary primitive integers
"""
