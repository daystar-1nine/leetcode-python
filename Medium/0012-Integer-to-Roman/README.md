# 0012. Integer to Roman

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)
![Topic: Math](https://img.shields.io/badge/Topic-Math-blue?style=for-the-badge)
![Topic: String](https://img.shields.io/badge/Topic-String-green?style=for-the-badge)
![Topic: Greedy](https://img.shields.io/badge/Topic-Greedy-purple?style=for-the-badge)

---

## 1. Problem Information

- **Problem Name:** Integer to Roman
- **LeetCode Number:** 12
- **Difficulty:** Medium
- **Tags:** Hash Table, Math, String, Greedy
- **Language Used:** Python
- **Problem Link:** [LeetCode #12 - Integer to Roman](https://leetcode.com/problems/integer-to-roman/)

---

## 2. Problem Overview

Seven different symbols represent Roman numerals:

| Symbol | Value |
| :---: | :---: |
| **I** | `1` |
| **V** | `5` |
| **X** | `10` |
| **L** | `50` |
| **C** | `100` |
| **D** | `500` |
| **M** | `1000` |

Roman numerals are usually written largest to smallest from left to right. However, there are six instances where **subtractive notation** is used:
- `I` can be placed before `V` (5) and `X` (10) to make **4** (`IV`) and **9** (`IX`).
- `X` can be placed before `L` (50) and `C` (100) to make **40** (`XL`) and **90** (`XC`).
- `C` can be placed before `D` (500) and `M` (1000) to make **400** (`CD`) and **900** (`CM`).

Given an integer `num`, convert it to a **Roman numeral string**.

### Input & Output Specifications
- **Input:** An integer `num` ($1 \le \text{num} \le 3999$).
- **Output:** A string representing the Roman numeral format.

### Examples
- **Example 1:**
  - **Input:** `num = 3749` $\rightarrow$ **Output:** `"MMDCCXLIX"`
  - **Explanation:** $3000 = \text{MMM}$, $700 = \text{DCC}$, $40 = \text{XL}$, $9 = \text{IX}$.
- **Example 2:**
  - **Input:** `num = 58` $\rightarrow$ **Output:** `"LVIII"`
  - **Explanation:** $50 = \text{L}$, $8 = \text{VIII}$.
- **Example 3:**
  - **Input:** `num = 1994` $\rightarrow$ **Output:** `"MCMXCVI"`
  - **Explanation:** $1000 = \text{M}$, $900 = \text{CM}$, $90 = \text{XC}$, $4 = \text{IV}$.

### Real-World Intuition
Think of a cash register dispensing change using standard currency bills and coins. To minimize the number of bills handed to a customer, the register greedily picks the largest available denomination ($\$100, \$50, \$20, \$10, \$5, \$1$) repeatedly until the full balance is paid off.

---

## 3. Intuition

> [!TIP]
> **Key Insight:** Include subtractive combinations (`CM`, `CD`, `XC`, `XL`, `IX`, `IV`) directly in your lookup tables!

Instead of writing complex nested conditional logic to handle cases where digits are 4 or 9, we can treat the 6 subtractive pairs as fundamental values alongside the 7 primary symbols, creating a **13-element lookup table**:

```text
Values:  [1000, 900,  500, 400,  100, 90,   50,  40,   10,  9,    5,   4,    1]
Symbols: ["M",  "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
```

Because these values are arranged in strictly descending order, a **Greedy Strategy** guarantees correctness:
1. Find the largest value $V$ in our table that is $\le \text{num}$.
2. Append its symbol to our output string.
3. Subtract $V$ from `num`.
4. Repeat until `num == 0`.

---

## 4. Thought Process

```mermaid
flowchart TD
    A[Start: Input num] --> B[Initialize values and symbols arrays in descending order]
    B --> C[Initialize result = empty string]
    C --> D[Loop index i from 0 to len values - 1]
    D --> E{Is num >= values[i]?}
    E -- Yes --> F[Append symbols[i] to result]
    F --> G[Subtract values[i] from num]
    G --> E
    E -- No --> H{More values in array?}
    H -- Yes --> D
    H -- No --> I[Return result string]
```

1. **Construct Ordered Lookup Arrays:**
   - Define `values` array containing 13 elements: `[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]`.
   - Define `symbols` array containing matching symbols: `["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]`.

2. **Greedy Loop:**
   - Iterate through each index `i` from `0` to `12`.
   - While `num >= values[i]`:
     - Concatenate `symbols[i]` onto `result`.
     - Decrement `num -= values[i]`.

3. **Return Result:**
   - Return the concatenated string `result`.

---

## 5. Concepts Used

### 1. Greedy Choice Property
- **What it is:** Making locally optimal choices (picking the largest possible denomination) at each step to reach a global optimum.
- **Why it is used here:** Roman numeral representation always prioritizes the largest valid symbol denomination.
- **Future applications:** Coin Change, Gas Station, Jump Game.

### 2. Table-Driven Lookup Mapping
- **What it is:** Flattening special-case logic (subtractive notation pairs) into static aligned arrays.
- **Why it is used here:** Eliminates complex `if-else` branching and keeps the algorithm clean and maintainable.
- **Future applications:** Integer to English Words, Number to Hexadecimal.

---

## 6. Algorithm Used

### Greedy Value-Symbol Mapping

- **Algorithm Category:** Greedy / Math / String
- **Why selected:** Extremely simple, highly efficient, and runs in bounded $\mathcal{O}(1)$ time for all valid inputs up to 3999.
- **Time Complexity:** $\mathcal{O}(1)$
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

---

## 7. Code Walkthrough

Below is the line-by-line breakdown of the submitted solution:

```python
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        # Line 9-13: Descending value breakdown including subtractive pairs
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        # Line 15-19: Aligned Roman symbol strings matching values by index
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        # Line 21: String accumulator for output
        result = ""

        # Line 23: Iterate through thresholds from largest (1000) to smallest (1)
        for i in range(len(values)):
            # Line 24-26: Greedily subtract values[i] while num is large enough
            while num >= values[i]:
                result += symbols[i]
                num -= values[i]

        # Line 28: Return fully built Roman numeral string
        return result
```

---

## 8. Dry Run

Let's dry run for `num = 1994`.

### Initial State
- `num = 1994`, `result = ""`.

### Execution Trace

| Step `i` | `values[i]` | `symbols[i]` | `num >= values[i]` Check | Action | `num` (After) | `result` (After) |
| :---: | :---: | :---: | :---: | :--- | :---: | :--- |
| **0** | `1000` | `"M"` | $1994 \ge 1000$ (True) | Append `"M"`, `num -= 1000` | `994` | `"M"` |
| **0** | `1000` | `"M"` | $994 \ge 1000$ (False) | Next `i` | `994` | `"M"` |
| **1** | `900` | `"CM"` | $994 \ge 900$ (True) | Append `"CM"`, `num -= 900` | `94` | `"MCM"` |
| **1** | `900` | `"CM"` | $94 \ge 900$ (False) | Next `i` | `94` | `"MCM"` |
| **2-4** | `500,400,100` | `"D","CD","C"` | $94 < \text{val}$ (False) | Next `i` | `94` | `"MCM"` |
| **5** | `90` | `"XC"` | $94 \ge 90$ (True) | Append `"XC"`, `num -= 90` | `4` | `"MCMXC"` |
| **5** | `90` | `"XC"` | $4 \ge 90$ (False) | Next `i` | `4` | `"MCMXC"` |
| **6-10**| `50..5` | - | $4 < \text{val}$ (False) | Next `i` | `4` | `"MCMXC"` |
| **11** | `4` | `"IV"` | $4 \ge 4$ (True) | Append `"IV"`, `num -= 4` | `0` | `"MCMXCIV"` |
| **12** | `1` | `"I"` | $0 \ge 1$ (False) | Loop Ends | `0` | **`"MCMXCIV"`** |

---

## 9. Complexity Analysis

### Time Complexity: $\mathcal{O}(1)$
- The lookup arrays contain a fixed $13$ elements.
- For any input $1 \le \text{num} \le 3999$, the maximum number of symbol appends occurs at `3888` (`MMM888`), taking at most 15 loop iterations.
- Overall time complexity is strictly bounded $\mathcal{O}(1)$ constant time.

### Space Complexity: $\mathcal{O}(1)$ Auxiliary Space
- The `values` and `symbols` arrays consume constant space ($13$ elements).
- The returned `result` string length is at most 15 characters.
- Overall auxiliary space is $\mathcal{O}(1)$.

---

## 10. Edge Cases

| Edge Case Scenario | Input Example | Behavior & Output | How Code Handles It |
| :--- | :--- | :--- | :--- |
| **Minimum Value** | `num = 1` | Output: `"I"` | First 12 values skipped, appends `"I"`, returns `"I"`. |
| **Maximum Value** | `num = 3999` | Output: `"MMMCMXCIX"` | Greedily matches 3000 (`MMM`), 900 (`CM`), 90 (`XC`), 9 (`IX`). |
| **Single Symbol Values** | `num = 1000` | Output: `"M"` | Appends `"M"` once, `num` becomes `0`, loop terminates. |
| **Subtractive Pairs** | `num = 4` | Output: `"IV"` | Matches `values[11] = 4` directly, returning `"IV"`. |

---

## 11. Alternative Approaches

### Approach 1: Hardcoded Place-Value Digits Array ($\mathcal{O}(1)$ Time, $\mathcal{O}(1)$ Space)
- **Idea:** Create separate lookup arrays for thousands, hundreds, tens, and ones places:
  ```python
  M = ["", "M", "MM", "MMM"]
  C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
  X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
  I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
  return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]
  ```
- **Drawback:** Requires defining 40 string literals across 4 arrays; slightly less intuitive than greedy subtraction.

### Approach 2: Greedy Value-Symbol Mapping (User's Solution - Recommended)
- **Idea:** Loop through 13-element value array with `while num >= values[i]:`.
- **Complexity:** $\mathcal{O}(1)$ time, $\mathcal{O}(1)$ space.
- **Why Optimal:** Cleanest code structure, easy to explain in interviews.

---

## 12. Common Mistakes

> [!WARNING]
> 1. **Omitting Subtractive Pairs in Lookup:** Defining only `[1000, 500, 100, 50, 10, 5, 1]` forces tedious manual checks for `4` and `9` across every decimal position.
> 2. **Using `if` Instead of `while`:** Using `if num >= values[i]:` will only append `'M'` once for `3000` instead of 3 times.
> 3. **Sorting Values Ascending:** Placing `1` before `1000` causes `3749` to be converted into 3749 `'I'` symbols!

---

## 13. Interview Questions

1. **Q: Why does a Greedy Algorithm work for Roman Numeral conversion?**
   - *A:* Because the Roman numeral system is constructed such that choosing the largest valid symbol at each step always leaves a remainder that can be optimally represented by smaller symbols without violating notation rules.

2. **Q: How would you implement the inverse conversion (Roman to Integer)?**
   - *A:* Map symbols to values in a hash map. Traverse the string left-to-right: if current symbol value < next symbol value, subtract current value (e.g. `IV` $\rightarrow -1 + 5 = 4$); otherwise add current value.

3. **Q: What is the maximum length of a Roman numeral string for `num <= 3999`?**
   - *A:* 15 characters (e.g. `num = 3888` $\rightarrow$ `"MMMDCCCLXXXVIII"`).

---

## 14. Similar Problems

- **Easy:**
  - [LeetCode #13 - Roman to Integer](https://leetcode.com/problems/roman-to-integer/)
- **Hard:**
  - [LeetCode #273 - Integer to English Words](https://leetcode.com/problems/integer-to-english-words/)

---

## 15. Learning Summary

- **Pattern Recognized:** Greedy Selection with Pre-Defined Threshold Table.
- **Key Strategy:** Including subtractive pairs (`CM`, `CD`, `XC`, `XL`, `IX`, `IV`) directly in lookup tables simplifies branching logic.
- **Efficiency:** Achieving $\mathcal{O}(1)$ bounded runtime.

---

## 16. Optimization Notes

Your solution is **100% optimal** ($\mathcal{O}(1)$ Time, $\mathcal{O}(1)$ Space). It is clean, highly readable, and represents interview best practices!
