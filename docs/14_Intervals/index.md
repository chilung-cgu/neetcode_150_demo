# Chapter 14: Intervals

Interval problems typically require sorting. Once sorted, we can process them linearly to detect overlaps or merge them.

## Problem List

1.  **[Insert Interval](insert_interval_visualizer.html)**
    - **Type**: Merge
    - **Key Idea**: `left` (before) + `merged` (overlap) + `right` (after).

2.  **[Merge Intervals](merge_intervals_visualizer.html)**
    - **Type**: Sort & Merge
    - **Key Idea**: Sort by Start. If `curr.start <= last.end`, merge.

3.  **[Non-overlapping Intervals](non_overlapping_intervals_visualizer.html)**
    - **Type**: Greedy Removal
    - **Key Idea**: Sort by Start. If overlap, remove interval with _larger_ end time.

4.  **[Meeting Rooms](meeting_rooms_visualizer.html)**
    - **Type**: Overlap Check
    - **Key Idea**: Sort. Check `i.start < (i-1).end`.

5.  **[Meeting Rooms II](meeting_rooms_ii_visualizer.html)**
    - **Type**: Chronological / Sweep Line
    - **Key Idea**: Track Start/End events. `max(count)` is the answer.

6.  **[Minimum Interval to Include Each Query](minimum_interval_to_include_each_query_visualizer.html)**
    - **Type**: Heap + Sweep Line
    - **Key Idea**: Sort Queries & Intervals. Add valid to Heap. Remove ended from Heap. Top is best.
