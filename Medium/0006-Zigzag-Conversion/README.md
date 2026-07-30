# 0006. Zigzag Conversion

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)
![Topic: String](https://img.shields.io/badge/Topic-String-blue?style=for-the-badge)
![Topic: Simulation](https://img.shields.io/badge/Topic-Simulation-green?style=for-the-badge)

---

## 1. Problem Information

- **Problem Name:** Zigzag Conversion
- **LeetCode Number:** 6
- **Difficulty:** Medium
- **Tags:** String, Simulation
- **Language Used:** Python
- **Problem Link:** [LeetCode #6 - Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion/)

---

## 2. Problem Overview

The problem asks us to take a given string `s` and arrange its characters in a **zigzag pattern** across a specified number of rows (`numRows`). Once the zigzag visual layout is established, we read the characters row by row, from top to bottom, left to right, to generate a new concatenated output string.

### Visual Representation of Zigzag Pattern

For `s = "PAYPALISHIRING"` and `numRows = 3`:

```text
P   A   H   N
A P L S I I G
Y   I   R
```

Reading line-by-line yields:
- **Row 0:** `"PAHN"`
- **Row 1:** `"APLSIIG"`
- **Row 2:** `"YIR"`

**Final Concatenated Result:** `"PAHNAPLSIIGYIR"`

### Input & Output Specifications
- **Input:**
  - `s`: A string of length $N$ containing alphanumeric characters, commas, and periods.
  - `numRows`: A positive integer representing the target number of rows.
- **Output:** A single string representing the row-by-row concatenation.
- **Constraints:**
  - $1 \le \text{len}(s) \le 1000$
  - $1 \le \text{numRows} \le 1000$

### Real-World Intuition
Think of a printer head moving up and down across parallel text tracks, or signal data being sampled in a continuous triangle-wave pattern across frequency channels. Instead of allocating a huge two-dimensional grid filled with blank spaces, we collect text into bucket rows as the print head bounces between the top and bottom margins.

---

## 3. Intuition

> [!TIP]
> **Key Insight:** We do **not** need to store empty spaces or construct a 2D matrix grid. We only care about which row each character belongs to!

When writing text in a zigzag pattern:
1. We start at **Row 0** and move **downwards** incrementing row index by `+1`.
2. When we reach the bottom margin (**Row `numRows - 1`**), we bounce and change direction to move **upwards** decrementing row index by `-1`.
3. When we reach the top margin (**Row `0`**), we bounce again and move **downwards**.

By creating an array of `numRows` string buckets, we simply append each character to its current row bucket and update the row tracker based on our current movement direction.

---

## 4. Thought Process

```mermaid
flowchart TD
    A[Start: Input s, numRows] --> B{Is numRows == 1 or numRows >= len(s)?}
    B -- Yes --> C[Return original string s]
    B -- No --> D[Initialize rows = array of empty strings of size numRows]
    D --> E[Set current_row = 0, direction = -1]
    E --> F[For each character 'ch' in s]
    F --> G[Append 'ch' to rows[current_row]]
    G --> H{Is current_row == 0 or current_row == numRows - 1?}
    H -- Yes --> I[Toggle direction: direction = direction * -1]
    H -- No --> J[Keep current direction]
    I --> K[current_row += direction]
    J --> K
    K --> L{More characters in s?}
    L -- Yes --> F
    L -- No --> M[Join all string buckets in rows]
    M --> N[Return final concatenated string]
```

1. **Handle Boundary Edge Cases:**
   - If `numRows == 1`, no zigzagging occurs because there is only one row. Returning `s` directly avoids unnecessary computation.
   - If `numRows >= len(s)`, every character gets its own row vertically, so the output order remains identical to `s`.

2. **Setup State Variables:**
   - `rows`: List of `numRows` empty strings: `["", "", ..., ""]`.
   - `current_row`: Pointer tracking the active row index `0 <= current_row < numRows`.
   - `direction`: Direction indicator. We start at `-1` because the first character check at `current_row == 0` toggles `-1 * -1 = +1` (moving down).

3. **Simulate Character Placement:**
   - Iterate through every character `ch` in string `s`.
   - Append `ch` to `rows[current_row]`.
   - Check boundary hit: If `current_row == 0` or `current_row == numRows - 1`, invert `direction = direction * -1`.
   - Move to next row: `current_row += direction`.

4. **Combine Results:**
   - Perform `"".join(rows)` to merge all row strings sequentially into the final answer.

---

## 5. Concepts Used

### 1. Bucket Pattern / Array of Strings
- **What it is:** Using an array where each index holds a collection or sub-string representing a distinct category or row.
- **Why it is used here:** To collect characters destined for the same row without keeping track of horizontal column spacing or blank cells.
- **Future applications:** Bucket sort, frequency counting, grouping anagrams.

### 2. State Control / Direction Toggling
- **What it is:** A technique using state variables (like `+1` and `-1`) to simulate oscillating physical motion or directional bouncing.
- **Why it is used here:** Seamlessly switches row movement between descending (`+1`) and ascending (`-1`).
- **Future applications:** Matrix spiral traversal, snake/bouncing movements in 2D grids, game loop physics.

---

## 6. Algorithm Used

### Simulated Bouncing Row Traversal

- **Algorithm Category:** Simulation / Dynamic Traversal
- **Why selected:** It mimics the natural physical motion of drawing a zigzag without performing complex index mathematics.
- **How it works:** Iterates through string `s` once ($O(N)$ steps), appending each character to one of the $K$ row buckets.
- **Time Complexity:** $O(N)$ where $N$ is the length of string `s`.
- **Space Complexity:** $O(N)$ to hold the characters across all row buckets.

---

## 7. Code Walkthrough

Below is the line-by-line explanation of the accepted Python solution:

```python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        # Line 9-10: Guard Clause for Boundary Conditions
        # If there's only 1 row or if numRows is greater than/equal to the string length,
        # no zigzagging is possible. Returning s immediately handles this efficiently.
        if numRows == 1 or numRows >= len(s):
            return s

        # Line 12: Bucket Allocation
        # Create an array of 'numRows' empty strings to store characters for each row.
        rows = [""] * numRows

        # Line 13-14: Motion Control Initialization
        # current_row tracks the active row index (0-indexed).
        # direction is set to -1 so that when the loop starts at row 0,
        # direction * -1 turns it into +1 (moving downward).
        current_row = 0
        direction = -1

        # Line 16: Iterate through each character in the input string s
        for ch in s:
            # Line 17: Append current character to its respective row bucket
            rows[current_row] += ch

            # Line 19-20: Margin Bouncing Detection
            # If current_row hits the top margin (0) or bottom margin (numRows - 1),
            # invert the direction vector (-1 becomes +1, +1 becomes -1).
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1

            # Line 22: Advance to the next row using current direction
            current_row += direction

        # Line 24: Concatenate all row buckets into a single string and return
        return "".join(rows)
```

---

## 8. Dry Run

Let's dry run the solution with `s = "PAYPALISHIRING"` and `numRows = 3`.

### Initial State
- `numRows = 3`, `len(s) = 14`. Guard clause `3 == 1 or 3 >= 14` is `False`.
- `rows = ["", "", ""]`
- `current_row = 0`
- `direction = -1`

### Step-by-Step Execution

| Step | Char `ch` | `current_row` (Before) | Action on `rows[current_row]` | Boundary Check (`0` or `2`) | `direction` (After) | `current_row` (After) | State of `rows` |
| :---: | :---: | :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `'P'` | `0` | `rows[0] += 'P'` | `0 == 0` (True) | `-1 * -1 = 1` | `0 + 1 = 1` | `["P", "", ""]` |
| 2 | `'A'` | `1` | `rows[1] += 'A'` | Neither | `1` | `1 + 1 = 2` | `["P", "A", ""]` |
| 3 | `'Y'` | `2` | `rows[2] += 'Y'` | `2 == 2` (True) | `1 * -1 = -1` | `2 + (-1) = 1` | `["P", "A", "Y"]` |
| 4 | `'P'` | `1` | `rows[1] += 'P'` | Neither | `-1` | `1 + (-1) = 0` | `["P", "AP", "Y"]` |
| 5 | `'A'` | `0` | `rows[0] += 'A'` | `0 == 0` (True) | `-1 * -1 = 1` | `0 + 1 = 1` | `["PA", "AP", "Y"]` |
| 6 | `'L'` | `1` | `rows[1] += 'L'` | Neither | `1` | `1 + 1 = 2` | `["PA", "APL", "Y"]` |
| 7 | `'I'` | `2` | `rows[2] += 'I'` | `2 == 2` (True) | `1 * -1 = -1` | `2 + (-1) = 1` | `["PA", "APL", "YI"]` |
| 8 | `'S'` | `1` | `rows[1] += 'S'` | Neither | `-1` | `1 + (-1) = 0` | `["PA", "APLS", "YI"]` |
| 9 | `'H'` | `0` | `rows[0] += 'H'` | `0 == 0` (True) | `-1 * -1 = 1` | `0 + 1 = 1` | `["PAH", "APLS", "YI"]` |
| 10 | `'I'` | `1` | `rows[1] += 'I'` | Neither | `1` | `1 + 1 = 2` | `["PAH", "APLSI", "YI"]` |
| 11 | `'R'` | `2` | `rows[2] += 'R'` | `2 == 2` (True) | `1 * -1 = -1` | `2 + (-1) = 1` | `["PAH", "APLSI", "YIR"]` |
| 12 | `'I'` | `1` | `rows[1] += 'I'` | Neither | `-1` | `1 + (-1) = 0` | `["PAH", "APLSII", "YIR"]` |
| 13 | `'N'` | `0` | `rows[0] += 'N'` | `0 == 0` (True) | `-1 * -1 = 1` | `0 + 1 = 1` | `["PAHN", "APLSII", "YIR"]` |
| 14 | `'G'` | `1` | `rows[1] += 'G'` | Neither | `1` | `1 + 1 = 2` | `["PAHN", "APLSIIG", "YIR"]` |

### Final Assembly
`"".join(["PAHN", "APLSIIG", "YIR"])` $\rightarrow$ **`"PAHNAPLSIIGYIR"`**

---

## 9. Complexity Analysis

### Time Complexity: $\mathcal{O}(N)$
- **Iterating String:** We process each of the $N$ characters in string `s` exactly once.
- **String Concatenation:** Appending single characters to strings in Python takes $O(1)$ amortized time.
- **Joining Buckets:** `"".join(rows)` iterates through all $N$ accumulated characters to produce the result in $O(N)$ time.
- **Overall Time Complexity:** $\mathcal{O}(N)$ across Best, Average, and Worst cases.

### Space Complexity: $\mathcal{O}(N)$
- **Auxiliary Bucket Memory:** The `rows` array stores $N$ total characters across `numRows` strings.
- **Output String:** The returned joined string requires $O(N)$ space.
- **Overall Space Complexity:** $\mathcal{O}(N)$ extra memory.

---

## 10. Edge Cases

| Edge Case Scenario | Input Example | Behavior & Outcome | How Code Handles It |
| :--- | :--- | :--- | :--- |
| **Single Row** | `s = "ABC"`, `numRows = 1` | Output: `"ABC"` | Caught by `if numRows == 1:` guard clause. Returns `s` instantly. |
| **numRows $\ge$ len(s)** | `s = "AB"`, `numRows = 5` | Output: `"AB"` | Caught by `numRows >= len(s)` guard clause. Returns `s` instantly. |
| **Single Character** | `s = "A"`, `numRows = 3` | Output: `"A"` | Caught by `numRows >= len(s)` guard clause ($3 \ge 1$). Returns `"A"`. |
| **Two Rows** | `s = "ABCD"`, `numRows = 2` | Alternates between Row 0 & 1 | Toggles direction at every single character step smoothly. Output: `"ACBD"`. |

---

## 11. Alternative Approaches

### Approach 1: 2D Matrix Grid (Brute Force)
- **Idea:** Create a 2D grid matrix of dimensions `numRows` $\times$ `len(s)`. Fill empty cells with spaces `' '`. Write characters along the diagonal and vertical grid paths, then traverse row by row skipping spaces.
- **Time Complexity:** $\mathcal{O}(\text{numRows} \times N)$
- **Space Complexity:** $\mathcal{O}(\text{numRows} \times N)$
- **Drawbacks:** Wasteful memory usage and excessive inner loop traversal over blank spaces.

### Approach 2: Row Bucket Simulation (User's Solution - Recommended for Interviews)
- **Idea:** Maintain `numRows` strings and track row direction using a state variable.
- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(N)$
- **Why it's great:** Simple to explain, highly intuitive, clean code, optimal time complexity.

### Approach 3: Direct Index Math / Cycle Jump ($\mathcal{O}(1)$ Auxiliary Space)
- **Idea:** Observe that characters in row $r$ follow a cycle pattern of length $\text{cycle} = 2 \times (\text{numRows} - 1)$. Jump directly through index arithmetic without allocating row buckets.
- **Time Complexity:** $\mathcal{O}(N)$
- **Auxiliary Space Complexity:** $\mathcal{O}(1)$ (excluding output string storage).

---

## 12. Common Mistakes

> [!WARNING]
> 1. **Forgetting `numRows == 1` Base Case:** If `numRows == 1`, `numRows - 1 == 0`. The condition `current_row == 0 or current_row == numRows - 1` is always true, causing continuous direction toggling and potential index out of bound bugs.
> 2. **Initial Direction Misconfiguration:** Initializing `direction = 1` before checking row boundaries can cause `current_row` to skip row 1 or double bounce. Initializing `direction = -1` with early boundary check `current_row == 0` cleanly flips it to `+1` on step 1.
> 3. **Creating Fixed-Size Matrix:** Allocating $O(N \times \text{numRows})$ 2D array unnecessarily degrades spatial efficiency when `numRows` is large (e.g. `numRows = 1000`).

---

## 13. Interview Questions

1. **Q: Why is `numRows == 1` treated as a special case?**
   - *A:* When `numRows == 1`, top (`0`) and bottom (`numRows - 1`) margins are identical. Without early exit, direction toggles every character without advancing rows properly.

2. **Q: Can we solve this problem in $\mathcal{O}(1)$ auxiliary space?**
   - *A:* Yes, by calculating index jumps mathematically using cycle length $2 \times (\text{numRows} - 1)$ for top/bottom rows and intermediate diagonals.

3. **Q: How does string immutability in Python affect time complexity when doing `rows[current_row] += ch`?**
   - *A:* In Python, string concatenation within a list is optimized (CPython performs in-place appends when refcount is 1), leading to amortized $\mathcal{O}(1)$ appends per character.

4. **Q: How would you extend this algorithm if the zigzag pattern went diagonally backwards across 2 columns?**
   - *A:* We would adjust the direction vector and maintain a column counter alongside `current_row`.

---

## 14. Similar Problems

- **Easier:**
  - [LeetCode #38 - Count and Say](https://leetcode.com/problems/count-and-say/)
- **Similar Difficulty:**
  - [LeetCode #498 - Diagonal Traverse](https://leetcode.com/problems/diagonal-traverse/)
  - [LeetCode #54 - Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
- **Harder:**
  - [LeetCode #68 - Text Justification](https://leetcode.com/problems/text-justification/)

---

## 15. Learning Summary

- **Pattern Recognized:** Oscillating boundary bouncing / State direction toggling (`direction *= -1`).
- **Core Strategy:** Grouping elements by target row buckets rather than physically modeling empty space.
- **Key Takeaway:** Avoid 2D grid allocation when grouping elements by projection row or column is sufficient.

---

## 16. Optimization Notes

Your submitted code is **optimal in terms of Time Complexity ($\mathcal{O}(N)$)** and exhibits standard interview-best practices for clarity and readability.

### Optional Mathematical Optimization ($\mathcal{O}(1)$ Auxiliary Space)
If an interviewer explicitly asks for **$\mathcal{O}(1)$ auxiliary space**, you can calculate indices directly using the cycle formula:
$$\text{cycle} = 2 \times (\text{numRows} - 1)$$

For row $i$:
- For top ($i=0$) and bottom ($i=\text{numRows}-1$) rows, index increments by `cycle`.
- For internal rows ($0 < i < \text{numRows}-1$), indices alternate between `j + cycle - 2*i` and `j + cycle`.

*(Note: Your current solution is already optimal in time and preferred for code readability during timed coding interviews!)*
