# 0001. Two Sum

![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen?style=for-the-badge)
![Topic: Array](https://img.shields.io/badge/Topic-Array-blue?style=for-the-badge)
![Topic: Hash Table](https://img.shields.io/badge/Topic-Hash%20Table-purple?style=for-the-badge)

---

## 1. Problem Information

- **Problem Name:** Two Sum
- **LeetCode Number:** 1
- **Difficulty:** Easy
- **Tags:** Array, Hash Table
- **Language Used:** Python
- **Problem Link:** [LeetCode #1 - Two Sum](https://leetcode.com/problems/two-sum/)

---

## 2. Problem Overview

Given an array of integers `nums` and an integer `target`, return the **0-based indices** of the two numbers such that they add up to `target`.

### Input & Output Specifications
- **Input:**
  - `nums`: An array of integers.
  - `target`: An integer target sum.
- **Output:** A list containing the two indices `[index1, index2]`.
- **Constraints & Rules:**
  - $2 \le \text{len}(nums) \le 10^4$
  - $-10^9 \le \text{nums}[i] \le 10^9$
  - $-10^9 \le \text{target} \le 10^9$
  - **Exactly one valid answer exists.**
  - You may not use the same element twice.

### Examples
- **Example 1:**
  - **Input:** `nums = [2,7,11,15]`, `target = 9`
  - **Output:** `[0, 1]` (Because `nums[0] + nums[1] == 2 + 7 == 9`).
- **Example 2:**
  - **Input:** `nums = [3,2,4]`, `target = 6`
  - **Output:** `[1, 2]`
- **Example 3:**
  - **Input:** `nums = [3,3]`, `target = 6`
  - **Output:** `[0, 1]`

### Real-World Intuition
Think of an online shopping cart checkout where a customer has a \$50 gift voucher (`target`). To maximize the coupon, the server wants to find two items in the cart whose total sum equals exactly \$50. Instead of checking every pair of items in the cart, the system checks if `50 - current_item_price` is already present in the user's cart lookup table.

---

## 3. Intuition

> [!TIP]
> **Key Insight:** Transform the 2-variable problem ($A + B = \text{target}$) into a 1-variable lookup problem ($B = \text{target} - A$)!

A brute-force solution checks every pair $(i, j)$ to see if `nums[i] + nums[j] == target`, taking $\mathcal{O}(N^2)$ time.

We can optimize this to $\mathcal{O}(N)$ by keeping track of the numbers we have already seen in a **Hash Map** (`seen` dictionary):
1. For each number `nums[i]`, calculate its required matching value: `complement = target - nums[i]`.
2. Check if `complement` is already in our `seen` dictionary.
3. If it is in `seen`, we immediately return `[seen[complement], i]`.
4. If it is not in `seen`, we add `seen[nums[i]] = i` and continue to the next element.

---

## 4. Thought Process

```mermaid
flowchart TD
    A[Start: Input nums, target] --> B[Initialize seen = empty dictionary]
    B --> C[Loop index i from 0 to len(nums) - 1]
    C --> D[Calculate complement = target - nums[i]]
    D --> E{Is complement in seen?}
    E -- Yes --> F[Return array: [seen[complement], i]]
    E -- No --> G[Store seen[nums[i]] = i]
    G --> H{More elements in nums?}
    H -- Yes --> C
    H -- No --> I[End]
```

1. **Hash Map Allocation:**
   - Create an empty dictionary `seen = {}`. Keys will be array numbers, and values will be their corresponding array indices.

2. **Single Pass Iteration:**
   - Iterate through index `i` from `0` to `len(nums) - 1`.
   - At each step, compute `complement = target - nums[i]`.

3. **Instant Lookup:**
   - Query `if complement in seen:`
     - **Match Found:** Return `[seen[complement], i]`. Because we check prior to inserting `nums[i]`, we automatically prevent using the exact same array element twice!
     - **No Match:** Record `seen[nums[i]] = i` to make the current number available as a potential complement for future iterations.

---

## 5. Concepts Used

### 1. Hash Table / Dictionary Lookups
- **What it is:** A data structure offering average $\mathcal{O}(1)$ time complexity for insertions and key lookups using key hashing.
- **Why it is used here:** Reduces element lookup time from $\mathcal{O}(N)$ linear scan to $\mathcal{O}(1)$ instant dictionary check.
- **Future applications:** Contains Duplicate, Group Anagrams, Longest Consecutive Sequence.

### 2. Complement Algebra
- **What it is:** Expressing target relationship algebraically: $B = \text{target} - A$.
- **Why it is used here:** Allows single-pass search without double-loop combinations.
- **Future applications:** 3Sum, 4Sum, Two Sum II, Subarray Sum Equals K.

---

## 6. Algorithm Used

### One-Pass Hash Map Lookup

- **Algorithm Category:** Array / Hash Table
- **Why selected:** Optimal $\mathcal{O}(N)$ time complexity in a single pass without needing sorted input.
- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(N)$

---

## 7. Code Walkthrough

Below is the line-by-line breakdown of the accepted Python solution:

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Line 9: Initialize Hash Map
        # 'seen' maps number values to their corresponding index in nums
        seen = {}

        # Line 11: Iterate through array index i
        for i in range(len(nums)):
            # Line 12: Calculate the required complementary value needed to reach target
            complement = target - nums[i]

            # Line 14-15: Instant Hash Map Lookup
            # If complement exists in seen, return pair of indices immediately
            if complement in seen:
                return [seen[complement], i]

            # Line 17: Store current number and its index in seen for future elements
            seen[nums[i]] = i
```

---

## 8. Dry Run

Let's dry run the solution with `nums = [2, 7, 11, 15]` and `target = 9`.

### Initial State
- `seen = {}`
- `target = 9`

### Step-by-Step Execution

| Step `i` | `nums[i]` | `complement` (`9 - nums[i]`) | Check `complement in seen` | Action | State of `seen` (After) | Output |
| :---: | :---: | :---: | :---: | :--- | :--- | :---: |
| **0** | `2` | `9 - 2 = 7` | `'7' in {}` $\rightarrow$ False | Store `seen[2] = 0` | `{2: 0}` | - |
| **1** | `7` | `9 - 7 = 2` | `'2' in {2: 0}` $\rightarrow$ **True!** | Found! Return `[seen[2], 1]` | `{2: 0}` | **`[0, 1]`** |

---

## 9. Complexity Analysis

### Time Complexity: $\mathcal{O}(N)$
- **Array Traversal:** The `for` loop iterates through the list of length $N$ at most once.
- **Hash Table Operations:** Dictionary lookup `complement in seen` and insertion `seen[nums[i]] = i` take $\mathcal{O}(1)$ average time.
- **Overall Time Complexity:** $\mathcal{O}(N)$ across Best, Average, and Worst cases.

### Space Complexity: $\mathcal{O}(N)$
- **Auxiliary Hash Map:** In the worst-case scenario (e.g. solution is found at the last pair), `seen` stores up to $N - 1$ key-value pairs.
- **Overall Space Complexity:** $\mathcal{O}(N)$ extra space.

---

## 10. Edge Cases

| Edge Case Scenario | Input Example | Behavior & Output | How Code Handles It |
| :--- | :--- | :--- | :--- |
| **Duplicate Values** | `nums = [3, 3]`, `target = 6` | Output: `[0, 1]` | `i=0` stores `{3: 0}`. At `i=1`, `complement = 3` matches `seen[3]=0`. Returns `[0, 1]`. |
| **Negative Numbers** | `nums = [-3, 4, 3, 90]`, `target = 0` | Output: `[0, 2]` | `target - (-3) = 3`. Matches when `nums[2]=3` is visited. |
| **Negative Target** | `nums = [-1, -2, -3, -4]`, `target = -5` | Output: `[1, 2]` | `(-5) - (-3) = -2`. Handles negative arithmetic seamlessly. |
| **Minimum Size Array** | `nums = [1, 5]`, `target = 6` | Output: `[0, 1]` | Traverses loop twice and returns `[0, 1]`. |

---

## 11. Alternative Approaches

### Approach 1: Brute Force Double Loop ($\mathcal{O}(N^2)$ Time, $\mathcal{O}(1)$ Space)
- **Idea:** Test all pairs `(i, j)` where `i != j` using nested loops.
- **Drawback:** Slow for $N = 10,000$ ($10^8$ operations).

### Approach 2: Sorting + Two Pointers ($\mathcal{O}(N \log N)$ Time, $\mathcal{O}(N)$ Space)
- **Idea:** Sort array while storing original indices, then use two pointers (`left` at 0, `right` at end) moving inward based on sum comparison with `target`.
- **Drawback:** Requires $\mathcal{O}(N \log N)$ sorting time and extra space to preserve original index positions.

### Approach 3: One-Pass Hash Map (User's Solution - Optimal)
- **Idea:** Single pass hash map lookup.
- **Complexity:** $\mathcal{O}(N)$ time, $\mathcal{O}(N)$ space.
- **Why Optimal:** Fast, single pass, optimal time complexity.

---

## 12. Common Mistakes

> [!WARNING]
> 1. **Two-Pass Hash Map Index Collision:** If all elements are populated into the hash map *before* searching, checking `complement in seen` for `nums = [3, 2, 4], target = 6` at `i=0` (`nums[0]=3`) finds `seen[3]=0` and incorrectly pairs an element with itself unless explicit index inequality checks (`seen[complement] != i`) are written.
> 2. **Returning Values Instead of Indices:** Returning `[nums[i], complement]` instead of the index array `[seen[complement], i]`.
> 3. **Modifying/Sorting `nums` in Place:** Sorting `nums` directly destroys original index positions required by the problem statement.

---

## 13. Interview Questions

1. **Q: Why is the One-Pass Hash Map preferred over Two-Pass Hash Map?**
   - *A:* One-Pass checks for complements prior to insertion, naturally preventing an element from matching with itself and completing in a single iteration.

2. **Q: How would you solve this problem if the input array is already sorted?**
   - *A:* We can use **Two Pointers** (LeetCode #167) in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ auxiliary space without needing a hash map.

3. **Q: What if there are multiple pairs that add up to target and we need to return all unique pairs?**
   - *A:* This transforms into **3Sum / 2Sum unique pair variation**, requiring sorting and pointer skipping to avoid duplicate pairs in output.

---

## 14. Similar Problems

- **Easier:**
  - [LeetCode #167 - Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
  - [LeetCode #217 - Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
- **Similar Difficulty:**
  - [LeetCode #15 - 3Sum](https://leetcode.com/problems/3sum/)
  - [LeetCode #560 - Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
- **Harder:**
  - [LeetCode #18 - 4Sum](https://leetcode.com/problems/4sum/)
  - [LeetCode #149 - Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/)

---

## 15. Learning Summary

- **Pattern Recognized:** Complement Lookup using Hash Map ($B = \text{target} - A$).
- **Efficiency Boost:** Upgrading lookup time from $\mathcal{O}(N)$ to $\mathcal{O}(1)$ reduces overall complexity from $\mathcal{O}(N^2)$ to $\mathcal{O}(N)$.
- **Key Takeaway:** Hash maps are ideal for turning nested search loops into single-pass linear scans.

---

## 16. Optimization Notes

Your code is **100% optimal** ($\mathcal{O}(N)$ Time, $\mathcal{O}(N)$ Space). It represents the exact standard solution expected in top-tier technical interviews!
