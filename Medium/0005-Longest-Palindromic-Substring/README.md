# 0005. Longest Palindromic Substring

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)
![Topic: String](https://img.shields.io/badge/Topic-String-blue?style=for-the-badge)
![Topic: Two Pointers](https://img.shields.io/badge/Topic-Two%20Pointers-purple?style=for-the-badge)
![Topic: Dynamic Programming](https://img.shields.io/badge/Topic-Dynamic%20Programming-red?style=for-the-badge)

---

## 1. Problem Information

- **Problem Name:** Longest Palindromic Substring
- **LeetCode Number:** 5
- **Difficulty:** Medium
- **Tags:** String, Two Pointers, Dynamic Programming
- **Language Used:** Python
- **Problem Link:** [LeetCode #5 - Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

---

## 2. Problem Overview

Given a string `s`, find and return the **longest contiguous substring** within `s` that is a **palindrome**. 

A **palindrome** is a string that reads identically forwards and backwards (e.g., `"aba"`, `"racecar"`, `"noon"`).

### Input & Output Specifications
- **Input:** `s` (a string of length $N$).
- **Output:** A string representing the longest palindromic substring. If multiple palindromic substrings have the same maximum length, returning any valid one is accepted.
- **Constraints:**
  - $1 \le \text{len}(s) \le 1000$
  - `s` consists of digits and English letters.

### Examples
- **Example 1:**
  - **Input:** `s = "babad"`
  - **Output:** `"bab"` (Note: `"aba"` is also a valid answer).
- **Example 2:**
  - **Input:** `s = "cbbd"`
  - **Output:** `"bb"`

### Real-World Intuition
In bioinformatics, DNA sequences contain palindromic recognition sites where restriction enzymes bind and cut double-stranded DNA. Finding the longest palindromic sequence helps identify structural symmetries in gene editing, text analysis engines, and string compression routines.

---

## 3. Intuition

> [!TIP]
> **Core Concept:** A palindrome expands symmetrically around its center!

Instead of generating all possible substrings and checking if each is a palindrome (which takes $\mathcal{O}(N^3)$ time), we can leverage palindrome symmetry:
- Every palindrome has a **center**.
- If we know the center, we can expand outward using two pointers (`left` moving left, `right` moving right) as long as `s[left] == s[right]`.

### The Two Types of Palindromic Centers
1. **Odd-Length Palindromes:** Center is a single character (e.g., `"a b a"` centered at `'b'`).
2. **Even-Length Palindromes:** Center lies between two identical characters (e.g., `"a b b a"` centered between `'b'` and `'b'`).

For a string of length $N$, there are $N$ odd centers and $N-1$ even centers, making a total of $2N - 1$ possible centers. Expanding around each center takes $\mathcal{O}(N)$ time, leading to an overall $\mathcal{O}(N^2)$ algorithm.

---

## 4. Thought Process

```mermaid
flowchart TD
    A[Start: Input s] --> B{Is len(s) < 2?}
    B -- Yes --> C[Return s directly]
    B -- No --> D[Initialize start = 0, max_len = 1]
    D --> E[Loop i from 0 to len(s) - 1]
    E --> F[Expand Odd Palindrome: left = i, right = i]
    F --> G[Expand while s[left] == s[right]]
    G --> H{Is right - left + 1 > max_len?}
    H -- Yes --> I[Update start = left, max_len = length]
    H -- No --> J[Continue expansion]
    I --> J
    J --> K[Expand Even Palindrome: left = i, right = i + 1]
    K --> L[Expand while s[left] == s[right]]
    L --> M{Is right - left + 1 > max_len?}
    M -- Yes --> N[Update start = left, max_len = length]
    M -- No --> O[Next iteration i]
    N --> O
    O --> P{Finished all centers i?}
    P -- No --> E
    P -- Yes --> Q[Return substring s[start : start + max_len]]
```

1. **Boundary Guard Clause:**
   - If string length is less than 2 (`len(s) < 2`), the string itself is trivially a palindrome of length 0 or 1. Return `s` immediately.

2. **Track Best Substring:**
   - Instead of creating and copying string slices on every update, maintain two lightweight integer variables:
     - `start`: Starting index of the longest palindrome found so far.
     - `max_len`: Length of the longest palindrome found so far.

3. **Iterate Through All Possible Centers ($i$ from $0$ to $N-1$):**
   - **Expand Odd-length:** Set `left = i`, `right = i`. While `left >= 0` and `right < len(s)` and `s[left] == s[right]`:
     - If current length `right - left + 1 > max_len`, update `start = left` and `max_len = right - left + 1`.
     - Move `left -= 1`, `right += 1`.
   - **Expand Even-length:** Set `left = i`, `right = i + 1`. While `left >= 0` and `right < len(s)` and `s[left] == s[right]`:
     - If current length `right - left + 1 > max_len`, update `start = left` and `max_len = right - left + 1`.
     - Move `left -= 1`, `right += 1`.

4. **Return Final Slice:**
   - Return slice `s[start : start + max_len]`.

---

## 5. Concepts Used

### 1. Two Pointers / Expand Around Center
- **What it is:** Using two pointer indices (`left`, `right`) initialized at center positions and moving them outwards in opposite directions.
- **Why it is used here:** Capitalizes on structural symmetry to verify palindromes in $\mathcal{O}(N)$ per center without redundant checks.
- **Future applications:** Container With Most Water, Trapping Rain Water, Palindromic Substrings.

### 2. Odd vs. Even Parity Handling
- **What it is:** Differentiating discrete single-element centers from dual-element interval centers.
- **Why it is used here:** Ensures even-length palindromes like `"abba"` are not missed during single-index loops.
- **Future applications:** Median of Two Sorted Arrays, Divide and Conquer algorithms.

---

## 6. Algorithm Used

### Expand Around Center Technique

- **Algorithm Category:** Two Pointers / String Manipulation
- **Why selected:** Provides optimal $\mathcal{O}(1)$ auxiliary space while remaining intuitive and fast in practice.
- **Time Complexity:** $\mathcal{O}(N^2)$
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

---

## 7. Code Walkthrough

Below is the line-by-line explanation of the accepted solution:

```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Line 9-10: Guard Clause for Short Strings
        # If length is 0 or 1, string is already a valid palindrome.
        if len(s) < 2:
            return s

        # Line 12-13: Track Longest Substring Window
        # start: starting index of longest palindrome found
        # max_len: maximum length of palindrome found (initialized to 1 for single char)
        start = 0
        max_len = 1

        # Line 15: Iterate through each index i as a potential center
        for i in range(len(s)):

            # -------------------------------------------------------------
            # Case 1: Odd length palindrome expansion (center at index i)
            # -------------------------------------------------------------
            left = i
            right = i

            # Line 22: Expand outwards while boundaries are valid and chars match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # Line 23-25: Check if current expanded palindrome is longer than max_len
                if right - left + 1 > max_len:
                    start = left
                    max_len = right - left + 1
                # Line 26-27: Expand pointers outward
                left -= 1
                right += 1

            # -------------------------------------------------------------
            # Case 2: Even length palindrome expansion (center between i and i+1)
            # -------------------------------------------------------------
            left = i
            right = i + 1

            # Line 33: Expand outwards while boundaries are valid and chars match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # Line 34-36: Check if current expanded palindrome is longer than max_len
                if right - left + 1 > max_len:
                    start = left
                    max_len = right - left + 1
                # Line 37-38: Expand pointers outward
                left -= 1
                right += 1

        # Line 40: Return the slice of s starting at 'start' with length 'max_len'
        return s[start:start + max_len]
```

---

## 8. Dry Run

Let's dry run for `s = "babad"`.

### Initial State
- `s = "babad"`, `len(s) = 5`.
- `start = 0`, `max_len = 1`.

### Step-by-Step Traversal

| $i$ | Type | Initial `(left, right)` | Expansion Steps (`s[left] == s[right]`) | Palindrome Found | Length | Update (`start`, `max_len`) |
| :---: | :---: | :---: | :--- | :---: | :---: | :---: |
| **0** | Odd | `(0, 0)` | `s[0]=='b'` $\rightarrow$ Expand to `(-1, 1)` (out of bounds) | `"b"` | 1 | No change (`start=0, max_len=1`) |
| **0** | Even | `(0, 1)` | `s[0]=='b' != s[1]=='a'` $\rightarrow$ Loop fails | - | - | No change |
| **1** | Odd | `(1, 1)` | `s[1]=='a'` $\rightarrow$ Expand `(0, 2)` (`s[0]=='b' == s[2]=='b'`) $\rightarrow$ Expand `(-1, 3)` (out of bounds) | `"bab"` | 3 | **`start=0, max_len=3`** |
| **1** | Even | `(1, 2)` | `s[1]=='a' != s[2]=='b'` $\rightarrow$ Loop fails | - | - | No change |
| **2** | Odd | `(2, 2)` | `s[2]=='b'` $\rightarrow$ Expand `(1, 3)` (`s[1]=='a' == s[3]=='a'`) $\rightarrow$ Expand `(0, 4)` (`s[0]=='b' != s[4]=='d'`) | `"aba"` | 3 | No change ($3 \ngtr 3$) |
| **2** | Even | `(2, 3)` | `s[2]=='b' != s[3]=='a'` $\rightarrow$ Loop fails | - | - | No change |
| **3** | Odd | `(3, 3)` | `s[3]=='a'` $\rightarrow$ Expand `(2, 4)` (`s[2]=='b' != s[4]=='d'`) | `"a"` | 1 | No change |
| **3** | Even | `(3, 4)` | `s[3]=='a' != s[4]=='d'` $\rightarrow$ Loop fails | - | - | No change |
| **4** | Odd | `(4, 4)` | `s[4]=='d'` $\rightarrow$ Expand `(3, 5)` (out of bounds) | `"d"` | 1 | No change |
| **4** | Even | `(4, 5)` | `right = 5` out of bounds | - | - | No change |

### Final Slice
`s[start : start + max_len]` = `s[0 : 0 + 3]` = `s[0:3]` $\rightarrow$ **`"bab"`**

---

## 9. Complexity Analysis

### Time Complexity: $\mathcal{O}(N^2)$
- **Outer Loop:** Runs $N$ times for each character index $i$.
- **Inner Expansion Loops:** In the worst case (e.g. `s = "aaaaa"`), expanding around center takes $\mathcal{O}(N)$ steps.
- **Overall Time Complexity:**
  - **Best Case:** $\mathcal{O}(N)$ (e.g. `s = "abcdef"` where no expansion happens beyond 1 char).
  - **Average Case:** $\mathcal{O}(N^2)$
  - **Worst Case:** $\mathcal{O}(N^2)$ (e.g. `s = "aaaaa"`).

### Space Complexity: $\mathcal{O}(1)$ Auxiliary Space
- **Auxiliary Variables:** Uses only primitive integers (`start`, `max_len`, `left`, `right`, `i`).
- **Return Slice:** Python string slicing `s[start:start+max_len]` produces the output string of length $\le N$.
- **Overall Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

---

## 10. Edge Cases

| Edge Case Scenario | Input Example | Behavior & Output | How Code Handles It |
| :--- | :--- | :--- | :--- |
| **Single Character** | `s = "a"` | Output: `"a"` | Guard clause `len(s) < 2` returns `"a"` directly. |
| **Two Same Chars** | `s = "aa"` | Output: `"aa"` | Even expansion at `i=0` (`left=0, right=1`) matches `'a' == 'a'`. Sets `max_len=2`. |
| **Two Different Chars** | `s = "ab"` | Output: `"a"` | `max_len` remains `1`. Returns `s[0:1]` = `"a"`. |
| **All Identical Chars** | `s = "aaaa"` | Output: `"aaaa"` | Expands to full length on center `i=1` (even expansion `left=0, right=3`). |
| **No Palindrome > 1** | `s = "abcde"` | Output: `"a"` | `max_len` remains `1`, returns first character `"a"`. |

---

## 11. Alternative Approaches

### Approach 1: Brute Force ($\mathcal{O}(N^3)$ Time, $\mathcal{O}(1)$ Space)
- **Idea:** Generate all $\mathcal{O}(N^2)$ possible substrings and check if each is a palindrome in $\mathcal{O}(N)$ time.
- **Drawback:** TLE (Time Limit Exceeded) for $N = 1000$.

### Approach 2: Dynamic Programming 2D Table ($\mathcal{O}(N^2)$ Time, $\mathcal{O}(N^2)$ Space)
- **Idea:** Let `dp[i][j]` be `True` if substring `s[i..j]` is a palindrome.
  - Base cases: `dp[i][i] = True`, `dp[i][i+1] = (s[i] == s[i+1])`.
  - Transition: `dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]`.
- **Drawback:** Requires $\mathcal{O}(N^2)$ extra space for the 2D DP matrix.

### Approach 3: Expand Around Center (User's Solution - Interview Optimal)
- **Idea:** Expand two pointers outward from all $2N-1$ possible centers.
- **Complexity:** $\mathcal{O}(N^2)$ time, $\mathcal{O}(1)$ space.
- **Why Optimal:** Fast execution, minimal memory overhead, zero extra allocations.

### Approach 4: Manacher's Algorithm ($\mathcal{O}(N)$ Time, $\mathcal{O}(N)$ Space)
- **Idea:** Advanced algorithm that uses previously computed palindrome radii to avoid redundant expansions.
- **Complexity:** $\mathcal{O}(N)$ time, $\mathcal{O}(N)$ auxiliary space.
- **Drawback:** Overly complex to code under interview pressure; rarely required unless explicitly requested.

---

## 12. Common Mistakes

> [!WARNING]
> 1. **Omitting Even-Length Centers:** Searching only odd centers (`left = i, right = i`) misses even palindromes like `"abba"` or `"cbbd"`.
> 2. **String Slicing Inside Expansion Loops:** Doing `sub = s[left:right+1]` inside the `while` loop creates $O(N)$ string copies on every step, degrading performance to $\mathcal{O}(N^3)$.
> 3. **Incorrect Length Calculation:** Calculating palindrome length as `right - left` instead of `right - left + 1`.

---

## 13. Interview Questions

1. **Q: Why does Expand Around Center require checking $2N - 1$ centers instead of $N$?**
   - *A:* Because palindromes can have odd lengths ($N$ single-character centers) or even lengths ($N-1$ center gaps between adjacent characters).

2. **Q: How does this Expand Around Center approach compare to 2D Dynamic Programming?**
   - *A:* Both have $\mathcal{O}(N^2)$ time complexity, but Expand Around Center uses $\mathcal{O}(1)$ auxiliary space compared to $\mathcal{O}(N^2)$ space for DP.

3. **Q: Can we optimize this solution to run in linear time $\mathcal{O}(N)$?**
   - *A:* Yes, Manacher's Algorithm solves this problem in $\mathcal{O}(N)$ time by maintaining a palindrome radius array and exploiting symmetry from already processed centers.

4. **Q: How would you modify the solution if we only needed to count the total number of palindromic substrings?**
   - *A:* Instead of updating `max_len` and `start`, increment a `count` variable each time `s[left] == s[right]` during expansion (this is LeetCode #647).

---

## 14. Similar Problems

- **Easier:**
  - [LeetCode #125 - Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
  - [LeetCode #234 - Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
- **Similar Difficulty:**
  - [LeetCode #647 - Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
  - [LeetCode #516 - Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)
- **Harder:**
  - [LeetCode #214 - Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/)
  - [LeetCode #1312 - Minimum Insertion Steps to Make a String Palindrome](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/)

---

## 15. Learning Summary

- **Pattern Recognized:** Two Pointers / Center Expansion for palindromic symmetry.
- **Space Efficiency:** Storing pointer indices (`start`, `max_len`) instead of cloning substring instances keeps memory at $\mathcal{O}(1)$.
- **Interview Rule:** For palindrome substring problems, always remember to evaluate both **odd** and **even** center configurations.

---

## 16. Optimization Notes

Your code is ** optimal for coding interviews**, operating in $\mathcal{O}(N^2)$ time and $\mathcal{O}(1)$ extra memory.

### Helper Function Refactoring (Cleanliness Tip)
While your inline expansion loops are perfectly optimal, in an interview setting you can reduce code duplication by extracting a helper function:

```python
def expand(self, s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    # Returns (start_index, length) of valid palindrome
    return left + 1, right - left - 1
```

*(Note: Keeping your current code as-is is 100% accepted and preserves your personal coding style!)*
