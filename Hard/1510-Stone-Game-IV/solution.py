"""
LeetCode Problem: 1510. Stone Game IV
Difficulty: Hard
Language: Python
Approach: Bottom-Up Dynamic Programming (Game Theory Sub-State Transition)
Concepts Used: Dynamic Programming, Game Theory, Square Numbers, Boolean DP

Time Complexity: O(N * sqrt(N))
Space Complexity: O(N)

Author: Suraj Sawant
"""

class Solution(object):
    def winnerSquareGame(self, n):
        """
        Determines if Alice wins the square stone game starting with n stones assuming optimal play.

        Args:
            n (int): Initial number of stones.

        Returns:
            bool: True if Alice wins, False if Bob wins.
        """

        # dp[i] stores True if the active player can guarantee a win starting with i stones,
        # and False if the active player is forced into a losing position.
        dp = [False] * (n + 1)

        # Build DP table bottom-up from 1 to n stones.
        for i in range(1, n + 1):

            j = 1

            # Try removing any valid non-zero square number of stones (j * j <= i).
            while j * j <= i:

                # If removing j*j stones leaves the next player in a losing state (dp[i - j*j] == False),
                # then the current player can force a win by taking j*j stones!
                if dp[i - j * j] == False:
                    dp[i] = True
                    break

                j += 1

        # dp[n] represents whether Alice (the first player) can force a win starting with n stones.
        return dp[n]

"""
Algorithm Used: Bottom-Up Dynamic Programming with Square Moves
Key Concepts: Game Theory Winning/Losing States, Perfect Square Removal, Short-Circuit Evaluation
Time Complexity: O(N * sqrt(N)) - Outer loop runs N times, inner loop runs up to sqrt(N) times
Space Complexity: O(N) - DP array of size N + 1
"""
