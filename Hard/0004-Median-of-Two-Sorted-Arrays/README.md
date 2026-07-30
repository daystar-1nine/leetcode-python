# 0004. Median of Two Sorted Arrays

![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red?style=for-the-badge)
![Topic: Array](https://img.shields.io/badge/Topic-Array-blue?style=for-the-badge)
![Topic: Binary Search](https://img.shields.io/badge/Topic-Binary%20Search-purple?style=for-the-badge)
![Topic: Divide and Conquer](https://img.shields.io/badge/Topic-Divide%20and%20Conquer-orange?style=for-the-badge)

---

## 1. Problem Information

- **Problem Name:** Median of Two Sorted Arrays
- **LeetCode Number:** 4
- **Difficulty:** Hard
- **Tags:** Array, Binary Search, Divide and Conquer
- **Language Used:** Python
- **Problem Link:** [LeetCode #4 - Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

---

## 2. Problem Overview

Given two sorted arrays `nums1` and `nums2` of sizes $m$ and $n$ respectively, return the **median** of the two combined sorted arrays.

The key constraint of this problem is that your solution **must run in $\mathcal{O}(\log(m+n))$ time complexity**.

### Input & Output Specifications
- **Input:**
  - `nums1`: A sorted array of integers of size $m$.
  - `nums2`: A sorted array of integers of size $n$.
- **Output:** A floating-point number representing the median.
- **Constraints:**
  - $0 \le m \le 1000$
  - $0 \le n \le 1000$
  - $1 \le m + n \le 2000$
  - $-10^6 \le \text{nums1}[i], \text{nums2}[i] \le 10^6$

### Examples
- **Example 1:**
  - **Input:** `nums1 = [1, 3]`, `nums2 = [2]`
  - **Output:** `2.00000` (Merged array = `[1, 2, 3]`, median is `2`).
- **Example 2:**
  - **Input:** `nums1 = [1, 2]`, `nums2 = [3, 4]`
  - **Output:** `2.50000` (Merged array = `[1, 2, 3, 4]`, median is $(2 + 3) / 2 = 2.5$).

### Real-World Intuition
Consider a distributed database where transaction logs are sharded across two server nodes in sorted timestamp order. To determine the 50th percentile (median) query response latency across the entire cluster without fetching and merging gigabytes of log data over the network, we binary search for the cut position across the smaller shard node.

---

## 3. Intuition

> [!TIP]
> **Key Insight:** Partition both arrays into a Left Half and a Right Half such that every element in the combined Left Half is $\le$ every element in the combined Right Half!

### Understanding the Median Partition
The median splits a combined dataset into two halves of equal size:
- **Left Half Size:** $\lfloor \frac{m + n + 1}{2} \rfloor$
- If we choose $i$ elements from `nums1` for the left half, we must choose $j = \text{half} - i$ elements from `nums2`.

```text
nums1:  [  left1  |  right1  ]   -> split at index i
nums2:  [  left2  |  right2  ]   -> split at index j
```

A partition is **valid** if:
1. $\text{left1} \le \text{right2}$ (The largest element from `nums1`'s left half $\le$ smallest element from `nums2`'s right half)
2. $\text{left2} \le \text{right1}$ (The largest element from `nums2`'s left half $\le$ smallest element from `nums1`'s right half)

Since `nums1` is sorted, as $i$ increases, `left1` increases and `right2` decreases. This monotonic property enables **Binary Search** over the partition index $i$ in range $[0, m]$!

---

## 4. Thought Process

```mermaid
flowchart TD
    A[Start: Input nums1, nums2] --> B{Is len(nums1) > len(nums2)?}
    B -- Yes --> C[Swap nums1 and nums2 to ensure nums1 is smaller]
    B -- No --> D[Keep nums1 as smaller array]
    C --> E[Set m = len(nums1), n = len(nums2)]
    D --> E
    E --> F[Initialize left = 0, right = m, half = (m + n + 1) // 2]
    F --> G[While left <= right]
    G --> H[Compute i = (left + right) // 2, j = half - i]
    H --> I[Assign left1, right1, left2, right2 using infinity guards]
    I --> J{Is left1 <= right2 and left2 <= right1?}
    J -- Valid Partition --> K{(m + n) is Odd?}
    K -- Yes --> L[Return float(max(left1, left2))]
    K -- No --> M[Return (max(left1, left2) + min(right1, right2)) / 2.0]
    J -- Invalid: left1 > right2 --> N[Partition i too far right: right = i - 1]
    J -- Invalid: left2 > right1 --> O[Partition i too far left: left = i + 1]
    N --> G
    O --> G
```

1. **Ensure `nums1` is the Smaller Array:**
   - If `len(nums1) > len(nums2)`, swap `nums1` and `nums2`.
   - **Why?** Binary searching on the smaller array ensures $\mathcal{O}(\log(\min(m, n)))$ runtime and guarantees $j = \text{half} - i \ge 0$ remains valid without underflowing array bounds.

2. **Binary Search Range Allocation:**
   - `left = 0`, `right = m`
   - `half = (m + n + 1) // 2` (Integer division rounding up handles both odd and even total lengths cleanly).

3. **Infinity Guard Boundary Checks:**
   - `left1 = float("-inf")` if $i == 0$ else `nums1[i - 1]`
   - `right1 = float("inf")` if $i == m$ else `nums1[i]`
   - `left2 = float("-inf")` if $j == 0$ else `nums2[j - 1]`
   - `right2 = float("inf")` if $j == n$ else `nums2[j]`

4. **Partition Validity Check & Result:**
   - **If `left1 <= right2` and `left2 <= right1`:**
     - **Odd Total Length (`(m + n) % 2 == 1`):** Median is $\max(\text{left1}, \text{left2})$.
     - **Even Total Length:** Median is $\frac{\max(\text{left1}, \text{left2}) + \min(\text{right1}, \text{right2})}{2.0}$.
   - **If `left1 > right2`:** $i$ is too big $\rightarrow$ Move binary search left (`right = i - 1`).
   - **Else (`left2 > right1`):** $i$ is too small $\rightarrow$ Move binary search right (`left = i + 1`).

---

## 5. Concepts Used

### 1. Binary Search on Partition Index
- **What it is:** Applying binary search to locate a valid boundary cut between two arrays rather than searching for a specific target value.
- **Why it is used here:** Reduces combined search time from linear $\mathcal{O}(m+n)$ to logarithmic $\mathcal{O}(\log(\min(m, n)))$.
- **Future applications:** K-th Smallest Element in Two Sorted Arrays, Split Array Largest Sum.

### 2. Infinity Sentinel Guard Values
- **What it is:** Using `float('-inf')` and `float('inf')` for virtual boundary padding.
- **Why it is used here:** Avoids tedious `if-else` branches when partition cuts fall on array edges ($i=0, i=m, j=0, j=n$).
- **Future applications:** Interval Merging, Segment Tree boundary conditions.

---

## 6. Algorithm Used

### Binary Search Partitioning

- **Algorithm Category:** Binary Search / Divide and Conquer
- **Why selected:** It is the only algorithm that achieves the mandatory $\mathcal{O}(\log(m+n))$ time constraint set by LeetCode.
- **Time Complexity:** $\mathcal{O}(\log(\min(m, n)))$
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

---

## 7. Code Walkthrough

Below is the line-by-line explanation of the submitted solution:

```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # Line 10-11: Guarantee Binary Search runs on the smaller array
        # This optimizes time complexity to O(log(min(m, n))) and prevents j from becoming negative.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        # Line 16-18: Binary Search Boundary Initialization
        left = 0
        right = m
        # half computes the required size of the combined left partition
        half = (m + n + 1) // 2

        # Line 20: Binary Search Loop
        while left <= right:
            # i is partition cut for nums1, j is partition cut for nums2
            i = (left + right) // 2
            j = half - i

            # Line 24-28: Infinity Sentinel Guards
            # If partition cut is at index 0, left element is -infinity.
            # If partition cut is at index m, right element is +infinity.
            left1 = float("-inf") if i == 0 else nums1[i - 1]
            right1 = float("inf") if i == m else nums1[i]

            left2 = float("-inf") if j == 0 else nums2[j - 1]
            right2 = float("inf") if j == n else nums2[j]

            # Line 30: Validity Check for Correct Partition
            if left1 <= right2 and left2 <= right1:
                # Odd length: max of left partition elements is the median
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))
                # Even length: average of max(left) and min(right)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2.0

            # Line 37: left1 > right2 -> took too many elements from nums1, shift left
            elif left1 > right2:
                right = i - 1
            # Line 39: left2 > right1 -> took too few elements from nums1, shift right
            else:
                left = i + 1

        return 0.0
```

---

## 8. Dry Run

Let's dry run for `nums1 = [1, 3]` ($m=2$) and `nums2 = [2]` ($n=1$).

### Initial State
1. `len(nums1) > len(nums2)` ($2 > 1$) $\rightarrow$ **Swap!**
   - `nums1 = [2]` ($m=1$)
   - `nums2 = [1, 3]` ($n=2$)
2. `left = 0`, `right = 1`.
3. `half = (1 + 2 + 1) // 2 = 2`.

### Binary Search Iterations

| Iteration | `left` | `right` | `i` | `j` (`2-i`) | `left1` | `right1` | `left2` | `right2` | Check (`left1 <= right2` & `left2 <= right1`) | Action |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | `0` | `1` | `0` | `2` | $-\infty$ | `2` | `nums2[1]=3` | `+\infty` | `-\infty <= +\infty` (True)<br>`3 <= 2` (**False!**) | `left2 > right1` $\rightarrow$ `left = i + 1 = 1` |
| **2** | `1` | `1` | `1` | `1` | `nums1[0]=2` | $+\infty$ | `nums2[0]=1` | `nums2[1]=3` | `2 <= 3` (True)<br>`1 <= +\infty` (True) | **Valid Partition Found!** |

### Output Computation
- Total length = $1 + 2 = 3$ (Odd).
- Return `float(max(left1, left2))` = `float(max(2, 1))` $\rightarrow$ **`2.0`**

---

## 9. Complexity Analysis

### Time Complexity: $\mathcal{O}(\log(\min(m, n)))$
- Binary search operates on the smaller array of size $\min(m, n)$.
- Halving the search space each step takes $\mathcal{O}(\log(\min(m, n)))$ iterations.
- Meets the mandatory $\mathcal{O}(\log(m+n))$ problem requirement.

### Space Complexity: $\mathcal{O}(1)$ Auxiliary Space
- Uses only primitive variables (`left`, `right`, `i`, `j`, `left1`, `right1`, `left2`, `right2`).
- No array copying or recursion stack allocation.

---

## 10. Edge Cases

| Edge Case Scenario | Input Example | Behavior & Output | How Code Handles It |
| :--- | :--- | :--- | :--- |
| **One Array Empty** | `nums1 = []`, `nums2 = [1, 2, 3]` | Output: `2.0` | `nums1` becomes `[]` ($m=0$). `i=0`, `left1=-\infty`, `right1=+\infty`. Uses `nums2` values cleanly. |
| **Disjoint Ranges** | `nums1 = [1, 2]`, `nums2 = [3, 4]` | Output: `2.5` | Partitions cleanly at `i=2` and `j=0`. |
| **Single Element Arrays** | `nums1 = [2]`, `nums2 = []` | Output: `2.0` | $m=0, n=1$ after swap, evaluates `max(left1, left2)` to `2.0`. |
| **Negative Numbers** | `nums1 = [-3, -1]`, `nums2 = [-2]` | Output: `-2.0` | Negative values compare correctly with $-\infty$ and $+\infty$. |

---

## 11. Alternative Approaches

### Approach 1: Merge and Sort ($\mathcal{O}((m+n) \log(m+n))$ Time, $\mathcal{O}(m+n)$ Space)
- **Idea:** Concatenate both arrays and call `sort()`, then take the middle element(s).
- **Drawback:** Fails the $\mathcal{O}(\log(m+n))$ time complexity requirement.

### Approach 2: Two-Pointer Merge Simulation ($\mathcal{O}(m+n)$ Time, $\mathcal{O}(1)$ Space)
- **Idea:** Use two pointers to step through `nums1` and `nums2` sequentially up to index $\frac{m+n}{2}$.
- **Drawback:** $\mathcal{O}(m+n)$ linear time complexity is too slow for the required logarithmic constraint.

### Approach 3: Binary Search Partitioning (User's Solution - Optimal)
- **Idea:** Binary search partition cut on smaller array.
- **Complexity:** $\mathcal{O}(\log(\min(m, n)))$ time, $\mathcal{O}(1)$ auxiliary space.
- **Why Optimal:** Strictly satisfies all requirements with minimal space.

---

## 12. Common Mistakes

> [!WARNING]
> 1. **Binary Searching on the Larger Array:** Forgetting `if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1` can lead to negative `j` values (`j = half - i < 0`) causing index errors.
> 2. **Wrong `half` Formula:** Using `(m + n) // 2` instead of `(m + n + 1) // 2` causes off-by-one errors for odd length outputs.
> 3. **Integer Division in Python 2:** Returning `(max(...) + min(...)) / 2` without `.0` in Python 2 performs integer truncation. The user code correctly uses `/ 2.0`.

---

## 13. Interview Questions

1. **Q: Why do we use `(m + n + 1) // 2` instead of `(m + n) // 2` for `half`?**
   - *A:* Adding `1` before integer division ensures that when total length $(m+n)$ is odd, the left partition receives the extra element, making `max(left1, left2)` the exact median.

2. **Q: How can this problem be generalized to find the $K$-th smallest element of two sorted arrays?**
   - *A:* Set `half = K` instead of `(m + n + 1) // 2` and binary search for the cut position where left partition size equals $K$.

3. **Q: Why do we set infinity sentinels `float('-inf')` and `float('inf')`?**
   - *A:* They eliminate boundary condition checks when a partition cut falls at index `0` or `m`/`n`, seamlessly handling cases where all elements of an array belong to one side of the partition.

---

## 14. Similar Problems

- **Easier:**
  - [LeetCode #35 - Search Insert Position](https://leetcode.com/problems/search-insert-position/)
- **Similar Difficulty:**
  - [LeetCode #33 - Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
  - [LeetCode #378 - Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)
- **Harder:**
  - [LeetCode #719 - Find K-th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance/)

---

## 15. Learning Summary

- **Pattern Recognized:** Binary Search on Partition Boundaries rather than element values.
- **Key Formula:** $j = \lfloor \frac{m + n + 1}{2} \rfloor - i$.
- **Core Takeaway:** Infinity guard values simplify multi-array boundary conditions, preventing edge-case bugs.

---

## 16. Optimization Notes

Your code is ** optimal** ($\mathcal{O}(\log(\min(m, n)))$ Time, $\mathcal{O}(1)$ Space). It represents the exact gold-standard solution for top tech company coding interviews!
