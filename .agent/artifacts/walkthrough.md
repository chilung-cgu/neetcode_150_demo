# Visualizing NeetCode 150: Chapters 1-5 Complete

We have successfully implemented interactive visualizations for the first five chapters of the NeetCode 150 roadmap. This massive update brings clarity and interactivity to 34 algorithmic problems.

## 🌟 Key Achievements

- **Scalable Architecture**: Created a shared `core.js` and `style.css` foundation, allowing rapid development of consistent visualizers.
- **Workflow Automation**: Established a repeatable workflow for creating and embedding visualizations.
- **Five Chapters Complete**: 100% coverage for the initial set of problems.

## 📊 Coverage Summary

| Chapter                 | Problems | Visualized | Status      |
| :---------------------- | :------: | :--------: | :---------- |
| **1. Arrays & Hashing** |    9     |     9      | ✅ Complete |
| **2. Two Pointers**     |    5     |     5      | ✅ Complete |
| **3. Sliding Window**   |    6     |     6      | ✅ Complete |
| **4. Stack**            |    7     |     7      | ✅ Complete |
| **5. Binary Search**    |    7     |     7      | ✅ Complete |
| **Total**               |  **34**  |   **34**   | **100%**    |

## 🎨 Visualization Gallery

### Two Pointers: Trapping Rain Water

Uses two pointers (left and right) to calculate trapped water based on max heights.
![Trapping Rain Water](/docs/02_Two_Pointers/trapping_rain_water_visualizer.html)

### Sliding Window: Minimum Window Substring

Dynamically expands and shrinks the window to find the smallest substring covering all target characters.
![Minimum Window Substring](/docs/03_Sliding_Window/minimum_window_visualizer.html)

### Stack: Car Fleet

Simulates cars moving towards a target and merging into fleets based on arrival times.
![Car Fleet](/docs/04_Stack/car_fleet_visualizer.html)

### Binary Search: Search 2D Matrix

Treats a matrix as a flattened sorted array to perform binary search efficiently.
![Search 2D Matrix](/docs/05_Binary_Search/search_2d_matrix_visualizer.html)

## 🛠️ Technical Details

- **Stack**: MkDocs Material + HTML5/JS (Vanilla).
- **Integration**: Using `iframe` to ensure style isolation and responsiveness.
- **Layout**: `55%` visualization / `45%` code split for optimal learning experience.
- **Theme**: Premium dark mode with consistent color palette (Primary Blue, Success Green, Secondary Purple).

## 🚀 Next Steps

- **Phase 3 Expansion**: Continue to "Linked List", "Trees", and "Tries".
- **Interactive Features**: Add "Step Back" and "Auto Play" controls to the core library.
