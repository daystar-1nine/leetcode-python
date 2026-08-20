"""
LeetCode Problem: 2029. Stone Game IX
Difficulty: Medium
Language: Python
Approach: Modulo Remainder Counting & Minimax Game Theory Case Analysis
Concepts Used: Array, Math, Greedy, Counting, Game Theory, Modulo Arithmetic

Time Complexity: O(N)
Space Complexity: O(1)

Author: Suraj Sawant
"""

class Solution(object):
    def stoneGameIX(self, stones):
        """
        Determines if Alice wins the stone game given an array of stone values.

        Args:
            stones (List[int]): List of positive integer stone values.

        Returns:
            bool: True if Alice wins assuming optimal play, False if Bob wins.
        """

        # Frequency array to count stones based on value % 3.
        # count[0] -> stones divisible by 3
        # count[1] -> stones with remainder 1
        # count[2] -> stones with remainder 2
        count = [0, 0, 0]

        # Populate frequency array of remainders modulo 3.
        for stone in stones:
            count[stone % 3] += 1

        # Case 1: If count of stones divisible by 3 (count[0]) is EVEN,
        # count[0] does not change the turn order or remainder parity for critical moves.
        # Alice can win if and only if both remainder 1 and remainder 2 types exist (count[1] > 0 and count[2] > 0).
        if count[0] % 2 == 0:
            return count[1] > 0 and count[2] > 0

        # Case 2: If count of stones divisible by 3 (count[0]) is ODD,
        # count[0] flips the turn order once.
        # Alice can win if and only if the difference between count[1] and count[2] is greater than 2.
        return abs(count[1] - count[2]) > 2

"""
Algorithm Used: Modulo Remainder Frequency Analysis
Key Concepts: Modulo Arithmetic (% 3), Turn Order Flipping, Minimax Game Theory, Parity Analysis
Time Complexity: O(N) - Single linear pass to count remainders
Space Complexity: O(1) - Constant size 3 array for frequency counting
"""
