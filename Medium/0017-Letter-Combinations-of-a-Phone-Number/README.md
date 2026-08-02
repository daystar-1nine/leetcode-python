# 0017. Letter Combinations of a Phone Number

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)
![Topic: Hash Table](https://img.shields.io/badge/Topic-Hash%20Table-blue?style=for-the-badge)
![Topic: String](https://img.shields.io/badge/Topic-String-green?style=for-the-badge)
![Topic: Backtracking](https://img.shields.io/badge/Topic-Backtracking-purple?style=for-the-badge)

---

## 1. Problem Information

- **Problem Name:** Letter Combinations of a Phone Number
- **LeetCode Number:** 17
- **Difficulty:** Medium
- **Tags:** Hash Table, String, Backtracking, Depth-First Search
- **Language Used:** Python
- **Problem Link:** [LeetCode #17 - Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

---

## 2. Problem Overview

Given a string containing digits from `2-9` inclusive, return all possible **letter combinations** that the number could represent. You may return the answer in **any order**.

A mapping of digits to letters (just like on telephone buttons) is given below:

```text
2 -> "abc"    3 -> "def"    4 -> "ghi"
5 -> "jkl"    6 -> "mno"    7 -> "pqrs"
8 -> "tuv"    9 -> "wxyz"
```

### Input & Output Specifications
- **Input:** A string `digits` ($0 \le \text{len}(digits) \le 4$).
- **Output:** A list of strings containing all valid combinations.
- **Constraints:** `digits[i]` is a digit in the range `['2', '9']`.

### Examples
- **Example 1:**
  - **Input:** `digits = "23"`
  - **Output:** `["ad","ae","af","bd","be","bf","cd","ce","cf"]`
- **Example 2:**
  - **Input:** `digits = ""` $\rightarrow$ **Output:** `[]`
- **Example 3:**
  - **Input:** `digits = "2"` $\rightarrow$ **Output:** `["a","b","c"]`

### Real-World Intuition
Think of T9 predictive text messaging on legacy mobile phone keypads or vanity phone number generators (e.g. mapping `1-800-FLOWERS` to numeric dialing codes). The system explores all possible character branches represented by the sequence of key presses.

---

## 3. Intuition

> [!TIP]
> **Decision Tree Traversal:** Each digit represents a level in a decision tree. Branching factor equals the number of letters for that digit (3 or 4 choices per level)!

```text
               ( Root: "" )
              /     |      \
           'a'     'b'     'c'       <- Level 0 (Digit '2')
          / | \   / | \   / | \
         d  e  f d  e  f d  e  f     <- Level 1 (Digit '3')
```

1. **Backtracking / DFS Pattern:**
   - Start at `index = 0` with an empty string `current = ""`.
   - Retrieve the candidate letters for `digits[index]`.
   - For each letter, append it to `current` and recursively call `backtrack(index + 1, current + ch)`.
   - When `index == len(digits)`, we have reached a leaf node representing a complete valid combination. Append `current` to `result` and return!

---

## 4. Thought Process

```mermaid
flowchart TD
    A[Start: Input digits] --> B{Is digits empty?}
    B -- Yes --> C[Return empty list []]
    B -- No --> D[Initialize phone keypad dictionary]
    D --> E[Initialize result = empty list]
    E --> F[Call backtrack index=0, current=""]
    F --> G{Is index == len digits?}
    G -- Yes --> H[Append current to result]
    H --> I[Return / Step Back]
    G -- No --> J[Fetch letters = phone[digits[index]]]
    J --> K[Loop ch in letters]
    K --> L[Recursive call: backtrack index + 1, current + ch]
    L --> K
    K -- Done all letters --> I
    I --> M[Return result]
```

1. **Guard Clause:**
   - If `digits` is empty, return `[]` immediately (avoid returning `[""]`).

2. **Keypad Mapping:**
   - Hash map `phone` mapping `'2'` to `"abc"`, `'3'` to `"def"`, ..., `'9'` to `"wxyz"`.

3. **Recursive Function `backtrack(index, current)`:**
   - **Base Case:** `if index == len(digits): result.append(current); return`.
   - **Recursive Step:**
     - Get `letters = phone[digits[index]]`.
     - For each `ch` in `letters`:
       - Recursively invoke `backtrack(index + 1, current + ch)`.

4. **Return Accumulator:**
   - Return `result`.

---

## 5. Concepts Used

### 1. Recursive Backtracking (DFS)
- **What it is:** Exploring a search space by building candidates incrementally and abandoning paths once target conditions are satisfied.
- **Why it is used here:** Systematically generates all Cartesian product combinations without requiring hardcoded nested loops.
- **Future applications:** Permutations, Combinations, N-Queens, Sudoku Solver.

### 2. Decision Tree Depth
- **What it is:** Structuring state spaces into levels where depth corresponds to input length $N$.
- **Why it is used here:** Guarantees that every generated string has length exactly equal to `len(digits)`.
- **Future applications:** Generate Parentheses, Combination Sum.

---

## 6. Algorithm Used

### Recursive Backtracking (DFS Decision Tree)

- **Algorithm Category:** Backtracking / Depth-First Search
- **Why selected:** Cleanest, most natural approach for generating multi-level decision combinations.
- **Time Complexity:** $\mathcal{O}(4^N \cdot N)$
- **Space Complexity:** $\mathcal{O}(N)$ auxiliary stack space

---

## 7. Code Walkthrough

Below is the line-by-line breakdown of the submitted solution:

```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        # Line 9-10: Guard Clause for Empty Input
        if not digits:
            return []

        # Line 12-21: Phone Keypad Hash Map
        phone = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        # Line 23: Result List Accumulator
        result = []

        # Line 25: Recursive Backtracking Helper Function
        def backtrack(index, current):

            # Line 27-29: Base Case - Leaf Node Reached
            if index == len(digits):
                result.append(current)
                return

            # Line 31: Get letter choices for active digit
            letters = phone[digits[index]]

            # Line 33-34: Branching Step - Explore each letter choice
            for ch in letters:
                backtrack(index + 1, current + ch)

        # Line 36: Kickoff backtracking from index 0 with empty string path
        backtrack(0, "")

        # Line 38: Return all collected combinations
        return result
```

---

## 8. Dry Run

Let's dry run for `digits = "23"` ($N=2$).

### Keypad Mapping: `'2'` $\rightarrow$ `"abc"`, `'3'` $\rightarrow$ `"def"`.

### Decision Tree Recursion Trace

```text
backtrack(0, "")
  ├─ '2' -> 'a': backtrack(1, "a")
  │   ├─ '3' -> 'd': backtrack(2, "ad") -> Base Case! Append "ad"
  │   ├─ '3' -> 'e': backtrack(2, "ae") -> Base Case! Append "ae"
  │   └─ '3' -> 'f': backtrack(2, "af") -> Base Case! Append "af"
  ├─ '2' -> 'b': backtrack(1, "b")
  │   ├─ '3' -> 'd': backtrack(2, "bd") -> Base Case! Append "bd"
  │   ├─ '3' -> 'e': backtrack(2, "be") -> Base Case! Append "be"
  │   └─ '3' -> 'f': backtrack(2, "bf") -> Base Case! Append "bf"
  └─ '2' -> 'c': backtrack(1, "c")
      ├─ '3' -> 'd': backtrack(2, "cd") -> Base Case! Append "cd"
      ├─ '3' -> 'e': backtrack(2, "ce") -> Base Case! Append "ce"
      └─ '3' -> 'f': backtrack(2, "cf") -> Base Case! Append "cf"
```

### Output
Returns **`["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`**.

---

## 9. Complexity Analysis

### Time Complexity: $\mathcal{O}(4^N \cdot N)$
- Where $N = \text{len}(digits)$.
- Each digit maps to 3 or 4 letters. The maximum number of leaf nodes generated is $4^N$ (e.g. for `digits = "7979"`).
- For each of the $4^N$ combinations, string concatenation of length $N$ takes $\mathcal{O}(N)$ time.
- Total time complexity: $\mathcal{O}(4^N \cdot N)$. Since $N \le 4$, $4^4 \cdot 4 = 1024$ operations max (instantaneous).

### Space Complexity: $\mathcal{O}(N)$ Auxiliary Space
- **Recursion Stack:** Maximum call stack depth equals $N$ (height of decision tree).
- **Result Output:** $\mathcal{O}(4^N \cdot N)$ space to store the returned combinations.

---

## 10. Edge Cases

| Edge Case Scenario | Input Example | Behavior & Output | How Code Handles It |
| :--- | :--- | :--- | :--- |
| **Empty Input** | `digits = ""` | Output: `[]` | `if not digits: return []` returns empty array. |
| **Single Digit** | `digits = "2"` | Output: `["a", "b", "c"]` | Recursion depth 1, appends 3 single-char strings. |
| **4-Letter Digits** | `digits = "7"` | Output: `["p", "q", "r", "s"]` | Maps `'7'` to 4 choices smoothly. |
| **Max Length (4)** | `digits = "9999"` | Output: $4^4=256$ strings | Explores all 256 paths to length 4. |

---

## 11. Alternative Approaches

### Approach 1: Iterative Queue (BFS / Breadth-First Search)
- **Idea:** Use a queue starting with `[""]`. For each digit, pop element, append each candidate letter, and push back onto queue.
  ```python
  result = [""]
  for d in digits:
      result = [prev + ch for prev in result for ch in phone[d]]
  return result if digits else []
  ```
- **Why Great:** Iterative, concise list comprehension, no recursion stack overhead.

### Approach 2: Recursive Backtracking (User's Solution - Recommended)
- **Idea:** Depth-First Search down decision tree.
- **Complexity:** $\mathcal{O}(4^N \cdot N)$ time, $\mathcal{O}(N)$ stack space.
- **Why Optimal:** Standard interview blueprint for backtracking problems.

---

## 12. Common Mistakes

> [!WARNING]
> 1. **Returning `[""]` for Empty Input:** Omitting `if not digits: return []` causes `backtrack(0, "")` to execute once and return `[""]` instead of `[]`.
> 2. **String Immutability Overhead:** Passing `current + ch` creates a new string at each call. (In Python this is fast and clean; in languages like Java a `StringBuilder` is preferred).
> 3. **Confusing Backtracking with Permutations:** Attempting to track a `visited` set when digits can produce repeated characters across levels.

---

## 13. Interview Questions

1. **Q: Why does the recursion stack require only $\mathcal{O}(N)$ space?**
   - *A:* Because Depth-First Search explores one path completely to depth $N$ before stepping back. At any point in time, the maximum number of frames on the call stack is equal to the height of the tree ($N$).

2. **Q: How would you implement this iteratively using BFS?**
   - *A:* Maintain a queue initialized with `[""]`. For each digit, pop all current combinations, append every candidate letter for that digit, and enqueue the new strings.

3. **Q: What is the maximum number of combinations possible for input length $N \le 4$?**
   - *A:* $4^4 = 256$ combinations (when digits consist of `'7'` or `'9'`).

---

## 14. Similar Problems

- **Medium:**
  - [LeetCode #22 - Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
  - [LeetCode #39 - Combination Sum](https://leetcode.com/problems/combination-sum/)
  - [LeetCode #46 - Permutations](https://leetcode.com/problems/permutations/)
- **Hard:**
  - [LeetCode #51 - N-Queens](https://leetcode.com/problems/n-queens/)

---

## 15. Learning Summary

- **Pattern Recognized:** Decision Tree Exploration via Recursive Backtracking (DFS).
- **Base Case Condition:** `index == len(digits)` signifies reaching a complete combination path.
- **Complexity Bound:** Bounded by max choices per level ($4^N$).

---

## 16. Optimization Notes

Your solution is **100% optimal** ($\mathcal{O}(4^N \cdot N)$ Time, $\mathcal{O}(N)$ Auxiliary Space). It is clean, readable, and represents the exact gold-standard solution for backtracking interviews!
