"""
LeetCode Problem: 17. Letter Combinations of a Phone Number
Difficulty: Medium
Language: Python
Approach: Recursive Backtracking (DFS Decision Tree)
Concepts Used: Hash Table, String, Backtracking, Depth-First Search

Time Complexity: O(4^N * N)
Space Complexity: O(N) auxiliary space (recursion call stack depth)

Author: Suraj Sawant
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        Generates all possible letter combinations that the input digit string could represent.

        Args:
            digits (str): String containing digits from 2-9 inclusive.

        Returns:
            List[str]: List of all possible letter combinations in any order.
        """

        # Guard Clause: An empty digit string yields no combinations.
        if not digits:
            return []

        # Hash map mapping digit characters to their corresponding telephone keypad letters.
        phone = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        # List accumulator storing all valid generated combinations.
        result = []

        def backtrack(index, current):
            """
            Recursive DFS helper function to explore combinations index by index.

            Args:
                index (int): Active digit index being processed.
                current (str): String path constructed so far.
            """
            # Base Case: When path length equals digits length, a valid combination is complete.
            if index == len(digits):
                result.append(current)
                return

            # Fetch corresponding letter set for the current digit character.
            letters = phone[digits[index]]

            # Explore each candidate character choice recursively (DFS branch).
            for ch in letters:
                backtrack(index + 1, current + ch)

        # Initiate backtracking starting from digit index 0 with an empty string path.
        backtrack(0, "")

        # Return full list of generated letter combinations.
        return result

"""
Algorithm Used: Recursive Backtracking (Depth-First Search)
Key Concepts: Decision Tree Traversal, Hash Map Lookup, Path Construction
Time Complexity: O(4^N * N) - N is number of digits (each digit maps to up to 4 letters)
Space Complexity: O(N) - Recursion call stack depth of N (excluding result output array)
"""
