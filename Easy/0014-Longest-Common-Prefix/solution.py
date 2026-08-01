"""
LeetCode Problem: 14. Longest Common Prefix
Difficulty: Easy
Language: Python
Approach: Horizontal Scanning (Prefix Truncation)
Concepts Used: String, Array Traversal, Substring Matching

Time Complexity: O(S)
Space Complexity: O(1)

Author: Suraj Sawant
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        Finds the longest common prefix string amongst an array of strings.

        Args:
            strs (List[str]): List of input strings.

        Returns:
            str: Longest common prefix string, or "" if no common prefix exists.
        """

        # Guard Clause: Return empty string if input array is empty.
        if not strs:
            return ""

        # Initialize common prefix candidate with the first string in the list.
        prefix = strs[0]

        # Horizontally scan remaining strings in the list from index 1 onward.
        for i in range(1, len(strs)):
            # Trim prefix from right by 1 character (prefix[:-1]) until strs[i] starts with prefix.
            # strs[i].find(prefix) == 0 verifies that prefix is located at index 0 (starts-with check).
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]

                # Early exit: If prefix shrinks to empty string, no common prefix exists across all strings.
                if prefix == "":
                    return ""

        # Return final validated common prefix.
        return prefix

"""
Algorithm Used: Horizontal Scanning (Horizontal Prefix Truncation)
Key Concepts: Prefix Truncation, Substring Searching, Guard Clause
Time Complexity: O(S) - Where S is the total number of characters across all strings in the array
Space Complexity: O(1) - Constant auxiliary memory space (excluding input/output string space)
"""
