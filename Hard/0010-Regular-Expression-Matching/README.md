# 0010. Regular Expression Matching

![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red?style=for-the-badge)
![Topic: String](https://img.shields.io/badge/Topic-String-blue?style=for-the-badge)
![Topic: Dynamic Programming](https://img.shields.io/badge/Topic-Dynamic%20Programming-purple?style=for-the-badge)
![Topic: Recursion](https://img.shields.io/badge/Topic-Recursion-green?style=for-the-badge)

---

## 1. Problem Information

- **Problem Name:** Regular Expression Matching
- **LeetCode Number:** 10
- **Difficulty:** Hard
- **Tags:** String, Dynamic Programming, Recursion, Memoization
- **Language Used:** Python
- **Problem Link:** [LeetCode #10 - Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)

---

## 2. Problem Overview

Given an input string `s` and a pattern `p`, implement **regular expression matching** with support for `'.'` and `'*'` where:
- `'.'` Matches any single character.
- `'*'` Matches **zero or more** of the preceding element.

The matching must cover the **entire** input string `s` (not just a partial substring).

### Input & Output Specifications
- **Input:**
  - `s`: A text string of length $M$ containing lowercase English letters.
  - `p`: A pattern string of length $N$ containing lowercase English letters, `'.'`, and `'*'`.
- **Output:** `True` if pattern `p` matches string `s` completely, otherwise `False`.
- **Constraints:**
  - $1 \le \text{len}(s) \le 20$
  - $1 \le \text{len}(p) \le 20$
  - It is guaranteed that for each appearance of the character `'*'`, there will be a previous valid character to match.

### Examples
- **Example 1:**
  - **Input:** `s = "aa"`, `p = "a"` $\rightarrow$ **Output:** `False`
- **Example 2:**
  - **Input:** `s = "aa"`, `p = "a*"` $\rightarrow$ **Output:** `True` (`'a*'` means zero or more `'a'`s).
- **Example 3:**
  - **Input:** `s = "ab"`, `p = ".*"` $\rightarrow$ **Output:** `True` (`'.*'` means zero or more of any character).
- **Example 4:**
  - **Input:** `s = "aab"`, `p = "c*a*b"` $\rightarrow$ **Output:** `True` (`'c*'` matches zero `'c'`s, `'a*'` matches two `'a'`s, `'b'` matches `'b'`).

### Real-World Intuition
Think of compiler lexical analysis or text search engines (like `grep` or SQL `LIKE` queries). When matching complex text against regular expression patterns containing wildcards, the engine branches into multiple state transitions and caches evaluated path states to avoid exponential backtracking.

---

## 3. Intuition

> [!TIP]
> **Key State Machine Rule:** When a character is followed by `'*'`, we face a decision branch: either match **0 occurrences** (skip the pattern pair) OR match **1+ occurrences** (consume 1 character in `s` and stay on the pattern pair)!

### Defining the State: `dp(i, j)`
Let `dp(i, j)` be a recursive boolean function checking whether the suffix `s[i:]` matches the pattern suffix `p[j:]`.

1. **First Character Match Check:**
   `first_match = (i < len(s)) and (s[i] == p[j] or p[j] == '.')`

2. **Wildcard Branching (`p[j+1] == '*'`):**
   When `'*'` follows character `p[j]`, we have two options:
   - **Option 1 (Zero Occurrences):** Ignore `p[j]*` completely and advance pattern index by 2 $\rightarrow$ `dp(i, j + 2)`.
   - **Option 2 (One or More Occurrences):** If `first_match` is True, consume character `s[i]` and remain at pattern index `j` to match further instances $\rightarrow$ `first_match and dp(i + 1, j)`.

3. **Standard Character Matching (`p[j+1] != '*'`):**
   - Require `first_match` to be True and advance both pointers $\rightarrow$ `first_match and dp(i + 1, j + 1)`.

By storing computed `(i, j)` state results in a `memo` dictionary, we prevent redundant computation of overlapping subproblems.

---

## 4. Thought Process

```mermaid
flowchart TD
    A[Start: dp(i, j)] --> B{(i, j) in memo?}
    B -- Yes --> C[Return cached memo[(i, j)]]
    B -- No --> D{Is j == len(p)?}
    D -- Yes --> E[Return i == len(s)]
    D -- No --> F[first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')]
    F --> G{Is j + 1 < len(p) and p[j + 1] == '*'}
    G -- Yes --> H[ans = dp(i, j + 2) OR (first_match and dp(i + 1, j))]
    G -- No --> I[ans = first_match and dp(i + 1, j + 1)]
    H --> J[Cache memo[(i, j)] = ans]
    I --> J
    J --> K[Return ans]
```

1. **State Space & Memoization Cache:**
   - Define a hash map `memo = {}` storing boolean outputs indexed by tuples `(i, j)`.

2. **Base Case:**
   - If pattern `p` is fully consumed (`j == len(p)`), return `True` if text `s` is also fully consumed (`i == len(s)`), else `False`.

3. **Match Evaluation:**
   - `first_match = (i < len(s)) and (s[i] == p[j] or p[j] == '.')`

4. **Recursive Transitions:**
   - If `j + 1 < len(p)` and `p[j + 1] == '*'`:
     - Result is `dp(i, j + 2)` (zero match) **OR** `(first_match and dp(i + 1, j))` (repeat match).
   - Otherwise:
     - Result is `first_match and dp(i + 1, j + 1)`.

5. **Return Initial Call:**
   - Execute `return dp(0, 0)`.

---

## 5. Concepts Used

### 1. Top-Down Dynamic Programming (Memoization)
- **What it is:** Caching the output of recursive calls indexed by state tuples `(i, j)` to eliminate redundant exponential branch paths.
- **Why it is used here:** Reduces recursive time complexity from $\mathcal{O}(2^{M+N})$ to $\mathcal{O}(M \times N)$.
- **Future applications:** Wildcard Matching, Edit Distance, Longest Common Subsequence.

### 2. State Machine Wildcard Branching
- **What it is:** Modeling `'*'` as an OR choice between zero occurrences (`j + 2`) and multiple occurrences (`i + 1, j`).
- **Why it is used here:** Accurately models non-deterministic finite automaton (NFA) state transitions.
- **Future applications:** Parsing engines, Lexical Analyzers.

---

## 6. Algorithm Used

### Top-Down Dynamic Programming with Memoization

- **Algorithm Category:** Dynamic Programming / Recursion
- **Why selected:** Provides an optimal $\mathcal{O}(M \times N)$ runtime and clean recursive structure for handling complex pattern branching.
- **Time Complexity:** $\mathcal{O}(M \times N)$
- **Space Complexity:** $\mathcal{O}(M \times N)$

---

## 7. Code Walkthrough

Below is the line-by-line breakdown of the submitted solution:

```python
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        # Line 10: State Cache Dictionary
        # Store boolean results for subproblem key tuple (i, j)
        memo = {}

        def dp(i, j):
            # Line 14-15: Cache Return Guard
            if (i, j) in memo:
                return memo[(i, j)]

            # Line 18-19: Base Case
            # If pattern is exhausted, text must also be exhausted for a valid match.
            if j == len(p):
                return i == len(s)

            # Line 22-25: Single Character Matching Logic
            # Verify i is within bounds and characters match (or pattern contains '.')
            first_match = (
                i < len(s) and
                (s[i] == p[j] or p[j] == '.')
            )

            # Line 28: Wildcard '*' Check
            if j + 1 < len(p) and p[j + 1] == '*':
                # Branch 1: Skip 'ch*' entirely (zero occurrences -> dp(i, j + 2))
                # Branch 2: Consume current s[i] and keep 'ch*' (dp(i + 1, j))
                ans = (
                    dp(i, j + 2) or
                    (first_match and dp(i + 1, j))
                )
            else:
                # Line 35: Standard Single Character Match Transition
                ans = first_match and dp(i + 1, j + 1)

            # Line 37-38: Store Result in Cache and Return
            memo[(i, j)] = ans
            return ans

        # Line 40: Initiate recursion from start of both strings
        return dp(0, 0)
```

---

## 8. Dry Run

Let's dry run for `s = "aa"` ($M=2$) and `p = "a*"` ($N=2$).

### Subproblem Call Trace

| Call | `i` (`s`) | `j` (`p`) | `first_match` | `p[j+1] == '*'` | Evaluated Expression | Result | Memoized `(i, j)` |
| :---: | :---: | :---: | :---: | :---: | :--- | :---: | :---: |
| `dp(2, 2)` | `2` | `2` | - | - | Base case: `j == 2`, `i == 2` $\rightarrow$ `2 == 2` | `True` | `(2, 2): True` |
| `dp(2, 0)` | `2` | `0` | `False` (`2 < 2` False) | `True` (`p[1]=='*'`) | `dp(2, 2) or (False and ...)` $\rightarrow$ `True or False` | `True` | `(2, 0): True` |
| `dp(1, 0)` | `1` | `0` | `True` (`'a'=='a'`) | `True` (`p[1]=='*'`) | `dp(1, 2) or (True and dp(2, 0))` $\rightarrow$ `dp(1,2)` (False) `or True` | `True` | `(1, 0): True` |
| `dp(0, 0)` | `0` | `0` | `True` (`'a'=='a'`) | `True` (`p[1]=='*'`) | `dp(0, 2) or (True and dp(1, 0))` $\rightarrow$ `dp(0,2)` (False) `or True` | `True` | `(0, 0): True` |

### Final Result
`dp(0, 0)` returns **`True`**.

---

## 9. Complexity Analysis

### Time Complexity: $\mathcal{O}(M \times N)$
- Where $M = \text{len}(s)$ and $N = \text{len}(p)$.
- There are $(M + 1) \times (N + 1)$ unique subproblem states `(i, j)`.
- Thanks to memoization, each state `(i, j)` is evaluated at most once in $\mathcal{O}(1)$ work.

### Space Complexity: $\mathcal{O}(M \times N)$
- **Memoization Dictionary:** Stores up to $(M + 1) \times (N + 1)$ cached boolean entries.
- **Call Stack:** Maximum recursion depth is $M + N$.

---

## 10. Edge Cases

| Edge Case Scenario | Input Example | Behavior & Output | How Code Handles It |
| :--- | :--- | :--- | :--- |
| **Empty Strings** | `s = ""`, `p = ""` | Output: `True` | Base case `j == len(p)` returns `i == len(s)` ($0 == 0$). |
| **Skipping Unmatched Patterns** | `s = "b"`, `p = "a*b"` | Output: `True` | `dp(0, 0)` skips `'a*'` via `dp(0, 2)` (zero match), matching `'b'` with `'b'`. |
| **Dot-Star Match All** | `s = "abc"`, `p = ".*"` | Output: `True` | `'.*'` consumes characters iteratively until string `s` is exhausted. |
| **Partial Pattern Remaining** | `s = "a"`, `p = "ab*"` | Output: `True` | Matches `'a'`, then skips `'b*'` via `dp(1, 3)`. |
| **Unmatched Extra Text** | `s = "ab"`, `p = "a"` | Output: `False` | After matching `'a'`, `dp(1, 1)` hits `j == 1` while `i = 1 != 2`. Returns `False`. |

---

## 11. Alternative Approaches

### Approach 1: Un-memoized Pure Recursion ($\mathcal{O}(2^{M+N})$ Time, $\mathcal{O}(M+N)$ Space)
- **Idea:** Explore recursive choices without state caching.
- **Drawback:** Time Limit Exceeded (TLE) due to exponential state explosion.

### Approach 2: Top-Down Memoization DP (User's Solution - Recommended)
- **Idea:** Recursive evaluation with `memo` dictionary lookup.
- **Complexity:** $\mathcal{O}(M \times N)$ time, $\mathcal{O}(M \times N)$ space.
- **Why Optimal:** Clean, intuitive state transition logic, optimal time complexity.

### Approach 3: Bottom-Up Iterative 2D DP Table ($\mathcal{O}(M \times N)$ Time, $\mathcal{O}(M \times N)$ Space)
- **Idea:** Construct a 2D boolean array `dp[i][j]` filled iteratively backwards from `dp[M][N]`.
- **Complexity:** Identical asymptotic performance; top-down memoization is often preferred for readability under interview conditions.

---

## 12. Common Mistakes

> [!WARNING]
> 1. **Treating `*` as a Standalone Character:** Expecting `*` to match anything directly (like in shell wildcards) instead of anchoring it to the **preceding element** (`p[j-1]` or `p[j]`).
> 2. **Incrementing Pattern Index by 1 for `*`:** When skipping a zero-occurrence `ch*` pattern, pattern pointer must advance by **2** (`j + 2`).
> 3. **Index Out of Bounds on Text `s`:** Checking `s[i] == p[j]` without validating `i < len(s)` leads to `IndexError`.

---

## 13. Interview Questions

1. **Q: How does this problem differ from LeetCode #44 (Wildcard Matching)?**
   - *A:* In LC #44, `'*'` matches any sequence of characters independently. In LC #10, `'*'` matches zero or more of the **preceding element**.

2. **Q: Why do we check `j + 1 < len(p) and p[j + 1] == '*'` before matching single characters?**
   - *A:* Because if the next character is `'*'`, current element `p[j]` can be skipped entirely (0 occurrences). Checking single match first would prematurely enforce consumption of `s[i]`.

3. **Q: How would you optimize space complexity if using bottom-up DP?**
   - *A:* Since `dp[i][j]` only depends on row `i` and `i + 1`, space can be compressed to 2 1D arrays of size $N + 1$, achieving $\mathcal{O}(N)$ space complexity.

---

## 14. Similar Problems

- **Medium:**
  - [LeetCode #72 - Edit Distance](https://leetcode.com/problems/edit-distance/)
  - [LeetCode #1143 - Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
- **Hard:**
  - [LeetCode #44 - Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)

---

## 15. Learning Summary

- **Pattern Recognized:** Top-Down Dynamic Programming for Non-Deterministic Pattern Matching.
- **State Representation:** `dp(i, j)` mapping text index `i` and pattern index `j`.
- **Branching Rule:** `'*'` wildcard generates an OR branch: skip pattern pair (`j + 2`) vs consume text character (`i + 1, j`).

---

## 16. Optimization Notes

Your code is **100% optimal** ($\mathcal{O}(M \times N)$ Time, $\mathcal{O}(M \times N)$ Space). It represents the standard gold-standard solution for Hard-difficulty DP pattern matching in top-tier coding interviews!
