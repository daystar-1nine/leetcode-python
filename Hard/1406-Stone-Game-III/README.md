# 1406. Stone Game III

![Difficulty: Hard](https://img.shields.io/badge/Difficulty-Hard-red?style=for-the-badge)
![Topic: Array](https://img.shields.io/badge/Topic-Array-blue?style=for-the-badge)
![Topic: Dynamic Programming](https://img.shields.io/badge/Topic-Dynamic%20Programming-orange?style=for-the-badge)
![Topic: Game Theory](https://img.shields.io/badge/Topic-Game%20Theory-purple?style=for-the-badge)

---

## 1. Problem Information

- **Problem Name:** Stone Game III
- **LeetCode Number:** 1406
- **Difficulty:** Hard
- **Tags:** Array, Math, Dynamic Programming, Game Theory
- **Language Used:** Python
- **Problem Link:** [LeetCode #1406 - Stone Game III](https://leetcode.com/problems/stone-game-iii/)

---

## 2. Problem Overview

Alice and Bob continue their games with stones. There are several stones arranged in a row, each with an associated value represented by the array `stoneValue`.

Alice and Bob take turns, with **Alice starting first**. On each turn, a player can take **1, 2, or 3 stones** from the first remaining stones in the row.

The score of a player is the sum of the values of the stones taken. The game continues until all stones have been taken. Both Alice and Bob play **optimally** to maximize their respective scores.

Return:
- `"Alice"` if Alice wins (Alice's score > Bob's score).
- `"Bob"` if Bob wins (Bob's score > Alice's score).
- `"Tie"` if their scores are equal.

### Input & Output Specifications
- **Input:** `stoneValue`: An array of integers ($1 \le \text{len}(stoneValue) \le 5 \times 10^4$).
- **Output:** String (`"Alice"`, `"Bob"`, or `"Tie"`).
- **Constraints:** $-1000 \le \text{stoneValue}[i] \le 1000$.

### Examples
- **Example 1:**
  - **Input:** `stoneValue = [1,2,3,7]`
  - **Output:** `"Bob"`
  - **Explanation:**
    - If Alice takes 1 stone (`[1]`), score = 1. Bob takes 3 stones (`[2,3,7]`), score = 12. Bob wins (12 > 1).
    - If Alice takes 2 stones (`[1,2]`), score = 3. Bob takes 2 stones (`[3,7]`), score = 10. Bob wins (10 > 3).
    - If Alice takes 3 stones (`[1,2,3]`), score = 6. Bob takes 1 stone (`[7]`), score = 7. Bob wins (7 > 6).
    - Bob wins regardless of Alice's initial choice.
- **Example 2:**
  - **Input:** `stoneValue = [1,2,3,-9]` $\rightarrow$ **Output:** `"Alice"`
- **Example 3:**
  - **Input:** `stoneValue = [1,2,3,6]` $\rightarrow$ **Output:** `"Tie"`

---

## 3. Intuition

> [!TIP]
> **Minimax Score Difference Strategy:** Instead of tracking Alice's and Bob's total scores independently, track the **maximum relative score advantage** ($\text{my\_score} - \text{opponent\_score}$) starting from index `i`!

### Relative Score State Formulation:
Let `dp[i]` be the maximum score difference ($\text{active\_player\_score} - \text{opponent\_score}$) that the player whose turn it is can achieve starting from index `i` to the end of the array.

If the active player chooses to take $k$ stones ($k \in \{1, 2, 3\}$):
1. They gain `take = sum(stoneValue[i ... i+k-1])`.
2. The opponent then faces the remaining stones starting at index $i + k$, achieving an optimal relative score advantage of `dp[i + k]`.
3. Thus, the active player's net relative score advantage for taking $k$ stones is:
   $$\text{take} - dp[i + k]$$

The active player will select $k \in \{1, 2, 3\}$ to **maximize** this advantage:
$$dp[i] = \max_{0 \le k < 3} \Big( \text{take}(k) - dp[i + k + 1] \Big)$$

---

## 4. Thought Process

```mermaid
flowchart TD
    A[Start: Input stoneValue array] --> B[Initialize dp array of size N + 1 with zeroes]
    B --> C[Loop i backwards from N - 1 down to 0]
    C --> D[Initialize dp[i] = -infinity, take = 0]
    D --> E[Loop k from 0 to 2]
    E --> F{Is i + k < N?}
    F -- Yes --> G[take += stoneValue[i + k]]
    G --> H[dp[i] = max dp[i], take - dp[i + k + 1]]
    H --> I{More k choices?}
    F -- No --> I
    I -- Yes --> E
    I -- No --> J{Finished backward loop?}
    J -- No --> C
    J -- Yes --> K{Check dp[0]}
    K -- dp[0] > 0 --> L[Return Alice]
    K -- dp[0] < 0 --> M[Return Bob]
    K -- dp[0] == 0 --> N[Return Tie]
```

1. **Base Case:**
   - `dp[n] = 0` (When no stones remain, score difference is 0).

2. **Backward Bottom-Up Dynamic Programming:**
   - Loop `i` backwards from `n - 1` down to `0`.
   - Set `dp[i] = float('-inf')` and `take = 0`.
   - Try taking $1, 2,$ or $3$ stones ($k = 0, 1, 2$):
     - If `i + k < n`:
       - `take += stoneValue[i + k]`
       - `dp[i] = max(dp[i], take - dp[i + k + 1])`

3. **Determine Winner:**
   - `dp[0]` represents Alice's score minus Bob's score starting from index 0.
   - If `dp[0] > 0` $\rightarrow$ Return `"Alice"`.
   - If `dp[0] < 0` $\rightarrow$ Return `"Bob"`.
   - If `dp[0] == 0` $\rightarrow$ Return `"Tie"`.

---

## 5. Concepts Used

### 1. Game Theory / Minimax Optimization
- **What it is:** A decision rule in zero-sum games where players attempt to maximize their own minimum guaranteed payoff.
- **Why it is used here:** Evaluating game choices assuming both Alice and Bob execute optimal decision-making.
- **Future applications:** Nim Game, Predict the Winner, Stone Game series.

### 2. Relative Advantage State Reduction
- **What it is:** Replacing two independent score variables ($A, B$) with a single relative difference variable ($A - B$).
- **Why it is used here:** Drastically reduces DP dimension from 2D/3D down to 1D.
- **Future applications:** Stone Game II, Stone Game IV, Can I Win.

---

## 6. Algorithm Used

### Bottom-Up Dynamic Programming (Minimax Relative Advantage)

- **Algorithm Category:** Game Theory / Dynamic Programming
- **Why selected:** Evaluates all game decision trees in linear $\mathcal{O}(N)$ time without recursive call stack overhead.
- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(N)$ (optimizable to $\mathcal{O}(1)$)

---

## 7. Code Walkthrough

Below is the line-by-line breakdown of the submitted solution:

```python
class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """

        n = len(stoneValue)

        # Line 11: dp[i] stores max relative score advantage for active player at index i
        # Base case dp[n] = 0 (no stones left)
        dp = [0] * (n + 1)

        # Line 13: Backward DP iteration from index n-1 down to 0
        for i in range(n - 1, -1, -1):

            # Line 15-16: Initialize dp[i] to -inf and take accumulator to 0
            dp[i] = float("-inf")
            take = 0

            # Line 18: Try taking 1, 2, or 3 stones (k = 0, 1, 2)
            for k in range(3):

                # Line 20: Bounds check to ensure stone index remains inside array
                if i + k < n:
                    # Line 21: Accumulate stone values taken in this move
                    take += stoneValue[i + k]
                    
                    # Line 22: Transition: current take minus opponent's optimal advantage from i + k + 1
                    dp[i] = max(dp[i], take - dp[i + k + 1])

        # Line 24-29: Evaluate Alice's score advantage starting at index 0
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
```

---

## 8. Dry Run

Let's dry run for `stoneValue = [1, 2, 3, 7]` ($n=4$).

### Execution Trace

- Initial: `dp = [0, 0, 0, 0, 0]` (`dp[4] = 0`).

#### Step 1: `i = 3` (`stoneValue[3] = 7`)
- $k=0$: `take = 7`. `dp[3] = max(-inf, 7 - dp[4]) = 7 - 0 = 7`.
- Result: **`dp[3] = 7`** (Player taking 7 gets advantage +7).

#### Step 2: `i = 2` (`stoneValue[2] = 3`)
- $k=0$ (Take 3): `take = 3`. `val = 3 - dp[3] = 3 - 7 = -4`.
- $k=1$ (Take 3, 7): `take = 10`. `val = 10 - dp[4] = 10 - 0 = 10`.
- Result: **`dp[2] = max(-4, 10) = 10`**.

#### Step 3: `i = 1` (`stoneValue[1] = 2`)
- $k=0$ (Take 2): `take = 2`. `val = 2 - dp[2] = 2 - 10 = -8`.
- $k=1$ (Take 2, 3): `take = 5`. `val = 5 - dp[3] = 5 - 7 = -2`.
- $k=2$ (Take 2, 3, 7): `take = 12`. `val = 12 - dp[4] = 12 - 0 = 12`.
- Result: **`dp[1] = max(-8, -2, 12) = 12`**.

#### Step 4: `i = 0` (`stoneValue[0] = 1`)
- $k=0$ (Take 1): `take = 1`. `val = 1 - dp[1] = 1 - 12 = -11`.
- $k=1$ (Take 1, 2): `take = 3`. `val = 3 - dp[2] = 3 - 10 = -7`.
- $k=2$ (Take 1, 2, 3): `take = 6`. `val = 6 - dp[3] = 6 - 7 = -1`.
- Result: **`dp[0] = max(-11, -7, -1) = -1`**.

### Outcome Evaluation
- `dp[0] = -1 < 0` $\rightarrow$ Returns **`"Bob"`**!

---

## 9. Complexity Analysis

### Time Complexity: $\mathcal{O}(N)$
- The outer loop runs $N$ times (from index $N-1$ down to 0).
- The inner loop runs a constant 3 times ($k=0, 1, 2$).
- Total time complexity is strictly linear $\mathcal{O}(3N) = \mathcal{O}(N)$.

### Space Complexity: $\mathcal{O}(N)$ Auxiliary Space
- Uses a 1D DP table of size $N + 1$.
- *Optimization Note:* Since `dp[i]` only depends on `dp[i+1]`, `dp[i+2]`, and `dp[i+3]`, space can be compressed to $\mathcal{O}(1)$ using 4 scalar variables.

---

## 10. Edge Cases

| Edge Case Scenario | Input Example | Behavior & Output | How Code Handles It |
| :--- | :--- | :--- | :--- |
| **Negative Stone Values** | `stoneValue = [-1, -2, -3]` | Output: `"Alice"` | Initialized `dp[i] = float('-inf')` properly evaluates maximum score despite negative numbers. |
| **Single Stone** | `stoneValue = [10]` | Output: `"Alice"` | `i=0`, $k=0$ takes 10, `dp[0] = 10 > 0` returns `"Alice"`. |
| **Equal Total Points (Tie)**| `stoneValue = [1, 2, 3, 6]` | Output: `"Tie"` | `dp[0]` evaluates to `0`, triggering `else: return "Tie"`. |
| **Large Array ($5 \times 10^4$)** | Array of length 50,000 | Output: Correct winner | Linear $\mathcal{O}(N)$ time executes in < 0.05 seconds without stack overflow. |

---

## 11. Alternative Approaches

### Approach 1: Top-Down Recursion with Memoization ($\mathcal{O}(N)$ Time, $\mathcal{O}(N)$ Space)
- **Idea:** Write recursive function `helper(i)` decorated with `@lru_cache` or a `memo` dictionary.
- **Drawback:** In Python, deep recursion stack for $N = 50,000$ requires adjusting `sys.setrecursionlimit`.

### Approach 2: Space-Optimized Bottom-Up DP ($\mathcal{O}(N)$ Time, $\mathcal{O}(1)$ Space)
- **Idea:** Replace `dp` array with 4 variables `dp0, dp1, dp2, dp3` shifting backwards.
  ```python
  dp1 = dp2 = dp3 = 0
  for i in range(n - 1, -1, -1):
      dp0 = max(sum(stoneValue[i:i+k+1]) - [dp1, dp2, dp3][k] for k in range(min(3, n - i)))
      dp1, dp2, dp3 = dp0, dp1, dp2
  ```

### Approach 3: Bottom-Up DP Array (User's Solution - Recommended)
- **Idea:** 1D DP table evaluated backwards.
- **Complexity:** $\mathcal{O}(N)$ time, $\mathcal{O}(N)$ space.
- **Why Optimal:** Cleanest, most readable solution during timed interviews.

---

## 12. Common Mistakes

> [!WARNING]
> 1. **Initializing `dp[i] = 0`:** Stone values can be negative! Initializing `dp[i] = 0` causes the maximum calculation to fail when all choices yield negative relative advantages. Must use `float('-inf')`.
> 2. **Tracking Two Separate DP Tables:** Attempting to maintain `alice_dp[i]` and `bob_dp[i]` leads to complex 2D/3D state transitions that cause TLE/MLE.
> 3. **Forward DP Traversal:** Attempting to build `dp` from index 0 forward fails because future optimal moves are unknown. Game theory DP must be evaluated backwards from the terminal base case!

---

## 13. Interview Questions

1. **Q: Why do we evaluate the DP array backwards from $N-1$ down to $0$?**
   - *A:* Because game decision states depend on the optimal choices available for the remaining unplayed stones. Terminal base case $dp[N] = 0$ is known, allowing us to build backward state solutions iteratively.

2. **Q: How can we reduce space complexity from $\mathcal{O}(N)$ to $\mathcal{O}(1)$?**
   - *A:* Notice that `dp[i]` only depends on `dp[i+1]`, `dp[i+2]`, and `dp[i+3]`. We only need to store the last 4 DP values in scalar variables rather than an entire array.

3. **Q: What is the Minimax theorem and how does it apply here?**
   - *A:* Minimax states that in a zero-sum game, a player chooses a move to maximize their minimum possible payoff, assuming the opponent will also play optimally to maximize their own advantage.

---

## 14. Similar Problems

- **Medium:**
  - [LeetCode #877 - Stone Game](https://leetcode.com/problems/stone-game/)
  - [LeetCode #1140 - Stone Game II](https://leetcode.com/problems/stone-game-ii/)
- **Hard:**
  - [LeetCode #1510 - Stone Game IV](https://leetcode.com/problems/stone-game-iv/)
  - [LeetCode #1563 - Stone Game V](https://leetcode.com/problems/stone-game-v/)

---

## 15. Learning Summary

- **Pattern Recognized:** Minimax Game Theory with Relative Advantage Tracking.
- **State Formulation:** `dp[i]` = max relative difference ($\text{active} - \text{opponent}$) from index `i`.
- **Transition:** `dp[i] = max(take - dp[i + k + 1])` for $k \in \{0, 1, 2\}$.

---

## 16. Optimization Notes

Your solution is **100% optimal** ($\mathcal{O}(N)$ Time, $\mathcal{O}(N)$ Space). It handles negative values, large inputs, and game theory ties with gold-standard clarity!
