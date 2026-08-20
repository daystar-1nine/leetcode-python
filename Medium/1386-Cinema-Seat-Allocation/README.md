# 1386. Cinema Seat Allocation

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)
![Topic: Array](https://img.shields.io/badge/Topic-Array-blue?style=for-the-badge)
![Topic: Hash Table](https://img.shields.io/badge/Topic-Hash%20Table-purple?style=for-the-badge)
![Topic: Bit Manipulation](https://img.shields.io/badge/Topic-Bit%20Manipulation-green?style=for-the-badge)
![Topic: Greedy](https://img.shields.io/badge/Topic-Greedy-orange?style=for-the-badge)

---

## 1. Problem Information

- **Problem Name:** Cinema Seat Allocation
- **LeetCode Number:** 1386
- **Difficulty:** Medium
- **Tags:** Array, Hash Table, Bit Manipulation, Greedy
- **Language Used:** Python
- **Problem Link:** [LeetCode #1386 - Cinema Seat Allocation](https://leetcode.com/problems/cinema-seat-allocation/)

---

## 2. Problem Overview

A cinema has $N$ rows of seats, labeled $1$ to $N$. Each row contains 10 seats, labeled $1$ to $10$.

You are given an array `reservedSeats` where `reservedSeats[i] = [row_i, seat_i]` indicates that the seat `seat_i` in row `row_i` is reserved.

Return the **maximum number of 4-person families** you can seat such that:
- Each 4-person family sits in 4 adjacent seats in the same row.
- Seats across an aisle (between seats 3 & 4 or seats 7 & 8) do not count as adjacent, except that a 4-person family can sit across the middle section (seats 4, 5, 6, 7).

### Valid 4-Person Family Block Configurations per Row:
1. **Left Block:** Seats 2, 3, 4, 5
2. **Right Block:** Seats 6, 7, 8, 9
3. **Middle Block:** Seats 4, 5, 6, 7

*Note: Seats 1 and 10 do not belong to any 4-person family block.*

### Input & Output Specifications
- **Input:**
  - `n`: Total number of rows ($1 \le n \le 10^9$).
  - `reservedSeats`: Array of `[row, seat]` pairs ($1 \le \text{len} \le \min(10 \cdot n, 10^4)$).
- **Output:** Integer representing the maximum 4-person family groups that can be seated.

### Examples
- **Example 1:**
  - **Input:** `n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]`
  - **Output:** `4`
  - **Explanation:**
    - Row 1: Seats 4-7 (middle block) is available $\rightarrow 1$ family.
    - Row 2: Seats 2-5 (left block) is available $\rightarrow 1$ family.
    - Row 3: Seats 2-5 (left) and 6-9 (right) are available $\rightarrow 2$ families. Total = 4 families.
- **Example 2:**
  - **Input:** `n = 2, reservedSeats = [[2,1],[1,8],[2,6]]` $\rightarrow$ **Output:** `3`

---

## 3. Intuition

> [!TIP]
> **Sparse Row Bitmasking:** $N$ can be up to $10^9$, but `reservedSeats` has at most $10^4$ entries.
> - Completely unreserved rows automatically accommodate **2 families** `(left 2-5 & right 6-9)`.
> - For rows with reservations, use a 10-bit integer mask for $O(1)$ block overlap checks!

### Bitmask Representation:
For any row, represent reserved seats as bits:
- Seat $s \rightarrow$ bit $(s-1)$.

Define the 3 candidate block bitmasks:
```text
Left Block   (Seats 2, 3, 4, 5) -> bits 1, 2, 3, 4 -> mask: 0000011110 (binary)
Middle Block (Seats 4, 5, 6, 7) -> bits 3, 4, 5, 6 -> mask: 0001111000 (binary)
Right Block  (Seats 6, 7, 8, 9) -> bits 5, 6, 7, 8 -> mask: 0111100000 (binary)
```

### Seating Logic per Row:
- `can_left   = (mask & left) == 0`
- `can_middle = (mask & middle) == 0`
- `can_right  = (mask & right) == 0`

1. If **both** `can_left` AND `can_right` are True $\rightarrow$ seat **2 families**.
2. Else if **any** of `can_left`, `can_middle`, or `can_right` is True $\rightarrow$ seat **1 family**.
3. Else $\rightarrow$ seat **0 families**.

---

## 4. Thought Process

```mermaid
flowchart TD
    A[Start: Input n, reservedSeats] --> B[Initialize rows hash map]
    B --> C[Loop reservedSeats: rows[row] |= 1 << seat - 1]
    C --> D[Initialize answer = n - len rows * 2]
    D --> E[Define left, middle, right bitmasks]
    E --> F[Loop each row mask in rows.values]
    F --> G[Check can_left, can_middle, can_right]
    G --> H{can_left and can_right?}
    H -- Yes --> I[answer += 2]
    H -- No --> J{can_left or can_middle or can_right?}
    J -- Yes --> K[answer += 1]
    J -- No --> L[Skip]
    I --> M{More rows?}
    K --> M
    L --> M
    M -- Yes --> F
    M -- No --> N[Return answer]
```

1. **Hash Map Reservation Bitmasking:**
   - Map `rows = {}`.
   - For `[row, seat]` in `reservedSeats`: `rows[row] |= (1 << (seat - 1))`.

2. **Handle Unreserved Rows:**
   - Total unreserved rows = `n - len(rows)`.
   - Each unreserved row gets 2 families $\rightarrow$ `answer = (n - len(rows)) * 2`.

3. **Bitwise Block Checks for Reserved Rows:**
   - `left = (1<<1) | (1<<2) | (1<<3) | (1<<4)`
   - `middle = (1<<3) | (1<<4) | (1<<5) | (1<<6)`
   - `right = (1<<5) | (1<<6) | (1<<7) | (1<<8)`
   - Loop `mask` in `rows.values()`:
     - `if can_left and can_right: answer += 2`
     - `elif can_left or can_middle or can_right: answer += 1`

4. **Return Answer:**
   - Return `answer`.

---

## 5. Concepts Used

### 1. Sparse Matrix Compression via Hash Table
- **What it is:** Storing data only for rows containing active reservations instead of building an $N \times 10$ matrix.
- **Why it is used here:** Prevents Memory Limit Exceeded (MLE) when $N = 10^9$.
- **Future applications:** Sparse Matrix Multiplication, Grid Hashing.

### 2. Bitmasking & Bitwise Overlap Detection (`mask & block == 0`)
- **What it is:** Representing seat occupancy using individual bit positions and checking for collisions via bitwise AND.
- **Why it is used here:** Evaluates 4-seat block availability in $\mathcal{O}(1)$ time.
- **Future applications:** N-Queens, Traveling Salesperson (TSP), State Compression DP.

---

## 6. Algorithm Used

### Hash Map with Bitmasking for Row Seat Reservations

- **Algorithm Category:** Array / Hash Table / Bit Manipulation / Greedy
- **Why selected:** Optimal $\mathcal{O}(R + M)$ execution time handling up to $N = 10^9$ rows seamlessly.
- **Time Complexity:** $\mathcal{O}(R + M)$ where $R = \text{len}(reservedSeats)$ and $M$ is unique reserved rows.
- **Space Complexity:** $\mathcal{O}(M)$ auxiliary space.

---

## 7. Code Walkthrough

Below is the line-by-line breakdown of the submitted solution:

```python
class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """

        # Line 9: Hash map to store bitmask of reserved seats for active rows
        rows = {}

        # Line 12-16: Populate row bitmask for each reserved seat
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = 0

            # Set (seat - 1)-th bit to 1
            rows[row] |= 1 << (seat - 1)

        # Line 19: Completely unreserved rows get 2 families each
        answer = (n - len(rows)) * 2

        # Line 22-24: Bitmasks for the 3 valid 4-seat block locations
        left = (1 << 1) | (1 << 2) | (1 << 3) | (1 << 4)   # Seats 2-5
        middle = (1 << 3) | (1 << 4) | (1 << 5) | (1 << 6) # Seats 4-7
        right = (1 << 5) | (1 << 6) | (1 << 7) | (1 << 8) # Seats 6-9

        # Line 26: Process each reserved row
        for mask in rows.values():

            # Line 28-30: Check if corresponding 4-seat block is completely empty
            can_left = (mask & left) == 0
            can_middle = (mask & middle) == 0
            can_right = (mask & right) == 0

            # Line 32-33: Both left and right blocks available -> 2 families
            if can_left and can_right:
                answer += 2

            # Line 35-36: At least one block available -> 1 family
            elif can_left or can_middle or can_right:
                answer += 1

        # Line 38: Return total maximum families seated
        return answer
```

---

## 8. Dry Run

Let's dry run for $N = 3$, `reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]`.

### Bitmask Construction
- `row 1`: seats 2, 3, 8 reserved $\rightarrow$ `mask = (1<<1) | (1<<2) | (1<<7)`.
- `row 2`: seat 6 reserved $\rightarrow$ `mask = (1<<5)`.
- `row 3`: seats 1, 10 reserved $\rightarrow$ `mask = (1<<0) | (1<<9)`.
- Completely empty rows: $3 - 3 = 0 \rightarrow$ `answer = 0 * 2 = 0`.

### Row Processing
1. **Row 1 (`mask` has seats 2, 3, 8):**
   - `can_left` = False (blocked by seats 2, 3).
   - `can_right` = False (blocked by seat 8).
   - `can_middle` = True (seats 4, 5, 6, 7 are clear!).
   - Match `elif can_middle` $\rightarrow$ `answer += 1` (`answer = 1`).
2. **Row 2 (`mask` has seat 6):**
   - `can_left` = True (seats 2, 3, 4, 5 clear).
   - `can_right` = False (blocked by seat 6).
   - `can_middle` = False (blocked by seat 6).
   - Match `elif can_left` $\rightarrow$ `answer += 1` (`answer = 2`).
3. **Row 3 (`mask` has seats 1, 10):**
   - `can_left` = True (seats 2, 3, 4, 5 clear).
   - `can_right` = True (seats 6, 7, 8, 9 clear).
   - Match `if can_left and can_right` $\rightarrow$ `answer += 2` (`answer = 4`).

### Output
Returns **`4`**.

---

## 9. Complexity Analysis

### Time Complexity: $\mathcal{O}(R + M)$
- Where $R$ is the number of reservations in `reservedSeats` ($R \le 10^4$) and $M$ is the number of unique reserved rows ($M \le R$).
- Constructing `rows` bitmasks takes $\mathcal{O}(R)$ time.
- Processing each unique row bitmask takes $\mathcal{O}(1)$ bitwise operations per row $\Rightarrow \mathcal{O}(M)$ time.
- Total time complexity is $\mathcal{O}(R + M)$ (executes in $< 2$ milliseconds).

### Space Complexity: $\mathcal{O}(M)$ Auxiliary Space
- Storing $M$ unique reserved row entries in `rows` hash map requires $\mathcal{O}(M)$ space.
- Total space complexity is $\mathcal{O}(M)$ auxiliary space.

---

## 10. Edge Cases

| Edge Case Scenario | Input Example | Behavior & Output | How Code Handles It |
| :--- | :--- | :--- | :--- |
| **No Reserved Seats** | `n = 10^9, reservedSeats = []` | Output: `2 * 10^9` | `len(rows) = 0`, returns `n * 2`. |
| **Only Window Seats Reserved** | `n = 1, reservedSeats = [[1,1],[1,10]]` | Output: `2` | Seats 1 & 10 don't block 2-5 or 6-9, returns 2. |
| **Middle Block Selection** | `n = 1, reservedSeats = [[1,3],[1,8]]` | Output: `1` | Left & right blocked, middle 4-7 available, returns 1. |

---

## 11. Alternative Approaches

### Approach 1: Full $N \times 10$ Boolean Grid ($\mathcal{O}(N)$ Time, $\mathcal{O}(N)$ Space)
- **Idea:** Allocate a 2D matrix of size $N \times 10$.
- **Drawback:** Fails with Memory Limit Exceeded (MLE) because $N = 10^9$.

### Approach 2: Hash Map + Bitmasking (User's Solution - Recommended)
- **Idea:** Sparse hash map with bitwise AND block checks.
- **Complexity:** $\mathcal{O}(R + M)$ time, $\mathcal{O}(M)$ auxiliary space.
- **Why Optimal:** Gold standard for Cinema Seat Allocation; handles sparse large $N$ efficiently.

---

## 12. Common Mistakes

> [!WARNING]
> 1. **Allocating Matrix for $N$ Rows:** Building arrays of size $N$ causes Memory Limit Exceeded (MLE) when $N = 10^9$.
> 2. **Assuming Seats 1 & 10 Block Families:** Seats 1 and 10 are outside the 4-seat blocks (2-5, 4-7, 6-9). Reservations on 1 or 10 do NOT block 4-person groups!
> 3. **Double Counting Middle Block:** Adding 3 families when both left, middle, and right are free (a row can seat at most 2 families).

---

## 13. Interview Questions

1. **Q: Why do we multiply `(n - len(rows)) * 2` for unreserved rows?**
   - *A:* Because a completely empty row can always seat 2 family groups: one in the left block (seats 2-5) and one in the right block (seats 6-9).

2. **Q: Why don't seats 1 and 10 matter for family block allocation?**
   - *A:* The valid 4-seat family configurations are 2-5, 4-7, and 6-9. None of these configurations include seat 1 or seat 10. Therefore, reservations on seats 1 and 10 can be safely ignored.

---

## 14. Similar Problems

- **Medium:**
  - [LeetCode #855 - Exam Room](https://leetcode.com/problems/exam-room/)
- **Hard:**
  - [LeetCode #2286 - Booking Concert Tickets in Groups](https://leetcode.com/problems/booking-concert-tickets-in-groups/)

---

## 15. Learning Summary

- **Pattern Recognized:** Sparse Matrix Bitmasking with Hash Map Compression.
- **Bitwise Check Invariant:** `(mask & block_mask) == 0` for $\mathcal{O}(1)$ seat availability detection.
- **Efficiency Constraint:** Scaling to $N = 10^9$ via sparse representation.

---

## 16. Optimization Notes

Your solution is **100% optimal** ($\mathcal{O}(R + M)$ Time, $\mathcal{O}(M)$ Space). It is clean, elegant, and represents the gold-standard interview implementation!
