"""
LeetCode Problem: 19. Remove Nth Node From End of List
Difficulty: Medium
Language: Python
Approach: Two Pointers (Fast & Slow Gap Traversal) with Dummy Node
Concepts Used: Linked List, Two Pointers, Sentinel Node Pattern

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
    def removeNthFromEnd(self, head, n):
        """
        Removes the n-th node from the end of a singly-linked list.

        Args:
            head (ListNode): Head node of the singly-linked list.
            n (int): Position from the end of the node to remove (1-indexed).

        Returns:
            ListNode: Head of the modified linked list.
        """

        # Create a dummy sentinel node pointing to head to gracefully handle edge cases
        # such as removing the head node itself (e.g. list of length 1 or removing head).
        dummy = ListNode(0)
        dummy.next = head

        # Initialize fast and slow pointers both starting at the dummy node.
        fast = dummy
        slow = dummy

        # Advance fast pointer n + 1 steps ahead to create a gap of n nodes between fast and slow.
        # This ensures that when fast reaches None (end of list), slow will rest at the node
        # immediately preceding the target node to be deleted.
        for i in range(n + 1):
            fast = fast.next

        # Move both fast and slow pointers forward at equal speed until fast reaches None.
        while fast:
            fast = fast.next
            slow = slow.next

        # Unlink the n-th node from the end by bypassing it: slow.next points to slow.next.next.
        slow.next = slow.next.next

        # Return head of list, skipping the dummy sentinel node.
        return dummy.next

"""
Algorithm Used: Two Pointers (Fast & Slow Pointer Gap Traversal)
Key Concepts: Fixed-Gap Pointer Search, Sentinel Node, In-Place Node Unlinking
Time Complexity: O(N) - Single pass traversal through the linked list of length N
Space Complexity: O(1) - Constant auxiliary memory space
"""
