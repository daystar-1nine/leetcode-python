"""
LeetCode Problem: 22. Generate Parentheses
Difficulty: Medium
Language: Python
Approach: Recursive Backtracking with Open/Close Count Pruning
Concepts Used: Backtracking, String, Recursion, Catalyst Decision Tree

Time Complexity: O(4^N / sqrt(N)) - Catalan number sequence C_N
Space Complexity: O(N) auxiliary stack space

Author: Suraj Sawant
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        Generates all combinations of well-formed parentheses for n pairs.

        Args:
            n (int): Number of pairs of parentheses.

        Returns:
            List[str]: List of valid well-formed parenthesis combinations.
        """

        # List accumulator to store all valid well-formed combinations.
        result = []

        def backtrack(current, open_count, close_count):
            """
            Recursive helper function to construct valid parenthesis combinations.

            Args:
                current (str): String path constructed so far.
                open_count (int): Total number of '(' added to current path.
                close_count (int): Total number of ')' added to current path.
            """
            # Base Case: When string length reaches 2 * n, a complete well-formed combination is formed.
            if len(current) == 2 * n:
                result.append(current)
                return

            # Branch 1: Add an opening bracket '(' if open_count is less than total allowed pairs n.
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Branch 2: Add a closing bracket ')' only if close_count is strictly less than open_count
            # to guarantee that brackets remain validly balanced at every step.
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        # Kickoff recursive backtracking starting with an empty path and zero counts.
        backtrack("", 0, 0)

        # Return all generated valid combinations.
        return result

"""
Algorithm Used: Recursive Backtracking with Open/Close Count Constraints
Key Concepts: Decision Tree Pruning, Catalan Number Combinatorics, Depth-First Search
Time Complexity: O(4^N / sqrt(N)) - Total valid sequences generated is the N-th Catalan Number C_N
Space Complexity: O(N) - Maximum recursion stack depth of 2 * N (excluding output list)
"""
