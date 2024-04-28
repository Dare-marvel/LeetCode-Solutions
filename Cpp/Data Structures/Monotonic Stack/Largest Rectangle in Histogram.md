### [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/description/)

## Explanation:
1. **Problem Statement**: The problem is to find the largest rectangle area that can be formed in a histogram, given the heights of the bars.

2. **Approach Overview**:
   - We're using a stack-based approach to efficiently find the next smaller bar on the left and right of each bar in the histogram.
   - Once we have this information, we can calculate the area of the largest rectangle for each bar and find the maximum among them.

3. **Stack-Based Approach**:
   - We iterate through the histogram from left to right.
   - At each step, we maintain a stack of indices of bars such that the heights are in increasing order from bottom to top of the stack.
   - If the current bar's height is greater than or equal to the height of the bar at the top of the stack, we pop elements from the stack until we find a smaller bar or until the stack becomes empty.
   - For each bar, the index of the next smaller bar to its left is either the index of the bar at the top of the stack or 0 if the stack is empty.
   - We repeat the same process from right to left to find the next smaller bar on the right for each bar.

4. **Finding Next Smaller Bar**:
   - The idea is that for a bar, we want to find the closest bar on the left and right with a smaller height, as these will form the boundaries of the rectangle with the current bar.
   - Using the stack, we efficiently find the next smaller bar to the left and right for each bar in the histogram.

5. **Calculating Maximum Area**:
   - Once we have the indices of the next smaller bars on the left and right for each bar, we can calculate the area of the largest rectangle that can be formed using each bar as its height.
   - The width of the rectangle is determined by the distance between the next smaller bars on the left and right (plus one to include the current bar).
   - We iterate through all bars, calculate the area for each, and keep track of the maximum area found so far.

## Time and Space Complexity:
### Time Complexity:
   - The algorithm involves traversing the histogram twice (once from left to right and once from right to left), each time taking O(n) time.
   - Therefore, the overall time complexity of the algorithm is O(n).

### Space Complexity:
   - The algorithm uses an additional stack of size at most O(n) to store the indices of bars.
   - It also uses two arrays of size n to store the indices of the next smaller bars on the left and right.
   - Hence, the overall space complexity is O(n).
     
## Code:
```cpp
class Solution {
public:
    // Function to find the largest rectangle area in a histogram represented by heights
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size(); // Number of bars in the histogram
        stack<int> st; // Stack to store indices of bars

        // Arrays to store the indices of the next smaller bar to the left and right of each bar
        int leftsmall[n], rightsmall[n];

        // Finding the index of the next smaller bar to the left of each bar
        for(int i = 0; i < n; i++) {
            // Pop bars from the stack until a smaller bar is found or stack becomes empty
            while(!st.empty() && heights[st.top()] >= heights[i]) {
                st.pop();
            }

            // If the stack is empty, there is no smaller bar to the left
            if(st.empty()) {
                leftsmall[i] = 0;
            } else {
                leftsmall[i] = st.top() + 1; // Index of the next smaller bar
            }
            
            st.push(i); // Push the current bar's index onto the stack
        }

        // Clear the stack for reusing
        while(!st.empty()) {
            st.pop();
        }

        // Finding the index of the next smaller bar to the right of each bar
        for(int i = n - 1; i >= 0; i--) {
            // Pop bars from the stack until a smaller bar is found or stack becomes empty
            while(!st.empty() && heights[st.top()] >= heights[i]) {
                st.pop();
            }

            // If the stack is empty, there is no smaller bar to the right
            if(st.empty()) {
                rightsmall[i] = n - 1;
            } else {
                rightsmall[i] = st.top() - 1; // Index of the next smaller bar
            }

            st.push(i); // Push the current bar's index onto the stack
        }

        int maxArea = 0; // Variable to store the maximum area

        // Calculate the area of the largest rectangle formed by each bar
        for(int i = 0; i < n; i++) {
            // Calculate the area using the height of the bar and the width between the next smaller bars
            maxArea = max(maxArea, heights[i] * (rightsmall[i] - leftsmall[i] + 1));
        }

        return maxArea; // Return the maximum area
    }
};
```
