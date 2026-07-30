"""
LeetCode Problem: 3. Longest Substring Without Repeating Characters
Difficulty: Medium
Language: Python
Approach: Dynamic Sliding Window with Hash Set
Concepts Used: Hash Table, String, Sliding Window, Two Pointers

Time Complexity: O(N)
Space Complexity: O(min(N, M))

Author: Suraj Sawant
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Calculates the length of the longest substring without duplicate characters.

        Args:
            s (str): Input string.

        Returns:
            int: Maximum length of substring with unique characters.
        """
        # Set storing unique characters currently present in active sliding window s[left..right].
        char_set = set()
        # Pointer tracking the left boundary of the sliding window.
        left = 0
        # Variable tracking the maximum valid substring length found so far.
        max_length = 0

        # Expand the right boundary of the sliding window index by index.
        for right in range(len(s)):

            # If current character s[right] is already in set, shrink window from left
            # until all characters in s[left..right] are unique again.
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add current character to set now that window contains no duplicates.
            char_set.add(s[right])

            # Update max_length with size of current valid sliding window (right - left + 1).
            max_length = max(max_length, right - left + 1)

        # Return maximum length recorded across all window steps.
        return max_length

"""
Algorithm Used: Dynamic Sliding Window with Hash Set Lookup
Key Concepts: Sliding Window, Hash Set Uniqueness, Two Pointers
Time Complexity: O(N) - Each character is added and removed at most once
Space Complexity: O(min(N, M)) - Memory bounded by string length N and character set size M
"""
