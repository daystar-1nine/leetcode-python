"""
LeetCode Problem: 3345. Smallest Divisible Digit Product I
Difficulty: Easy
Language: Python
Approach: Linear Search Simulation with Digit Product Computation
Concepts Used: Math, Simulation, Digit Extraction, Modulo Arithmetic

Time Complexity: O(1) - Bounded by at most 10 iterations
Space Complexity: O(1)

Author: Suraj Sawant
"""

class Solution(object):
    def smallestNumber(self, n, t):
        """
        Finds the smallest number greater than or equal to n whose digit product is divisible by t.

        Args:
            n (int): Starting integer value (1 <= n <= 100).
            t (int): Target divisor integer (1 <= t <= 10).

        Returns:
            int: Smallest integer >= n with digit product divisible by t.
        """

        def get_digit_product(num):
            """
            Helper function to compute the product of digits of a given number.

            Args:
                num (int): Input integer.

            Returns:
                int: Product of all digits in num.
            """
            product = 1
            # Convert number to string to extract digits individually.
            for digit in str(num):
                product *= int(digit)
            return product

        # Start search from the input integer n.
        curr = n

        # Linearly test consecutive integers until a valid digit product is found.
        # Since any number with digit '0' has a digit product of 0 (which is divisible by all t),
        # this loop will terminate in at most 10 iterations.
        while True:
            # Check if the product of digits of curr is divisible by t.
            if get_digit_product(curr) % t == 0:
                return curr
            
            # Increment to check the next integer candidate.
            curr += 1

"""
Algorithm Used: Linear Search Simulation with Digit Product Computation
Key Concepts: Digit Multiplication, Modulo Divisibility, Constant Bounded Search
Time Complexity: O(1) - Search space is bounded by at most 10 consecutive numbers
Space Complexity: O(1) - Constant auxiliary memory space
"""
