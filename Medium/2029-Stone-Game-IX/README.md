# 2029. Stone Game IX

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)
![Topic: Array](https://img.shields.io/badge/Topic-Array-blue?style=for-the-badge)
![Topic: Math](https://img.shields.io/badge/Topic-Math-green?style=for-the-badge)
![Topic: Game Theory](https://img.shields.io/badge/Topic-Game%20Theory-purple?style=for-the-badge)
![Topic: Greedy](https://img.shields.io/badge/Topic-Greedy-orange?style=for-the-badge)

---

## 1. Problem Information

- **Problem Name:** Stone Game IX
- **LeetCode Number:** 2029
- **Difficulty:** Medium
- **Tags:** Array, Math, Greedy, Counting, Game Theory
- **Language Used:** Python
- **Problem Link:** [LeetCode #2029 - Stone Game IX](https://leetcode.com/problems/stone-game-ix/)

---

## 2. Problem Overview

Alice and Bob play a game with stones. There is a array of integers `stones` where `stones[i]` represents the value of the $i$-th stone.

Alice and Bob take turns, with **Alice starting first**. On each turn, the active player can remove any stone from `stones` such that:
- The **sum of values of all removed stones so far** is **not divisible by 3**.

If a player cannot make a valid move (either all stones have been removed or every available stone makes the cumulative sum divisible by 3), that player **loses**.

Assuming Alice and Bob play **optimally**, return `True` if Alice wins the game, or `False` if Bob wins.

### Input & Output Specifications
- **Input:** `stones`: An array of positive integers ($1 \le \text{len}(stones) \le 10^5$, $1 \le \text{stones}[i] \le 10^4$).
- **Output:** `True` if Alice can guarantee a win, `False` if Bob wins.

### Examples
- **Example 1:**
  - **Input:** `stones = [2,1]`
  - **Output:** `True`
  - **Explanation:** Alice takes 1 (sum = 1). Bob cannot take 2 (sum = 3 $\rightarrow$ divisible by 3). Bob loses. Alice wins.
- **Example 2:**
  - **Input:** `stones = [2]`
  - **Output:** `False`
  - **Explanation:** Alice cannot pick 2 (sum = 2 $\rightarrow$ not divisible by 3, but then no more stones remain and Alice loses). Wait, Alice picks 2 (sum = 2), but no stones remain so Bob has no moves, but wait: if sum is not divisible by 3 and all stones are removed, Bob wins.
- **Example 3:**
  - **Input:** `stones = [5,1,2,4,3]`
  - **Output:** `False`

---

## 3. Intuition

> [!TIP]
> **Modulo 3 Remainder Reduction:**
> Every stone value can be categorized purely by its remainder modulo 3:
> - $C_0$: stones where $\text{val} \pmod 3 == 0$
> - $C_1$: stones where $\text{val} \pmod 3 == 1$
> - $C_2$: stones where $\text{val} \pmod 3 == 2$

### Winning Conditions Derivation:
1. **Role of $C_0$ stones (divisible by 3):**
   - Picking a $C_0$ stone does NOT change the cumulative sum modulo 3! It merely passes the turn to the other player.
   - Thus, only the **parity** of $C_0$ ($\text{even}$ vs $\text{odd}$) matters.

2. **Case 1: $C_0$ is EVEN**
   - Since $C_0$ is even, $C_0$ stones can be paired up and neutralized.
   - If Alice starts with $C_1$, Bob MUST respond with $C_1$, then Alice $C_2$, Bob $C_1 \dots$ to avoid sum $\equiv 0 \pmod 3$.
   - Alice wins if and only if **both** $C_1 > 0$ and $C_2 > 0$.

3. **Case 2: $C_0$ is ODD**
   - Since $C_0$ is odd, the extra $C_0$ stone flips turn order once.
   - This turn flip allows Bob to force Alice into a losing position unless the imbalance between $C_1$ and $C_2$ is large enough.
   - Alice wins if and only if $|C_1 - C_2| > 2$.

---

## 4. Thought Process

```mermaid
flowchart TD
    A[Start: Input stones array] --> B[Count remainders: count[stone % 3]++]
    B --> C{Is count[0] % 2 == 0?}
    C -- Yes EVEN --> D{Is count[1] > 0 and count[2] > 0?}
    D -- Yes --> E[Return True: Alice Wins]
    D -- No --> F[Return False: Bob Wins]
    C -- No ODD --> G{Is abs count[1] - count[2] > 2?}
    G -- Yes --> E
    G -- No --> F
```

1. **Count Modulo Frequencies:**
   - Initialize `count = [0, 0, 0]`.
   - Loop `stone` in `stones`: `count[stone % 3] += 1`.

2. **Parity Decision:**
   - **If `count[0] % 2 == 0` (EVEN):**
     - Return `count[1] > 0 and count[2] > 0`.
   - **If `count[0] % 2 != 0` (ODD):**
     - Return `abs(count[1] - count[2]) > 2`.

---

## 5. Concepts Used

### 1. Equivalence Class Reduction (Modulo Arithmetic)
- **What it is:** Mapping infinite integer values into finite equivalence classes $\{0, 1, 2\}$ based on remainder modulo 3.
- **Why it is used here:** Condenses $N \le 10^5$ arbitrary stone values into just 3 frequency counters.
- **Future applications:** Subarray Sums Divisible by K, Divisible Array Pairs.

### 2. Game Theory Strategy Invariants (Parity & Turn Flipping)
- **What it is:** Analyzing optimal moves via parity of zero-impact moves ($C_0$).
- **Why it is used here:** Avoids expensive $\mathcal{O}(3^N)$ minimax recursion tree searches, converting game theory to $\mathcal{O}(N)$ counting.
- **Future applications:** Stone Game I-VIII, Nim Games, Combinatorial Game Theory.

---

## 6. Algorithm Used

### Modulo Remainder Frequency Analysis

- **Algorithm Category:** Array / Math / Game Theory / Greedy
- **Why selected:** Reduces a complex game theory problem into an optimal $\mathcal{O}(N)$ single-pass frequency count and $\mathcal{O}(1)$ case evaluation.
- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space

---

## 7. Code Walkthrough

Below is the line-by-line breakdown of the submitted solution:

```python
class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """

        # Line 9: Frequency array for remainders [mod 0, mod 1, mod 2]
        count = [0, 0, 0]

        # Line 11-12: Populate count array in O(N) linear time
        for stone in stones:
            count[stone % 3] += 1

        # Line 15-16: Case 1 - count[0] is EVEN
        if count[0] % 2 == 0:
            return count[1] > 0 and count[2] > 0

        # Line 19: Case 2 - count[0] is ODD
        return abs(count[1] - count[2]) > 2
```

---

## 8. Dry Run

Let's dry run for 3 representative test cases:

### Case 1: `stones = [2, 1]`
- `count = [0, 1, 1]` ($C_0 = 0, C_1 = 1, C_2 = 1$).
- `count[0] % 2 == 0` (EVEN).
- Check: `count[1] > 0 and count[2] > 0` $\rightarrow 1 > 0$ and $1 > 0 \rightarrow$ **`True`**.

### Case 2: `stones = [2]`
- `count = [0, 0, 1]` ($C_0 = 0, C_1 = 0, C_2 = 1$).
- `count[0] % 2 == 0` (EVEN).
- Check: `count[1] > 0 and count[2] > 0` $\rightarrow 0 > 0$ (False) $\rightarrow$ **`False`**.

### Case 3: `stones = [5, 1, 2, 4, 3]`
- `stones % 3 = [2, 1, 2, 1, 0]`.
- `count = [1, 2, 2]` ($C_0 = 1, C_1 = 2, C_2 = 2$).
- `count[0] % 2 == 1` (ODD).
- Check: `abs(count[1] - count[2]) > 2` $\rightarrow |2 - 2| = 0 > 2$ (False) $\rightarrow$ **`False`**.

---

## 9. Complexity Analysis

### Time Complexity: $\mathcal{O}(N)$
- Where $N$ is the number of elements in `stones`.
- Single pass through `stones` to compute `count[stone % 3]`.
- Modulo and comparison operations take $\mathcal{O}(1)$ constant time.
- Total time complexity is strictly linear $\mathcal{O}(N)$.

### Space Complexity: $\mathcal{O}(1)$ Auxiliary Space
- Uses a fixed size-3 array `count = [0, 0, 0]`.
- Total auxiliary memory is $\mathcal{O}(1)$ constant space.

---

## 10. Edge Cases

| Edge Case Scenario | Input Example | Behavior & Output | How Code Handles It |
| :--- | :--- | :--- | :--- |
| **No $C_0$ Stones** | `stones = [1, 2]` | Output: `True` | `count[0] = 0` (even), `count[1]=1, count[2]=1` $\rightarrow$ True. |
| **Only $C_0$ Stones** | `stones = [3, 6, 9]` | Output: `False` | `count[1]=0, count[2]=0` $\rightarrow$ False. |
| **Large Difference in $C_1, C_2$ with Odd $C_0$** | `stones = [3, 1, 1, 1, 1]` | Output: `True` | `count[0]=1` (odd), `|4 - 0| = 4 > 2` $\rightarrow$ True. |

---

## 11. Alternative Approaches

### Approach 1: Minimax Top-Down Memoization ($\mathcal{O}(C_0 \cdot C_1 \cdot C_2)$ Time/Space)
- **Idea:** Recursively simulate game states `dp(rem_sum, c0, c1, c2, turn)`.
- **Drawback:** Extremely slow $\mathcal{O}(N^3)$ time and memory; exceeds limits for $N = 10^5$.

### Approach 2: Mathematical Case Analysis (User's Solution - Recommended)
- **Idea:** Remainder modulo 3 counting + parity case analysis.
- **Complexity:** $\mathcal{O}(N)$ time, $\mathcal{O}(1)$ space.
- **Why Optimal:** Gold standard solution; optimal $\mathcal{O}(N)$ execution time and zero auxiliary space.

---

## 12. Common Mistakes

> [!WARNING]
> 1. **Simulating the Entire Game Tree:** Attempting backtracking or full minimax DP on $N = 10^5$ leads to Time Limit Exceeded (TLE) or Memory Limit Exceeded (MLE).
> 2. **Ignoring Parity of $C_0$:** Treating $C_0$ as a single turn flip regardless of whether $C_0$ is even or odd.
> 3. **Misunderstanding Win Condition:** Forgetting that if all stones are removed without any player making cumulative sum divisible by 3, Bob automatically wins!

---

## 13. Interview Questions

1. **Q: Why does Bob win if all stones are removed without making the sum divisible by 3?**
   - *A:* According to the problem rules, Alice starts first and wants to force a win by making Bob hit a sum divisible by 3. If all stones are removed safely, Alice ran out of winning moves, so Bob wins by default.

2. **Q: Why does $C_0$ parity matter so much?**
   - *A:* Because taking a $C_0$ stone does not alter the cumulative sum modulo 3, it simply passes the turn to the opponent. If $C_0$ is even, both players can pair up $C_0$ picks without altering who gets the first non-zero pick. If $C_0$ is odd, one player gets an extra turn flip.

---

## 14. Similar Problems

- **Medium:**
  - [LeetCode #877 - Stone Game](https://leetcode.com/problems/stone-game/)
  - [LeetCode #1140 - Stone Game II](https://leetcode.com/problems/stone-game-ii/)
- **Hard:**
  - [LeetCode #1406 - Stone Game III](https://leetcode.com/problems/stone-game-iii/)
  - [LeetCode #1510 - Stone Game IV](https://leetcode.com/problems/stone-game-iv/)

---

## 15. Learning Summary

- **Pattern Recognized:** Game Theory State Space Reduction via Modulo Arithmetic.
- **Key Invariant:** $C_0$ parity determines turn-order dynamics.
- **Mathematical Formula:** Even $C_0 \Rightarrow C_1 > 0 \land C_2 > 0$; Odd $C_0 \Rightarrow |C_1 - C_2| > 2$.

---

## 16. Optimization Notes

Your solution is **100% optimal** ($\mathcal{O}(N)$ Time, $\mathcal{O}(1)$ Auxiliary Space). It is clean, readable, and represents the gold-standard interview implementation!
