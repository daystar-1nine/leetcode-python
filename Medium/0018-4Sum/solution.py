"""
LeetCode Problem: 18. 4Sum
Difficulty: Medium
Language: Python
Approach: Sorting + Nested Loops with Two Pointers Convergence
Concepts Used: Array, Two Pointers, Sorting, Duplicate Elimination

Time Complexity: O(N^3)
Space Complexity: O(1) auxiliary space (O(N) for sorting stack memory)

Author: Suraj Sawant
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        Finds all unique quadruplets in nums that sum to target.

        Args:
            nums (List[int]): Array of integers.
            target (int): Target sum integer.

        Returns:
            List[List[int]]: List of unique quadruplets [nums[i], nums[j], nums[k], nums[l]].
        """

        # Sort the input array to enable Two Pointers search and duplicate skipping.
        nums.sort()
        n = len(nums)
        result = []

        # Outer loop fixing the first element nums[i].
        # Runs up to n - 3 to leave room for j, left, and right pointers.
        for i in range(n - 3):

            # Skip duplicate first numbers to prevent duplicate quadruplets starting with nums[i].
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Second loop fixing the second element nums[j].
            # Runs up to n - 2 to leave room for left and right pointers.
            for j in range(i + 1, n - 2):

                # Skip duplicate second numbers for the active i fixed boundary.
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Initialize two pointers for remaining sub-array nums[j+1 ... n-1].
                left = j + 1
                right = n - 1

                # Two Pointers search loop for nums[left] + nums[right] == target - nums[i] - nums[j].
                while left < right:

                    # Compute total sum of current 4-element quadruplet.
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    # Case 1: Matching quadruplet sum found (total == target).
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # Advance both pointers inward.
                        left += 1
                        right -= 1

                        # Skip duplicate third numbers (left pointer).
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        # Skip duplicate fourth numbers (right pointer).
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    # Case 2: Total sum is less than target, move left pointer rightward to increase sum.
                    elif total < target:
                        left += 1

                    # Case 3: Total sum is greater than target, move right pointer leftward to decrease sum.
                    else:
                        right -= 1

        # Return complete list of unique quadruplets.
        return result

"""
Algorithm Used: Sorting + Double Loop with Two Pointers Search
Key Concepts: Multi-Pointer Convergence, Duplicate Elimination, Array Pre-Sorting
Time Complexity: O(N^3) - O(N log N) sorting + O(N^3) nested loops with two pointers
Space Complexity: O(1) - Constant auxiliary memory space (excluding result array)
"""
