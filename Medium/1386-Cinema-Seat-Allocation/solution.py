"""
LeetCode Problem: 1386. Cinema Seat Allocation
Difficulty: Medium
Language: Python
Approach: Hash Map with Bitmasking for Row Seat Reservations
Concepts Used: Array, Hash Table, Bit Manipulation, Bitwise AND / Bitmasking, Greedy

Time Complexity: O(R + M) where R = len(reservedSeats) and M = count of unique reserved rows
Space Complexity: O(M) for hash map of unique reserved rows

Author: Suraj Sawant
"""

class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        Calculates the maximum number of 4-person families that can be seated in a cinema.

        Args:
            n (int): Total number of rows in the cinema (1 to 10^9).
            reservedSeats (List[List[int]]): List of [row, seat] pairs already reserved.

        Returns:
            int: Maximum 4-person family groups that can be seated.
        """

        # Hash map storing bitmasks of reserved seats for rows with at least one reservation.
        rows = {}

        # Store reserved seats for each row as a bitmask (1-indexed converted to 0-indexed bit positions).
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = 0

            # Set the bit corresponding to (seat - 1).
            rows[row] |= 1 << (seat - 1)

        # Every completely unreserved row can seat at most 2 family groups (seats 2-5 and 6-9).
        answer = (n - len(rows)) * 2

        # Define bitmasks for the three potential 4-seat block configurations in a row:
        # Left block: Seats 2, 3, 4, 5  -> bits 1, 2, 3, 4
        left = (1 << 1) | (1 << 2) | (1 << 3) | (1 << 4)   # 2-5
        
        # Middle block: Seats 4, 5, 6, 7 -> bits 3, 4, 5, 6
        middle = (1 << 3) | (1 << 4) | (1 << 5) | (1 << 6) # 4-7
        
        # Right block: Seats 6, 7, 8, 9 -> bits 5, 6, 7, 8
        right = (1 << 5) | (1 << 6) | (1 << 7) | (1 << 8) # 6-9

        # Process each row with reservations using bitwise AND operations.
        for mask in rows.values():

            # A block is available if none of its 4 seats overlap with reserved seats.
            can_left = (mask & left) == 0
            can_middle = (mask & middle) == 0
            can_right = (mask & right) == 0

            # If both left and right blocks are free, we can seat 2 families in this row.
            if can_left and can_right:
                answer += 2

            # Otherwise, if at least one of left, middle, or right blocks is free, we can seat 1 family.
            elif can_left or can_middle or can_right:
                answer += 1

        return answer

"""
Algorithm Used: Bitmask Representation & Bitwise Alignment Checking
Key Concepts: Bitmasking, Fast Overlap Detection (mask & block == 0), Sparse Row Handling
Time Complexity: O(R + M) - Linear in size of reservedSeats array
Space Complexity: O(M) - Auxiliary memory proportional to rows containing reservations
"""
