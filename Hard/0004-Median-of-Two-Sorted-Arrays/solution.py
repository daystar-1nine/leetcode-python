"""
LeetCode Problem: 4. Median of Two Sorted Arrays
Difficulty: Hard
Language: Python
Approach: Binary Search Partitioning
Concepts Used: Array, Binary Search, Divide and Conquer, Infinity Guards

Time Complexity: O(log(min(M, N)))
Space Complexity: O(1)

Author: Suraj Sawant
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        Finds the median of two combined sorted arrays in O(log(min(M, N))) time.

        Args:
            nums1 (List[int]): First sorted array of size m.
            nums2 (List[int]): Second sorted array of size n.

        Returns:
            float: Median value of combined sorted elements.
        """

        # Always perform binary search on smaller array to optimize runtime to O(log(min(m, n)))
        # and prevent negative index partition errors for array j.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        # Binary search boundary initialization on nums1 range [0, m].
        left = 0
        right = m
        # Calculate size of combined left partition half (rounded up for odd lengths).
        half = (m + n + 1) // 2

        # Binary search loop for partition cut i in nums1.
        while left <= right:
            # i is partition cut index in nums1, j is partition cut index in nums2.
            i = (left + right) // 2
            j = half - i

            # Use infinity sentinels for out-of-bound cuts at array edges (0 or m/n).
            left1 = float("-inf") if i == 0 else nums1[i - 1]
            right1 = float("inf") if i == m else nums1[i]

            left2 = float("-inf") if j == 0 else nums2[j - 1]
            right2 = float("inf") if j == n else nums2[j]

            # Check if partition is valid: left1 <= right2 AND left2 <= right1.
            if left1 <= right2 and left2 <= right1:
                # If combined length is odd, median is the maximum element of the left partition.
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))
                # If combined length is even, median is average of max(left) and min(right).
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2.0

            # Partition i is too far right (left1 > right2), shift binary search left.
            elif left1 > right2:
                right = i - 1
            # Partition i is too far left (left2 > right1), shift binary search right.
            else:
                left = i + 1

        return 0.0

"""
Algorithm Used: Binary Search Partitioning
Key Concepts: Binary Search, Sentinel Values, Array Partitions
Time Complexity: O(log(min(M, N))) - Logarithmic search on smaller array
Space Complexity: O(1) - Constant auxiliary space
"""
