"""
LeetCode Problem: 21. Merge Two Sorted Lists
Difficulty: Easy
Language: Python
Approach: Iterative Two-Pointer Merging with Sentinel Dummy Node
Concepts Used: Linked List, Two Pointers, Sentinel Node Pattern

Time Complexity: O(N + M)
Space Complexity: O(1)

Author: Suraj Sawant
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        Merges two sorted singly-linked lists into one sorted list.

        Args:
            list1 (Optional[ListNode]): Head of first sorted linked list.
            list2 (Optional[ListNode]): Head of second sorted linked list.

        Returns:
            Optional[ListNode]: Head of merged sorted linked list.
        """

        # Create a dummy sentinel node to simplify head node linking and avoid special null checks.
        dummy = ListNode(0)
        
        # Pointer to track the tail of the newly merged linked list.
        current = dummy

        # Traverse both lists simultaneously while elements remain in both list1 and list2.
        while list1 and list2:

            # Compare the values of the active head nodes of list1 and list2.
            # Splice the smaller node into the merged list to maintain ascending order.
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            # Advance the tail pointer of the merged list.
            current = current.next

        # If one list is exhausted before the other, attach all remaining nodes of the non-empty list.
        # Since input lists are already sorted, the remaining chain is naturally in sorted order.
        if list1:
            current.next = list1
        else:
            current.next = list2

        # Return head of the merged sorted list, skipping the initial dummy node.
        return dummy.next

"""
Algorithm Used: Iterative Two-Pointer Merging
Key Concepts: Two Pointers Comparison, Dummy Sentinel Node, In-Place Pointer Splicing
Time Complexity: O(N + M) - N and M are the lengths of list1 and list2 respectively
Space Complexity: O(1) - Constant auxiliary memory space (splicing existing nodes in-place)
"""
