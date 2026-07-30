# 0002. Add Two Numbers

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)
![Topic: Linked List](https://img.shields.io/badge/Topic-Linked%20List-blue?style=for-the-badge)
![Topic: Math](https://img.shields.io/badge/Topic-Math-green?style=for-the-badge)
![Topic: Simulation](https://img.shields.io/badge/Topic-Simulation-purple?style=for-the-badge)

---

## 1. Problem Information

- **Problem Name:** Add Two Numbers
- **LeetCode Number:** 2
- **Difficulty:** Medium
- **Tags:** Linked List, Math, Simulation, Recursion
- **Language Used:** Python
- **Problem Link:** [LeetCode #2 - Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

---

## 2. Problem Overview

You are given two **non-empty** singly linked lists representing two non-negative integers. The digits are stored in **reverse order**, such that each node contains a single digit. Add the two numbers and return the sum as a new linked list.

### Input & Output Specifications
- **Input:**
  - `l1`: Head of the first singly-linked list.
  - `l2`: Head of the second singly-linked list.
- **Output:** Head of the new singly-linked list representing the sum.
- **Constraints:**
  - The number of nodes in each linked list is in the range $[1, 100]$.
  - $0 \le \text{Node.val} \le 9$
  - It is guaranteed that the list represents a number that does not contain leading zeros, except the number `0` itself.

### Examples
- **Example 1:**
  ```text
  l1: (2) -> (4) -> (3)   (represents 342)
  l2: (5) -> (6) -> (4)   (represents 465)
  ----------------------------------------
  Sum: (7) -> (0) -> (8)   (represents 807)
  ```
  - **Input:** `l1 = [2,4,3]`, `l2 = [5,6,4]`
  - **Output:** `[7,0,8]` (Explanation: $342 + 465 = 807$)

- **Example 2:**
  - **Input:** `l1 = [0]`, `l2 = [0]`
  - **Output:** `[0]`

- **Example 3:**
  - **Input:** `l1 = [9,9,9,9,9,9,9]`, `l2 = [9,9,9,9]`
  - **Output:** `[8,9,9,9,0,0,0,1]`

### Real-World Intuition
This problem simulates **BigInteger / Arbitrary Precision Arithmetic**. Standard computer hardware primitive types (like `uint64`) overflow when dealing with 100-digit numbers. Storing digits in a reversed linked list allows us to perform addition from the least significant digit (ones place) upwards, mimicking standard long addition taught in grade school!

---

## 3. Intuition

> [!TIP]
> **Key Advantage:** Digits stored in reverse order mean `head` points to the least significant digit (ones place)!

When adding numbers manually on paper:
1. Start at the rightmost column (ones place).
2. Add digits together plus any carried value from the previous column.
3. Keep the single-digit remainder (`sum % 10`) for the current position.
4. Pass the overflow carry (`sum // 10`) to the next higher digit column.

Since `l1` and `l2` already begin at the ones place, we can traverse both lists simultaneously, adding corresponding digits and maintaining a `carry` variable across loop iterations.

Using a **Dummy Head Node** (`dummy = ListNode(0)`) simplifies node insertions so we do not need complex conditional branches for creating the initial list head.

---

## 4. Thought Process

```mermaid
flowchart TD
    A[Start: Input l1, l2] --> B[Create dummy = ListNode(0), current = dummy, carry = 0]
    B --> C{Is l1 != None or l2 != None or carry > 0?}
    C -- No --> D[Return dummy.next]
    C -- Yes --> E[Extract x = l1.val if l1 else 0]
    E --> F[Extract y = l2.val if l2 else 0]
    F --> G[Calculate total = x + y + carry]
    G --> H[Update carry = total // 10]
    H --> I[Create current.next = ListNode(total % 10)]
    I --> J[Advance current = current.next]
    J --> K[Advance l1 = l1.next if l1 exists]
    K --> L[Advance l2 = l2.next if l2 exists]
    L --> C
```

1. **Setup Sentinel Node & State:**
   - `dummy`: Dummy head node to anchor the result list.
   - `current`: Pointer tracking the tail of our growing result list.
   - `carry`: Integer tracking overflow value carried over to the next column.

2. **Unified Loop Condition (`while l1 or l2 or carry`):**
   - Combining `l1`, `l2`, and `carry` in a single loop condition gracefully handles:
     - Lists of different lengths (e.g. 5 digits + 2 digits).
     - A remaining carry after both lists have been fully traversed (e.g. $99 + 1 = 100$).

3. **Digit Extraction & Carry Mechanics:**
   - Extract `x = l1.val` if `l1` is valid, else `0`.
   - Extract `y = l2.val` if `l2` is valid, else `0`.
   - Compute `total = x + y + carry`.
   - New `carry = total // 10`.
   - Attach new node `current.next = ListNode(total % 10)`.

4. **Pointer Progression:**
   - Advance `current = current.next`.
   - Advance `l1 = l1.next` if `l1` is not `None`.
   - Advance `l2 = l2.next` if `l2` is not `None`.

5. **Return Result:**
   - Return `dummy.next` (skipping the dummy placeholder).

---

## 5. Concepts Used

### 1. Dummy Head Pattern
- **What it is:** A dummy/placeholder node allocated at the beginning of a linked list construction.
- **Why it is used here:** Eliminates edge-case checks for initializing the list `head` on step 1.
- **Future applications:** Merge Two Sorted Lists, Partition List, Reverse Linked List II.

### 2. Elementary Long Addition (Carry Propagation)
- **What it is:** Column-by-column digit addition utilizing modulo (`% 10`) for single-digit storage and integer division (`// 10`) for carry propagation.
- **Why it is used here:** Performs accurate arbitrary-precision addition without converting to standard numeric primitives.
- **Future applications:** Add Binary, Multiply Strings, Plus One.

---

## 6. Algorithm Used

### Simultaneous Linked List Traversal with Carry

- **Algorithm Category:** Linked List / Math Simulation
- **Why selected:** Runs in single-pass linear time $\mathcal{O}(\max(N, M))$ and handles lists of arbitrary length up to 100 digits without integer overflow.
- **Time Complexity:** $\mathcal{O}(\max(N, M))$
- **Space Complexity:** $\mathcal{O}(\max(N, M))$

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
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Line 15-17: Sentinel Setup
        # Create dummy node to anchor the result list.
        # current points to the latest node in the result list.
        # carry holds integer overflow (0 or 1).
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # Line 19: Unified Loop
        # Continue while l1 has nodes, OR l2 has nodes, OR a carry remains to be added.
        while l1 or l2 or carry:

            # Line 21-22: Safe Value Extraction
            # Extract digit from l1 if node exists, otherwise default to 0.
            x = l1.val if l1 else 0
            # Extract digit from l2 if node exists, otherwise default to 0.
            y = l2.val if l2 else 0

            # Line 24: Total Column Sum
            total = x + y + carry

            # Line 26: Update Carry for Next Position (e.g. 15 // 10 = 1)
            carry = total // 10

            # Line 28: Append New Digit Node (e.g. 15 % 10 = 5)
            current.next = ListNode(total % 10)

            # Line 30: Advance Current Tail Pointer
            current = current.next

            # Line 32-36: Advance Input List Pointers if Nodes Exist
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        # Line 38: Return Head of Constructed Linked List (Skipping Dummy Node)
        return dummy.next
```

---

## 8. Dry Run

Let's dry run for `l1 = [2, 4, 3]` ($342$) and `l2 = [5, 6, 4]` ($465$).

### Initial State
- `dummy = ListNode(0)`, `current = dummy`, `carry = 0`.
- `l1.val = 2`, `l2.val = 5`.

### Step-by-Step Execution

| Iteration | `l1.val` | `l2.val` | `carry` (In) | `total` ($x+y+\text{carry}$) | `carry` (Out) | Node Value (`total % 10`) | Result List State | Next `l1` | Next `l2` |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: | :---: |
| **1** | `2` | `5` | `0` | $2 + 5 + 0 = 7$ | `0` | `7` | `(0) -> (7)` | `[4, 3]` | `[6, 4]` |
| **2** | `4` | `6` | `0` | $4 + 6 + 0 = 10$ | `1` | `0` | `(0) -> (7) -> (0)` | `[3]` | `[4]` |
| **3** | `3` | `4` | `1` | $3 + 4 + 1 = 8$ | `0` | `8` | `(0) -> (7) -> (0) -> (8)` | `None` | `None` |

### Loop Termination Check
`l1 is None`, `l2 is None`, `carry == 0` $\rightarrow$ Loop terminates.

### Result
Returns `dummy.next` $\rightarrow$ **`[7, 0, 8]`** (represents $807$).

---

## 9. Complexity Analysis

### Time Complexity: $\mathcal{O}(\max(N, M))$
- Where $N$ is the number of nodes in `l1` and $M$ is the number of nodes in `l2`.
- The loop runs $\max(N, M)$ times (or $\max(N, M) + 1$ if there is a final carry).
- Each step performs constant $\mathcal{O}(1)$ operations (arithmetic, node creation, pointer movement).

### Space Complexity: $\mathcal{O}(\max(N, M))$
- **Auxiliary Memory:** The algorithm creates a new linked list with length at most $\max(N, M) + 1$.
- **Extra Variables:** Uses $\mathcal{O}(1)$ primitive integers (`x`, `y`, `total`, `carry`, `current`).

---

## 10. Edge Cases

| Edge Case Scenario | Input Example | Behavior & Output | How Code Handles It |
| :--- | :--- | :--- | :--- |
| **Unequal List Lengths** | `l1 = [9,9]`, `l2 = [1]` | Output: `[0,0,1]` ($99 + 1 = 100$) | Non-existent node defaults value to `0` using `x = l1.val if l1 else 0`. |
| **Final Carry Remaining** | `l1 = [5]`, `l2 = [5]` | Output: `[0, 1]` ($5 + 5 = 10$) | `while ... or carry:` condition ensures extra node is created for carry `1`. |
| **Single Zeros** | `l1 = [0]`, `l2 = [0]` | Output: `[0]` | Loop runs once, `total = 0`, outputs `[0]`. |
| **Long List + Short List** | `l1 = [9,9,9,9]`, `l2 = [1]` | Output: `[0,0,0,0,1]` | `carry` cascades through remaining nodes smoothly. |

---

## 11. Alternative Approaches

### Approach 1: Convert to BigInteger and Back ($\mathcal{O}(N + M)$ Time, $\mathcal{O}(N + M)$ Space)
- **Idea:** Traverse `l1` to build integer $N_1$, traverse `l2` to build integer $N_2$, compute $S = N_1 + N_2$, and construct a new linked list from digits of $S$.
- **Drawback:** In languages like C++/Java, converting 100 digits exceeds standard 64-bit integer limits (`long long` / `uint64_t`).

### Approach 2: Simultaneous Traversal with Carry (User's Solution - Optimal)
- **Idea:** Traverse both lists node-by-node and simulate addition with carry.
- **Complexity:** $\mathcal{O}(\max(N, M))$ time, $\mathcal{O}(\max(N, M))$ space.
- **Why Optimal:** Handles arbitrary length inputs efficiently in a single pass without numeric overflow.

---

## 12. Common Mistakes

> [!WARNING]
> 1. **Omitting `carry` in Loop Condition:** Writing `while l1 or l2:` misses the final carry node when inputs sum to a higher order digit (e.g., $[5] + [5] = [0, 1]$).
> 2. **Attempting `l1.val` on `None`:** Calling `l1.val` without checking if `l1` is `None` causes `AttributeError: 'NoneType' object has no attribute 'val'`.
> 3. **Losing Reference to List Head:** Modifying the root pointer directly instead of using a `dummy` node.

---

## 13. Interview Questions

1. **Q: Why do we use a dummy node at the beginning?**
   - *A:* A dummy node avoids special conditional logic for creating the list head, allowing every node (including the first) to be added uniformly via `current.next = ListNode(...)`.

2. **Q: What if the digits were stored in forward order instead of reverse order (e.g. `(3) -> (4) -> (2)` for $342$)?**
   - *A:* This is **LeetCode #445 (Add Two Numbers II)**. Options include reversing both input lists first, using two Stacks to process digits from right to left, or using recursion.

3. **Q: Could we modify one of the existing input linked lists in-place to achieve $\mathcal{O}(1)$ auxiliary space?**
   - *A:* Yes, by writing sum values into `l1` (or the longer list) directly and only creating new nodes when extension is required.

---

## 14. Similar Problems

- **Easier:**
  - [LeetCode #67 - Add Binary](https://leetcode.com/problems/add-binary/)
  - [LeetCode #66 - Plus One](https://leetcode.com/problems/plus-one/)
- **Similar Difficulty:**
  - [LeetCode #445 - Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/)
  - [LeetCode #43 - Multiply Strings](https://leetcode.com/problems/multiply-strings/)
  - [LeetCode #369 - Plus One Linked List](https://leetcode.com/problems/plus-one-linked-list/)
- **Harder:**
  - [LeetCode #224 - Basic Calculator](https://leetcode.com/problems/basic-calculator/)

---

## 15. Learning Summary

- **Pattern Recognized:** Linked List Traversal + Grade School Arithmetic Carry Propagation.
- **Key Technique:** Using `dummy = ListNode(0)` for clean linked list creation.
- **Rule of Thumb:** Always include `carry` in the primary loop condition (`while l1 or l2 or carry`) to automatically process leftover carry digits.

---

## 16. Optimization Notes

Your code is **100% optimal** in terms of Time Complexity ($\mathcal{O}(\max(N, M))$) and Space Complexity ($\mathcal{O}(\max(N, M))$). It handles all edge cases elegantly with clean Python idioms. No further logic optimizations are required!
