"""
LeetCode Problem: 7. Reverse Integer
Difficulty: Medium
Language: Python
Approach: Base-10 Arithmetic Digit Reversal with 32-bit Bounds Checking
Concepts Used: Math, Modulo Arithmetic, Integer Range Bounds

Time Complexity: O(log10(|x|))
Space Complexity: O(1)

Author: Suraj Sawant
"""

class Solution(object):
    def reverse(self, x):
        """
        Reverses the digits of a signed 32-bit integer.

        Args:
            x (int): Input 32-bit signed integer.

        Returns:
            int: Reversed integer if within [-2^31, 2^31 - 1], otherwise 0.
        """

        # Define 32-bit signed integer boundaries as specified by problem constraints.
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Isolate sign (-1 or 1) and operate on absolute magnitude to make Python modulo deterministic.
        sign = -1 if x < 0 else 1
        x = abs(x)

        # Accumulator variable holding the reversed digit number.
        rev = 0

        # Loop until all base-10 digits are extracted from x.
        while x != 0:
            # Extract rightmost (least significant) digit using modulo 10.
            digit = x % 10
            # Shift accumulator left by 1 decimal place and append current digit.
            rev = rev * 10 + digit
            # Truncate rightmost digit from x using integer division.
            x = x // 10

        # Restore original sign to the reversed number.
        rev *= sign

        # Verify that reversed value lies strictly within signed 32-bit integer limits.
        if rev < INT_MIN or rev > INT_MAX:
            return 0

        # Return valid reversed integer.
        return rev

"""
Algorithm Used: Mathematical Digit Reversal via Modulo and Division
Key Concepts: Base-10 Digit Extraction, Signed Range Checking, Absolute Value
Time Complexity: O(log10(|x|)) - Maximum 10 iterations for a 32-bit integer
Space Complexity: O(1) - Constant auxiliary space
"""
