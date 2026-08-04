# 0023. Merge k Sorted Lists

![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red?style=for-the-badge)
![Topic: Linked List](https://img.shields.io/badge/Topic-Linked%20List-blue?style=for-the-badge)
![Topic: Divide and Conquer](https://img.shields.io/badge/Topic-Divide%20and%20Conquer-orange?style=for-the-badge)
![Topic: Merge Sort](https://img.shields.io/badge/Topic-Merge%20Sort-purple?style=for-the-badge)

---

## 1. Problem Information

- **Problem Name:** Merge k Sorted Lists
- **LeetCode Number:** 23
- **Difficulty:** Hard
- **Tags:** Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort
- **Language Used:** Python
- **Problem Link:** [LeetCode #23 - Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

---

## 2. Problem Overview

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

### Input & Output Specifications
- **Input:** `lists`: An array of $k$ sorted singly-linked list heads ($0 \le k \le 10^4$).
- **Output:** Head of the merged sorted singly-linked list.
- **Constraints:**
  - $0 \le \text{lists}[i].\text{length} \le 500$
  - $-10^4 \le \text{lists}[i][j] \le 10^4$
  - `lists[i]` is sorted in ascending order.
  - Total sum of nodes across all lists $\le 10^4$.

### Examples
- **Example 1:**
  - **Input:** `lists = [[1,4,5],[1,3,4],[2,6]]`
  - **Output:** `[1,1,2,3,4,4,5,6]`
  - **Explanation:** The linked-lists are:
    ```text
    [
      1 -> 4 -> 5,
      1 -> 3 -> 4,
      2 -> 6
    ]
    merging them into one sorted list:
    1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
    ```
- **Example 2:**
  - **Input:** `lists = []` $\rightarrow$ **Output:** `[]`
- **Example 3:**
  - **Input:** `lists = [[]]` $\rightarrow$ **Output:** `[]`

### Real-World Intuition
Imagine a distributed log aggregation engine (like Kafka or Elasticsearch) receiving $K$ independent sorted log streams from $K$ servers. To output a single unified chronological timeline of all events across the cluster, the engine merges the streams logarithmically in pairs ($\log K$ depth) to minimize stream comparison overhead.

---

## 3. Intuition

> [!TIP]
> **Divide and Conquer Reduction:** Pair up the $K$ lists and merge them pairwise using LeetCode #21 (`mergeTwoLists`). Repeat until only 1 list remains!

### Why Pairwise Merging Beats Sequential Merging:
1. **Sequential Merging (Bad):** Merge list 1 with list 2, then result with list 3, then result with list 4...
   - List 1 nodes get processed $K-1$ times!
   - Time Complexity: $\mathcal{O}(N \cdot K)$ (Time Limit Exceeded for large $K$).
2. **Divide and Conquer Pairwise Merging (Optimal):**
   - Round 1: Merge pairs $(0,1), (2,3), (4,5) \dots \rightarrow K/2$ lists.
   - Round 2: Merge pairs $(0,1), (2,3) \dots \rightarrow K/4$ lists.
   - ...
   - Total Rounds: $\log_2 K$.
   - In each round, every node in the entire dataset ($N$ total nodes) is processed at most once.
   - Total Time Complexity: $\mathcal{O}(N \log K)$!

---

## 4. Thought Process

```mermaid
flowchart TD
    A[Start: Input lists array] --> B{Is lists empty?}
    B -- Yes --> C[Return None]
    B -- No --> D{Is len lists > 1?}
    D -- Yes --> E[Initialize merged = empty list]
    E --> F[Loop i from 0 to len lists with step 2]
    F --> G[l1 = lists[i]]
    G --> H{Is i + 1 < len lists?}
    H -- Yes --> I[l2 = lists[i+1]]
    H -- No --> J[l2 = None]
    I --> K[merged.append mergeTwoLists l1, l2]
    J --> K
    K --> L{More pairs in loop?}
    L -- Yes --> F
    L -- No --> M[Update lists = merged]
    M --> D
    D -- No --> N[Return lists[0]]
```

1. **Guard Clause:**
   - If `not lists: return None`.

2. **Logarithmic Reduction Loop:**
   - While `len(lists) > 1`:
     - Create an empty list `merged = []`.
     - Step through `lists` in increments of 2 (`range(0, len(lists), 2)`):
       - `l1 = lists[i]`
       - `l2 = lists[i + 1]` if `i + 1 < len(lists)` else `None`
       - Append `self.mergeTwoLists(l1, l2)` to `merged`.
     - Set `lists = merged`.

3. **Return Single Merged Head:**
   - Return `lists[0]`.

---

## 5. Concepts Used

### 1. Divide and Conquer Logarithmic Tree Reduction
- **What it is:** Halving problem size $K \rightarrow K/2 \rightarrow K/4 \dots \rightarrow 1$ at every reduction level.
- **Why it is used here:** Reduces node re-traversal depth from $K$ down to $\log_2 K$.
- **Future applications:** Merge Sort, Segment Tree Construction, FFT.

### 2. Pairwise Linked List Merging
- **What it is:** Using the two-pointer sentinel technique (from LC #21) to splice two pre-sorted lists in $\mathcal{O}(N_1 + N_2)$ time.
- **Why it is used here:** Reuses optimal 2-list merging as the primitive building block for $K$-list merging.
- **Future applications:** Sort List, Inorder Successor in BST.

---

## 6. Algorithm Used

### Divide and Conquer Pairwise Merging

- **Algorithm Category:** Linked List / Divide and Conquer / Sorting
- **Why selected:** Achieves theoretical minimum time complexity $\mathcal{O}(N \log K)$ with $\mathcal{O}(1)$ auxiliary space without heap memory overhead.
- **Time Complexity:** $\mathcal{O}(N \log K)$
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

---

## 7. Code Walkthrough

Below is the line-by-line breakdown of the submitted solution:

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        # Line 15-16: Guard Clause for Empty Input Array
        if not lists:
            return None

        # Line 18: Logarithmic Pairwise Reduction Loop
        while len(lists) > 1:

            merged = []

            # Line 22: Step through lists in pairs (step size 2)
            for i in range(0, len(lists), 2):

                l1 = lists[i]

                # Line 26-29: Safe boundary check for adjacent list l2
                if i + 1 < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None

                # Line 31: Merge pair and append to merged list
                merged.append(self.mergeTwoLists(l1, l2))

            # Line 33: Replace lists array with newly merged pairs
            lists = merged

        # Line 35: Return single remaining merged head
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        """
        Helper function to merge 2 sorted lists (LC #21 logic)
        """
        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1:
            current.next = l1
        else:
            current.next = l2

        return dummy.next
```

---

## 8. Dry Run

Let's dry run for `lists = [[1,4,5], [1,3,4], [2,6]]` ($K=3$, $N=8$).

### Initial State
- `lists = [L1, L2, L3]` where:
  - `L1 = 1 -> 4 -> 5`
  - `L2 = 1 -> 3 -> 4`
  - `L3 = 2 -> 6`

### Round 1 (`len(lists) = 3 > 1`):
- `i = 0`: `mergeTwoLists(L1, L2)` $\rightarrow$ `M1 = 1 -> 1 -> 3 -> 4 -> 4 -> 5`.
- `i = 2`: `mergeTwoLists(L3, None)` $\rightarrow$ `M2 = 2 -> 6`.
- New state: `lists = [M1, M2]` (`len(lists) = 2`).

### Round 2 (`len(lists) = 2 > 1`):
- `i = 0`: `mergeTwoLists(M1, M2)` $\rightarrow$ `M3 = 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6`.
- New state: `lists = [M3]` (`len(lists) = 1`).

### Output
Loop terminates. Returns `lists[0]` $\rightarrow$ **`[1, 1, 2, 3, 4, 4, 5, 6]`**.

---

## 9. Complexity Analysis

### Time Complexity: $\mathcal{O}(N \log K)$
- Where $N$ is total nodes across all $K$ lists, and $K$ is the number of linked lists.
- The `while` loop runs $\log_2 K$ times.
- In each round, every node in $N$ total nodes is traversed at most once during `mergeTwoLists`.
- Total time complexity: $\mathcal{O}(N \log K)$.

### Space Complexity: $\mathcal{O}(1)$ Auxiliary Space
- Nodes are spliced in-place by updating `next` pointer references.
- Temporary `merged` list allocations per round use $\mathcal{O}(K)$ pointer references, which can be further optimized to $\mathcal{O}(1)$ with in-place pointer step manipulation.
- Overall auxiliary space: $\mathcal{O}(1)$.

---

## 10. Edge Cases

| Edge Case Scenario | Input Example | Behavior & Output | How Code Handles It |
| :--- | :--- | :--- | :--- |
| **Empty Input Array** | `lists = []` | Output: `None` | `if not lists: return None` triggers immediately. |
| **Array of Empty Lists**| `lists = [[], []]` | Output: `None` | `mergeTwoLists(None, None)` returns `None`. |
| **Odd Number of Lists** | `lists = [L1, L2, L3]` | Output: Merged list | Unpaired last list `L3` is merged with `None` safely. |
| **Single List Input** | `lists = [[1, 2, 3]]` | Output: `[1, 2, 3]` | `len(lists) > 1` is False, returns `lists[0]` immediately. |

---

## 11. Alternative Approaches

### Approach 1: Min-Heap / Priority Queue ($\mathcal{O}(N \log K)$ Time, $\mathcal{O}(K)$ Auxiliary Space)
- **Idea:** Push head of all $K$ lists into a min-heap. Pop smallest node, attach to result, and push `node.next` into heap.
- **Drawback:** In Python 2/3, pushing raw `ListNode` objects into `heapq` fails unless wrapped in tuples `(val, id(node), node)` to avoid object comparison errors.

### Approach 2: Collect All Values & Sort ($\mathcal{O}(N \log N)$ Time, $\mathcal{O}(N)$ Space)
- **Idea:** Traverse all lists, append all values to a Python list, sort array, and reconstruct linked list.
- **Drawback:** Requires $\mathcal{O}(N)$ extra memory allocations and completely ignores that input lists are already sorted.

### Approach 3: Divide and Conquer Pairwise Merging (User's Solution - Recommended)
- **Idea:** Logarithmic pairwise list reduction.
- **Complexity:** $\mathcal{O}(N \log K)$ time, $\mathcal{O}(1)$ auxiliary space.
- **Why Optimal:** Theoretical minimum time, zero extra node allocation, clean and elegant code.

---

## 12. Common Mistakes

> [!WARNING]
> 1. **Sequential Merging ($\mathcal{O}(N \cdot K)$):** Merging list 0 with 1, then result with 2, then result with 3... causes Time Limit Exceeded (TLE) for $K = 10^4$.
> 2. **Index Overflow on Odd $K$:** Not checking `if i + 1 < len(lists)` causes `IndexError` when $K$ is odd.
> 3. **Heap Comparison Crashes:** In Python, pushing `(val, node)` into `heapq` crashes when two nodes have identical `val` because `ListNode` has no `__lt__` operator implemented.

---

## 13. Interview Questions

1. **Q: Why is Divide and Conquer ($\mathcal{O}(N \log K)$) vastly superior to Sequential Merging ($\mathcal{O}(N \cdot K)$)?**
   - *A:* In sequential merging, early nodes are re-traversed $K$ times. In Divide and Conquer, each node is processed only $\log_2 K$ times because the number of lists is halved at every level.

2. **Q: How does this approach compare to the Min-Heap approach?**
   - *A:* Both run in $\mathcal{O}(N \log K)$ time. Divide and Conquer requires $\mathcal{O}(1)$ auxiliary space (in-place splicing), whereas Min-Heap requires $\mathcal{O}(K)$ heap memory.

3. **Q: Can we implement Divide and Conquer recursively?**
   - *A:* Yes! `mergeKLists(lists, left, right)` recursively splits list array in half (`mid = (left + right)//2`) and merges left half and right half using `mergeTwoLists`.

---

## 14. Similar Problems

- **Easy:**
  - [LeetCode #21 - Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- **Medium:**
  - [LeetCode #148 - Sort List](https://leetcode.com/problems/sort-list/)
  - [LeetCode #632 - Smallest Range Covering Elements from K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/)

---

## 15. Learning Summary

- **Pattern Recognized:** Divide and Conquer Logarithmic List Reduction.
- **Pairwise Merge:** Halving number of active lists $K \rightarrow K/2 \rightarrow \dots \rightarrow 1$ in $\log_2 K$ rounds.
- **In-Place Efficiency:** Splicing nodes in $\mathcal{O}(1)$ auxiliary space.

---

## 16. Optimization Notes

Your solution is **100% optimal** ($\mathcal{O}(N \log K)$ Time, $\mathcal{O}(1)$ Auxiliary Space). It is clean, readable, and represents the gold-standard hard problem solution!
