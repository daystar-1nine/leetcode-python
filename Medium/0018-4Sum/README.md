# 0018. 4Sum

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)
![Topic: Array](https://img.shields.io/badge/Topic-Array-blue?style=for-the-badge)
![Topic: Two Pointers](https://img.shields.io/badge/Topic-Two%20Pointers-purple?style=for-the-badge)
![Topic: Sorting](https://img.shields.io/badge/Topic-Sorting-green?style=for-the-badge)

---

## 1. Problem Information

- **Problem Name:** 4Sum
- **LeetCode Number:** 18
- **Difficulty:** Medium
- **Tags:** Array, Two Pointers, Sorting
- **Language Used:** Python
- **Problem Link:** [LeetCode #18 - 4Sum](https://leetcode.com/problems/4sum/)

---

## 2. Problem Overview

Given an array `nums` of `n` integers and an integer `target`, return an array of all the **unique quadruplets** `[nums[a], nums[b], nums[c], nums[d]]` such that:
1. $0 \le a, b, c, d < n$
2. $a$, $b$, $c$, and $d$ are **distinct**.
3. $\text{nums}[a] + \text{nums}[b] + \text{nums}[c] + \text{nums}[d] == \text{target}$

You may return the answer in **any order**.

### Input & Output Specifications
- **Input:**
  - `nums`: An integer array ($1 \le \text{len}(nums) \le 200$).
  - `target`: Target sum integer ($-10^9 \le \text{target} \le 10^9$).
- **Output:** A list of unique integer quadruplets.
- **Constraints:** $-10^9 \le \text{nums}[i] \le 10^9$.

### Examples
- **Example 1:**
  - **Input:** `nums = [1,0,-1,0,-2,2]`, `target = 0`
  - **Output:** `[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]`
- **Example 2:**
  - **Input:** `nums = [2,2,2,2,2]`, `target = 8`
  - **Output:** `[[2,2,2,2]]`

---

## 3. Intuition

> [!TIP]
> **Generalizing $K$-Sum to $2$-Sum:** Fix $K - 2$ variables using nested loops, and solve the remaining 2 variables using Two Pointers on a sorted array!

1. **Brute Force:** Checking every quadruplet combination takes $\mathcal{O}(N^4)$ time.
2. **Double Loop + Two Pointers Strategy:**
   - **Sort** `nums` in ascending order.
   - Fix the first variable `nums[i]` (outer loop).
   - Fix the second variable `nums[j]` (inner loop).
   - Place two pointers for the remaining sub-array: `left = j + 1` and `right = n - 1`.
   - Compute `total = nums[i] + nums[j] + nums[left] + nums[right]`:
     - If `total == target`: Found a quadruplet! Append to result, move `left` and `right` inward, and skip duplicates for `left` and `right`.
     - If `total < target`: Move `left += 1`.
     - If `total > target`: Move `right -= 1`.

---

## 4. Thought Process

```mermaid
flowchart TD
    A[Start: Input nums, target] --> B[Sort nums in ascending order]
    B --> C[Initialize result = empty list]
    C --> D[Loop i from 0 to n - 4]
    D --> E{i > 0 and nums[i] == nums[i-1]?}
    E -- Yes --> F[Skip duplicate i: continue]
    F --> D
    E -- No --> G[Loop j from i + 1 to n - 3]
    G --> H{j > i + 1 and nums[j] == nums[j-1]?}
    H -- Yes --> I[Skip duplicate j: continue]
    I --> G
    H -- No --> J[Set left = j + 1, right = n - 1]
    J --> K{Is left < right?}
    K -- Yes --> L[total = nums[i] + nums[j] + nums[left] + nums[right]]
    L --> M{total == target?}
    M -- Yes --> N[Append quadruplet to result]
    N --> O[left += 1, right -= 1]
    O --> P[Skip duplicate left and right values]
    P --> K
    M -- total < target --> Q[left += 1]
    Q --> K
    M -- total > target --> R[right -= 1]
    R --> K
    K -- No --> G
    G -- Done j loop --> D
    D -- Done i loop --> S[Return result]
```

1. **Sort Input Array:**
   - Execute `nums.sort()`.

2. **Outer Loop `i` (First Element):**
   - Loop `i` from `0` to `n - 4`.
   - De-duplicate `i`: `if i > 0 and nums[i] == nums[i-1]: continue`.

3. **Inner Loop `j` (Second Element):**
   - Loop `j` from `i + 1` to `n - 3`.
   - De-duplicate `j`: **`if j > i + 1 and nums[j] == nums[j-1]: continue`** (Crucial: `j > i + 1` prevents skipping valid duplicate pairs where `nums[i] == nums[j]`).

4. **Two Pointers Search (`left` & `right`):**
   - Set `left = j + 1`, `right = n - 1`.
   - While `left < right`:
     - `total = nums[i] + nums[j] + nums[left] + nums[right]`
     - If `total == target`:
       - Append `[nums[i], nums[j], nums[left], nums[right]]` to `result`.
       - `left += 1; right -= 1`
       - Skip duplicate `left`: `while left < right and nums[left] == nums[left-1]: left += 1`
       - Skip duplicate `right`: `while left < right and nums[right] == nums[right+1]: right -= 1`
     - Elif `total < target`: `left += 1`
     - Else: `right -= 1`

5. **Return Quadruplets:**
   - Return `result`.

---

## 5. Concepts Used

### 1. Multi-Pointer Search & Reduction
- **What it is:** Extending two-pointer convergence to 4 variables by nesting $K-2$ outer loops.
- **Why it is used here:** Reduces time complexity from $\mathcal{O}(N^4)$ to $\mathcal{O}(N^3)$.
- **Future applications:** 3Sum, 4Sum II, K-Sum.

### 2. Multi-Level De-duplication
- **What it is:** Enforcing duplicate-skipping checks at every level ($i$, $j$, `left`, `right`).
- **Why it is used here:** Guarantees unique output quadruplets without needing extra set hashing memory.
- **Future applications:** Combination Sum II, Subsets II.

---

## 6. Algorithm Used

### Sorting + Double Loop with Two Pointers Search

- **Algorithm Category:** Array / Two Pointers / Sorting
- **Why selected:** Standard optimal algorithm for 4Sum with $\mathcal{O}(N^3)$ time and $\mathcal{O}(1)$ auxiliary space.
- **Time Complexity:** $\mathcal{O}(N^3)$
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

---

## 7. Code Walkthrough

Below is the line-by-line breakdown of the submitted solution:

```python
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # Line 9: Sort input array
        nums.sort()
        n = len(nums)
        result = []

        # Line 14: Outer loop fixing first element nums[i]
        for i in range(n - 3):

            # Line 17-18: Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Line 21: Inner loop fixing second element nums[j]
            for j in range(i + 1, n - 2):

                # Line 24-25: Skip duplicate second numbers for current i
                # Note: 'j > i + 1' ensures identical adjacent values (nums[i] == nums[j]) are not skipped
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Line 27-28: Initialize Two Pointers
                left = j + 1
                right = n - 1

                # Line 31: Convergence loop for two pointers
                while left < right:

                    # Line 33: Calculate total 4-element sum
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    # Line 36-37: Matching quadruplet found
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        left += 1
                        right -= 1

                        # Line 43-44: Skip duplicate third numbers (left)
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        # Line 47-48: Skip duplicate fourth numbers (right)
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    # Line 50-51: Sum too small, move left pointer rightward
                    elif total < target:
                        left += 1

                    # Line 53-54: Sum too large, move right pointer leftward
                    else:
                        right -= 1

        # Line 56: Return complete list of unique quadruplets
        return result
```

---

## 8. Dry Run

Let's dry run for `nums = [1, 0, -1, 0, -2, 2]` ($n=6$) and `target = 0`.

### Sorted Array
`nums = [-2, -1, 0, 0, 1, 2]`

### Execution Trace

| `i` | `nums[i]` | `j` | `nums[j]` | `L` | `R` | Quadruplet Sum | Action | `result` State |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **0** | `-2` | **1** | `-1` | `2` (`0`) | `5` (`2`) | $-2 + (-1) + 0 + 2 = \mathbf{0}$ | **Found!** Append `[-2,-1,0,2]`, move `L=3, R=4` | `[[-2,-1,0,2]]` |
| **0** | `-2` | **1** | `-1` | `3` (`0`) | `4` (`1`) | $-2 + (-1) + 0 + 1 = -2$ | `total < 0` $\rightarrow$ `L += 1` (`L=4==R`) | `[[-2,-1,0,2]]` |
| **0** | `-2` | **2** | `0` | `3` (`0`) | `5` (`2`) | $-2 + 0 + 0 + 2 = \mathbf{0}$ | **Found!** Append `[-2,0,0,2]`, move `L=4, R=4` | `[[-2,-1,0,2], [-2,0,0,2]]` |
| **1** | `-1` | **2** | `0` | `3` (`0`) | `5` (`2`) | $-1 + 0 + 0 + 2 = 1$ | `total > 0` $\rightarrow$ `R -= 1` | `[[-2,-1,0,2], [-2,0,0,2]]` |
| **1** | `-1` | **2** | `0` | `3` (`0`) | `4` (`1`) | $-1 + 0 + 0 + 1 = \mathbf{0}$ | **Found!** Append `[-1,0,0,1]` | `[[-2,-1,0,2], [-2,0,0,2], [-1,0,0,1]]` |

### Output
Returns **`[[-2, -1, 0, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]`**.

---

## 9. Complexity Analysis

### Time Complexity: $\mathcal{O}(N^3)$
- **Sorting:** `nums.sort()` takes $\mathcal{O}(N \log N)$ time.
- **Triple Nested Loops:** Outer loop runs $N$ times, second loop runs $N$ times, inner two pointers loop runs $N$ times.
- **Overall Time Complexity:** $\mathcal{O}(N \log N + N^3) = \mathcal{O}(N^3)$.

### Space Complexity: $\mathcal{O}(1)$ Auxiliary Space
- Algorithm uses primitive pointer variables (`i`, `j`, `left`, `right`, `total`).
- Auxiliary space is $\mathcal{O}(1)$ (excluding output array).

---

## 10. Edge Cases

| Edge Case Scenario | Input Example | Behavior & Output | How Code Handles It |
| :--- | :--- | :--- | :--- |
| **Identical Elements** | `nums = [2, 2, 2, 2, 2]`, `target = 8` | Output: `[[2, 2, 2, 2]]` | Duplicate checks for `i`, `j`, `left`, `right` ensure only 1 quadruplet is added. |
| **$N < 4$ Elements** | `nums = [1, 2, 3]`, `target = 6` | Output: `[]` | Outer loop range `n - 3` fails immediately. |
| **Large Target Values** | `nums = [10^9, 10^9...]`, `target = 4*10^9` | Output: `[[10^9, 10^9, 10^9, 10^9]]` | Python handles large integers seamlessly without overflow. |
| **No Match Possible** | `nums = [1, 2, 3, 4]`, `target = 100` | Output: `[]` | Loops finish with `total < target` everywhere. |

---

## 11. Alternative Approaches

### Approach 1: Generic $K$-Sum Recursion ($\mathcal{O}(N^{K-1})$ Time, $\mathcal{O}(K)$ Stack Space)
- **Idea:** Write a recursive $K$-Sum solver that reduces $K$ to 2Sum recursively.
- **Why Great:** Scalable for 4Sum, 5Sum, or any arbitrary $K$-Sum.

### Approach 2: Sorting + Double Loop with Two Pointers (User's Solution - Recommended)
- **Idea:** 2 nested loops + 2 pointers.
- **Complexity:** $\mathcal{O}(N^3)$ time, $\mathcal{O}(1)$ space.
- **Why Optimal:** Direct, optimal runtime for $K=4$, easy to write in interviews.

---

## 12. Common Mistakes

> [!WARNING]
> 1. **Incorrect Duplicate Check for `j`:** Writing `if j > 0 and nums[j] == nums[j - 1]:` instead of `j > i + 1`. This skips valid quadruplets where `nums[i]` and `nums[j]` happen to have the same value!
> 2. **32-Bit Integer Overflow in C++/Java:** In statically typed languages, `nums[i] + nums[j] + nums[left] + nums[right]` can exceed $2^{31}-1$. Type casting to `long long` is mandatory.
> 3. **Not Sorting `nums` First:** Two Pointers relies entirely on sorted order to adjust bounds.

---

## 13. Interview Questions

1. **Q: Why must the duplicate check for $j$ be `j > i + 1` instead of `j > 0`?**
   - *A:* Because `j` starts at `i + 1`. The first choice for $j$ after fixing $i$ should be allowed to have the same value as $nums[i]$ (e.g. `[-1, -1, 0, 2]`). `j > i + 1` ensures we only skip duplicates for *subsequent* choices of $j$ within the same outer $i$ loop.

2. **Q: How can we prune the search space to optimize performance?**
   - *A:* Add early exit guards inside the loops:
     - Minimum possible sum: `if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target: break`
     - Maximum possible sum: `if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target: continue`

3. **Q: How would you generalize 4Sum to $K$-Sum?**
   - *A:* Use recursion. Base case: $K == 2$ (use two pointers on sorted array). For $K > 2$, loop fixed index and recursively call $(K-1)$-Sum with target `target - nums[i]`.

---

## 14. Similar Problems

- **Easy:**
  - [LeetCode #1 - Two Sum](https://leetcode.com/problems/two-sum/)
- **Medium:**
  - [LeetCode #15 - 3Sum](https://leetcode.com/problems/3sum/)
  - [LeetCode #16 - 3Sum Closest](https://leetcode.com/problems/3sum-closest/)
  - [LeetCode #454 - 4Sum II](https://leetcode.com/problems/4sum-ii/)

---

## 15. Learning Summary

- **Pattern Recognized:** $K$-Sum Reduction to 2-Pointers via Nested Loops.
- **De-duplication Condition:** `j > i + 1 and nums[j] == nums[j-1]` for secondary fixed elements.
- **Generality:** Same algorithm extends cleanly from 2Sum to 3Sum to 4Sum.

---

## 16. Optimization Notes

Your solution is **100% optimal** ($\mathcal{O}(N^3)$ Time, $\mathcal{O}(1)$ Auxiliary Space). It is clean, readable, and represents interview best practices!
