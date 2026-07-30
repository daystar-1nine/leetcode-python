"""
LeetCode Problem: 8. String to Integer (atoi)
Difficulty: Medium
Language: Python
Approach: Sequential State Parsing with In-Loop Overflow Protection
Concepts Used: String, ASCII Math, Boundary Clamping, Simulation

Time Complexity: O(N)
Space Complexity: O(1)

Author: Suraj Sawant
"""

class Solution(object):
    def myAtoi(self, s):
        """
        Parses a string into a 32-bit signed integer following C-style atoi rules.

        Args:
            s (str): Input string to be converted into an integer.

        Returns:
            int: Converted 32-bit signed integer, clamped within [-2^31, 2^31 - 1].
        """

        # 32-bit signed integer limits as specified by hardware constraints.
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Pointer for sequential character inspection and total string length.
        i = 0
        n = len(s)

        # Step 1: Skip leading whitespace characters to locate start of numeric content.
        while i < n and s[i] == " ":
            i += 1

        # If string consists solely of whitespace characters, return 0 as base case.
        if i == n:
            return 0

        # Step 2: Determine sign from optional leading '+' or '-' character.
        sign = 1
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1

        # Accumulator for building the absolute magnitude of the integer.
        num = 0

        # Step 3: Process contiguous digit characters until a non-digit or end of string.
        while i < n and s[i].isdigit():
            # Convert ASCII character digit to integer value using character code offset.
            digit = ord(s[i]) - ord('0')

            # Step 4: Check for potential 32-bit signed overflow BEFORE updating num.
            # Using algebraically rearranged inequality: num * 10 + digit > INT_MAX
            # prevents overflow errors in environments with fixed integer widths.
            if num > (INT_MAX - digit) // 10:
                # Clamp result directly to INT_MAX for positive numbers or INT_MIN for negative numbers.
                return INT_MAX if sign == 1 else INT_MIN

            # Append current digit to numerical accumulator.
            num = num * 10 + digit
            i += 1

        # Apply sign to accumulated magnitude and return final integer.
        return sign * num

"""
Algorithm Used: Sequential State-Machine Parsing with In-Loop Overflow Check
Key Concepts: ASCII Arithmetic, State Machine Parsing, Range Clamping
Time Complexity: O(N) - Linear scan of input string of length N
Space Complexity: O(1) - Constant auxiliary memory
"""
