"""
LeetCode Problem: 1140. Stone Game II
Difficulty: Medium
Language: Python
Approach: Top-Down Dynamic Programming with Memoization & Suffix Sums
Concepts Used: Dynamic Programming, Game Theory, Minimax / Zero-Sum State, Suffix Sum

Time Complexity: O(N^3)
Space Complexity: O(N^2)

Author: Suraj Sawant
"""

class Solution(object):
    def stoneGameII(self, piles):
        """
        Calculates the maximum number of stones Alice can collect playing optimally.

        Args:
            piles (List[int]): Array representing stones in each pile.

        Returns:
            int: Maximum stones Alice can obtain starting first.
        """

        n = len(piles)

        # Precompute suffix sums where suffix_sum[i] stores the sum of all stones from index i to end.
        # This allows O(1) retrieval of total remaining stones from any index i.
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        # Memoization dictionary mapping (i, M) state tuples to max stones obtainable.
        memo = {}

        def dp(i, M):
            """
            Recursive helper returning max stones active player can get starting from index i with parameter M.

            Args:
                i (int): Current pile index.
                M (int): Active M multiplier parameter.

            Returns:
                int: Maximum stones obtainable for the active player.
            """
            # Base Case: If remaining piles can all be taken in a single turn (i + 2*M >= n),
            # the active player takes all remaining stones.
            if i + 2 * M >= n:
                return suffix_sum[i]

            # Return cached result if state (i, M) was previously evaluated.
            if (i, M) in memo:
                return memo[(i, M)]

            res = 0

            # Try taking X piles where 1 <= X <= 2 * M.
            for X in range(1, 2 * M + 1):
                # By taking X piles, opponent gets optimal stones from (i + X, max(M, X)).
                # Current player receives: (total remaining stones from i) - (opponent's optimal share).
                res = max(res, suffix_sum[i] - dp(i + X, max(M, X)))

            # Cache evaluated result for state (i, M).
            memo[(i, M)] = res
            return res

        # Game starts at index 0 with initial M parameter = 1.
        return dp(0, 1)

"""
Algorithm Used: Top-Down DP with Minimax State Complement & Suffix Sums
Key Concepts: Game Theory Zero-Sum Reduction, Suffix Sum Optimization, State Memoization
Time Complexity: O(N^3) - State space is O(N^2) where i <= N, M <= N, and each state loops up to 2M <= N times
Space Complexity: O(N^2) - Auxiliary memory for memoization dictionary and recursion stack
"""
