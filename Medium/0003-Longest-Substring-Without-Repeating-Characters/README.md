# 0003. Longest Substring Without Repeating Characters

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)
![Topic: Hash Table](https://img.shields.io/badge/Topic-Hash%20Table-blue?style=for-the-badge)
![Topic: String](https://img.shields.io/badge/Topic-String-green?style=for-the-badge)
![Topic: Sliding Window](https://img.shields.io/badge/Topic-Sliding%20Window-purple?style=for-the-badge)

---

## 1. Problem Information

- **Problem Name:** Longest Substring Without Repeating Characters
- **LeetCode Number:** 3
- **Difficulty:** Medium
- **Tags:** Hash Table, String, Sliding Window, Two Pointers
- **Language Used:** Python
- **Problem Link:** [LeetCode #3 - Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

## 2. Problem Overview

Given a string `s`, find the length of the **longest contiguous substring** that contains **no duplicate characters**.

### Input & Output Specifications
- **Input:** A string `s` of length $N$.
- **Output:** An integer representing the length of the longest unique-character substring.
- **Constraints:**
  - $0 \le \text{len}(s) \le 5 \times 10^4$
  - `s` consists of English letters, digits, symbols, and spaces.

### Examples
- **Example 1:**
  - **Input:** `s = "abcabcbb"`
  - **Output:** `3` (The answer is `"abc"`, with length 3).
- **Example 2:**
  - **Input:** `s = "bbbbb"`
  - **Output:** `1` (The answer is `"b"`, with length 1).
- **Example 3:**
  - **Input:** `s = "pwwkew"`
  - **Output:** `3` (The answer is `"wke"`, with length 3. Note that `"pwke"` is a subsequence, not a substring).

### Real-World Intuition
Imagine a network router decoding continuous telemetry packets. To guarantee data integrity, the router must isolate the longest contiguous sequence of non-duplicate frame IDs before a duplicate frame forces a protocol reset. The sliding window acts as an active buffer that dynamically grows when receiving new IDs and contracts when collisions occur.

---

## 3. Intuition

> [!TIP]
> **Key Insight:** Maintain a dynamic "Sliding Window" `[left...right]` of unique characters using a Hash Set!

Instead of checking all $\mathcal{O}(N^2)$ possible substrings and checking for duplicates in $\mathcal{O}(N)$ time (total $\mathcal{O}(N^3)$ brute force), we can use **Two Pointers**:
1. Move the `right` pointer forward to expand the window by introducing character `s[right]`.
2. If `s[right]` is already present in our active character set (`char_set`), we have a collision.
3. We contract the window from the left by removing `s[left]` and incrementing `left += 1` repeatedly until `s[right]` is no longer in `char_set`.
4. Once `s[right]` is unique in the window, we insert it into `char_set` and update `max_length = max(max_length, right - left + 1)`.

---

## 4. Thought Process

```mermaid
flowchart TD
    A[Start: Input string s] --> B[Initialize char_set = empty set, left = 0, max_length = 0]
    B --> C[Loop right from 0 to len(s) - 1]
    C --> D{Is s[right] in char_set?}
    D -- Yes --> E[Remove s[left] from char_set]
    E --> F[Increment left by 1]
    F --> D
    D -- No --> G[Add s[right] to char_set]
    G --> H[Update max_length = max(max_length, right - left + 1)]
    H --> I{Finished loop for all right?}
    I -- No --> C
    I -- Yes --> J[Return max_length]
```

1. **Initialize State:**
   - `char_set`: A Python set storing characters present in the current active window `s[left..right]`.
   - `left`: Pointer marking the start of the current substring.
   - `max_length`: Integer recording the maximum unique substring length seen so far.

2. **Expand Right Boundary (`right` loop):**
   - For every character `s[right]`:
     - **Shrink Window on Collision:** While `s[right]` is in `char_set`, remove `s[left]` from `char_set` and shift `left` one step right (`left += 1`).
     - **Add New Character:** Insert `s[right]` into `char_set`.
     - **Track Maximum Length:** Calculate current window size as `right - left + 1` and update `max_length`.

3. **Return Result:**
   - After visiting all characters, return `max_length`.

---

## 5. Concepts Used

### 1. Dynamic Sliding Window
- **What it is:** A variable-size range defined by two pointers (`left` and `right`) that adjusts boundaries based on problem constraints.
- **Why it is used here:** Guarantees that every character is added and removed from the active window at most once, avoiding redundant rescans.
- **Future applications:** Minimum Window Substring, Max Consecutive Ones, Subarray Product Less Than K.

### 2. Hash Set (Lookups & Uniqueness)
- **What it is:** A hash-table-based data structure providing $\mathcal{O}(1)$ average time complexity for insertions, deletions, and lookup operations.
- **Why it is used here:** Allows instant detection of duplicate characters in the active window.
- **Future applications:** Contains Duplicate, Two Sum, Longest Consecutive Sequence.

---

## 6. Algorithm Used

### Sliding Window with Hash Set

- **Algorithm Category:** Two Pointers / Sliding Window
- **Why selected:** Extremely simple, highly efficient, and optimal $\mathcal{O}(N)$ time complexity.
- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(\min(N, M))$ where $M$ is the size of the alphabet/character set.

---

## 7. Code Walkthrough

Below is the line-by-line explanation of the submitted solution:

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Line 8-10: State Variable Initialization
        # char_set: HashSet holding unique characters in current sliding window s[left..right]
        # left: Left boundary pointer of sliding window
        # max_length: Track maximum valid window length found
        char_set = set()
        left = 0
        max_length = 0

        # Line 12: Iterate right pointer from 0 to len(s) - 1
        for right in range(len(s)):

            # Line 14-16: Duplicate Resolution Loop
            # While s[right] already exists in char_set, shrink window from left
            # by removing s[left] and incrementing left pointer.
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Line 18: Insert current character s[right] into unique character set
            char_set.add(s[right])

            # Line 19: Compute current window size (right - left + 1)
            # and update max_length if current window is larger.
            max_length = max(max_length, right - left + 1)

        # Line 21: Return the overall maximum length found
        return max_length
```

---

## 8. Dry Run

Let's dry run the solution with `s = "abcabcbb"`.

### Initial State
- `s = "abcabcbb"`, `len(s) = 8`.
- `char_set = set()`, `left = 0`, `max_length = 0`.

### Step-by-Step Execution

| `right` | `s[right]` | `while s[right] in char_set` Action | `left` (After) | `char_set` (After) | Window `s[left..right]` | Length (`right - left + 1`) | `max_length` |
| :---: | :---: | :--- | :---: | :--- | :---: | :---: | :---: |
| **0** | `'a'` | Not in set $\rightarrow$ No shrink | `0` | `{'a'}` | `"a"` | `0 - 0 + 1 = 1` | **1** |
| **1** | `'b'` | Not in set $\rightarrow$ No shrink | `0` | `{'a', 'b'}` | `"ab"` | `1 - 0 + 1 = 2` | **2** |
| **2** | `'c'` | Not in set $\rightarrow$ No shrink | `0` | `{'a', 'b', 'c'}` | `"abc"` | `2 - 0 + 1 = 3` | **3** |
| **3** | `'a'` | In set $\rightarrow$ Remove `s[0]` (`'a'`), `left=1` | `1` | `{'b', 'c', 'a'}` | `"bca"` | `3 - 1 + 1 = 3` | 3 |
| **4** | `'b'` | In set $\rightarrow$ Remove `s[1]` (`'b'`), `left=2` | `2` | `{'c', 'a', 'b'}` | `"cab"` | `4 - 2 + 1 = 3` | 3 |
| **5** | `'c'` | In set $\rightarrow$ Remove `s[2]` (`'c'`), `left=3` | `3` | `{'a', 'b', 'c'}` | `"abc"` | `5 - 3 + 1 = 3` | 3 |
| **6** | `'b'` | In set $\rightarrow$ Remove `s[3]` (`'a'`), `left=4`<br>Still in set $\rightarrow$ Remove `s[4]` (`'b'`), `left=5` | `5` | `{'c', 'b'}` | `"cb"` | `6 - 5 + 1 = 2` | 3 |
| **7** | `'b'` | In set $\rightarrow$ Remove `s[5]` (`'c'`), `left=6`<br>Still in set $\rightarrow$ Remove `s[6]` (`'b'`), `left=7` | `7` | `{'b'}` | `"b"` | `7 - 7 + 1 = 1` | 3 |

### Final Result
`max_length` = **`3`**

---

## 9. Complexity Analysis

### Time Complexity: $\mathcal{O}(N)$
- **Right Pointer Movement:** The outer loop executes $N$ times, incrementing `right` from `0` to $N-1$.
- **Left Pointer Movement:** The `while` loop increments `left` at most $N$ times across the entire runtime (since `left` never decreases).
- **Set Operations:** `add`, `remove`, and `in` operations on `char_set` run in $\mathcal{O}(1)$ average time.
- **Total Operations:** At most $2N$ steps $\rightarrow \mathcal{O}(N)$ overall.

### Space Complexity: $\mathcal{O}(\min(N, M))$ Auxiliary Space
- **Memory Allocation:** The `char_set` holds distinct characters in the current window.
- **Alphabet Bound:** $M$ is the size of the character set (e.g., $M = 128$ for ASCII or $M = 256$ for Extended ASCII).
- **Overall Space Complexity:** $\mathcal{O}(\min(N, M))$, which simplifies to $\mathcal{O}(1)$ for fixed character sets.

---

## 10. Edge Cases

| Edge Case Scenario | Input Example | Behavior & Output | How Code Handles It |
| :--- | :--- | :--- | :--- |
| **Empty String** | `s = ""` | Output: `0` | Loop does not execute (`range(0)`). Returns `max_length = 0`. |
| **Single Character** | `s = "a"` | Output: `1` | Loop runs once for `right=0`. Returns `max_length = 1`. |
| **All Duplicates** | `s = "bbbbb"` | Output: `1` | `while` loop removes previous character on every step. `max_length` stays `1`. |
| **All Unique Chars** | `s = "abcdef"` | Output: `6` | `while` loop never triggers. `max_length` grows to `6`. |
| **Spaces & Symbols** | `s = "a b c"` | Output: `3` | Spaces are treated as distinct characters in `char_set`. |

---

## 11. Alternative Approaches

### Approach 1: Brute Force All Substrings ($\mathcal{O}(N^3)$ Time, $\mathcal{O}(N)$ Space)
- **Idea:** Generate all $\mathcal{O}(N^2)$ substrings and use a set to check if each has unique characters in $\mathcal{O}(N)$ time.
- **Drawback:** Time Limit Exceeded (TLE) for $N = 50,000$.

### Approach 2: Sliding Window with HashSet (User's Solution - Recommended)
- **Idea:** Maintain `char_set` and shrink `left` pointer step-by-step when duplicate is hit.
- **Complexity:** $\mathcal{O}(N)$ time, $\mathcal{O}(\min(N, M))$ space.
- **Why Great:** Clean, easy to implement in interview settings, optimal time complexity.

### Approach 3: Optimized Sliding Window with HashMap / Index Array ($\mathcal{O}(N)$ Single-Pass Direct Jump)
- **Idea:** Store the last seen index of each character in a HashMap (`char_map`). When `s[right]` is encountered in `char_map`, jump `left = max(left, char_map[s[right]] + 1)` directly without a `while` loop!
- **Complexity:** $\mathcal{O}(N)$ time (single pass), $\mathcal{O}(\min(N, M))$ space.

---

## 12. Common Mistakes

> [!WARNING]
> 1. **Using `if` instead of `while` for duplicate removal:** Using `if s[right] in char_set:` only shifts `left` once. If the duplicate character is further right in the window, duplicates will remain in the set.
> 2. **Forgetting to increment `left` after `remove`:** Omitting `left += 1` causes an infinite `while` loop.
> 3. **Using Substring Slicing Inside Loops:** Doing `if s[right] in s[left:right]` performs an $\mathcal{O}(N)$ linear search per step, degrading total time to $\mathcal{O}(N^2)$.

---

## 13. Interview Questions

1. **Q: Why does the two-pointer sliding window run in $\mathcal{O}(N)$ time even though there is a nested `while` loop?**
   - *A:* Because `left` only moves forward and can be incremented at most $N$ times throughout the entire execution. Amortized time per element is $\mathcal{O}(1)$.

2. **Q: How can we skip the `while` loop when a duplicate is found?**
   - *A:* Use a HashMap mapping each character to its most recent index. When a duplicate is seen, jump `left` directly to `char_map[s[right]] + 1`.

3. **Q: What if the character set is strictly ASCII (128 characters)? How can we optimize memory?**
   - *A:* Replace `set()` with a fixed-size boolean or integer array of size 128 (e.g. `seen = [False] * 128`), giving true $\mathcal{O}(1)$ space with smaller memory overhead.

4. **Q: How would you modify this problem to allow at most $K$ duplicate characters?**
   - *A:* Maintain a frequency map and count of duplicate characters in the window, shrinking `left` only when duplicate count exceeds $K$.

---

## 14. Similar Problems

- **Easier:**
  - [LeetCode #387 - First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)
- **Similar Difficulty:**
  - [LeetCode #159 - Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)
  - [LeetCode #1004 - Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)
  - [LeetCode #904 - Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)
- **Harder:**
  - [LeetCode #76 - Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
  - [LeetCode #30 - Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)

---

## 15. Learning Summary

- **Pattern Recognized:** Sliding Window with Hash Set for substring constraint optimization.
- **Core Principle:** Expand `right` to include new elements; contract `left` to restore validity.
- **Key Takeaway:** Using a Hash Set transforms substring duplication checks from $\mathcal{O}(N)$ to $\mathcal{O}(1)$, reducing total time complexity from $\mathcal{O}(N^3)$ to $\mathcal{O}(N)$.

---

## 16. Optimization Notes

Your code is **optimal and interview-ready ($\mathcal{O}(N)$ time)**.

### HashMap Direct-Jump Variation (Single Pass)
If an interviewer asks to eliminate the `while` loop for shrinking the window, you can maintain character index mappings using a dictionary:

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_map = {}
        left = 0
        max_length = 0

        for right, ch in enumerate(s):
            if ch in char_map and char_map[ch] >= left:
                left = char_map[ch] + 1
            
            char_map[ch] = right
            max_length = max(max_length, right - left + 1)

        return max_length
```

*(Note: Your current Hash Set implementation is already $\mathcal{O}(N)$ and often preferred during interviews because it is easier to write bug-free under time constraints!)*
