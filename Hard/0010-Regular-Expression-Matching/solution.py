"""
LeetCode Problem: 10. Regular Expression Matching
Difficulty: Hard
Language: Python
Approach: Top-Down Dynamic Programming with Memoization
Concepts Used: String, Dynamic Programming, Recursion, Memoization, Pattern Matching

Time Complexity: O(M * N)
Space Complexity: O(M * N)

Author: Suraj Sawant
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        Evaluates if string s matches pattern p supporting '.' and '*' wildcard operators.

        Args:
            s (str): Input text string.
            p (str): Pattern string containing '.' and '*' characters.

        Returns:
            bool: True if text s matches pattern p completely, False otherwise.
        """

        # Dictionary for memoizing state subproblem results to avoid exponential recalculation.
        # Key format: (i, j) where i is index in s, and j is index in p.
        memo = {}

        def dp(i, j):
            """
            Recursive helper function checking if s[i:] matches p[j:].
            
            Args:
                i (int): Active index in text string s.
                j (int): Active index in pattern string p.
            
            Returns:
                bool: Subproblem match result.
            """
            # Return cached result if subproblem state (i, j) was already evaluated.
            if (i, j) in memo:
                return memo[(i, j)]

            # Base Case: When pattern string p is completely consumed (j == len(p)),
            # match is successful ONLY if text string s is also completely consumed (i == len(s)).
            if j == len(p):
                return i == len(s)

            # Evaluate single character match between s[i] and p[j].
            # '.' matches any single character. Text index i must remain within bounds.
            first_match = (
                i < len(s) and
                (s[i] == p[j] or p[j] == '.')
            )

            # Check if next pattern character is the '*' wildcard operator.
            if j + 1 < len(p) and p[j + 1] == '*':
                # '*' wildcard presents two structural choices:
                # 1. Zero occurrences: Ignore 'ch*' in pattern and advance pattern by 2 -> dp(i, j + 2)
                # 2. One or more occurrences: Consume 1 character in s and keep 'ch*' in pattern -> (first_match and dp(i + 1, j))
                ans = (
                    dp(i, j + 2) or
                    (first_match and dp(i + 1, j))
                )
            else:
                # Standard character match (no '*' following):
                # Require current character match and advance both pointers by 1 -> dp(i + 1, j + 1)
                ans = first_match and dp(i + 1, j + 1)

            # Cache the computed state result before returning to optimize recursive depth.
            memo[(i, j)] = ans
            return ans

        # Kick off top-down recursion starting from index 0 of both string s and pattern p.
        return dp(0, 0)

"""
Algorithm Used: Top-Down Dynamic Programming (Recursion + Memoization)
Key Concepts: State-Space Search, Subproblem Caching, Wildcard Matching Logic
Time Complexity: O(M * N) - Where M is length of string s and N is length of pattern p
Space Complexity: O(M * N) - Memory for memoization dictionary and call stack depth
"""
