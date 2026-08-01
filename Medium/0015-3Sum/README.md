# 0015. 3Sum

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)
![Topic: Array](https://img.shields.io/badge/Topic-Array-blue?style=for-the-badge)
![Topic: Two Pointers](https://img.shields.io/badge/Topic-Two%20Pointers-purple?style=for-the-badge)
![Topic: Sorting](https://img.shields.io/badge/Topic-Sorting-green?style=for-the-badge)

---

## 1. Problem Information

- **Problem Name:** 3Sum
- **LeetCode Number:** 15
- **Difficulty:** Medium
- **Tags:** Array, Two Pointers, Sorting
- **Language Used:** Python
- **Problem Link:** [LeetCode #15 - 3Sum](https://leetcode.com/problems/3sum/)

---

## 2. Problem Overview

Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that:
1. $i \neq j$, $i \neq k$, and $j \neq k$
2. $\text{nums}[i] + \text{nums}[j] + \text{nums}[k] == 0$

Notice that the solution set **must not contain duplicate triplets**.

### Input & Output Specifications
- **Input:** `nums`: An integer array ($3 \le \text{len}(nums) \le 3000$).
- **Output:** A list of unique integer triplet lists.
- **Constraints:** $-10^5 \le \text{nums}[i] \le 10^5$.

### Examples
- **Example 1:**
  - **Input:** `nums = [-1,0,1,2,-1,-4]`
  - **Output:** `[[-1,-1,2],[-1,0,1]]`
  - **Explanation:**
    - `nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0`.
    - `nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0`.
    - `nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0`.
    - The unique triplets are `[-1,0,1]` and `[-1,-1,2]`.
- **Example 2:**
  - **Input:** `nums = [0,1,1]` $\rightarrow$ **Output:** `[]`
- **Example 3:**
  - **Input:** `nums = [0,0,0]` $\rightarrow$ **Output:** `[[0,0,0]]`

---

## 3. Intuition

> [!TIP]
> **Key Strategy:** Sort the array first! Sorting enables the **Two Pointers** technique and makes skipping duplicate elements effortless.

1. **Brute Force:** Checking every triplet combination $(i, j, k)$ takes $\mathcal{O}(N^3)$ time, which will result in Time Limit Exceeded (TLE) for $N = 3000$.
2. **Two Pointers Reduction:**
   - If we **sort** `nums` in ascending order, we can iterate through the array fixing `nums[i]` as the first element.
   - The problem then reduces to finding two numbers in `nums[i+1...n-1]` that sum to `-nums[i]` (Two Sum on a sorted sub-array).
   - Place `left = i + 1` and `right = n - 1`.
   - Calculate `total = nums[i] + nums[left] + nums[right]`:
     - If `total == 0`: Found a valid triplet! Save it, and shift both pointers inward while skipping duplicates.
     - If `total < 0`: Sum is too small $\rightarrow$ move `left += 1` to increase sum.
     - If `total > 0`: Sum is too large $\rightarrow$ move `right -= 1` to decrease sum.

---

## 4. Thought Process

```mermaid
flowchart TD
    A[Start: Input nums] --> B[Sort nums in ascending order]
    B --> C[Initialize result = empty list]
    C --> D[Loop i from 0 to n - 3]
    D --> E{Is i > 0 and nums[i] == nums[i-1]?}
    E -- Yes --> F[Skip duplicate i: continue]
    F --> D
    E -- No --> G[Set left = i + 1, right = n - 1]
    G --> H{Is left < right?}
    H -- Yes --> I[total = nums[i] + nums[left] + nums[right]]
    I --> J{total == 0?}
    J -- Yes --> K[Append triplet to result]
    K --> L[left += 1, right -= 1]
    L --> M[Skip duplicate left and right values]
    M --> H
    J -- total < 0 --> N[left += 1]
    N --> H
    J -- total > 0 --> O[right -= 1]
    O --> H
    H -- No --> D
    D -- Loop Finished --> P[Return result]
```

1. **Sort the Input Array:**
   - Execute `nums.sort()`.

2. **Outer Loop (Fixing `nums[i]`):**
   - Iterate `i` from `0` to `n - 3`.
   - **Skip Duplicates for `i`:** If `i > 0` and `nums[i] == nums[i-1]`, skip to avoid duplicate triplets starting with the same value.

3. **Inner Two Pointers Search (`left` & `right`):**
   - Set `left = i + 1`, `right = n - 1`.
   - While `left < right`:
     - Compute `total = nums[i] + nums[left] + nums[right]`.
     - **If `total == 0`:**
       - Append `[nums[i], nums[left], nums[right]]` to `result`.
       - Advance `left += 1` and `right -= 1`.
       - **Skip Duplicate `left` values:** `while left < right and nums[left] == nums[left - 1]: left += 1`.
       - **Skip Duplicate `right` values:** `while left < right and nums[right] == nums[right + 1]: right -= 1`.
     - **If `total < 0`:** Shift `left += 1`.
     - **If `total > 0`:** Shift `right -= 1`.

4. **Return Answer:**
   - Return `result`.

---

## 5. Concepts Used

### 1. Two Pointers Search on Sorted Array
- **What it is:** Using two pointer indices (`left`, `right`) moving towards each other based on comparison of their combined sum against a target.
- **Why it is used here:** Reduces pair search complexity from $\mathcal{O}(N^2)$ to $\mathcal{O}(N)$ per fixed element.
- **Future applications:** 3Sum Closest, 4Sum, Two Sum II, Container With Most Water.

### 2. Duplicate Skipping / De-duplication
- **What it is:** Explicitly advancing pointer indices whenever adjacent elements are identical.
- **Why it is used here:** Guarantees unique output triplets without needing expensive post-processing set conversions.
- **Future applications:** Combination Sum II, Permutations II, 4Sum.

---

## 6. Algorithm Used

### Sorting + Two Pointers Strategy

- **Algorithm Category:** Array / Two Pointers / Sorting
- **Why selected:** It optimizes runtime from $\mathcal{O}(N^3)$ brute force down to $\mathcal{O}(N^2)$ with $\mathcal{O}(1)$ auxiliary space.
- **Time Complexity:** $\mathcal{O}(N^2)$
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

---

## 7. Code Walkthrough

Below is the line-by-line breakdown of the submitted solution:

```python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # Line 9: Sort input array to enable Two Pointers and duplicate skipping
        nums.sort()
        result = []

        n = len(nums)

        # Line 14: Loop fixing the first element nums[i]
        for i in range(n - 2):

            # Line 17-18: Skip duplicate first elements to prevent duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Line 20-21: Two Pointers initialization for sub-array nums[i+1...n-1]
            left = i + 1
            right = n - 1

            # Line 23: Convergence loop for two pointers
            while left < right:

                total = nums[i] + nums[left] + nums[right]

                # Line 27-28: Matching triplet found
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Line 34-35: Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Line 38-39: Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                # Line 41-42: Sum too small, move left pointer rightward
                elif total < 0:
                    left += 1

                # Line 44-45: Sum too large, move right pointer leftward
                else:
                    right -= 1

        # Line 47: Return list of all unique triplets found
        return result
```

---

## 8. Dry Run

Let's dry run for `nums = [-1, 0, 1, 2, -1, -4]`.

### Sorted Array
`nums = [-4, -1, -1, 0, 1, 2]` ($n=6$)

### Iteration Trace

| `i` | `nums[i]` | `left` | `right` | `total` ($nums[i]+nums[L]+nums[R]$) | Action | `result` State |
| :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **0** | `-4` | `1` (`-1`) | `5` (`2`) | $-4 + (-1) + 2 = -3$ | `total < 0` $\rightarrow$ `left += 1` | `[]` |
| **0** | `-4` | `2` (`-1`) | `5` (`2`) | $-4 + (-1) + 2 = -3$ | `total < 0` $\rightarrow$ `left += 1` | `[]` |
| **0** | `-4` | `3` (`0`) | `5` (`2`) | $-4 + 0 + 2 = -2$ | `total < 0` $\rightarrow$ `left += 1` | `[]` |
| **0** | `-4` | `4` (`1`) | `5` (`2`) | $-4 + 1 + 2 = -1$ | `total < 0` $\rightarrow$ `left += 1` | `[]` |
| **0** | `-4` | `5` | `5` | - | `left == right` $\rightarrow$ Next `i` | `[]` |
| **1** | `-1` | `2` (`-1`) | `5` (`2`) | $-1 + (-1) + 2 = \mathbf{0}$ | **Found!** Append `[-1,-1,2]`, move `L=3, R=4` | `[[-1,-1,2]]` |
| **1** | `-1` | `3` (`0`) | `4` (`1`) | $-1 + 0 + 1 = \mathbf{0}$ | **Found!** Append `[-1,0,1]`, move `L=4, R=3` | `[[-1,-1,2], [-1,0,1]]` |
| **2** | `-1` | - | - | `nums[2] == nums[1]` (`-1 == -1`) | **Skip duplicate `i=2`!** | `[[-1,-1,2], [-1,0,1]]` |
| **3** | `0` | `4` (`1`) | `5` (`2`) | $0 + 1 + 2 = 3$ | `total > 0` $\rightarrow$ `right -= 1` | `[[-1,-1,2], [-1,0,1]]` |

### Output
Returns **`[[-1, -1, 2], [-1, 0, 1]]`**.

---

## 9. Complexity Analysis

### Time Complexity: $\mathcal{O}(N^2)$
- **Sorting:** `nums.sort()` takes $\mathcal{O}(N \log N)$ time.
- **Nested Search:** Outer loop runs $N$ times. Inner two-pointer loop runs in $\mathcal{O}(N)$ time. Combined nested search takes $\mathcal{O}(N^2)$ time.
- **Overall Time Complexity:** $\mathcal{O}(N \log N + N^2) = \mathcal{O}(N^2)$.

### Space Complexity: $\mathcal{O}(1)$ Auxiliary Space
- Uses only primitive pointer variables (`i`, `left`, `right`, `total`).
- In Python, Timsort takes $\mathcal{O}(N)$ memory stack space for sorting, but auxiliary space for the algorithm itself is $\mathcal{O}(1)$ (excluding output list).

---

## 10. Edge Cases

| Edge Case Scenario | Input Example | Behavior & Output | How Code Handles It |
| :--- | :--- | :--- | :--- |
| **All Zeroes** | `nums = [0, 0, 0]` | Output: `[[0, 0, 0]]` | `i=0` finds `[0,0,0]`, inner duplicate loops advance `left` and `right` to exit cleanly. |
| **All Positive** | `nums = [1, 2, 3]` | Output: `[]` | `total > 0` everywhere, `right` shifts to left boundary without matches. |
| **Duplicates Galore** | `nums = [-2, 0, 0, 2, 2]` | Output: `[[-2, 0, 2]]` | Inner duplicate skipping loops prevent duplicate `[-2,0,2]` entries. |
| **Minimum Length (3)**| `nums = [0, 1, -1]` | Output: `[[-1, 0, 1]]` | Sorts to `[-1, 0, 1]`, `i=0` matches triplet immediately. |

---

## 11. Alternative Approaches

### Approach 1: Brute Force Triple Loop ($\mathcal{O}(N^3)$ Time, $\mathcal{O}(1)$ Space)
- **Idea:** Test all triplet combinations `(i, j, k)` using three nested loops.
- **Drawback:** Time Limit Exceeded (TLE) for $N = 3000$ ($2.7 \times 10^{10}$ operations).

### Approach 2: Hash Set 2Sum Conversion ($\mathcal{O}(N^2)$ Time, $\mathcal{O}(N)$ Space)
- **Idea:** Fix `nums[i]` and use a Hash Set for the remaining 2Sum lookup.
- **Drawback:** Requires allocating extra set memory and converting output triplets into sets to remove duplicate combinations.

### Approach 3: Sorting + Two Pointers (User's Solution - Recommended)
- **Idea:** Sort array, fix `i`, and use two pointers (`left`, `right`) with inline de-duplication.
- **Complexity:** $\mathcal{O}(N^2)$ time, $\mathcal{O}(1)$ auxiliary space.
- **Why Optimal:** Standard interview solution; zero extra hash map allocations, clean inline de-duplication.

---

## 12. Common Mistakes

> [!WARNING]
> 1. **Forgetting to Sort `nums`:** Attempting Two Pointers on an unsorted array causes incorrect pointer movement (`left += 1` vs `right -= 1`).
> 2. **Forgetting De-duplication for `i`:** Omitting `if i > 0 and nums[i] == nums[i - 1]: continue` yields duplicate triplet combinations in the output.
> 3. **Forgetting De-duplication for `left` / `right`:** Failing to skip duplicates after `total == 0` causes duplicate triplets when multiple identical values exist in `nums`.

---

## 13. Interview Questions

1. **Q: Why is sorting `nums` beneficial for 3Sum?**
   - *A:* Sorting allows us to use two pointers (`left` and `right`) to find target sums in linear $\mathcal{O}(N)$ time per element, and makes duplicate skipping simple by grouping identical elements adjacent to each other.

2. **Q: Can we optimize 3Sum further if `nums[i] > 0`?**
   - *A:* Yes! If `nums[i] > 0` in the sorted array, we can break early because all subsequent elements are also $> 0$, making a sum of $0$ impossible.

3. **Q: How would you extend this approach to solve 4Sum (LeetCode #18)?**
   - *A:* Add another outer loop fixing the second element `nums[j]`, then run the same Two Pointers logic on the remaining inner pair, achieving $\mathcal{O}(N^3)$ time complexity.

---

## 14. Similar Problems

- **Easy:**
  - [LeetCode #1 - Two Sum](https://leetcode.com/problems/two-sum/)
  - [LeetCode #167 - Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
- **Medium:**
  - [LeetCode #16 - 3Sum Closest](https://leetcode.com/problems/3sum-closest/)
  - [LeetCode #18 - 4Sum](https://leetcode.com/problems/4sum/)
  - [LeetCode #923 - 3Sum With Multiplicity](https://leetcode.com/problems/3sum-with-multiplicity/)

---

## 15. Learning Summary

- **Pattern Recognized:** Sorting + Two Pointers for Multi-Element Sum Constraints.
- **De-duplication Logic:** Skipping adjacent identical elements (`nums[k] == nums[k-1]`) at outer and inner loop levels.
- **Early Break Optimization:** Breaking when `nums[i] > 0` since sorted elements cannot sum to zero.

---

## 16. Optimization Notes

Your solution is **100% optimal** ($\mathcal{O}(N^2)$ Time, $\mathcal{O}(1)$ Auxiliary Space). It handles all edge cases, negative numbers, and duplicate triplets cleanly!
