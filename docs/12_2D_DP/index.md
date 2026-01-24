# Chapter 12: 2D Dynamic Programming

This chapter covers advanced Dynamic Programming problems, mostly involving 2D grids, string comparisons, or interval DP.

## Problem List

1.  **[Unique Paths](unique_paths_visualizer.html)**
    - **Type**: 2D Grid (Path Counting)
    - **Key Idea**: `dp[i][j] = dp[i-1][j] + dp[i][j-1]`

2.  **[Longest Common Subsequence](longest_common_subsequence_visualizer.html)**
    - **Type**: 2D Grid (String)
    - **Key Idea**: `if match: 1 + diag`. `else: max(top, left)`

3.  **[Best Time to Buy and Sell Stock with Cooldown](best_time_to_buy_and_sell_stock_with_cooldown_visualizer.html)**
    - **Type**: State Machine
    - **Key Idea**: States: Hold, Sold, Rest.

4.  **[Coin Change II](coin_change_ii_visualizer.html)**
    - **Type**: Unbounded Knapsack
    - **Key Idea**: `dp[i][j] = dp[i-1][j] (skip) + dp[i][j-coin] (use)`

5.  **[Target Sum](target_sum_visualizer.html)**
    - **Type**: Subset Sum Variant
    - **Key Idea**: `P - N = T` => `2P = T + Sum`. Find subset sum P.

6.  **[Interleaving String](interleaving_string_visualizer.html)**
    - **Type**: 2D Grid Pathfinding
    - **Key Idea**: Walk through grid if characters match s1 or s2.

7.  **[Longest Increasing Path in a Matrix](longest_increasing_path_in_a_matrix_visualizer.html)**
    - **Type**: DFS + Memoization
    - **Key Idea**: Store computed max path for each cell.

8.  **[Distinct Subsequences](distinct_subsequences_visualizer.html)**
    - **Type**: 2D Counting
    - **Key Idea**: `if match: dp[i-1][j-1] + dp[i-1][j]`.

9.  **[Edit Distance](edit_distance_visualizer.html)**
    - **Type**: 2D String Op
    - **Key Idea**: Min of Insert, Delete, Replace.

10. **[Burst Balloons](burst_balloons_visualizer.html)**
    - **Type**: Interval DP
    - **Key Idea**: Pick LAST balloon (pivot) to burst in `[i, j]`.

11. **[Regular Expression Matching](regular_expression_matching_visualizer.html)**
    - **Type**: Complex String DP
    - **Key Idea**: Handle `*` as 0 or 1+ occurrences.
