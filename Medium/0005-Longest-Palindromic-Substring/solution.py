"""
LeetCode Problem: 5. Longest Palindromic Substring
Difficulty: Medium
Language: Python
Approach: Expand Around Center (Two Pointers Expansion)
Concepts Used: String, Two Pointers, Dynamic Programming, Symmetry

Time Complexity: O(N^2)
Space Complexity: O(1)

Author: Suraj Sawant
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        Finds the longest palindromic substring in s.

        Args:
            s (str): Input string.

        Returns:
            str: Longest palindromic substring.
        """

        # Guard clause: Strings of length 0 or 1 are trivially palindromic.
        if len(s) < 2:
            return s

        # Track starting index and length of the longest palindromic substring found so far.
        start = 0
        max_len = 1

        # Iterate through every index i as a potential center of a palindrome.
        for i in range(len(s)):

            # Case 1: Odd-length palindrome expansion (single-character center at index i).
            left = i
            right = i

            # Expand pointers outward while characters match and bounds remain valid.
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # Update starting index and maximum length if current palindrome is longer.
                if right - left + 1 > max_len:
                    start = left
                    max_len = right - left + 1
                left -= 1
                right += 1

            # Case 2: Even-length palindrome expansion (two-character center between i and i + 1).
            left = i
            right = i + 1

            # Expand pointers outward while characters match and bounds remain valid.
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # Update starting index and maximum length if current palindrome is longer.
                if right - left + 1 > max_len:
                    start = left
                    max_len = right - left + 1
                left -= 1
                right += 1

        # Return substring slice using tracked start index and max_len.
        return s[start:start + max_len]

"""
Algorithm Used: Expand Around Center (Two Pointers Expansion)
Key Concepts: Palindromic Symmetry, Two Pointers, Odd/Even Parity Centers
Time Complexity: O(N^2) - Expands from 2N-1 centers, taking up to O(N) per expansion
Space Complexity: O(1) - Constant auxiliary space (excluding result slice)
"""
