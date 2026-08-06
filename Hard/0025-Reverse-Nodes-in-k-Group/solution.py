"""
LeetCode Problem: 25. Reverse Nodes in k-Group
Difficulty: Hard
Language: Python
Approach: Iterative Group-by-Group Linked List Reversal
Concepts Used: Linked List, Two Pointers, Group Reversal, Sentinel Node Pattern

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
    def reverseKGroup(self, head, k):
        """
        Reverses nodes of a linked list k at a time and returns its modified head.

        Args:
            head (ListNode): Head node of the singly-linked list.
            k (int): Size of groups to reverse.

        Returns:
            ListNode: Head of the modified linked list.
        """

        # Create dummy sentinel node to simplify head node pointer reassignment.
        dummy = ListNode(0)
        dummy.next = head

        # Pointer tracking the node immediately preceding the current k-group.
        group_prev = dummy

        while True:

            # Locate the k-th node from group_prev.
            kth = group_prev
            for i in range(k):
                kth = kth.next
                # If fewer than k nodes remain, leave remaining nodes as-is and return result.
                if not kth:
                    return dummy.next

            # Store reference to the node following the current k-group.
            group_next = kth.next

            # Reverse nodes within the current k-group:
            # Initialize prev pointer to group_next so that the first node of the group
            # automatically points to the start of the next group after reversal.
            prev = group_next
            curr = group_prev.next

            # Standard in-place linked list reversal loop for k nodes.
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Re-connect group_prev.next to kth (new head of reversed group).
            temp = group_prev.next
            group_prev.next = kth
            
            # Advance group_prev pointer to the tail of newly reversed group (original first node).
            group_prev = temp

"""
Algorithm Used: Iterative Group-by-Group Sub-List Reversal
Key Concepts: Sentinel Dummy Node, K-Node Group Checking, In-Place Reversal, Pointer Linkage
Time Complexity: O(N) - Every node in linked list of length N is traversed a constant number of times
Space Complexity: O(1) - Constant auxiliary memory (nodes re-linked in-place)
"""
