"""
LeetCode Problem: 24. Swap Nodes in Pairs
Difficulty: Medium
Language: Python
Approach: Iterative In-Place Pointer Swapping with Sentinel Dummy Node
Concepts Used: Linked List, Two Pointers, Sentinel Node Pattern, In-Place Re-linking

Time Complexity: O(N)
Space Complexity: O(1)

Author: Suraj Sawant
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        Swaps every two adjacent nodes in a singly-linked list and returns its head.

        Args:
            head (ListNode): Head node of the singly-linked list.

        Returns:
            ListNode: Head node of the pairwise-swapped linked list.
        """

        # Create a dummy sentinel node to simplify head node pointer reassignment
        # and prevent edge case checks when swapping the first two nodes.
        dummy = ListNode(0)
        dummy.next = head

        # Pointer to track the node immediately preceding the current pair being swapped.
        prev = dummy

        # Traverse the list as long as there is a valid adjacent pair (first and second nodes exist).
        while prev.next and prev.next.next:

            # Identify the two nodes in the current pair to swap.
            first = prev.next
            second = first.next

            # Execute 3-step pointer re-linking swap:
            # 1. Point first node's next to the start of the next pair (second.next).
            first.next = second.next
            
            # 2. Point second node's next back to the first node (reversing pair order).
            second.next = first
            
            # 3. Connect previous node's next to second node (new head of this pair).
            prev.next = second

            # Advance prev pointer to the first node (which is now the second node of the swapped pair).
            prev = first

        # Return head of the modified linked list, skipping the dummy sentinel node.
        return dummy.next

"""
Algorithm Used: Iterative In-Place Pair Swapping
Key Concepts: Sentinel Dummy Node, 3-Step Pointer Re-linking, In-Place Mutation
Time Complexity: O(N) - Single linear pass over linked list of length N
Space Complexity: O(1) - Constant auxiliary space (swapping node pointers in-place)
"""
