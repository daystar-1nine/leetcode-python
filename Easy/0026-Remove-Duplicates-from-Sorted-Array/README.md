# 0026. Remove Duplicates from Sorted Array

![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen?style=for-the-badge)
![Topic: Array](https://img.shields.io/badge/Topic-Array-blue?style=for-the-badge)
![Topic: Two Pointers](https://img.shields.io/badge/Topic-Two%20Pointers-purple?style=for-the-badge)

---

## 1. Problem Information

- **Problem Name:** Remove Duplicates from Sorted Array
- **LeetCode Number:** 26
- **Difficulty:** Easy
- **Tags:** Array, Two Pointers
- **Language Used:** Python
- **Problem Link:** [LeetCode #26 - Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

---

## 2. Problem Overview

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates **in-place** such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in `nums` to be $k$. After removing duplicates, return the number of unique elements $k$.

The first $k$ elements of `nums` should contain the unique numbers in sorted order. The remaining elements beyond index $k - 1$ can be ignored.

### Input & Output Specifications
- **Input:** `nums`: An array of integers sorted in non-decreasing order ($1 \le \text{len}(nums) \le 3 \cdot 10^4$).
- **Output:** An integer $k$ representing the count of unique elements, with `nums[:k]` containing the unique values.
- **Constraints:** $-100 \le \text{nums}[i] \le 100$.

### Examples
- **Example 1:**
  - **Input:** `nums = [1,1,2]`
  - **Output:** `2, nums = [1,2,_]`
  - **Explanation:** Your function should return $k = 2$, with the first two elements of `nums` being 1 and 2 respectively.
- **Example 2:**
  - **Input:** `nums = [0,0,1,1,1,2,2,3,3,4]`
  - **Output:** `5, nums = [0,1,2,3,4,_,_,_,_,_]`
  - **Explanation:** Your function should return $k = 5$, with the first five elements of `nums` being 0, 1, 2, 3, and 4 respectively.

---

## 3. Intuition

> [!TIP]
> **Fast / Slow Two Pointers In-Place Pattern:** Use a slow pointer `k` to track the write location for unique elements, and a fast pointer `i` to scan the sorted array for new unique values!

### Why Two Pointers Work:
- Because the array is already **sorted**, duplicate values are guaranteed to sit next to each other.
- The first element `nums[0]` is always unique, so `k` starts at index `1`.
- As the fast pointer `i` moves from index `1` to `N-1`, we compare `nums[i]` with `nums[i-1]`.
- If `nums[i] != nums[i-1]`, we found a new unique element! We copy it to `nums[k]` and increment `k`.

```text
Initial: [0, 0, 1, 1, 1, 2]
          k  i
          1  1 -> nums[1] == nums[0] (duplicate, skip)
          1  2 -> nums[2] != nums[1] (unique! nums[k] = nums[2], k++)
         [0, 1, 1, 1, 1, 2]
             k  i
```

---

## 4. Thought Process

```mermaid
flowchart TD
    A[Start: Input sorted nums array] --> B{Is nums empty?}
    B -- Yes --> C[Return 0]
    B -- No --> D[Initialize write pointer k = 1]
    D --> E[Loop fast pointer i from 1 to len nums - 1]
    E --> F{Is nums[i] != nums[i-1]?}
    F -- Yes --> G[nums[k] = nums[i]]
    G --> H[k = k + 1]
    F -- No --> I{More elements?}
    H --> I
    I -- Yes --> E
    I -- No --> J[Return k]
```

1. **Guard Clause:**
   - If `not nums: return 0`.

2. **Pointer Setup:**
   - Initialize slow write pointer `k = 1`.

3. **Fast Pointer Traversal:**
   - Loop `i` from `1` to `len(nums) - 1`:
     - If `nums[i] != nums[i - 1]`:
       - `nums[k] = nums[i]`
       - `k += 1`

4. **Return Answer:**
   - Return `k`.

---

## 5. Concepts Used

### 1. Fast / Slow Two Pointers
- **What it is:** Maintaining two pointers operating at different speeds across the same array.
- **Why it is used here:** Allows in-place array modification without extra memory allocation.
- **Future applications:** Remove Element, Move Zeroes, Partition Array.

### 2. Contiguous Duplicate Property in Sorted Arrays
- **What it is:** Exploiting pre-sorted order where identical values occupy contiguous index blocks.
- **Why it is used here:** Enables duplicate detection by comparing `nums[i]` with `nums[i-1]` in $\mathcal{O}(1)$ time.
- **Future applications:** 3Sum, 4Sum, Single Number in Sorted Array.

---

## 6. Algorithm Used

### Two Pointers In-Place Array Deduplication

- **Algorithm Category:** Array / Two Pointers
- **Why selected:** Achieves theoretical minimum time complexity $\mathcal{O}(N)$ with strict $\mathcal{O}(1)$ auxiliary space.
- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

---

## 7. Code Walkthrough

Below is the line-by-line breakdown of the submitted solution:

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Line 9-10: Guard Clause for empty array
        if not nums:
            return 0

        # Line 14: Slow pointer k tracks write index for next unique element
        k = 1

        # Line 17: Fast pointer i scans array from index 1
        for i in range(1, len(nums)):

            # Line 21: Check if current element differs from previous element
            if nums[i] != nums[i - 1]:

                # Line 24: Overwrite value at write index k with new unique element
                nums[k] = nums[i]

                # Line 27: Advance write pointer k
                k += 1

        # Line 30: Return total count of unique elements
        return k
```

---

## 8. Dry Run

Let's dry run for `nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]`.

### Setup
- `nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]`
- `k = 1`

### Step Trace

| `i` | `nums[i]` | `nums[i-1]` | `nums[i] != nums[i-1]` | Action | `nums` State | `k` |
| :---: | :---: | :---: | :---: | :--- | :--- | :---: |
| **1** | 0 | 0 | False | Skip duplicate | `[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]` | 1 |
| **2** | 1 | 0 | **True** | `nums[1] = 1`, `k++` | `[0, 1, 1, 1, 1, 2, 2, 3, 3, 4]` | **2** |
| **3** | 1 | 1 | False | Skip duplicate | `[0, 1, 1, 1, 1, 2, 2, 3, 3, 4]` | 2 |
| **4** | 1 | 1 | False | Skip duplicate | `[0, 1, 1, 1, 1, 2, 2, 3, 3, 4]` | 2 |
| **5** | 2 | 1 | **True** | `nums[2] = 2`, `k++` | `[0, 1, 2, 1, 1, 2, 2, 3, 3, 4]` | **3** |
| **6** | 2 | 2 | False | Skip duplicate | `[0, 1, 2, 1, 1, 2, 2, 3, 3, 4]` | 3 |
| **7** | 3 | 2 | **True** | `nums[3] = 3`, `k++` | `[0, 1, 2, 3, 1, 2, 2, 3, 3, 4]` | **4** |
| **8** | 3 | 3 | False | Skip duplicate | `[0, 1, 2, 3, 1, 2, 2, 3, 3, 4]` | 4 |
| **9** | 4 | 3 | **True** | `nums[4] = 4`, `k++` | `[0, 1, 2, 3, 4, 2, 2, 3, 3, 4]` | **5** |

### Output
Returns **`k = 5`** with `nums[:5] = [0, 1, 2, 3, 4]`.

---

## 9. Complexity Analysis

### Time Complexity: $\mathcal{O}(N)$
- Where $N$ is the number of elements in `nums`.
- The loop runs $N-1$ times, performing constant time $\mathcal{O}(1)$ operations per iteration.
- Total time complexity is strictly linear $\mathcal{O}(N)$.

### Space Complexity: $\mathcal{O}(1)$ Auxiliary Space
- The solution mutates `nums` in-place using two scalar pointer variables (`k` and `i`).
- No auxiliary lists or hash sets are allocated.
- Total space complexity is $\mathcal{O}(1)$.

---

## 10. Edge Cases

| Edge Case Scenario | Input Example | Behavior & Output | How Code Handles It |
| :--- | :--- | :--- | :--- |
| **Single Element** | `nums = [1]` | Output: `k = 1, [1]` | `range(1, 1)` is empty, returns `k = 1`. |
| **No Duplicates** | `nums = [1, 2, 3]` | Output: `k = 3, [1, 2, 3]` | Overwrites each element to its own index, `k = 3`. |
| **All Identical** | `nums = [2, 2, 2, 2]`| Output: `k = 1, [2, ...]` | Skips all $i \ge 1$, returns `k = 1`. |
| **Negative Numbers**| `nums = [-3, -3, -1]` | Output: `k = 2, [-3, -1]` | Comparison `nums[i] != nums[i-1]` works seamlessly. |

---

## 11. Alternative Approaches

### Approach 1: Extra Hash Set ($\mathcal{O}(N)$ Time, $\mathcal{O}(N)$ Space)
- **Idea:** Insert elements into a set, sort unique elements, and write back.
- **Drawback:** Fails the in-place $\mathcal{O}(1)$ auxiliary space requirement.

### Approach 2: Two Pointers (User's Solution - Recommended)
- **Idea:** Fast/slow pointer in-place array mutation.
- **Complexity:** $\mathcal{O}(N)$ time, $\mathcal{O}(1)$ auxiliary space.
- **Why Optimal:** Gold standard for in-place array deduplication in technical interviews.

---

## 12. Common Mistakes

> [!WARNING]
> 1. **Allocating New Array:** Creating a new array or converting `nums` via `list(set(nums))` violates the in-place constraint.
> 2. **Wrong Initial Write Pointer:** Starting `k = 0` overwrites the first element before comparing it.
> 3. **Array Bounds Indexing:** Comparing `nums[i]` with `nums[i+1]` without boundary checks causes `IndexError`.

---

## 13. Interview Questions

1. **Q: Why does the slow pointer `k` start at index `1` instead of `0`?**
   - *A:* Because an array with at least 1 element always has its first element (`nums[0]`) as unique. Therefore, `nums[0]` is already in its correct position, and the next unique element should be written at index `1`.

2. **Q: How would you extend this solution to allow at most 2 duplicates of each element (LeetCode #80)?**
   - *A:* Compare `nums[i]` with `nums[k-2]`. If `nums[i] != nums[k-2]`, set `nums[k] = nums[i]` and increment `k`.

---

## 14. Similar Problems

- **Easy:**
  - [LeetCode #27 - Remove Element](https://leetcode.com/problems/remove-element/)
  - [LeetCode #283 - Move Zeroes](https://leetcode.com/problems/move-zeroes/)
- **Medium:**
  - [LeetCode #80 - Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

---

## 15. Learning Summary

- **Pattern Recognized:** In-Place Array Deduplication using Fast/Slow Two Pointers.
- **Sorted Array Property:** Contiguous placement of identical elements.
- **Space Efficiency:** Achieving $\mathcal{O}(1)$ memory mutation.

---

## 16. Optimization Notes

Your solution is **100% optimal** ($\mathcal{O}(N)$ Time, $\mathcal{O}(1)$ Auxiliary Space). It is clean, readable, and represents the gold-standard interview implementation!
