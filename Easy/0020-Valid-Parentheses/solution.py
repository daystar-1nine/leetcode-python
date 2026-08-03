"""
LeetCode Problem: 20. Valid Parentheses
Difficulty: Easy
Language: Python
Approach: Stack-Based Bracket Matching (LIFO Data Structure)
Concepts Used: Stack, String, Hash Map, Last-In-First-Out (LIFO)

Time Complexity: O(N)
Space Complexity: O(N)

Author: Suraj Sawant
"""

class Solution(object):
    def isValid(self, s):
        """
        Determines if the input string containing brackets is valid.

        Args:
            s (str): String containing bracket characters '(', ')', '{', '}', '[', ']'.

        Returns:
            bool: True if input string has valid matching and closed brackets, False otherwise.
        """

        # Stack array to keep track of open brackets waiting to be matched.
        stack = []

        # Hash map mapping closing brackets to their corresponding opening bracket pair.
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        # Iterate through each character in the input string.
        for ch in s:

            # If character is an opening bracket, push it onto the stack.
            if ch in "([{":
                stack.append(ch)

            # Otherwise, character is a closing bracket.
            else:
                # If stack is empty, there is no matching opening bracket for this closing bracket.
                if not stack:
                    return False

                # Pop the most recent opening bracket from the top of the stack.
                top = stack.pop()

                # Verify if the popped opening bracket matches the required pair for closing bracket ch.
                if top != pairs[ch]:
                    return False

        # If stack is completely empty, all open brackets were correctly matched and closed.
        return len(stack) == 0

"""
Algorithm Used: Stack-Based Bracket Matching
Key Concepts: Last-In-First-Out (LIFO) Stack, Hash Map Pair Matching, Balanced Parentheses
Time Complexity: O(N) - Single linear pass over string of length N
Space Complexity: O(N) - Worst case stack allocation for all opening brackets
"""
