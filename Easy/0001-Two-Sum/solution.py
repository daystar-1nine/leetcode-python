"""
LeetCode Problem: 1. Two Sum
Difficulty: Easy
Language: Python
Approach: One-Pass Hash Map (Dictionary) Lookup
Concepts Used: Array, Hash Table, Complement Arithmetic

Time Complexity: O(N)
Space Complexity: O(N)

Author: Suraj Sawant
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        Finds two numbers in an array that sum to a given target.

        Args:
            nums (List[int]): Array of integers.
            target (int): Target sum value.

        Returns:
            List[int]: Indices of the two numbers that add up to target.
        """
        # Dictionary to map visited numbers to their corresponding 0-based index.
        # Format: { number_value: index }
        seen = {}

        # Iterate through the array once to process each element.
        for i in range(len(nums)):
            # Calculate the complementary value required to reach the target sum.
            complement = target - nums[i]

            # Check if the required complement has already been seen in earlier steps.
            # Lookup in a hash map takes O(1) average time.
            if complement in seen:
                # Return the stored index of the complement and the current index.
                return [seen[complement], i]

            # Record current number and its index to serve as a potential complement for future elements.
            seen[nums[i]] = i

"""
Algorithm Used: One-Pass Hash Map Lookup
Key Concepts: Hash Table, Array Traversal, Algebraic Complement Search
Time Complexity: O(N) - Single pass through array of length N
Space Complexity: O(N) - Storage for up to N elements in dictionary
"""
