"""
LeetCode Problem: 3702. Longest Subsequence With Non-Zero Bitwise XOR
Difficulty: Medium
Language: Python
Approach: Bitwise XOR Property Analysis & Single Element Removal
Concepts Used: Array, Bit Manipulation, Bitwise XOR Properties

Time Complexity: O(N)
Space Complexity: O(1)

Author: Suraj Sawant
"""

class Solution(object):
    def longestSubsequence(self, nums):
        """
        Calculates the length of the longest subsequence with a non-zero bitwise XOR sum.

        Args:
            nums (List[int]): Array of integers.

        Returns:
            int: Maximum length of a subsequence whose XOR sum is non-zero.
        """

        xor = 0

        # Calculate the cumulative bitwise XOR of all elements in the array.
        for num in nums:
            xor ^= num

        # Case 1: If total XOR sum is already non-zero, the entire array itself
        # is a valid subsequence with non-zero XOR sum.
        if xor != 0:
            return len(nums)

        # Case 2: Total XOR sum is 0. If there is at least one non-zero element in the array,
        # removing that single non-zero element flips the overall XOR sum from 0 to non-zero
        # (since 0 ^ num = num != 0). Thus, the max subsequence length is len(nums) - 1.
        for num in nums:
            if num != 0:
                return len(nums) - 1

        # Case 3: All elements in nums are 0. Any subsequence will have an XOR sum of 0,
        # so no non-zero XOR subsequence can be formed.
        return 0

"""
Algorithm Used: Bitwise XOR Cumulative Property & Non-Zero Flip
Key Concepts: XOR Self-Inverse Property (A ^ A = 0), Single Element Removal, Bitwise Optimization
Time Complexity: O(N) - Linear pass across array of length N
Space Complexity: O(1) - Constant auxiliary memory space
"""
