# 0022. Generate Parentheses

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)
![Topic: String](https://img.shields.io/badge/Topic-String-blue?style=for-the-badge)
![Topic: Dynamic Programming](https://img.shields.io/badge/Topic-Dynamic%20Programming-green?style=for-the-badge)
![Topic: Backtracking](https://img.shields.io/badge/Topic-Backtracking-purple?style=for-the-badge)

---

## 1. Problem Information

- **Problem Name:** Generate Parentheses
- **LeetCode Number:** 22
- **Difficulty:** Medium
- **Tags:** String, Dynamic Programming, Backtracking
- **Language Used:** Python
- **Problem Link:** [LeetCode #22 - Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

---

## 2. Problem Overview

Given `n` pairs of parentheses, write a function to generate all combinations of **well-formed parentheses**.

### Input & Output Specifications
- **Input:** An integer `n` ($1 \le n \le 8$).
- **Output:** A list of strings containing all valid well-formed parenthesis combinations.

### Examples
- **Example 1:**
  - **Input:** `n = 3`
  - **Output:** `["((()))","(()())","(())()","()(())","()()()"]`
- **Example 2:**
  - **Input:** `n = 1`
  - **Output:** `["()"]`

### Real-World Intuition
Think of compiler expression parsers or HTML/XML tag generators. When generating valid nested code structures (like `<div><div></div></div>`), the code generator enforces two invariants:
1. You can open a new scope as long as the total open tags haven't exceeded $N$.
2. You can close a scope only if there is currently an unclosed open tag waiting to be closed.

---

## 3. Intuition

> [!TIP]
> **Constraint-Guided Backtracking Rule:**
> 1. Add `'('` if `open_count < n`.
> 2. Add `')'` if `close_count < open_count`.

### Brute Force vs. Backtracking:
- **Brute Force:** Generate all $2^{2n}$ possible strings of length $2n$ consisting of `'('` and `')'`, then validate each with a stack. This takes $\mathcal{O}(2^{2n} \cdot n)$ time.
- **Smart Backtracking (Pruning):** Build only valid strings from left to right:
  - Track `open_count` (number of `'('` used) and `close_count` (number of `')'` used).
  - Can append `'('` whenever `open_count < n`.
  - Can append `')'` **only when** `close_count < open_count`.
  - When `len(current) == 2 * n`, the generated string is guaranteed to be valid!

---

## 4. Thought Process

```mermaid
flowchart TD
    A[Start: Input n] --> B[Initialize result = empty list]
    B --> C[Call backtrack path="", open_count=0, close_count=0]
    C --> D{Is len current == 2 * n?}
    D -- Yes --> E[Append current to result]
    E --> F[Return / Step Back]
    D -- No --> G{Is open_count < n?}
    G -- Yes --> H[Recursive call: backtrack current + '(', open_count + 1, close_count]
    G -- No --> I{Is close_count < open_count?}
    H --> I
    I -- Yes --> J[Recursive call: backtrack current + ')', open_count, close_count + 1]
    I -- No --> F
    J --> F
    F --> K[Return result]
```

1. **Initialize Output List:**
   - `result = []`

2. **Recursive Helper `backtrack(current, open_count, close_count)`:**
   - **Base Case:** `if len(current) == 2 * n:` append `current` to `result` and return.
   - **Branch 1 (Add '('):** If `open_count < n`, invoke `backtrack(current + "(", open_count + 1, close_count)`.
   - **Branch 2 (Add ')'):** If `close_count < open_count`, invoke `backtrack(current + ")", open_count, close_count + 1)`.

3. **Start Execution:**
   - Call `backtrack("", 0, 0)` and return `result`.

---

## 5. Concepts Used

### 1. Backtracking with State Constraints
- **What it is:** Incrementally constructing candidate solutions while pruning invalid decision branches early.
- **Why it is used here:** Ensures every generated path reaches length $2n$ as a valid parenthesis string without generating invalid candidates.
- **Future applications:** Combination Sum, N-Queens, Sudoku Solver.

### 2. Catalan Number Combinatorics
- **What it is:** The sequence of natural numbers that occur in various counting problems in combinatorics.
- **Why it is used here:** The total number of valid parenthesis combinations of length $2n$ equals the $n$-th Catalan number $C_n$:
  $$C_n = \frac{1}{n+1}\binom{2n}{n} \approx \frac{4^n}{n\sqrt{\pi n}}$$
- **Future applications:** Binary Trees enumeration, Polygon Triangulation.

---

## 6. Algorithm Used

### Recursive Backtracking with Open/Close Count Pruning

- **Algorithm Category:** Backtracking / Recursion / String
- **Why selected:** Generates exactly $C_n$ valid outputs without wasteful candidate creation.
- **Time Complexity:** $\mathcal{O}\left(\frac{4^n}{\sqrt{n}}\right)$
- **Space Complexity:** $\mathcal{O}(n)$ auxiliary call stack space

---

## 7. Code Walkthrough

Below is the line-by-line breakdown of the submitted solution:

```python
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        # Line 9: Initialize list accumulator
        result = []

        # Line 11: Recursive Backtracking helper function
        def backtrack(current, open_count, close_count):

            # Line 14-16: Base Case - Target length 2 * n reached
            if len(current) == 2 * n:
                result.append(current)
                return

            # Line 19-20: Branch 1 - Add '(' if remaining quota exists
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Line 23-24: Branch 2 - Add ')' if unmatched '(' exist
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        # Line 26: Kickoff backtracking with empty string and 0 counts
        backtrack("", 0, 0)

        # Line 28: Return list of all valid combinations
        return result
```

---

## 8. Dry Run

Let's dry run for `n = 2` ($2n = 4$).

### Decision Tree Recursion Trace

```text
backtrack("", 0, 0)
  ├─ '(' -> backtrack("(", 1, 0)
  │   ├─ '(' -> backtrack("((", 2, 0)
  │   │   └─ ')' -> backtrack("(())", 2, 1)
  │   │       └─ ')' -> backtrack("(())", 2, 2) -> Base Case! Append "(())"
  │   └─ ')' -> backtrack("()", 1, 1)
  │       └─ '(' -> backtrack("()(", 2, 1)
  │           └─ ')' -> backtrack("()()", 2, 2) -> Base Case! Append "()()"
```

### Output
Returns **`["(())", "()()"]`**.

---

## 9. Complexity Analysis

### Time Complexity: $\mathcal{O}\left(\frac{4^n}{\sqrt{n}}\right)$
- The number of valid parenthesis combinations for $n$ pairs is the $n$-th Catalan number $C_n = \frac{1}{n+1}\binom{2n}{n}$.
- Asymptotically, $C_n = \mathcal{O}\left(\frac{4^n}{n\sqrt{n}}\right)$.
- Each combination of length $2n$ requires $\mathcal{O}(n)$ time to copy into `result`.
- Total time complexity is $\mathcal{O}\left(C_n \cdot n\right) = \mathcal{O}\left(\frac{4^n}{\sqrt{n}}\right)$. For $n=8$, $C_8 = 1430$ operations (instantaneous).

### Space Complexity: $\mathcal{O}(n)$ Auxiliary Space
- The maximum depth of the recursion tree is $2n$.
- Auxiliary call stack space is $\mathcal{O}(n)$ (excluding space used by output list).

---

## 10. Edge Cases

| Edge Case Scenario | Input Example | Behavior & Output | How Code Handles It |
| :--- | :--- | :--- | :--- |
| **Minimum Input** | `n = 1` | Output: `["()"]` | Recursion reaches `len == 2`, returns `["()"]`. |
| **Maximum Input** | `n = 8` | Output: 1430 strings | Generates all 1430 valid sequences without stack overflow. |
| **Symmetric Pairs** | `n = 3` | Output: 5 valid strings | Correctly generates nested `((()))` and sequential `()()()`. |

---

## 11. Alternative Approaches

### Approach 1: Brute Force Generation + Stack Check ($\mathcal{O}(2^{2n} \cdot n)$ Time)
- **Idea:** Generate all $2^{2n}$ strings, test each with LC #20 Valid Parentheses algorithm.
- **Drawback:** Inefficient, tests thousands of invalid strings like `"))(("`.

### Approach 2: Closure Number Dynamic Programming ($\mathcal{O}\left(\frac{4^n}{\sqrt{n}}\right)$ Time, $\mathcal{O}(C_n)$ Space)
- **Idea:** Express valid string as `(` + `left_valid` + `)` + `right_valid`.
- **Complexity:** Same asymptotic time, but higher memory footprint.

### Approach 3: Backtracking with Open/Close Counts (User's Solution - Recommended)
- **Idea:** Direct DFS with `open_count` and `close_count` bounds.
- **Complexity:** $\mathcal{O}\left(\frac{4^n}{\sqrt{n}}\right)$ time, $\mathcal{O}(n)$ auxiliary stack space.
- **Why Optimal:** Standard, gold-standard interview implementation.

---

## 12. Common Mistakes

> [!WARNING]
> 1. **Allowing `close_count > open_count`:** Omitting `if close_count < open_count` allows closing brackets to precede opening brackets, generating invalid sequences like `")("`.
> 2. **Forgetting Base Case Condition:** Using `len(current) == n` instead of `len(current) == 2 * n`.
> 3. **Using Global State:** Mutating a single global list without clearing it between function invocations.

---

## 13. Interview Questions

1. **Q: Why does the condition `close_count < open_count` guarantee valid parentheses?**
   - *A:* A parenthesis string is valid if and only if at any prefix, the number of closing brackets never exceeds the number of opening brackets, and the total counts are equal at the end. Enforcing `close_count < open_count` guarantees this prefix invariant at every step.

2. **Q: What is the relationship between this problem and Catalan Numbers?**
   - *A:* The total number of valid parenthesis strings of $n$ pairs is given by the $n$-th Catalan number $C_n = \frac{1}{n+1}\binom{2n}{n}$.

3. **Q: What is the maximum value of $n$ on LeetCode and how many combinations does it yield?**
   - *A:* $n = 8$, yielding $C_8 = 1430$ combinations.

---

## 14. Similar Problems

- **Easy:**
  - [LeetCode #20 - Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- **Medium:**
  - [LeetCode #17 - Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
  - [LeetCode #39 - Combination Sum](https://leetcode.com/problems/combination-sum/)
- **Hard:**
  - [LeetCode #32 - Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)

---

## 15. Learning Summary

- **Pattern Recognized:** Decision Tree Backtracking with State Counters (`open_count`, `close_count`).
- **Pruning Logic:** `open_count < n` to add `'('`, `close_count < open_count` to add `')'`.
- **Combinatorial Growth:** Solution output size follows Catalan numbers $C_n$.

---

## 16. Optimization Notes

Your solution is **100% optimal** ($\mathcal{O}\left(\frac{4^n}{\sqrt{n}}\right)$ Time, $\mathcal{O}(n)$ Auxiliary Stack Space). It is clean, elegant, and represents the gold-standard interview implementation!
