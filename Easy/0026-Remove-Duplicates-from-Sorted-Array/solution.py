"""
LeetCode Problem: 26. Remove Duplicates from Sorted Array
Difficulty: Easy
Language: Python
Approach: Two Pointers (In-Place Fast/Slow Pointer Traversal)
Concepts Used: Array, Two Pointers, In-Place Array Mutation

Time Complexity: O(N)
Space Complexity: O(1)

Author: Suraj Sawant
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        Removes duplicates from a sorted array in-place and returns the count of unique elements.

        Args:
            nums (List[int]): Array of integers sorted in non-decreasing order.

        Returns:
            int: Number of unique elements k.
        """

        # Guard Clause: If the array is empty, return 0 unique elements.
        if not nums:
            return 0

        # Slow pointer 'k' tracks the write position for the next unique element.
        # Since nums is pre-sorted, the first element at index 0 is always unique.
        k = 1

        # Fast pointer 'i' scans the array from index 1 to the end.
        for i in range(1, len(nums)):

            # Compare current element with the previous element.
            # If a new unique element is encountered:
            if nums[i] != nums[i - 1]:

                # Write the unique element to position 'k'.
                nums[k] = nums[i]

                # Advance the write pointer 'k'.
                k += 1

        # Return the total count of unique elements (number of elements written).
        return k

"""
Algorithm Used: Two Pointers In-Place Array Deduplication
Key Concepts: Fast/Slow Pointers, Non-Decreasing Array Property, In-Place Mutation
Time Complexity: O(N) - Single linear pass over array of length N
Space Complexity: O(1) - Constant auxiliary space (array mutated in-place)
"""
