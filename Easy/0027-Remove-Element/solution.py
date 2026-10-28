"""
LeetCode Problem: 27. Remove Element
Difficulty: Easy
Language: Python
Approach: Two Pointers (In-Place Fast/Slow Pointer Traversal)
Concepts Used: Array, Two Pointers, In-Place Array Mutation

Time Complexity: O(N)
Space Complexity: O(1)

Author: Suraj Sawant
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        Removes all occurrences of val in nums in-place and returns the number of elements not equal to val.

        Args:
            nums (List[int]): Array of integers.
            val (int): Integer value to remove.

        Returns:
            int: Number of elements in nums not equal to val (k).
        """
        # Slow pointer 'k' tracks the write position for valid elements (elements != val).
        k = 0

        # Fast pointer 'i' scans every element in the array.
        for i in range(len(nums)):
            # If current element is not equal to val, retain it at index k.
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        # Return the count of elements that are not equal to val.
        return k

"""
Algorithm Used: Two Pointers In-Place Array Filtering
Key Concepts: Fast/Slow Pointers, Overwriting Elements, In-Place Mutation
Time Complexity: O(N) - Single linear pass over array of length N
Space Complexity: O(1) - Constant auxiliary space (array mutated in-place)
"""
