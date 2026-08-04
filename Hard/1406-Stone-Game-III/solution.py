"""
LeetCode Problem: 1406. Stone Game III
Difficulty: Hard
Language: Python
Approach: Bottom-Up Dynamic Programming (Minimax / Game Theory)
Concepts Used: Dynamic Programming, Game Theory, Minimax State Reduction, Array Traversal

Time Complexity: O(N)
Space Complexity: O(N) (can be optimized to O(1))

Author: Suraj Sawant
"""

class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        Determines the winner of Stone Game III assuming both Alice and Bob play optimally.

        Args:
            stoneValue (List[int]): Array of integer values of stones.

        Returns:
            str: "Alice", "Bob", or "Tie" based on optimal play outcome.
        """

        n = len(stoneValue)

        # dp[i] represents the maximum score difference (active_player_score - opponent_score)
        # that the player whose turn it is can achieve starting from index i to the end of the array.
        # dp[n] = 0 (base case when no stones remain).
        dp = [0] * (n + 1)

        # Process array backwards from index n-1 down to 0.
        for i in range(n - 1, -1, -1):

            # Initialize current state to negative infinity to maximize relative gain.
            dp[i] = float("-inf")
            take = 0

            # Active player can choose to take 1, 2, or 3 stones (k = 0, 1, 2).
            for k in range(3):

                # Ensure index boundary condition remains within array bounds.
                if i + k < n:
                    # Accumulate value of stones taken in current move.
                    take += stoneValue[i + k]

                    # Transition equation:
                    # Current player's relative advantage = (stones taken in this move) - (opponent's optimal advantage from i + k + 1).
                    dp[i] = max(dp[i], take - dp[i + k + 1])

        # Alice moves first from index 0. If dp[0] > 0, Alice gets more points than Bob.
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"

"""
Algorithm Used: Bottom-Up Dynamic Programming (Minimax State Advantage)
Key Concepts: Game Theory Minimax, Relative Score Difference, Backward State Evaluation
Time Complexity: O(N) - Single loop backwards of length N with fixed 3-choice inner loop
Space Complexity: O(N) - DP table of size N + 1 (O(1) space optimization possible using 4 variables)
"""
