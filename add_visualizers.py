#!/usr/bin/env python3
"""Script to add visualizer embeds to markdown files."""

import os
import re

# Mapping of markdown files to their visualizer files
mappings = {
    # Trees
    "07_Trees/03_Diameter_of_Binary_Tree.md": "diameter_visualizer.html",
    "07_Trees/04_Balanced_Binary_Tree.md": "balanced_tree_visualizer.html",
    "07_Trees/05_Same_Tree.md": "same_tree_visualizer.html",
    "07_Trees/06_Subtree_of_Another_Tree.md": "subtree_visualizer.html",
    "07_Trees/07_Lowest_Common_Ancestor_BST.md": "lca_bst_visualizer.html",
    "07_Trees/09_Binary_Tree_Right_Side_View.md": "right_side_view_visualizer.html",
    "07_Trees/10_Count_Good_Nodes.md": "count_good_nodes_visualizer.html",
    "07_Trees/12_Kth_Smallest_Element_BST.md": "kth_smallest_bst_visualizer.html",
    "07_Trees/13_Construct_Binary_Tree.md": "construct_tree_visualizer.html",
    "07_Trees/14_Binary_Tree_Maximum_Path_Sum.md": "max_path_sum_visualizer.html",
    "07_Trees/15_Serialize_Deserialize_Binary_Tree.md": "serialize_tree_visualizer.html",
    # Tries
    "08_Tries/02_Design_Add_Search_Words.md": "word_dictionary_visualizer.html",
    "08_Tries/03_Word_Search_II.md": "word_search_ii_visualizer.html",
    # Heap
    "09_Heap/01_Kth_Largest_Element_Stream.md": "kth_largest_stream_visualizer.html",
    "09_Heap/02_Last_Stone_Weight.md": "last_stone_visualizer.html",
    "09_Heap/03_K_Closest_Points.md": "k_closest_visualizer.html",
    "09_Heap/04_Kth_Largest_Element_Array.md": "kth_largest_array_visualizer.html",
    "09_Heap/05_Task_Scheduler.md": "task_scheduler_visualizer.html",
    "09_Heap/06_Design_Twitter.md": "twitter_visualizer.html",
    # Backtracking
    "10_Backtracking/02_Combination_Sum.md": "combination_sum_visualizer.html",
    "10_Backtracking/03_Permutations.md": "permutations_visualizer.html",
    "10_Backtracking/04_Subsets_II.md": "subsets_ii_visualizer.html",
    "10_Backtracking/05_Combination_Sum_II.md": "combination_sum_ii_visualizer.html",
    "10_Backtracking/06_Word_Search.md": "word_search_visualizer.html",
    "10_Backtracking/07_Palindrome_Partitioning.md": "palindrome_partition_visualizer.html",
    "10_Backtracking/08_Letter_Combinations.md": "letter_combinations_visualizer.html",
    # 1D DP
    "11_1D_DP/02_Min_Cost_Climbing_Stairs.md": "min_cost_stairs_visualizer.html",
    "11_1D_DP/03_House_Robber.md": "house_robber_visualizer.html",
    "11_1D_DP/04_House_Robber_II.md": "house_robber_ii_visualizer.html",
    "11_1D_DP/05_Longest_Palindromic_Substring.md": "longest_palindrome_visualizer.html",
    "11_1D_DP/06_Palindromic_Substrings.md": "palindromic_substrings_visualizer.html",
    "11_1D_DP/07_Decode_Ways.md": "decode_ways_visualizer.html",
    "11_1D_DP/09_Maximum_Product_Subarray.md": "max_product_visualizer.html",
    "11_1D_DP/10_Word_Break.md": "word_break_visualizer.html",
    "11_1D_DP/11_Longest_Increasing_Subsequence.md": "lis_visualizer.html",
    "11_1D_DP/12_Partition_Equal_Subset_Sum.md": "partition_subset_visualizer.html",
    # 2D DP
    "12_2D_DP/01_Unique_Paths.md": "unique_paths_visualizer.html",
    "12_2D_DP/03_Buy_Sell_Stock_Cooldown.md": "stock_cooldown_visualizer.html",
    "12_2D_DP/04_Coin_Change_II.md": "coin_change_ii_visualizer.html",
    "12_2D_DP/05_Target_Sum.md": "target_sum_visualizer.html",
    "12_2D_DP/06_Interleaving_String.md": "interleaving_string_visualizer.html",
    "12_2D_DP/07_Longest_Increasing_Path_Matrix.md": "longest_increasing_path_visualizer.html",
    "12_2D_DP/08_Distinct_Subsequences.md": "distinct_subsequences_visualizer.html",
    "12_2D_DP/09_Edit_Distance.md": "edit_distance_visualizer.html",
    "12_2D_DP/10_Burst_Balloons.md": "burst_balloons_visualizer.html",
    "12_2D_DP/11_Regular_Expression_Matching.md": "regex_matching_visualizer.html",
    # Greedy
    "13_Greedy/02_Jump_Game.md": "jump_game_visualizer.html",
    "13_Greedy/03_Jump_Game_II.md": "jump_game_ii_visualizer.html",
    "13_Greedy/04_Gas_Station.md": "gas_station_visualizer.html",
    "13_Greedy/05_Hand_of_Straights.md": "hand_of_straights_visualizer.html",
    "13_Greedy/06_Merge_Triplets.md": "merge_triplets_visualizer.html",
    "13_Greedy/07_Partition_Labels.md": "partition_labels_visualizer.html",
    "13_Greedy/08_Valid_Parenthesis_String.md": "valid_parenthesis_string_visualizer.html",
    # Intervals
    "14_Intervals/01_Insert_Interval.md": "insert_interval_visualizer.html",
    "14_Intervals/03_Non_Overlapping_Intervals.md": "non_overlapping_visualizer.html",
    "14_Intervals/04_Meeting_Rooms.md": "meeting_rooms_visualizer.html",
    "14_Intervals/05_Meeting_Rooms_II.md": "meeting_rooms_ii_visualizer.html",
    "14_Intervals/06_Minimum_Interval.md": "min_interval_query_visualizer.html",
    # Graphs
    "15_Graphs/02_Clone_Graph.md": "clone_graph_visualizer.html",
    "15_Graphs/03_Max_Area_of_Island.md": "max_area_island_visualizer.html",
    "15_Graphs/04_Pacific_Atlantic_Water_Flow.md": "pacific_atlantic_visualizer.html",
    "15_Graphs/05_Surrounded_Regions.md": "surrounded_regions_visualizer.html",
    "15_Graphs/06_Rotting_Oranges.md": "rotting_oranges_visualizer.html",
    "15_Graphs/07_Walls_and_Gates.md": "walls_gates_visualizer.html",
    "15_Graphs/09_Course_Schedule_II.md": "course_schedule_ii_visualizer.html",
    "15_Graphs/10_Redundant_Connection.md": "redundant_connection_visualizer.html",
    "15_Graphs/13_Word_Ladder.md": "word_ladder_visualizer.html",
    # Advanced Graphs
    "16_Advanced_Graphs/02_Min_Cost_Connect_Points.md": "min_cost_connect_points_visualizer.html",
    "16_Advanced_Graphs/04_Swim_in_Rising_Water.md": "swim_rising_water_visualizer.html",
    "16_Advanced_Graphs/06_Cheapest_Flights_K_Stops.md": "cheapest_flights_visualizer.html",
    # Math
    "17_Math_Geometry/02_Spiral_Matrix.md": "spiral_matrix_visualizer.html",
}

def get_embed_html(visualizer_name):
    return f'''### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../{visualizer_name}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../{visualizer_name}" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation'''

def process_file(md_path, vis_name, base_dir):
    full_path = os.path.join(base_dir, md_path)
    if not os.path.exists(full_path):
        print(f"SKIP: {md_path} (file not found)")
        return False
    
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has visualizer
    if 'visualizer.html' in content:
        print(f"SKIP: {md_path} (already has visualizer)")
        return False
    
    # Find ## 4. and insert before it
    pattern = r'---\s*\n\n## 4\. 💻 Implementation'
    replacement = get_embed_html(vis_name)
    
    if re.search(pattern, content):
        new_content = re.sub(pattern, replacement, content, count=1)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"OK: {md_path}")
        return True
    else:
        print(f"WARN: {md_path} (pattern not found)")
        return False

if __name__ == '__main__':
    base_dir = '/data/leo/chichi/neetcode_150_demo/docs'
    success = 0
    for md_file, vis_file in mappings.items():
        if process_file(md_file, vis_file, base_dir):
            success += 1
    print(f"\nProcessed {success} files successfully")
