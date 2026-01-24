# Chapter 10: Backtracking

Backtracking is an algorithmic-technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time (by time, here, is referred to the time elapsed till reaching any level of the search tree).

## Visualizers

| Problem                                                         | Type          | Visualization Focus                                                |
| :-------------------------------------------------------------- | :------------ | :----------------------------------------------------------------- |
| [Subsets](subsets_visualizer.html)                              | Decision Tree | Binary choice (Include/Exclude) at each step.                      |
| [Combination Sum](combination_sum_visualizer.html)              | DFS Tree      | Reusing elements, pruning when sum > target.                       |
| [Permutations](permutations_visualizer.html)                    | State Tree    | Swapping logic to generate orderings.                              |
| [Subsets II](subsets_ii_visualizer.html)                        | Decision Tree | Handling duplicates by sorting and skipping branches.              |
| [Combination Sum II](combination_sum_ii_visualizer.html)        | DFS Tree      | Unique combinations with limited element usage.                    |
| [Word Search](word_search_visualizer.html)                      | Grid DFS      | Visualizing path finding, visiting, and backtracking on a 2D grid. |
| [Palindrome Partitioning](palindrome_partition_visualizer.html) | String DFS    | Partitioning strings and validating palindromes.                   |
| [Letter Combinations](letter_combinations_visualizer.html)      | Mapping Tree  | Phone keypad mapping choices.                                      |
| [N-Queens](n_queens_visualizer.html)                            | Board         | Placing queens with row, col, and diagonal constraint checks.      |

## Key Concepts

1.  **Choice**: What decision do we make at each step?
2.  **Constraints**: When do we stop following a path? (Pruning)
3.  **Goal**: When do we know we have found a solution?
4.  **Backtrack**: How do we undo the choice to convert state back to previous valid state?
