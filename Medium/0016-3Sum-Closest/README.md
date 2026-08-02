# 0016. 3Sum Closest

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)
![Topic: Array](https://img.shields.io/badge/Topic-Array-blue?style=for-the-badge)
![Topic: Two Pointers](https://img.shields.io/badge/Topic-Two%20Pointers-purple?style=for-the-badge)
![Topic: Sorting](https://img.shields.io/badge/Topic-Sorting-green?style=for-the-badge)

---

## 1. Problem Information

- **Problem Name:** 3Sum Closest
- **LeetCode Number:** 16
- **Difficulty:** Medium
- **Tags:** Array, Two Pointers, Sorting
- **Language Used:** Python
- **Problem Link:** [LeetCode #16 - 3Sum Closest](https://leetcode.com/problems/3sum-closest/)

---

## 2. Problem Overview

Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that their sum is **closest to `target`**.

Return the **sum of the three integers**.

You may assume that each input would have **exactly one solution**.

### Input & Output Specifications
- **Input:**
  - `nums`: An integer array ($3 \le \text{len}(nums) \le 500$).
  - `target`: Target sum integer ($-10^4 \le \text{target} \le 10^4$).
- **Output:** An integer representing the triplet sum closest to `target`.
- **Constraints:** $-1000 \le \text{nums}[i] \le 1000$.

### Examples
- **Example 1:**
  - **Input:** `nums = [-1, 2, 1, -4]`, `target = 1`
  - **Output:** `2`
  - **Explanation:** The triplet sum closest to target is $2$ ($-1 + 2 + 1 = 2$).
- **Example 2:**
  - **Input:** `nums = [0, 0, 0]`, `target = 1`
  - **Output:** `0`
  - **Explanation:** The triplet sum closest to target is $0$ ($0 + 0 + 0 = 0$).

### Real-World Intuition
Imagine a financial portfolio management tool trying to assemble three investment assets whose total combined risk index comes closest to a client's target risk tolerance score. The system sorts the asset scores and uses convergent pointers to find the closest match.

---

## 3. Intuition

> [!TIP]
> **Key Strategy:** Sort the array first, then use **Two Pointers** (`left` and `right`) to minimize $| \text{current\_sum} - \text{target} |$!

1. **Brute Force:** Checking every triplet combination takes $\mathcal{O}(N^3)$ time.
2. **Two Pointers Strategy:**
   - **Sort** `nums` in ascending order.
   - Fix the first element `nums[i]` across a loop.
   - Place two pointers for the remaining sub-array: `left = i + 1` and `right = n - 1`.
   - Calculate `current = nums[i] + nums[left] + nums[right]`.
   - If $| \text{current} - \text{target} | < | \text{closest} - \text{target} |$, update `closest = current`.
   - **Pointer Movement:**
     - If `current == target`: Distance is zero! Return `current` immediately (exact match).
     - If `current < target`: We need a larger sum $\rightarrow$ move `left += 1`.
     - If `current > target`: We need a smaller sum $\rightarrow$ move `right -= 1`.

---

## 4. Thought Process

```mermaid
flowchart TD
    A[Start: Input nums, target] --> B[Sort nums in ascending order]
    B --> C[Initialize closest = nums[0] + nums[1] + nums[2]]
    C --> D[Loop i from 0 to n - 3]
    D --> E[Set left = i + 1, right = n - 1]
    E --> F{Is left < right?}
    F -- Yes --> G[Compute current = nums[i] + nums[left] + nums[right]]
    G --> H{abs current - target < abs closest - target?}
    H -- Yes --> I[Update closest = current]
    H -- No --> J{Is current == target?}
    I --> J
    J -- Yes --> K[Return current exact match]
    J -- No --> L{Is current < target?}
    L -- Yes --> M[Increase sum: left += 1]
    L -- No --> N[Decrease sum: right -= 1]
    M --> F
    N --> F
    F -- No --> D
    D -- Loop Finished --> O[Return closest]
```

1. **Sort Input Array:**
   - Run `nums.sort()`.

2. **Initialize Closest Tracker:**
   - Set `closest = nums[0] + nums[1] + nums[2]`.

3. **Outer Loop (Fixing `nums[i]`):**
   - Iterate `i` from `0` to `n - 3`.

4. **Inner Two Pointers Loop (`left` & `right`):**
   - Set `left = i + 1`, `right = n - 1`.
   - While `left < right`:
     - `current = nums[i] + nums[left] + nums[right]`
     - If `abs(current - target) < abs(closest - target)`: `closest = current`
     - If `current == target`: `return current` (early exit)
     - Elif `current < target`: `left += 1`
     - Else: `right -= 1`

5. **Return Closest Sum:**
   - Return `closest`.

---

## 5. Concepts Used

### 1. Two Pointers Distance Minimization
- **What it is:** Moving left and right boundary pointers inward on a sorted array to minimize absolute distance from a target.
- **Why it is used here:** Reduces triplet search from $\mathcal{O}(N^3)$ to $\mathcal{O}(N^2)$ while dynamically tracking the minimal difference $| \text{current} - \text{target} |$.
- **Future applications:** 3Sum, 4Sum, Two Sum II, Subarray Product.

### 2. Early Return Optimization
- **What it is:** Terminating execution as soon as an exact distance match ($0$) is discovered.
- **Why it is used here:** Avoids redundant iterations when a perfect triplet sum equals `target`.
- **Future applications:** Binary Search, Matrix Search.

---

## 6. Algorithm Used

### Sorting + Two Pointers Distance Minimization

- **Algorithm Category:** Array / Two Pointers / Sorting
- **Why selected:** Provides an optimal $\mathcal{O}(N^2)$ runtime with $\mathcal{O}(1)$ auxiliary space and straightforward implementation.
- **Time Complexity:** $\mathcal{O}(N^2)$
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

---

## 7. Code Walkthrough

Below is the line-by-line breakdown of the submitted solution:

```python
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # Line 9: Sort array to enable Two Pointers directional convergence
        nums.sort()
        n = len(nums)

        # Line 12: Initialize closest sum tracker with first three elements
        closest = nums[0] + nums[1] + nums[2]

        # Line 14: Loop fixing first element nums[i]
        for i in range(n - 2):

            # Line 16-17: Initialize left and right pointers for remaining sub-array
            left = i + 1
            right = n - 1

            # Line 19: Convergence loop for two pointers
            while left < right:

                # Line 21: Calculate current triplet sum
                current = nums[i] + nums[left] + nums[right]

                # Line 24-25: Update closest sum if current triplet is closer to target
                if abs(current - target) < abs(closest - target):
                    closest = current

                # Line 28-29: Perfect match (distance is 0), return immediately
                if current == target:
                    return current

                # Line 31-32: Current sum too small, move left pointer rightward
                elif current < target:
                    left += 1

                # Line 34-35: Current sum too large, move right pointer leftward
                else:
                    right -= 1

        # Line 37: Return best closest sum found
        return closest
```

---

## 8. Dry Run

Let's dry run for `nums = [-1, 2, 1, -4]` ($n=4$) and `target = 1`.

### Sorted Array
`nums = [-4, -1, 1, 2]`

### Execution Trace
- Initial `closest = -4 + (-1) + 1 = -4`. `abs(-4 - 1) = 5`.

| `i` | `nums[i]` | `left` | `right` | `current` ($nums[i]+nums[L]+nums[R]$) | `abs(current - 1)` | `closest` (After) | `abs(closest - 1)` | Action |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **0** | `-4` | `1` (`-1`) | `3` (`2`) | $-4 + (-1) + 2 = \mathbf{-3}$ | $|-3 - 1| = 4$ | **`-3`** | `4` | `current < 1` $\rightarrow$ `left += 1` |
| **0** | `-4` | `2` (`1`) | `3` (`2`) | $-4 + 1 + 2 = \mathbf{-1}$ | $|-1 - 1| = 2$ | **`-1`** | `2` | `current < 1` $\rightarrow$ `left += 1` |
| **0** | `-4` | `3` | `3` | - | - | `-1` | `2` | `left == right` $\rightarrow$ Next `i` |
| **1** | `-1` | `2` (`1`) | `3` (`2`) | $-1 + 1 + 2 = \mathbf{2}$ | $|2 - 1| = 1$ | **`2`** | `1` | `current > 1` $\rightarrow$ `right -= 1` |
| **1** | `-1` | `2` | `2` | - | - | `2` | `1` | `left == right` $\rightarrow$ Loop Ends |

### Output
Returns **`2`**.

---

## 9. Complexity Analysis

### Time Complexity: $\mathcal{O}(N^2)$
- **Sorting:** `nums.sort()` takes $\mathcal{O}(N \log N)$ time.
- **Nested Loop Search:** Outer loop runs $N$ times. Inner two-pointer loop runs in $\mathcal{O}(N)$ time. Combined nested search takes $\mathcal{O}(N^2)$ time.
- **Overall Time Complexity:** $\mathcal{O}(N \log N + N^2) = \mathcal{O}(N^2)$.

### Space Complexity: $\mathcal{O}(1)$ Auxiliary Space
- Uses primitive scalar variables (`closest`, `current`, `i`, `left`, `right`).
- Algorithm auxiliary space is $\mathcal{O}(1)$ constant memory.

---

## 10. Edge Cases

| Edge Case Scenario | Input Example | Behavior & Output | How Code Handles It |
| :--- | :--- | :--- | :--- |
| **Minimum Array Size (3)**| `nums = [1, 2, 3]`, `target = 1` | Output: `6` | Outer loop runs once (`i=0`), returns $1+2+3=6$. |
| **Exact Target Match** | `nums = [-1, 0, 1]`, `target = 0` | Output: `0` | Triggers `if current == target: return current` early exit. |
| **All Identical Elements**| `nums = [1, 1, 1, 1]`, `target = 10` | Output: `3` | Traverses pointers smoothly and outputs `3`. |
| **Target Far Outside Range**| `nums = [10, 20, 30]`, `target = -100` | Output: `60` | Computes minimum sum `60` as closest. |

---

## 11. Alternative Approaches

### Approach 1: Brute Force Triple Loop ($\mathcal{O}(N^3)$ Time, $\mathcal{O}(1)$ Space)
- **Idea:** Test all triplet combinations `(i, j, k)` using three nested loops.
- **Drawback:** Inefficient for $N = 500$ ($1.25 \times 10^8$ operations).

### Approach 2: Binary Search on 3rd Element ($\mathcal{O}(N^2 \log N)$ Time, $\mathcal{O}(1)$ Space)
- **Idea:** Fix `i` and `j`, then use binary search `bisect` for the closest `k` value.
- **Drawback:** $\mathcal{O}(N^2 \log N)$ is slower than Two Pointers $\mathcal{O}(N^2)$.

### Approach 3: Sorting + Two Pointers (User's Solution - Recommended)
- **Idea:** Sort array, fix `i`, and use convergent `left` and `right` pointers.
- **Complexity:** $\mathcal{O}(N^2)$ time, $\mathcal{O}(1)$ space.
- **Why Optimal:** Standard interview approach, optimal time and auxiliary space.

---

## 12. Common Mistakes

> [!WARNING]
> 1. **Initializing `closest` to 0:** Setting `closest = 0` before checking can produce wrong answers if the true closest sum is non-zero (e.g. `target = 100`, array sum is `60`). Always initialize to `nums[0] + nums[1] + nums[2]`.
> 2. **Forgetting to Sort `nums`:** Two Pointers require sorted order to determine whether to increment `left` or decrement `right`.
> 3. **Not Using Absolute Distance:** Comparing `current - target < closest - target` without `abs()` causes negative distances to miscalculate comparison.

---

## 13. Interview Questions

1. **Q: Why do we initialize `closest = nums[0] + nums[1] + nums[2]` instead of `float('inf')`?**
   - *A:* Initializing with a valid triplet sum guarantees that `closest` holds a valid return value of the correct data type even for $N=3$ arrays, avoiding infinity comparison edge cases.

2. **Q: How does 3Sum Closest differ from standard 3Sum (LC #15)?**
   - *A:* Standard 3Sum finds *exact* zero sums and requires duplicate triplet removal. 3Sum Closest finds the *minimal distance* sum to a target, returning a single scalar integer without needing duplicate triplet tracking.

3. **Q: Can we optimize 3Sum Closest further using early termination?**
   - *A:* Yes! If `current == target`, distance is 0 (the theoretical minimum possible difference), so returning `current` immediately saves remaining loop iterations.

---

## 14. Similar Problems

- **Easy:**
  - [LeetCode #1 - Two Sum](https://leetcode.com/problems/two-sum/)
- **Medium:**
  - [LeetCode #15 - 3Sum](https://leetcode.com/problems/3sum/)
  - [LeetCode #18 - 4Sum](https://leetcode.com/problems/4sum/)
  - [LeetCode #923 - 3Sum With Multiplicity](https://leetcode.com/problems/3sum-with-multiplicity/)

---

## 15. Learning Summary

- **Pattern Recognized:** Sorting + Two Pointers Distance Minimization.
- **Distance Formula:** Minimizing $| \text{current} - \text{target} |$.
- **Early Exit:** Returning immediately when `current == target`.

---

## 16. Optimization Notes

Your solution is **100% optimal** ($\mathcal{O}(N^2)$ Time, $\mathcal{O}(1)$ Auxiliary Space). It is clean, readable, and represents interview best practices!
