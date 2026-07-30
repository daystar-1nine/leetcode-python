# 0008. String to Integer (atoi)

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)
![Topic: String](https://img.shields.io/badge/Topic-String-blue?style=for-the-badge)
![Topic: Simulation](https://img.shields.io/badge/Topic-Simulation-green?style=for-the-badge)

---

## 1. Problem Information

- **Problem Name:** String to Integer (atoi)
- **LeetCode Number:** 8
- **Difficulty:** Medium
- **Tags:** String, Simulation
- **Language Used:** Python
- **Problem Link:** [LeetCode #8 - String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)

---

## 2. Problem Overview

Implement the `myAtoi(string s)` function, which converts a string into a 32-bit signed integer (similar to C/C++'s `atoi` function).

### Conversion Rules:
1. **Whitespace:** Read in and ignore any leading whitespace (`" "`).
2. **Sign:** Check if the next character is `'-'` or `'+'`. Assume the result is positive if neither is present.
3. **Conversion:** Read in characters until the next non-digit character or end of string. Ignore the rest of the string.
4. **Rounding / Clamping:** If the parsed integer falls outside the signed 32-bit range $[-2^{31}, 2^{31} - 1]$, clamp the result:
   - Integers $< -2^{31}$ clamp to $-2^{31} = -2147483648$.
   - Integers $> 2^{31} - 1$ clamp to $2^{31} - 1 = 2147483647$.

### Input & Output Specifications
- **Input:** A string `s` ($0 \le \text{len}(s) \le 200$).
- **Output:** A signed 32-bit integer.
- **Constraints:** `s` consists of English letters, digits (`0-9`), `' '`, `'+'`, `'-'`, and `'.'`.

### Examples
- **Example 1:**
  - **Input:** `s = "42"` $\rightarrow$ **Output:** `42`
- **Example 2:**
  - **Input:** `s = " -042"` $\rightarrow$ **Output:** `-42`
- **Example 3:**
  - **Input:** `s = "1337c0d3"` $\rightarrow$ **Output:** `1337` (Stops reading at `'c'`).
- **Example 4:**
  - **Input:** `s = "0-1"` $\rightarrow$ **Output:** `0` (Stops at `'-'`).
- **Example 5:**
  - **Input:** `s = "words and 987"` $\rightarrow$ **Output:** `0` (No leading digits found).

---

## 3. Intuition

> [!TIP]
> **State Machine Parsing:** Process the input string in 4 sequential stages: Whitespace $\rightarrow$ Sign $\rightarrow$ Digits $\rightarrow$ Clamping!

Instead of using complex Regular Expressions (Regex), we can model the algorithm as a sequential state machine:
1. **Skip Whitespace:** Advance pointer `i` past space characters `' '`.
2. **Inspect Sign:** Check if `s[i]` is `'+'` or `'-'`, set `sign` accordingly, and increment `i`.
3. **Parse Digits:** While `s[i]` is a digit:
   - Extract numerical value using ASCII code offset: `digit = ord(s[i]) - ord('0')`.
   - **Check for overflow BEFORE updating `num`**:
     $$\text{if } \text{num} > \frac{\text{INT\_MAX} - \text{digit}}{10}: \text{return INT\_MAX or INT\_MIN}$$
   - Update `num = num * 10 + digit`.

---

## 4. Thought Process

```mermaid
flowchart TD
    A[Start: Input s] --> B[Initialize INT_MAX = 2^31 - 1, INT_MIN = -2^31, i = 0]
    B --> C{i < n and s[i] == ' '?}
    C -- Yes --> D[i += 1]
    D --> C
    C -- No --> E{Is i == n?}
    E -- Yes --> F[Return 0 empty string]
    E -- No --> G[Initialize sign = 1]
    G --> H{s[i] == '+' or s[i] == '-'}
    H -- s[i] == '+' --> I[i += 1]
    H -- s[i] == '-' --> J[sign = -1, i += 1]
    H -- Neither --> K[Keep sign = 1]
    I --> L[Initialize num = 0]
    J --> L
    K --> L
    L --> M{i < n and s[i].isdigit()?}
    M -- Yes --> N[digit = ord s[i] - ord '0']
    N --> O{num > INT_MAX - digit // 10?}
    O -- Yes --> P[Return INT_MAX if sign == 1 else INT_MIN]
    O -- No --> Q[num = num * 10 + digit, i += 1]
    Q --> M
    M -- No --> R[Return sign * num]
```

1. **State 1: Ignore Leading Spaces:**
   - Loop `while i < n and s[i] == ' ': i += 1`.
   - Guard against empty/all-space strings: `if i == n: return 0`.

2. **State 2: Detect Optional Sign:**
   - Check `s[i] == '+'` or `s[i] == '-'`. Set `sign = -1` if `'-'`, advance pointer `i += 1`.

3. **State 3: Digit Conversion & In-Loop Overflow Protection:**
   - For every character `s[i]` where `s[i].isdigit()` is `True`:
     - Convert ASCII character to numeric digit: `digit = ord(s[i]) - ord('0')`.
     - **Pre-Overflow Inequality:** `num > (INT_MAX - digit) // 10`.
       - If this condition holds true, adding `digit` to `num * 10` will exceed `INT_MAX`. Clamp immediately and return `INT_MAX` (if `sign == 1`) or `INT_MIN` (if `sign == -1`).
     - Accumulate `num = num * 10 + digit`.
     - Advance pointer `i += 1`.

4. **Return Final Clamped Value:**
   - Return `sign * num`.

---

## 5. Concepts Used

### 1. Sequential State Machine Parsing
- **What it is:** Transitioning through explicit parsing phases (Whitespace $\rightarrow$ Sign $\rightarrow$ Digits $\rightarrow$ End).
- **Why it is used here:** Guarantees strict compliance with character sequence rules without backtracking.
- **Future applications:** Valid Number (LC #65), Basic Calculator (LC #224).

### 2. ASCII Character Arithmetic
- **What it is:** Subtracting character code `ord('0')` from `ord(ch)` to get single-digit integer value `0-9`.
- **Why it is used here:** Direct, fast, and language-independent conversion without string slicing.
- **Future applications:** Multiply Strings, Add Binary.

### 3. Algebraic In-Loop Overflow Prevention
- **What it is:** Rearranging $num \times 10 + digit > INT\_MAX$ to $num > \lfloor \frac{INT\_MAX - digit}{10} \rfloor$.
- **Why it is used here:** Prevents integer register overflow before multiplication occurs.
- **Future applications:** Reverse Integer, String to Integer.

---

## 6. Algorithm Used

### Sequential State Parsing with In-Loop Overflow Protection

- **Algorithm Category:** String / Simulation
- **Why selected:** Runs in single-pass $\mathcal{O}(N)$ linear time with $\mathcal{O}(1)$ auxiliary space and safe overflow guards.
- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

---

## 7. Code Walkthrough

Below is the line-by-line breakdown of the submitted solution:

```python
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Line 9-10: Hardware 32-bit Signed Integer Boundaries
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Line 12-13: Pointer and String Length Initialization
        i = 0
        n = len(s)

        # Line 16-17: Step 1 - Skip Leading Whitespace Characters
        while i < n and s[i] == " ":
            i += 1

        # Line 20-21: Guard Clause for Empty or Space-Only Strings
        if i == n:
            return 0

        # Line 24-29: Step 2 - Parse Optional Sign ('+' or '-')
        sign = 1
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1

        # Line 32: Accumulator for Unsigned Magnitude
        num = 0

        # Line 34: Step 3 - Process Contiguous Digits
        while i < n and s[i].isdigit():
            # Convert ASCII char to numeric digit using character code offset
            digit = ord(s[i]) - ord('0')

            # Line 38-40: Step 4 - In-Loop 32-Bit Overflow Protection Check
            # Rearranged formula (num > (INT_MAX - digit) // 10) prevents overflow before calculation.
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            # Line 42-43: Append digit to magnitude and move to next character
            num = num * 10 + digit
            i += 1

        # Line 45: Apply Sign and Return Final Integer
        return sign * num
```

---

## 8. Dry Run

Let's dry run for `s = " -042"` ($n=5$).

### Initial State
- `s = " -042"`, `i = 0`, `n = 5`, `INT_MAX = 2147483647`, `INT_MIN = -2147483648`.

### State Execution

| Phase | `i` | `s[i]` | Action | State Updates |
| :---: | :---: | :---: | :--- | :--- |
| **Space Skip** | `0` | `' '` | `s[0] == ' '` $\rightarrow$ Skip | `i = 1` |
| **Sign Check** | `1` | `'-'` | `s[1] == '-'` $\rightarrow$ Set sign | `sign = -1`, `i = 2` |
| **Digit 1** | `2` | `'0'` | `ord('0') - ord('0') = 0`<br>Check: $0 > \lfloor \frac{2147483647 - 0}{10} \rfloor$ (False) | `num = 0 * 10 + 0 = 0`, `i = 3` |
| **Digit 2** | `3` | `'4'` | `ord('4') - ord('0') = 4`<br>Check: $0 > \lfloor \frac{2147483647 - 4}{10} \rfloor$ (False) | `num = 0 * 10 + 4 = 4`, `i = 4` |
| **Digit 3** | `4` | `'2'` | `ord('2') - ord('0') = 2`<br>Check: $4 > \lfloor \frac{2147483645}{10} \rfloor$ (False) | `num = 4 * 10 + 2 = 42`, `i = 5` |
| **End** | `5` | - | `i == n` $\rightarrow$ Exit Loop | Return `sign * num` = `-1 * 42` = **`-42`** |

---

## 9. Complexity Analysis

### Time Complexity: $\mathcal{O}(N)$
- **Whitespace Scan:** At most $N$ operations.
- **Digit Scan:** Reads each character in `s` at most once.
- **Overall Time Complexity:** $\mathcal{O}(N)$ linear time.

### Space Complexity: $\mathcal{O}(1)$ Auxiliary Space
- Uses only primitive pointers and scalar values (`i`, `n`, `sign`, `num`, `digit`).
- No string copies or array allocations created.

---

## 10. Edge Cases

| Edge Case Scenario | Input Example | Behavior & Output | How Code Handles It |
| :--- | :--- | :--- | :--- |
| **Leading Whitespace** | `s = " 42"` | Output: `42` | `while s[i] == ' ':` skips space characters. |
| **Leading Zeroes** | `s = "000042"` | Output: `42` | `num = 0 * 10 + 0` handles zero digits correctly. |
| **Words After Digits** | `s = "4193 with words"` | Output: `4193` | `while s[i].isdigit()` stops when hitting space after `3`. |
| **Words Before Digits** | `s = "words and 987"` | Output: `0` | `s[0]` is `'w'`, fails `s[i].isdigit()`, returns `0`. |
| **Positive Overflow** | `s = "9223372036854775807"` | Output: `2147483647` | Pre-overflow check triggers `return INT_MAX`. |
| **Negative Overflow** | `s = "-91283472332"` | Output: `-2147483648` | Pre-overflow check triggers `return INT_MIN`. |
| **Invalid Double Sign** | `s = "+-12"` | Output: `0` | First sign advances `i` to `'-'`, which fails `.isdigit()`. |

---

## 11. Alternative Approaches

### Approach 1: Regular Expressions (`re` Module)
- **Idea:** Match pattern `r'^\s*([+-]?\d+)'` and convert group 1.
- **Drawback:** Slower execution, high memory overhead, hides low-level parsing logic expected in interviews.

### Approach 2: State Automaton (DFA) Table
- **Idea:** Create a formal 2D transition matrix for states `{START, SIGN, IN_NUM, END}`.
- **Drawback:** Requires verbose state matrix boilerplate.

### Approach 3: Sequential State Parsing (User's Solution - Recommended)
- **Idea:** 4-step pointer inspection with in-loop overflow protection.
- **Complexity:** $\mathcal{O}(N)$ time, $\mathcal{O}(1)$ space.
- **Why Optimal:** Clean, production-ready, interview standard.

---

## 12. Common Mistakes

> [!WARNING]
> 1. **Post-Overflow Checking:** Calculating `num = num * 10 + digit` *before* checking overflow causes integer overflow crashes in statically typed languages like C++/Java.
> 2. **Allowing Mid-String Spaces:** Continuing to parse digits after encountering non-digit characters (e.g., `"42 56"` yielding `4256` instead of `42`).
> 3. **Failing Double Signs:** Parsing `"+-42"` as `-42` instead of `0`.

---

## 13. Interview Questions

1. **Q: Why do we check `num > (INT_MAX - digit) // 10` before multiplying?**
   - *A:* Rearranging the inequality avoids computing `num * 10 + digit`, which would overflow 32-bit hardware registers before the check can be executed.

2. **Q: How does `ord(s[i]) - ord('0')` convert a character to a digit?**
   - *A:* ASCII character codes for digits `'0'` through `'9'` are contiguous ($48$ to $57$). Subtracting `ord('0')` ($48$) yields the exact integer value ($0$ to $9$).

3. **Q: What happens if `s = "+"` or `s = "-"`?**
   - *A:* `sign` is set to `1` or `-1`, `i` advances to `1` (`i == n`), loop `while s[i].isdigit()` fails, returns `0`.

---

## 14. Similar Problems

- **Easier:**
  - [LeetCode #7 - Reverse Integer](https://leetcode.com/problems/reverse-integer/)
- **Similar Difficulty:**
  - [LeetCode #43 - Multiply Strings](https://leetcode.com/problems/multiply-strings/)
  - [LeetCode #65 - Valid Number](https://leetcode.com/problems/valid-number/)
- **Harder:**
  - [LeetCode #224 - Basic Calculator](https://leetcode.com/problems/basic-calculator/)

---

## 15. Learning Summary

- **Pattern Recognized:** Sequential State Machine Parsing.
- **ASCII Conversion:** `ord(ch) - ord('0')` for digit evaluation.
- **Overflow Formula:** $num > \lfloor \frac{INT\_MAX - digit}{10} \rfloor$ for pre-overflow protection.

---

## 16. Optimization Notes

Your solution is **100% optimal** ($\mathcal{O}(N)$ Time, $\mathcal{O}(1)$ Auxiliary Space). It handles edge cases, leading whitespaces, invalid signs, and overflow clamping flawlessly!
