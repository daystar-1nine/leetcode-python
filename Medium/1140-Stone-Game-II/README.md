# 1140. Stone Game II

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)
![Topic: Array](https://img.shields.io/badge/Topic-Array-blue?style=for-the-badge)
![Topic: Dynamic Programming](https://img.shields.io/badge/Topic-Dynamic%20Programming-green?style=for-the-badge)
![Topic: Game Theory](https://img.shields.io/badge/Topic-Game%20Theory-purple?style=for-the-badge)

---

## 1. Problem Information

- **Problem Name:** Stone Game II
- **LeetCode Number:** 1140
- **Difficulty:** Medium
- **Tags:** Array, Math, Dynamic Programming, Game Theory, Prefix Sum
- **Language Used:** Python
- **Problem Link:** [LeetCode #1140 - Stone Game II](https://leetcode.com/problems/stone-game-ii/)

---

## 2. Problem Overview

Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each pile has a positive integer number of stones `piles[i]`. The objective of the game is to end with the **most stones**.

Alice and Bob take turns, with **Alice starting first**.

On each player's turn, that player can take all the stones in the first $X$ remaining piles, where $1 \le X \le 2M$. Then, we set $M = \max(M, X)$. Initially, $M = 1$.

The game continues until all the stones have been taken.

Assuming Alice and Bob play **optimally**, return the **maximum number of stones Alice can get**.

### Input & Output Specifications
- **Input:** `piles`: An array of positive integers ($1 \le \text{len}(piles) \le 100$).
- **Output:** An integer representing the maximum stones Alice can obtain.
- **Constraints:** $1 \le \text{piles}[i] \le 10^4$.

### Examples
- **Example 1:**
  - **Input:** `piles = [2,7,9,4,4]`
  - **Output:** `10`
  - **Explanation:**
    - If Alice takes 1 pile at beginning ($X=1, M=1$), remaining piles are `[7,9,4,4]`. Bob takes 2 piles ($X=2, M=2$). Alice takes remaining 2 piles ($X=2, M=2$). Alice gets $2 + 4 + 4 = 10$ stones.
    - If Alice takes 2 piles at beginning ($X=2, M=2$), Bob can take all 3 remaining piles. Alice gets $2 + 7 = 9$ stones.
    - Alice plays optimally and gets `10` stones.
- **Example 2:**
  - **Input:** `piles = [1,2,3,4,5,100]` $\rightarrow$ **Output:** `104`

---

## 3. Intuition

> [!TIP]
> **Zero-Sum Minimax Principle:**
> $$\text{Active\_Player\_Stones} = \text{Suffix\_Sum}[i] - \text{Opponent\_Optimal\_Stones}$$

### State Representation:
Define `dp(i, M)` as the **maximum number of stones the active player can collect** starting from pile index `i` with parameter `M`.

### Transitions:
1. **Base Case:** If $i + 2M \ge N$, the active player can take ALL remaining piles in a single turn and collect `suffix_sum[i]` stones!
2. **Choice Breakdown:** The active player can choose to take $X$ piles where $1 \le X \le 2M$.
   - Taking $X$ piles leaves the opponent facing state `(i + X, max(M, X))`.
   - The opponent will collect `dp(i + X, max(M, X))` stones.
   - Since total stones remaining from index `i` is `suffix_sum[i]`, the active player's share is:
     $$\text{suffix\_sum}[i] - dp(i + X, \max(M, X))$$
   - The active player chooses $X \in [1, 2M]$ to **maximize** their share!

---

## 4. Thought Process

```mermaid
flowchart TD
    A[Start: Input piles array] --> B[Precompute suffix_sum array backwards]
    B --> C[Initialize memo dictionary]
    C --> D[Call dp index=0, M=1]
    D --> E{Is i + 2M >= N?}
    E -- Yes --> F[Return suffix_sum[i]]
    E -- No --> G{Is i, M in memo?}
    G -- Yes --> H[Return memo[i, M]]
    G -- No --> I[Set res = 0]
    I --> J[Loop X from 1 to 2M]
    J --> K[res = max res, suffix_sum[i] - dp i + X, max M, X]
    K --> L{More X choices?}
    L -- Yes --> J
    L -- No --> M[Save memo[i, M] = res]
    M --> N[Return res]
```

1. **Precompute Suffix Sums:**
   - Compute `suffix_sum[i] = suffix_sum[i+1] + piles[i]` backwards from $i = N-1$ down to 0.

2. **Recursive Memoized Function `dp(i, M)`:**
   - **Base Case:** `if i + 2 * M >= n: return suffix_sum[i]`.
   - **Memoization Check:** `if (i, M) in memo: return memo[(i, M)]`.
   - **Recurrence Loop:**
     - `res = 0`
     - For $X$ in $1 \dots 2M$:
       - `res = max(res, suffix_sum[i] - dp(i + X, max(M, X)))`
     - Save `memo[(i, M)] = res` and return `res`.

3. **Kickoff Game:**
   - Return `dp(0, 1)`.

---

## 5. Concepts Used

### 1. Zero-Sum Complement Reduction
- **What it is:** Expressing the active player's score as the total available score minus the opponent's optimal score.
- **Why it is used here:** Avoids tracking two separate player scores, reducing state space dimension to just `(i, M)`.
- **Future applications:** Stone Game III, Predict the Winner.

### 2. Suffix Sum Precomputation
- **What it is:** Accumulating total values from the right end of an array.
- **Why it is used here:** Provides $\mathcal{O}(1)$ lookup of total remaining stones from index `i` to `N-1`.
- **Future applications:** Range Sum Queries, Subarray Sums.

---

## 6. Algorithm Used

### Top-Down Dynamic Programming with Memoization & Suffix Sums

- **Algorithm Category:** Dynamic Programming / Game Theory
- **Why selected:** Cleanest, most intuitive formulation executing well within time limits.
- **Time Complexity:** $\mathcal{O}(N^3)$
- **Space Complexity:** $\mathcal{O}(N^2)$ auxiliary space

---

## 7. Code Walkthrough

Below is the line-by-line breakdown of the submitted solution:

```python
class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """

        n = len(piles)

        # Line 12-14: Precompute suffix sums backwards
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        # Line 17: Memoization dictionary for state (i, M)
        memo = {}

        # Line 19: Recursive Top-Down DP helper
        def dp(i, M):

            # Line 22-23: Base Case - All remaining piles can be taken in one move
            if i + 2 * M >= n:
                return suffix_sum[i]

            # Line 26-27: Return memoized state if present
            if (i, M) in memo:
                return memo[(i, M)]

            res = 0

            # Line 32-35: Try taking X piles (1 <= X <= 2M)
            for X in range(1, 2 * M + 1):
                # Active player gets (remaining stones - opponent's optimal share)
                res = max(res, suffix_sum[i] - dp(i + X, max(M, X)))

            # Line 38-39: Cache and return state result
            memo[(i, M)] = res
            return res

        # Line 42: Kickoff game from index 0 with initial M = 1
        return dp(0, 1)
```

---

## 8. Dry Run

Let's dry run for `piles = [2, 7, 9, 4, 4]` ($N=5$).

### Suffix Sums
`suffix_sum = [26, 24, 17, 8, 4, 0]`

### Recursive Evaluation Trace
- `dp(0, 1)`: $2M = 2 < 5$. Must try $X \in [1, 2]$.
  - Try $X = 1$: Alice gets `suffix_sum[0] - dp(1, 1)` = $26 - \text{dp}(1, 1)$.
    - `dp(1, 1)` ($2M=2 < 4$). Try $X \in [1, 2]$.
      - $X=1 \rightarrow 24 - \text{dp}(2, 1) = 24 - 17 = 7$.
      - $X=2 \rightarrow 24 - \text{dp}(3, 2)$. Since $3 + 2(2) = 7 \ge 5$, $\text{dp}(3, 2) = \text{suffix\_sum}[3] = 8$. $24 - 8 = \mathbf{16}$.
      - $\text{dp}(1, 1) = \max(7, 16) = \mathbf{16}$.
    - Yield for $X=1$: $26 - 16 = \mathbf{10}$.
  - Try $X = 2$: Alice gets `suffix_sum[0] - dp(2, 2)`.
    - Since $2 + 2(2) = 6 \ge 5$, $\text{dp}(2, 2) = \text{suffix\_sum}[2] = 17$.
    - Yield for $X=2$: $26 - 17 = \mathbf{9}$.
  - $\text{dp}(0, 1) = \max(10, 9) = \mathbf{10}$.

### Output
Returns **`10`**.

---

## 9. Complexity Analysis

### Time Complexity: $\mathcal{O}(N^3)$
- State space is defined by pair `(i, M)`.
- $i$ ranges from $0$ to $N$. $M$ ranges from $1$ to $N$. Total unique states $\approx \frac{N^2}{2}$.
- For each state `(i, M)`, the loop runs $2M \le N$ times.
- Overall time complexity is $\mathcal{O}(N^3)$. For $N=100$, $100^3 / 6 \approx 1.6 \times 10^5$ operations (instantaneous).

### Space Complexity: $\mathcal{O}(N^2)$ Auxiliary Space
- Memory for memoization dictionary `memo` containing up to $\mathcal{O}(N^2)$ states.
- Recursion call stack depth bounded by $N \Rightarrow \mathcal{O}(N)$.
- Total space complexity is $\mathcal{O}(N^2)$.

---

## 10. Edge Cases

| Edge Case Scenario | Input Example | Behavior & Output | How Code Handles It |
| :--- | :--- | :--- | :--- |
| **Single Pile** | `piles = [10]` | Output: `10` | $i=0, 2M=2 \ge 1 \rightarrow$ Returns `suffix_sum[0]` (`10`). |
| **$2M \ge N$ Initially** | `piles = [1, 2]` | Output: `3` | $0 + 2(1) = 2 \ge 2 \rightarrow$ Takes all piles immediately. |
| **Large Last Element** | `piles = [1, 2, 3, 4, 5, 100]`| Output: `104` | Evaluates optimal multi-turn play correctly. |

---

## 11. Alternative Approaches

### Approach 1: Bottom-Up 2D/3D DP Table ($\mathcal{O}(N^3)$ Time, $\mathcal{O}(N^2)$ Space)
- **Idea:** Build DP table backwards from $i = N-1$ down to 0 and $M = N$ down to 1.
- **Drawback:** Slightly harder to write and handle boundary bounds compared to top-down recursion.

### Approach 2: Top-Down DP with Memoization (User's Solution - Recommended)
- **Idea:** Recursion with memoization dictionary and suffix sum.
- **Complexity:** $\mathcal{O}(N^3)$ time, $\mathcal{O}(N^2)$ space.
- **Why Optimal:** Cleanest, most intuitive formulation for game theory problems in interviews.

---

## 12. Common Mistakes

> [!WARNING]
> 1. **Not Using Suffix Sums:** Re-summing sub-arrays in $\mathcal{O}(N)$ inside the loop increases time complexity to $\mathcal{O}(N^4)$, resulting in TLE.
> 2. **Confusing Opponent's Move:** Failing to pass `max(M, X)` to the recursive call (passing just `X` or `M` instead).
> 3. **Upper Bound Error:** Iterating $X$ up to $M$ instead of $2M$.

---

## 13. Interview Questions

1. **Q: Why does the recurrence use `suffix_sum[i] - dp(i + X, max(M, X))`?**
   - *A:* Because `suffix_sum[i]` represents the total number of stones left in the game from index `i` to the end. Since `dp(i + X, max(M, X))` gives the opponent's optimal share of those remaining stones, the active player's share is simply total stones minus opponent's share!

2. **Q: What is the maximum value $M$ can reach for array length $N$?**
   - *A:* $M$ can at most reach $N$. In fact, $M$ rarely exceeds $N/2$ in practice because if $2M \ge N - i$, the game ends immediately.

---

## 14. Similar Problems

- **Medium:**
  - [LeetCode #877 - Stone Game](https://leetcode.com/problems/stone-game/)
- **Hard:**
  - [LeetCode #1406 - Stone Game III](https://leetcode.com/problems/stone-game-iii/)
  - [LeetCode #1510 - Stone Game IV](https://leetcode.com/problems/stone-game-iv/)

---

## 15. Learning Summary

- **Pattern Recognized:** Game Theory Minimax with Zero-Sum Complement Reduction.
- **State Definition:** `dp(i, M)` = max stones active player gets from index `i` with multiplier `M`.
- **Suffix Sum Optimization:** $\mathcal{O}(1)$ retrieval of remaining total score.

---

## 16. Optimization Notes

Your solution is **100% optimal** ($\mathcal{O}(N^3)$ Time, $\mathcal{O}(N^2)$ Space). It is clean, readable, and represents the gold-standard interview implementation!
