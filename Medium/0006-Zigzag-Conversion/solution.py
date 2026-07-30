"""
LeetCode Problem: 6. Zigzag Conversion
Difficulty: Medium
Language: Python
Approach: Simulated Row Bouncing Traversal
Concepts Used: String, Simulation, Bucket Pattern, Direction Vector

Time Complexity: O(N)
Space Complexity: O(N)

Author: Suraj Sawant
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        Converts a string into a zigzag pattern across numRows and reads line by line.

        Args:
            s (str): Input string.
            numRows (int): Target number of zigzag rows.

        Returns:
            str: Row-by-row concatenated output string.
        """

        # Guard clause: If numRows is 1 or numRows >= len(s), no zigzag pattern is formed.
        if numRows == 1 or numRows >= len(s):
            return s

        # Allocate an array of numRows empty string buckets to accumulate characters per row.
        rows = [""] * numRows
        # Track active row index (0-indexed).
        current_row = 0
        # Movement direction vector (-1 for upward, +1 for downward).
        # Initialized to -1 so first boundary check flips it to +1 (downward).
        direction = -1

        # Iterate through each character ch in string s.
        for ch in s:
            # Append character to its designated row bucket.
            rows[current_row] += ch

            # Toggle movement direction when hitting top boundary (0) or bottom boundary (numRows - 1).
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1

            # Advance current_row pointer using active direction.
            current_row += direction

        # Concatenate all row buckets into a single final string and return.
        return "".join(rows)

"""
Algorithm Used: Simulated Bouncing Row Traversal
Key Concepts: Bucket Pattern, Oscillating State Direction, String Joining
Time Complexity: O(N) - Single pass through string s of length N
Space Complexity: O(N) - Storage for N characters stored across row buckets
"""
