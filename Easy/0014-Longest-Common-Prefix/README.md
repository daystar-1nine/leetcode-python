# 0014. Longest Common Prefix

![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen?style=for-the-badge)
![Topic: String](https://img.shields.io/badge/Topic-String-blue?style=for-the-badge)
![Topic: Trie](https://img.shields.io/badge/Topic-Trie-purple?style=for-the-badge)

---

## 1. Problem Information

- **Problem Name:** Longest Common Prefix
- **LeetCode Number:** 14
- **Difficulty:** Easy
- **Tags:** String, Trie
- **Language Used:** Python
- **Problem Link:** [LeetCode #14 - Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

---

## 2. Problem Overview

Write a function to find the **longest common prefix** string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

### Input & Output Specifications
- **Input:** `strs`: An array of strings ($1 \le \text{len}(strs) \le 200$).
- **Output:** A string representing the longest common prefix.
- **Constraints:**
  - $0 \le \text{strs}[i].\text{length} \le 200$
  - `strs[i]` consists of only lowercase English letters.

### Examples
- **Example 1:**
  - **Input:** `strs = ["flower","flow","flight"]` $\rightarrow$ **Output:** `"fl"`
- **Example 2:**
  - **Input:** `strs = ["dog","racecar","car"]` $\rightarrow$ **Output:** `""`
  - **Explanation:** There is no common prefix among the input strings.

### Real-World Intuition
Consider auto-complete search engines or file path resolution systems (like Git branch auto-completion or Shell tab-completion). When a user types a command, the shell computes the longest common prefix of all matching directory names to complete as much text as possible.

---

## 3. Intuition

> [!TIP]
> **Horizontal Scanning Principle:** The common prefix of $N$ strings is equal to:
> $$LCP(S_1, S_2, \dots, S_N) = LCP(LCP(LCP(S_1, S_2), S_3), \dots, S_N)$$

### How Horizontal Scanning Works:
1. Assume `strs[0]` is our starting candidate `prefix`.
2. Compare `prefix` against `strs[1]`. If `strs[1]` does not start with `prefix`, trim 1 character off the right end of `prefix` (`prefix = prefix[:-1]`).
3. Repeat trimming until `strs[1]` starts with `prefix`.
4. Take this reduced `prefix` and repeat the process against `strs[2]`, `strs[3]`, ..., `strs[N-1]`.
5. If `prefix` ever shrinks to an empty string `""`, terminate early and return `""`!

---

## 4. Thought Process

```mermaid
flowchart TD
    A[Start: Input strs] --> B{Is strs empty?}
    B -- Yes --> C[Return empty string]
    B -- No --> D[Set prefix = strs[0]]
    D --> E[Loop i from 1 to len strs - 1]
    E --> F{Does strs[i] start with prefix? find == 0}
    F -- Yes --> G{More strings in array?}
    F -- No --> H[Trim rightmost char: prefix = prefix[:-1]]
    H --> I{Is prefix empty?}
    I -- Yes --> J[Return empty string]
    I -- No --> F
    G -- Yes --> E
    G -- No --> K[Return prefix]
```

1. **Guard Clause:**
   - If `strs` is empty (`if not strs:`), return `""`.

2. **Initialize Candidate:**
   - Set `prefix = strs[0]`.

3. **Horizontal Scan Loop:**
   - For index `i` from `1` to `len(strs) - 1`:
     - While `strs[i].find(prefix) != 0` (meaning `prefix` is not at index 0 of `strs[i]`):
       - Truncate `prefix = prefix[:-1]`.
       - If `prefix` reaches `""`, return `""` immediately.

4. **Return Final Result:**
   - Return `prefix`.

---

## 5. Concepts Used

### 1. Horizontal Scanning & Prefix Truncation
- **What it is:** Pairwise reduction of candidate prefix across array elements.
- **Why it is used here:** Progressively shrinks search bounds in a simple linear loop.
- **Future applications:** Longest Common Substring, Trie Traversal.

### 2. Substring Starts-With Verification (`find(prefix) == 0`)
- **What it is:** Checking if a substring is located strictly at index `0`.
- **Why it is used here:** Distinguishes a true prefix from substring matches located inside the string body.
- **Future applications:** String Matching, KMP Algorithm, Substring Search.

---

## 6. Algorithm Used

### Horizontal Scanning (Prefix Reduction)

- **Algorithm Category:** String / Array Traversal
- **Why selected:** Simple, clean, memory-efficient, and easy to explain in interviews.
- **Time Complexity:** $\mathcal{O}(S)$ where $S$ is total sum of characters across all strings.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

---

## 7. Code Walkthrough

Below is the line-by-line breakdown of the submitted solution:

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # Line 9-10: Guard Clause for Empty Array
        if not strs:
            return ""

        # Line 12: Initialize candidate prefix with the first string
        prefix = strs[0]

        # Line 14: Horizontally scan remaining strings from index 1 onward
        for i in range(1, len(strs)):
            # Line 15: Loop until strs[i] starts with prefix (find(prefix) == 0)
            while strs[i].find(prefix) != 0:
                # Line 16: Truncate 1 character from right end of prefix
                prefix = prefix[:-1]

                # Line 18-19: Early exit if prefix reduces to empty string
                if prefix == "":
                    return ""

        # Line 21: Return final validated common prefix
        return prefix
```

---

## 8. Dry Run

Let's dry run for `strs = ["flower", "flow", "flight"]`.

### Initial State
- `prefix = "flower"`

### Execution Trace

| Step `i` | Current `strs[i]` | `strs[i].find(prefix)` | Loop Condition (`!= 0`) | Action on `prefix` | `prefix` (After) |
| :---: | :---: | :---: | :---: | :--- | :---: |
| **1** | `"flow"` | `"flow".find("flower")` = `-1` | True | Truncate `prefix[:-1]` | `"flowe"` |
| **1** | `"flow"` | `"flow".find("flowe")` = `-1` | True | Truncate `prefix[:-1]` | `"flow"` |
| **1** | `"flow"` | `"flow".find("flow")` = `0` | **False** | Match found for `strs[1]`! Next `i` | `"flow"` |
| **2** | `"flight"` | `"flight".find("flow")` = `-1` | True | Truncate `prefix[:-1]` | `"flo"` |
| **2** | `"flight"` | `"flight".find("flo")` = `-1` | True | Truncate `prefix[:-1]` | `"fl"` |
| **2** | `"flight"` | `"flight".find("fl")` = `0` | **False** | Match found for `strs[2]`! Loop Ends | **`"fl"`** |

### Output
Returns **`"fl"`**.

---

## 9. Complexity Analysis

### Time Complexity: $\mathcal{O}(S)$
- Where $S$ is the sum of all characters in all strings $S = \sum \text{len}(\text{strs}[i])$.
- **Worst Case:** All strings are identical (e.g. `["aaaa", "aaaa", "aaaa"]`), comparing $\mathcal{O}(S)$ characters.
- **Best Case:** First two strings have no common prefix (e.g. `["a", "b"]`), running in $\mathcal{O}(\text{len}(\text{strs}[0]))$ time.

### Space Complexity: $\mathcal{O}(1)$ Auxiliary Space
- Uses only primitive pointers and string slice operations on `prefix`.
- No extra heap arrays or data structures allocated.

---

## 10. Edge Cases

| Edge Case Scenario | Input Example | Behavior & Output | How Code Handles It |
| :--- | :--- | :--- | :--- |
| **Single String Array** | `strs = ["flower"]` | Output: `"flower"` | Outer loop range `(1, 1)` doesn't run, returns `strs[0]`. |
| **Empty String Element** | `strs = ["", "b"]` | Output: `""` | `prefix = ""`, `find("") == 0` returns `""`. |
| **No Common Prefix** | `strs = ["dog", "racecar"]` | Output: `""` | `prefix` truncates to `""`, triggers `if prefix == "": return ""`. |
| **Identical Strings** | `strs = ["abc", "abc"]` | Output: `"abc"` | `find("abc") == 0` on first check, returns `"abc"`. |

---

## 11. Alternative Approaches

### Approach 1: Vertical Scanning ($\mathcal{O}(S)$ Time, $\mathcal{O}(1)$ Space)
- **Idea:** Compare characters column-by-column across all strings simultaneously.
  ```python
  for i in range(len(strs[0])):
      ch = strs[0][i]
      for s in strs[1:]:
          if i == len(s) or s[i] != ch:
              return strs[0][:i]
  return strs[0]
  ```
- **Why Great:** Stops early if mismatched character is at index 0 of a very long string.

### Approach 2: Sorting ($\mathcal{O}(N \log N \cdot M)$ Time, $\mathcal{O}(1)$ Space)
- **Idea:** Sort array lexicographically; common prefix of whole array must be common prefix between first (`strs[0]`) and last (`strs[-1]`) elements.

### Approach 3: Horizontal Scanning (User's Solution - Recommended)
- **Idea:** Pairwise prefix reduction.
- **Complexity:** $\mathcal{O}(S)$ time, $\mathcal{O}(1)$ space.
- **Why Optimal:** Clean, readable, standard interview approach.

---

## 12. Common Mistakes

> [!WARNING]
> 1. **Using `in` Operator:** Writing `while prefix in strs[i]` matches substrings anywhere inside `strs[i]` (e.g. `"flow"` in `"aflow"`), failing prefix alignment requirement. Must check `.find(prefix) == 0` or `.startswith(prefix)`.
> 2. **Forgetting Early Exit:** Omitting `if prefix == "": return ""` causes unnecessary remaining iterations.
> 3. **Index Errors on Empty List:** Accessing `strs[0]` without checking `if not strs:` causes `IndexError`.

---

## 13. Interview Questions

1. **Q: Why is `strs[i].find(prefix) != 0` used instead of `prefix in strs[i]`?**
   - *A:* `.find(prefix)` returns the exact starting index of `prefix`. Comparing `!= 0` ensures `prefix` appears at index 0 (the start of `strs[i]`), whereas `in` would return True for substrings in the middle or end.

2. **Q: How does Vertical Scanning differ from Horizontal Scanning?**
   - *A:* Horizontal Scanning compares full strings pairwise ($S_1$ vs $S_2$, then $S_{1..2}$ vs $S_3$). Vertical Scanning compares index 0 of all strings, then index 1 of all strings. Vertical scanning is faster when a mismatch occurs early in a very long string.

3. **Q: Can we solve this problem using a Trie?**
   - *A:* Yes. Insert all strings into a Trie. The longest common prefix is the path from root down until reaching a node with more than 1 child or a node representing the end of a word.

---

## 14. Similar Problems

- **Medium:**
  - [LeetCode #1143 - Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
- **Hard:**
  - [LeetCode #214 - Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/)

---

## 15. Learning Summary

- **Pattern Recognized:** Horizontal Scanning / Pairwise Prefix Reduction.
- **Prefix Alignment:** `find(prefix) == 0` or `startswith()` to enforce index 0 positioning.
- **Early Exit Optimization:** Returning `""` as soon as prefix shrinks to empty.

---

## 16. Optimization Notes

Your solution is **100% optimal** ($\mathcal{O}(S)$ Time, $\mathcal{O}(1)$ Space). It is clean, readable, and handles all edge cases perfectly!
