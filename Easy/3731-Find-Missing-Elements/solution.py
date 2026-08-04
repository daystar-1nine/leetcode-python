"""
LeetCode Problem: 3731. Find Missing Elements
Difficulty: Easy
Language: Python
Approach: Hash Set Lookup over Range Boundary [min(nums), max(nums)]
Concepts Used: Array, Hash Table / Set, Min/Max Range Traversal

Time Complexity: O(N + (max - min))
Space Complexity: O(N)

Author: Suraj Sawant
"""

class Solution(object):
    def findMissingElements(self, nums):
        """
        Finds all missing integers in the range [min(nums), max(nums)].

        Args:
            nums (List[int]): List of unique integers.

        Returns:
            List[int]: Sorted list of missing integers within the min to max range.
        """

        # Convert nums list into a hash set to enable O(1) constant-time presence checks.
        num_set = set(nums)

        # Find the minimum and maximum boundaries of the input array.
        minimum = min(nums)
        maximum = max(nums)

        # List accumulator to store missing elements in ascending order.
        result = []

        # Iterate through every integer from minimum to maximum inclusive.
        for num in range(minimum, maximum + 1):
            # If the current integer is not present in the set, append it to the result.
            if num not in num_set:
                result.append(num)

        # Return list of missing elements.
        return result

"""
Algorithm Used: Hash Set Lookup over Range Boundary
Key Concepts: Hash Set Fast Lookup O(1), Range Bounds [min, max], Linear Scan
Time Complexity: O(N + R) - N is len(nums), R is range span (max - min + 1)
Space Complexity: O(N) - Auxiliary memory for storing elements in num_set
"""
