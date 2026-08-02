"""
LeetCode Problem: 16. 3Sum Closest
Difficulty: Medium
Language: Python
Approach: Sorting + Two Pointers Distance Minimization
Concepts Used: Array, Two Pointers, Sorting, Distance Optimization

Time Complexity: O(N^2)
Space Complexity: O(1) auxiliary space (O(N) sorting memory depending on language)

Author: Suraj Sawant
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        Finds three integers in nums such that the sum is closest to target.

        Args:
            nums (List[int]): Array of integers.
            target (int): Target integer value.

        Returns:
            int: Sum of the three integers closest to target.
        """

        # Sort the array to enable Two Pointers directional convergence based on target comparison.
        nums.sort()
        n = len(nums)

        # Initialize closest tracker with sum of first three elements.
        closest = nums[0] + nums[1] + nums[2]

        # Fix the first element nums[i] and use Two Pointers for the remaining sub-array.
        for i in range(n - 2):

            # Initialize left and right pointers for sub-array nums[i+1 ... n-1].
            left = i + 1
            right = n - 1

            # Two Pointers search loop.
            while left < right:

                # Calculate sum of current triplet.
                current = nums[i] + nums[left] + nums[right]

                # If current triplet sum is closer to target than closest seen so far, update closest.
                if abs(current - target) < abs(closest - target):
                    closest = current

                # If current sum equals target, distance is 0 (optimal possible match), return immediately.
                if current == target:
                    return current

                # If current sum is less than target, move left pointer rightward to increase sum.
                elif current < target:
                    left += 1

                # If current sum is greater than target, move right pointer leftward to decrease sum.
                else:
                    right -= 1

        # Return closest sum found across all evaluated triplets.
        return closest

"""
Algorithm Used: Sorting + Two Pointers Distance Minimization
Key Concepts: Two Pointers Convergence, Distance Minimization, Array Sorting
Time Complexity: O(N^2) - O(N log N) sorting + O(N^2) nested two-pointer search
Space Complexity: O(1) - Constant auxiliary memory space
"""
