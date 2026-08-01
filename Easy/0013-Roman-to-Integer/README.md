# 0013. Roman to Integer

![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen?style=for-the-badge)
![Topic: Hash Table](https://img.shields.io/badge/Topic-Hash%20Table-blue?style=for-the-badge)
![Topic: Math](https://img.shields.io/badge/Topic-Math-green?style=for-the-badge)
![Topic: String](https://img.shields.io/badge/Topic-String-purple?style=for-the-badge)

---

## 1. Problem Information

- **Problem Name:** Roman to Integer
- **LeetCode Number:** 13
- **Difficulty:** Easy
- **Tags:** Hash Table, Math, String
- **Language Used:** Python
- **Problem Link:** [LeetCode #13 - Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

---

## 2. Problem Overview

Given a Roman numeral string `s`, convert it to an integer.

Roman numerals are represented by seven basic symbols:

| Symbol | Value |
| :---: | :---: |
| **I** | `1` |
| **V** | `5` |
| **X** | `10` |
| **L** | `50` |
| **C** | `100` |
| **D** | `500` |
| **M** | `1000` |

### Subtractive Rules:
- `I` before `V` (5) or `X` (10) $\rightarrow$ **4** (`IV`) and **9** (`IX`)
- `X` before `L` (50) or `C` (100) $\rightarrow$ **40** (`XL`) and **90** (`XC`)
- `C` before `D` (500) or `M` (1000) $\rightarrow$ **400** (`CD`) and **900** (`CM`)

### Input & Output Specifications
- **Input:** A valid Roman numeral string `s` ($1 \le \text{len}(s) \le 15$).
- **Output:** An integer representing the converted value ($1 \le \text{value} \le 3999$).

### Examples
- **Example 1:**
  - **Input:** `s = "III"` $\rightarrow$ **Output:** `3`
- **Example 2:**
  - **Input:** `s = "LVIII"` $\rightarrow$ **Output:** `58` ($L=50, V=5, III=3$)
- **Example 3:**
  - **Input:** `s = "MCMXCVI"` $\rightarrow$ **Output:** `1994` ($M=1000, CM=900, XC=90, IV=4$)

---

## 3. Intuition

> [!TIP]
> **Subtractive Rule Insight:** If a symbol's value is **strictly smaller** than the value of the symbol immediately following it, **subtract** it; otherwise **add** it!

### Mathematical Pattern:
Consider `"IV"`:
- `roman['I'] = 1`, `roman['V'] = 5`
- Since $1 < 5$, we subtract $1$: $-1 + 5 = 4$.

Consider `"VI"`:
- `roman['V'] = 5`, `roman['I'] = 1`
- Since $5 \ge 1$, we add $5$: $+5 + 1 = 6$.

By inspecting adjacent characters `(s[i], s[i+1])`, we can convert the entire string in a single linear scan without needing to pre-parse 2-character pairs!

---

## 4. Thought Process

```mermaid
flowchart TD
    A[Start: Input s] --> B[Initialize roman dictionary with 7 symbol values]
    B --> C[Initialize total = 0]
    C --> D[Loop i from 0 to len s - 1]
    D --> E{Is i < len s - 1 and roman s[i] < roman s[i+1]?}
    E -- Yes --> F[Subtract: total -= roman s[i]]
    E -- No --> G[Add: total += roman s[i]]
    F --> H{More characters?}
    G --> H
    H -- Yes --> D
    H -- No --> I[Return total]
```

1. **Map Symbols to Numeric Values:**
   - Create a dictionary `roman` mapping `'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000`.

2. **Single Pass Iteration with Lookahead:**
   - Iterate index `i` from `0` to `len(s) - 1`.
   - Compare `s[i]` value with next symbol `s[i+1]` (ensuring `i < len(s) - 1` to avoid index overflow).
   - If `roman[s[i]] < roman[s[i+1]]`:
     - Subtract current value: `total -= roman[s[i]]`.
   - Else:
     - Add current value: `total += roman[s[i]]`.

3. **Return Sum:**
   - Return accumulated `total`.

---

## 5. Concepts Used

### 1. Hash Table Mapping
- **What it is:** Using a dictionary for constant time $\mathcal{O}(1)$ key-value lookups.
- **Why it is used here:** Instantly resolves character symbols to their numeric values.
- **Future applications:** Integer to Roman, Group Anagrams, Two Sum.

### 2. Lookahead Comparison Pattern
- **What it is:** Inspecting index `i+1` while processing index `i`.
- **Why it is used here:** Dynamically detects subtractive notation without requiring complex string tokenization.
- **Future applications:** Text Parsing, String Matching, Lexical Scanners.

---

## 6. Algorithm Used

### Hash Map Traversal with Subtractive Lookahead

- **Algorithm Category:** Hash Table / String
- **Why selected:** Optimal, intuitive, and executes in a single linear pass.
- **Time Complexity:** $\mathcal{O}(N)$ (where $N \le 15 \Rightarrow \mathcal{O}(1)$).
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space.

---

## 7. Code Walkthrough

Below is the line-by-line breakdown of the submitted solution:

```python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Line 9-17: Hash Map of Roman symbols to integer values
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Line 19: Numerical Accumulator
        total = 0

        # Line 21: Iterate left-to-right through input string
        for i in range(len(s)):
            # Line 22-23: Lookahead Check for Subtractive Notation
            # If current character value is less than next character value, subtract it.
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            # Line 24-25: Additive Property
            else:
                total += roman[s[i]]

        # Line 27: Return total converted integer
        return total
```

---

## 8. Dry Run

Let's dry run for `s = "MCMXCVI"` ($N=7$).

### Execution Trace

| Index `i` | `s[i]` | `roman[s[i]]` | Lookahead `s[i+1]` | `roman[s[i+1]]` | Condition (`val < next_val`) | Action | `total` (After) |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| **0** | `'M'` | `1000` | `'C'` | `100` | $1000 < 100$ (False) | `total += 1000` | `1000` |
| **1** | `'C'` | `100` | `'M'` | `1000` | $100 < 1000$ (**True!**) | `total -= 100` | `900` |
| **2** | `'M'` | `1000` | `'X'` | `10` | $1000 < 10$ (False) | `total += 1000` | `1900` |
| **3** | `'X'` | `10` | `'C'` | `100` | $10 < 100$ (**True!**) | `total -= 10` | `1890` |
| **4** | `'C'` | `100` | `'V'` | `5` | $100 < 5$ (False) | `total += 100` | `1990` |
| **5** | `'V'` | `5` | `'I'` | `1` | $5 < 1$ (False) | `total += 5` | `1995` |
| **6** | `'I'` | `1` | None | - | End of string | `total += 1` | **`1994`** |

### Output
Returns **`1994`**.

---

## 9. Complexity Analysis

### Time Complexity: $\mathcal{O}(N)$
- Loops through input string `s` of length $N$ exactly once.
- Since valid Roman numerals are bounded by $3999$, $N \le 15$.
- Runtime is strictly bounded $\mathcal{O}(1)$ constant time.

### Space Complexity: $\mathcal{O}(1)$ Auxiliary Space
- Uses a fixed 7-element hash map `roman`.
- Uses a single primitive integer `total`.
- Overall auxiliary space is $\mathcal{O}(1)$.

---

## 10. Edge Cases

| Edge Case Scenario | Input Example | Behavior & Output | How Code Handles It |
| :--- | :--- | :--- | :--- |
| **Single Character** | `s = "M"` | Output: `1000` | Loop runs once, `i < len(s) - 1` is False, adds `1000`. |
| **All Additive** | `s = "VIII"` | Output: `8` | Lookahead condition is never True, adds $5+1+1+1=8$. |
| **Subtractive Pairs** | `s = "IV"` | Output: `4` | `i=0`: `'I' < 'V'` subtracts `1`. `i=1`: adds `5`. $-1+5 = 4$. |
| **Complex Subtractive** | `s = "CDXCIX"` | Output: `499` | Handles `CD` (-100+500), `XC` (-10+100), `IX` (-1+10). |

---

## 11. Alternative Approaches

### Approach 1: String Replacement Trick ($\mathcal{O}(N)$ Time, $\mathcal{O}(N)$ Space)
- **Idea:** Replace subtractive pairs with additive equivalents before summing:
  ```python
  s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
  return sum(roman[ch] for ch in s)
  ```
- **Drawback:** Creates temporary strings in memory via string replacement heap allocations.

### Approach 2: Right-to-Left Scan ($\mathcal{O}(N)$ Time, $\mathcal{O}(1)$ Space)
- **Idea:** Iterate backwards from last character, tracking `max_seen_val`. If current value $< \text{max\_seen\_val}$, subtract; else add and update `max_seen_val`.
- **Complexity:** Identical performance.

### Approach 3: Left-to-Right Lookahead Scan (User's Solution - Recommended)
- **Idea:** Compare `roman[s[i]] < roman[s[i+1]]`.
- **Complexity:** $\mathcal{O}(N)$ time, $\mathcal{O}(1)$ space.
- **Why Optimal:** Cleanest, most straightforward approach in coding interviews.

---

## 12. Common Mistakes

> [!WARNING]
> 1. **Index Out of Bounds:** Forgetting `i < len(s) - 1` check when inspecting `s[i + 1]`.
> 2. **Always Adding Values:** Failing to subtract when a smaller symbol precedes a larger one (e.g. evaluating `"IV"` as $1 + 5 = 6$ instead of $4$).
> 3. **Manual Substring Tokenization:** Hardcoding checks for 2-character substrings like `if s[i:i+2] == "IV":` which clutters code unnecessarily.

---

## 13. Interview Questions

1. **Q: Why does checking `roman[s[i]] < roman[s[i+1]]` work for all 6 subtractive cases?**
   - *A:* Because in Roman numeral rules, subtractive notation occurs *if and only if* a smaller value symbol immediately precedes a larger value symbol.

2. **Q: What is the maximum possible length of a valid Roman numeral string for `num <= 3999`?**
   - *A:* 15 characters (e.g., `"MMMDCCCLXXXVIII"` for `3888`).

3. **Q: How does this approach compare to Right-to-Left scanning?**
   - *A:* Both run in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space. Left-to-Right with lookahead reads in natural reading order and avoids extra pointer tracking variables.

---

## 14. Similar Problems

- **Medium:**
  - [LeetCode #12 - Integer to Roman](https://leetcode.com/problems/integer-to-roman/)
- **Hard:**
  - [LeetCode #273 - Integer to English Words](https://leetcode.com/problems/integer-to-english-words/)

---

## 15. Learning Summary

- **Pattern Recognized:** Single Pass Traversal with Lookahead Comparison.
- **Key Logic:** `total -= val` if `curr_val < next_val` else `total += val`.
- **Space Efficiency:** Constant $\mathcal{O}(1)$ auxiliary memory via simple dictionary lookups.

---

## 16. Optimization Notes

Your code is **100% optimal** ($\mathcal{O}(N)$ Time, $\mathcal{O}(1)$ Space). It is clean, elegant, and represents the standard interview solution!
