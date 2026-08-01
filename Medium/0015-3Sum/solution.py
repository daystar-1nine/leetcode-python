"""
LeetCode Problem: 15. 3Sum
Difficulty: Medium
Language: Python
Approach: Sorting + Two Pointers Strategy
Concepts Used: Array, Two Pointers, Sorting, Duplicate Elimination

Time Complexity: O(N^2)
Space Complexity: O(1) auxiliary space (O(N) for sorting depending on language)

Author: Suraj Sawant
"""

class Solution(object):
    def threeSum(self, nums):
        """
        Finds all unique triplets in the array which sum to zero.

        Args:
            nums (List[int]): Input array of integers.

        Returns:
            List[List[int]]: Unique triplets [nums[i], nums[j], nums[k]] summing to zero.
        """

        # Sort input array in-place.
        # Sorting enables Two Pointers traversal and allows clean skipping of duplicate elements.
        nums.sort()
        result = []

        n = len(nums)

        # Fix the first element nums[i] and use Two Pointers for the remaining sub-array.
        # Loop runs up to n - 2 to leave space for left and right pointers.
        for i in range(n - 2):

            # Skip duplicate values for the first element to avoid redundant triplet combinations.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize two pointers for the sub-array nums[i+1 ... n-1].
            left = i + 1
            right = n - 1

            # Two Pointers search loop for matching target sum: nums[left] + nums[right] == -nums[i].
            while left < right:

                total = nums[i] + nums[left] + nums[right]

                # Case 1: Matching triplet found (sum == 0).
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Advance both pointers to look for further valid pairs.
                    left += 1
                    right -= 1

                    # Skip duplicate left values to maintain uniqueness in result set.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values to maintain uniqueness in result set.
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                # Case 2: Total sum is too small (total < 0).
                # Move left pointer rightward to increase the sum.
                elif total < 0:
                    left += 1

                # Case 3: Total sum is too large (total > 0).
                # Move right pointer leftward to decrease the sum.
                else:
                    right -= 1

        # Return list of all unique triplets found.
        return result

"""
Algorithm Used: Sorting + Two Pointers Strategy
Key Concepts: Two-Pointer Convergence, Duplicate Skipping, Array Sorting
Time Complexity: O(N^2) - O(N log N) sorting + O(N^2) nested two-pointer search
Space Complexity: O(1) - Constant auxiliary space (excluding Timsort sorting stack O(N))
"""
