"""
LeetCode Problem: 23. Merge k Sorted Lists
Difficulty: Hard
Language: Python
Approach: Divide and Conquer (Pairwise Logarithmic Merging)
Concepts Used: Linked List, Divide and Conquer, Merge Sort, Two Pointers

Time Complexity: O(N log K)
Space Complexity: O(1) auxiliary space (O(K) list space per reduction level)

Author: Suraj Sawant
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        Merges k sorted linked lists into one single sorted linked list using Divide and Conquer.

        Args:
            lists (List[Optional[ListNode]]): List of k sorted linked list heads.

        Returns:
            Optional[ListNode]: Head of merged sorted linked list.
        """

        # Guard Clause: If input list array is empty, return None immediately.
        if not lists:
            return None

        # Repeat pairwise merging until only one single merged linked list remains in lists array.
        # This logarithmic reduction reduces number of lists from K -> K/2 -> K/4 ... -> 1 in O(log K) steps.
        while len(lists) > 1:

            merged = []

            # Pairwise iteration with step size of 2 across active list heads.
            for i in range(0, len(lists), 2):

                l1 = lists[i]

                # Fetch adjacent list l2 if available within bounds, otherwise pair with None.
                if i + 1 < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None

                # Merge active pair (l1, l2) and store merged result in temporary list.
                merged.append(self.mergeTwoLists(l1, l2))

            # Update lists array with newly merged pairs for next logarithmic reduction round.
            lists = merged

        # Return single remaining head node.
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        """
        Helper function to merge two sorted singly-linked lists into one sorted list.

        Args:
            l1 (Optional[ListNode]): Head of first sorted list.
            l2 (Optional[ListNode]): Head of second sorted list.

        Returns:
            Optional[ListNode]: Head of merged list.
        """
        # Sentinel dummy node to handle head node pointer assignment smoothly.
        dummy = ListNode(0)
        current = dummy

        # Merge nodes in ascending order by comparing current values of l1 and l2.
        while l1 and l2:

            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        # Attach any remaining un-exhausted node chain.
        if l1:
            current.next = l1
        else:
            current.next = l2

        return dummy.next

"""
Algorithm Used: Divide and Conquer Pairwise Merging
Key Concepts: Logarithmic List Reduction, Pairwise Two-Pointer Merge, Sentinel Node
Time Complexity: O(N log K) - N total nodes across all K lists, log K reduction rounds
Space Complexity: O(1) auxiliary space (nodes spliced in-place)
"""
