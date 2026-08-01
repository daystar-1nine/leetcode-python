"""
LeetCode Problem: 13. Roman to Integer
Difficulty: Easy
Language: Python
Approach: Hash Map Traversal with Subtractive Lookahead
Concepts Used: Hash Table, Math, String, Right-to-Left / Left-to-Right Comparison

Time Complexity: O(N)
Space Complexity: O(1)

Author: Suraj Sawant
"""

class Solution(object):
    def romanToInt(self, s):
        """
        Converts a Roman numeral string to an integer.

        Args:
            s (str): Input Roman numeral string.

        Returns:
            int: Converted integer value.
        """

        # Hash map mapping basic Roman numeral characters to their integer values.
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Accumulator tracking the total converted integer sum.
        total = 0

        # Iterate left-to-right through each character index in string s.
        for i in range(len(s)):
            # Lookahead check: If current character value is strictly less than the next character value,
            # it represents a subtractive pair (e.g. IV = -1 + 5 = 4, IX = -1 + 10 = 9).
            # Therefore, subtract current symbol value from total.
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                # Otherwise, standard additive representation applies. Add current symbol value to total.
                total += roman[s[i]]

        # Return accumulated total.
        return total

"""
Algorithm Used: Hash Map Traversal with Subtractive Lookahead
Key Concepts: Hash Table Lookup, Subtractive Notation Handling, Single Pass Scan
Time Complexity: O(N) - Where N is length of string s (N <= 15 for valid Roman numerals up to 3999)
Space Complexity: O(1) - Fixed 7-element hash map memory
"""
