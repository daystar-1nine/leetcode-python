# 0007. Reverse Integer

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)
![Topic: Math](https://img.shields.io/badge/Topic-Math-green?style=for-the-badge)

---

## 1. Problem Information

- **Problem Name:** Reverse Integer
- **LeetCode Number:** 7
- **Difficulty:** Medium
- **Tags:** Math
- **Language Used:** Python
- **Problem Link:** [LeetCode #7 - Reverse Integer](https://leetcode.com/problems/reverse-integer/)

---

## 2. Problem Overview

Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range $[-2^{31}, 2^{31} - 1]$, return `0`.

### Input & Output Specifications
- **Input:** A signed 32-bit integer `x`.
- **Output:** The integer with reversed digits, or `0` if an overflow occurs.
- **Constraints:**
  - $-2^{31} \le x \le 2^{31} - 1$
  - Signed 32-bit integer limits: $[-2147483648, 2147483647]$.

### Examples
- **Example 1:**
  - **Input:** `x = 123`
  - **Output:** `321`
- **Example 2:**
  - **Input:** `x = -123`
  - **Output:** `-321`
- **Example 3:**
  - **Input:** `x = 120`
  - **Output:** `21` (Leading zeros are dropped: `021` $\rightarrow$ `21`).
- **Example 4:**
  - **Input:** `x = 1534236469`
  - **Output:** `0` (Reversed number `9646324351` overflows $2^{31}-1$).

### Real-World Intuition
Consider low-level byte and digit re-ordering routines in network packet decoders (e.g. converting between Little-Endian and Big-Endian integer encodings), or verifying numerical symmetry in financial transaction IDs.

---

## 3. Intuition

> [!TIP]
> **Key Arithmetic Mechanics:** Use modulo `% 10` to pop the last digit, and multiplication `* 10` to push it onto the reversed number!

To reverse an integer mathematically without converting it to a string:
1. Extract the last digit of `x`: `digit = x % 10`.
2. Append `digit` to our reversed accumulator: `rev = rev * 10 + digit`.
3. Remove the last digit from `x`: `x = x // 10`.
4. Repeat until `x == 0`.

### Handling Negative Signs and 32-Bit Overflow
- In Python, negative integer modulo (e.g., `-123 % 10 = 7`) behaves differently than in C++/Java (where `-123 % 10 = -3`).
- To make sign handling clean and language-agnostic, extract `sign = -1 if x < 0 else 1`, and process the absolute value `x = abs(x)`.
- After re-applying `sign`, check if `rev` falls outside $[-2^{31}, 2^{31} - 1]$. If so, return `0`.

---

## 4. Thought Process

```mermaid
flowchart TD
    A[Start: Input x] --> B[Set INT_MAX = 2^31 - 1, INT_MIN = -2^31]
    B --> C[Set sign = -1 if x < 0 else 1]
    C --> D[Set x = abs(x), rev = 0]
    D --> E{Is x != 0?}
    E -- Yes --> F[Extract digit = x % 10]
    F --> G[Update rev = rev * 10 + digit]
    G --> H[Update x = x // 10]
    H --> E
    E -- No --> I[Re-apply sign: rev = rev * sign]
    I --> J{Is rev < INT_MIN or rev > INT_MAX?}
    J -- Yes --> K[Return 0 overflow]
    J -- No --> L[Return rev]
```

1. **Define Integer Range Limits:**
   - $\text{INT\_MAX} = 2^{31} - 1 = 2,147,483,647$
   - $\text{INT\_MIN} = -2^{31} = -2,147,483,648$

2. **Isolate Sign & Work with Magnitude:**
   - Extract `sign = -1` if negative, else `1`.
   - Take `x = abs(x)` to ensure standard base-10 modulo arithmetic.

3. **Digit Extraction & Reversal Loop:**
   - While `x != 0`:
     - `digit = x % 10`
     - `rev = rev * 10 + digit`
     - `x = x // 10`

4. **Sign Restoration & Overflow Validation:**
   - `rev *= sign`
   - If `rev < INT_MIN` or `rev > INT_MAX`, return `0`.
   - Otherwise, return `rev`.

---

## 5. Concepts Used

### 1. Base-10 Digit Manipulation
- **What it is:** Using `% 10` to extract the least significant digit (LSD) and `// 10` to truncate it.
- **Why it is used here:** Reverses digits purely via mathematical operations without extra string allocations.
- **Future applications:** Palindrome Number, Happy Number, Add Digits.

### 2. Fixed-Width Integer Range Checking
- **What it is:** Checking whether a variable exceeds standard 32-bit hardware register boundaries (`2^31 - 1` and `-2^31`).
- **Why it is used here:** Ensures compliance with signed 32-bit system limitations as required by the problem statement.
- **Future applications:** String to Integer (atoi), Multiply Strings.

---

## 6. Algorithm Used

### Mathematical Digit Reversal

- **Algorithm Category:** Math / Simulation
- **Why selected:** Runs in $\mathcal{O}(\log_{10}|x|)$ time (maximum 10 iterations) with $\mathcal{O}(1)$ auxiliary space.
- **Time Complexity:** $\mathcal{O}(\log_{10}|x|)$
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

---

## 7. Code Walkthrough

Below is the line-by-line breakdown of the submitted solution:

```python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        # Line 9-10: Define 32-bit Signed Integer Boundaries
        # INT_MAX = 2,147,483,647
        # INT_MIN = -2,147,483,648
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Line 12-13: Extract Sign and Absolute Value
        # Working with positive magnitude simplifies base-10 modulo arithmetic in Python.
        sign = -1 if x < 0 else 1
        x = abs(x)

        # Line 15: Initialize accumulator for reversed number
        rev = 0

        # Line 17-20: Pop digits from x and push onto rev
        while x != 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10

        # Line 22: Restore original sign to reversed number
        rev *= sign

        # Line 24-25: 32-Bit Overflow Verification
        # Return 0 if reversed value lies outside signed 32-bit integer limits
        if rev < INT_MIN or rev > INT_MAX:
            return 0

        # Line 27: Return valid reversed integer
        return rev
```

---

## 8. Dry Run

Let's dry run for `x = -123`.

### Initial State
- `x = -123`
- `INT_MAX = 2147483647`, `INT_MIN = -2147483648`
- `sign = -1`
- `x = abs(-123) = 123`
- `rev = 0`

### Step-by-Step Loop Execution

| Iteration | `x` (Before) | `digit` (`x % 10`) | `rev` (`rev * 10 + digit`) | `x` (After `x // 10`) |
| :---: | :---: | :---: | :---: | :---: |
| **1** | `123` | `3` | $0 \times 10 + 3 = \mathbf{3}$ | `12` |
| **2** | `12` | `2` | $3 \times 10 + 2 = \mathbf{32}$ | `1` |
| **3** | `1` | `1` | $32 \times 10 + 1 = \mathbf{321}$ | `0` |

### Post-Loop Operations
1. `rev *= sign` $\rightarrow$ `321 * -1 = -321`.
2. Overflow check: $-2147483648 \le -321 \le 2147483647$ (True).
3. Return **`-321`**.

---

## 9. Complexity Analysis

### Time Complexity: $\mathcal{O}(\log_{10}|x|)$
- A 32-bit signed integer has at most 10 decimal digits ($2,147,483,647$).
- The `while` loop runs at most 10 times $\rightarrow \mathcal{O}(1)$ constant time limit.

### Space Complexity: $\mathcal{O}(1)$ Auxiliary Space
- Uses only primitive integer variables (`INT_MAX`, `INT_MIN`, `sign`, `rev`, `digit`).
- Zero extra memory or string buffer allocations.

---

## 10. Edge Cases

| Edge Case Scenario | Input Example | Behavior & Output | How Code Handles It |
| :--- | :--- | :--- | :--- |
| **Zero** | `x = 0` | Output: `0` | `while x != 0:` loop doesn't execute, returns `0`. |
| **Trailing Zeroes** | `x = 120` | Output: `21` | First digit popped is `0`, `rev = 0`. Next is `2`, `rev = 2`. Trailing zeros naturally vanish. |
| **Positive Overflow** | `x = 1534236469` | Output: `0` | Reversed value `9646324351 > 2**31 - 1`. Triggers `rev > INT_MAX` return `0`. |
| **Negative Overflow** | `x = -2147483648` | Output: `0` | Reversed value `-8463847412 < -2**31`. Triggers `rev < INT_MIN` return `0`. |

---

## 11. Alternative Approaches

### Approach 1: String Conversion and Slicing ($\mathcal{O}(N)$ Time, $\mathcal{O}(N)$ Space)
- **Idea:** Convert `x` to string `str(abs(x))`, reverse using `[::-1]`, cast back to integer, apply sign, and check overflow.
- **Drawback:** Relies on string conversion heap allocations rather than clean mathematical operations.

### Approach 2: Mathematical Digit Reversal (User's Solution - Recommended)
- **Idea:** Use `% 10` and `// 10` arithmetic loop.
- **Complexity:** $\mathcal{O}(\log_{10}|x|)$ time, $\mathcal{O}(1)$ auxiliary space.
- **Why Great:** Fast, lightweight, pure mathematical execution.

### Approach 3: Strict 32-bit In-Loop Overflow Check (C++/Java Style)
- **Idea:** In languages where integers overflow and wrap around or crash without 64-bit support, check `if rev > INT_MAX // 10:` *before* multiplying by 10 inside the loop.

---

## 12. Common Mistakes

> [!WARNING]
> 1. **Forgetting 32-Bit Overflow Check:** Simply reversing `x` without checking against `2**31 - 1` and `-2**31` fails test cases where the reversed value exceeds integer limits.
> 2. **Relying on Python's Arbitrary Precision Ints:** In languages like C++, `rev * 10` will throw a runtime integer overflow error before the overflow check is reached. Checking `abs(x)` or doing pre-multiplication checks avoids this.
> 3. **Preserving Trailing Zeros as Strings:** Returning string output `"021"` instead of integer `21`.

---

## 13. Interview Questions

1. **Q: How would you handle this problem in a environment where 64-bit integers are completely prohibited?**
   - *A:* We would check for potential overflow *before* multiplying `rev * 10`:
     ```python
     if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > 7):
         return 0
     ```

2. **Q: Why do trailing zeros disappear during reversal?**
   - *A:* Because `rev = rev * 10 + digit` initializes `rev` to `0`. When the first popped digit is `0`, `0 * 10 + 0 = 0`, so leading zeros in the reversed number do not alter numeric magnitude.

3. **Q: What is the maximum number of digits a 32-bit signed integer can have?**
   - *A:* 10 digits (since $2^{31} - 1 = 2,147,483,647$).

---

## 14. Similar Problems

- **Easier:**
  - [LeetCode #9 - Palindrome Number](https://leetcode.com/problems/palindrome-number/)
  - [LeetCode #190 - Reverse Bits](https://leetcode.com/problems/reverse-bits/)
- **Similar Difficulty:**
  - [LeetCode #8 - String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)
  - [LeetCode #43 - Multiply Strings](https://leetcode.com/problems/multiply-strings/)

---

## 15. Learning Summary

- **Pattern Recognized:** Base-10 Digit Extraction via Modulo and Integer Division.
- **Boundary Control:** Checking signed 32-bit limits ($[-2^{31}, 2^{31} - 1]$).
- **Python Idiom:** Using `sign = -1 if x < 0 else 1` with `abs(x)` simplifies modulo operations across negative numbers.

---

## 16. Optimization Notes

Your code is **100% optimal** ($\mathcal{O}(\log_{10}|x|)$ Time, $\mathcal{O}(1)$ Space). It is clean, readable, and handles all edge cases and boundary limits perfectly!
