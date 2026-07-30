"""
LeetCode Problem: 2. Add Two Numbers
Difficulty: Medium
Language: Python
Approach: Simultaneous Linked List Traversal with Carry
Concepts Used: Linked List, Math, Simulation, Sentinel Dummy Node

Time Complexity: O(max(N, M))
Space Complexity: O(max(N, M))

Author: Suraj Sawant
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        Adds two numbers represented as reversed singly-linked lists.

        Args:
            l1 (Optional[ListNode]): Head node of the first number.
            l2 (Optional[ListNode]): Head node of the second number.

        Returns:
            Optional[ListNode]: Head node of the result list representing the sum.
        """
        # Create a dummy sentinel node to simplify list construction without special head checks.
        dummy = ListNode(0)
        # Pointer tracking the current tail of the constructed result linked list.
        current = dummy
        # Holds overflow carry value (0 or 1) carried over to the next digit position.
        carry = 0

        # Continue loop while either list has unprocessed nodes or a carry value remains.
        while l1 or l2 or carry:

            # Extract digit from l1 if node exists, default to 0 for uneven length lists.
            x = l1.val if l1 else 0
            # Extract digit from l2 if node exists, default to 0 for uneven length lists.
            y = l2.val if l2 else 0

            # Calculate total sum for the current digit column including carry.
            total = x + y + carry

            # Compute carry for the next column (e.g. 15 // 10 = 1).
            carry = total // 10

            # Append new node containing single-digit remainder for current column (e.g. 15 % 10 = 5).
            current.next = ListNode(total % 10)

            # Advance current tail pointer to the newly appended node.
            current = current.next

            # Advance input list pointers if nodes exist to process next digits.
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        # Return head of constructed list, skipping the initial placeholder dummy node.
        return dummy.next

"""
Algorithm Used: Simultaneous Linked List Traversal with Carry Propagation
Key Concepts: Dummy Head Pattern, Elementary Math Addition, Pointers
Time Complexity: O(max(N, M)) - Processes both lists in a single pass up to maximum list length
Space Complexity: O(max(N, M)) - Memory for newly constructed output linked list
"""
