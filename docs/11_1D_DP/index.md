# Chapter 11: 1D Dynamic Programming

## 核心概念

1D DP 通常涉及一個陣列或變數，根據先前的狀態計算當前狀態。
核心公式：`dp[i] = f(dp[i-1], dp[i-2], ...)`

## 題目列表

| 編號  | 題目                                                                             | 難度   | 核心技巧                              |
| ----- | -------------------------------------------------------------------------------- | ------ | ------------------------------------- |
| 11-01 | [Climbing Stairs](climbing_stairs_visualizer.html)                               | Easy   | Fibonacci (dp[i] = dp[i-1] + dp[i-2]) |
| 11-02 | [Min Cost Climbing Stairs](min_cost_climbing_stairs_visualizer.html)             | Easy   | Cost Minimization                     |
| 11-03 | [House Robber](house_robber_visualizer.html)                                     | Medium | Choice: Rob or Skip                   |
| 11-04 | [House Robber II](house_robber_ii_visualizer.html)                               | Medium | Circular Array (Break into linear)    |
| 11-05 | [Longest Palindromic Substring](longest_palindromic_substring_visualizer.html)   | Medium | Expand Around Center                  |
| 11-06 | [Palindromic Substrings](palindromic_substrings_visualizer.html)                 | Medium | Count by Expanding                    |
| 11-07 | [Decode Ways](decode_ways_visualizer.html)                                       | Medium | 1-digit / 2-digit logic               |
| 11-08 | [Coin Change](coin_change_visualizer.html)                                       | Medium | Unbounded Knapsack (Min)              |
| 11-09 | [Maximum Product Subarray](maximum_product_subarray_visualizer.html)             | Medium | Track Min & Max (Negatives)           |
| 11-10 | [Word Break](word_break_visualizer.html)                                         | Medium | String Segmentation Check             |
| 11-11 | [Longest Increasing Subsequence](longest_increasing_subsequence_visualizer.html) | Medium | O(n^2) Comparison                     |
| 11-12 | [Partition Equal Subset Sum](partition_equal_subset_sum_visualizer.html)         | Medium | Subset Sum Reachability (Set/Bool)    |

## 學習重點

1.  **State Definition (狀態定義)**: `dp[i]` 代表什麼？
2.  **Transition Equation (轉移方程式)**: 如何從 `i-1` 推導 `i`？
3.  **Base Cases (基底情況)**: 初始值是什麼？
