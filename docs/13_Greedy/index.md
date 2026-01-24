# Chapter 13: Greedy Algorithms

Greedy algorithms build up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit.

## Problem List

1.  **[Maximum Subarray](maximum_subarray_visualizer.html)**
    - **Type**: Kadane's Algorithm
    - **Key Idea**: `curSum = max(n, curSum + n)`. Reset if negative.

2.  **[Jump Game](jump_game_visualizer.html)**
    - **Type**: Greedy Reach
    - **Key Idea**: Work backwards. If `i + nums[i] >= goal`, then `goal = i`.

3.  **[Jump Game II](jump_game_ii_visualizer.html)**
    - **Type**: Implicit BFS
    - **Key Idea**: `l = r + 1`, `r = max_reach_in_current_level`.

4.  **[Gas Station](gas_station_visualizer.html)**
    - **Type**: Circular Greedy
    - **Key Idea**: If `sum(gas) < sum(cost)`, impossible. If `tank < 0`, reset start.

5.  **[Hand of Straights](hand_of_straights_visualizer.html)**
    - **Type**: Map Frequency
    - **Key Idea**: Always process min card available and try to form a straight.

6.  **[Merge Triplets to Form Target Triplet](merge_triplets_to_form_target_triplet_visualizer.html)**
    - **Type**: Filter & Merge
    - **Key Idea**: Ignore triplets where any value > target. Merge rest.

7.  **[Partition Labels](partition_labels_visualizer.html)**
    - **Type**: Interval Extend
    - **Key Idea**: `end = max(end, last[char])`. If `i == end`, cut.

8.  **[Valid Parenthesis String](valid_parenthesis_string_visualizer.html)**
    - **Type**: Greedy Range
    - **Key Idea**: Track `[min_open, max_open]`. `*` widens the range.
