"""
LeetCode Problem: 12. Integer to Roman
Difficulty: Medium
Language: Python
Approach: Greedy Value-Symbol Mapping
Concepts Used: Array, Math, String, Greedy Algorithm

Time Complexity: O(1)
Space Complexity: O(1)

Author: Suraj Sawant
"""

class Solution(object):
    def intToRoman(self, num):
        """
        Converts an integer to a Roman numeral string.

        Args:
            num (int): Input integer in range [1, 3999].

        Returns:
            str: Converted Roman numeral representation.
        """

        # Pre-defined mapping of integer values sorted in descending order.
        # Includes both standard symbols (M, D, C, L, X, V, I) and subtractive combinations (CM, CD, XC, XL, IX, IV)
        # to enable greedy top-down selection.
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        # Corresponding Roman numeral symbols aligned identically by index with values list.
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        # String accumulator to collect generated Roman numeral symbols.
        result = ""

        # Iterate through value thresholds from largest (1000) to smallest (1).
        for i in range(len(values)):
            # Greedily subtract the largest possible value[i] from num
            # and append its corresponding symbol[i] to result string.
            while num >= values[i]:
                result += symbols[i]
                num -= values[i]

        # Return fully accumulated Roman numeral string.
        return result

"""
Algorithm Used: Greedy Value-Symbol Mapping
Key Concepts: Greedy Selection, Subtractive Notation Mapping, Fixed Range Array Lookup
Time Complexity: O(1) - The number of iterations is strictly bounded since input num <= 3999
Space Complexity: O(1) - Constant auxiliary memory for fixed 13-element lookup arrays
"""
