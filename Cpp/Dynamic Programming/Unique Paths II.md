### [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/description/)

## Explanation:
Sure, let's break down the code:

1. **Class and Function Declaration**: The code is written in C++ and begins with the declaration of a class named `Solution`. Inside this class, there's a public function named `uniquePathsWithObstacles` which takes a 2D vector `obstacleGrid` as an argument.

2. **Grid Dimensions**: The function first determines the dimensions of the grid, `m` and `n`, which represent the number of rows and columns respectively.

3. **Dynamic Programming Array**: A 2D dynamic programming (DP) array `dp` of size `m` x `n` is initialized with `-1`. This array will be used to store the number of unique paths to reach each cell in the grid.

4. **Iterating Over the Grid**: The function then iterates over each cell in the grid. For each cell, it checks if the cell contains an obstacle (represented by `1`). If it does, it sets the corresponding cell in the DP array to `0` (indicating no paths can pass through this cell).

5. **Base Case**: If the cell is the starting cell (top-left corner of the grid), it sets the corresponding cell in the DP array to `1` (since there's only one way to reach the starting cell).

6. **Transition**: For all other cells, it calculates the number of unique paths to that cell by adding the number of paths to the cell above it (`up`) and the cell to its left (`left`). These values are then stored in the DP array.

7. **Result**: Finally, the function returns the value of the bottom-right cell in the DP array, which represents the total number of unique paths from the top-left to the bottom-right of the grid, considering the obstacles.

This code is a classic example of a dynamic programming problem where the solution to a larger problem depends on the solutions to smaller subproblems. The key idea here is to break down the problem into smaller, manageable parts and use the solutions to these parts to construct the solution to the original problem. This approach is what makes dynamic programming a powerful tool for solving complex problems efficiently.
## Time and Space Complexity:
### `Time Complexity`:
The **time complexity** of this code is **O(m*n)**, where `m` and `n` are the dimensions of the grid. This is because each cell in the grid is visited exactly once.

### `Space Complexity`:
The **space complexity** is also **O(m*n)** due to the extra space required for the DP array.

## Code:
```cpp
// Definition of the Solution class
class Solution {
public:
    // Function to calculate the number of unique paths with obstacles
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        // Get the number of rows in the obstacleGrid
        int m = obstacleGrid.size();
        // Get the number of columns in the obstacleGrid
        int n = obstacleGrid[0].size();
        
        // Create a 2D vector to store intermediate results with default value -1
        vector<vector<int>> dp(m, vector<int>(n, -1));

        // Iterate through each cell in the obstacleGrid
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                // Check if the current cell has an obstacle (value 1)
                if(obstacleGrid[i][j] == 1) {
                    // If there's an obstacle, set the number of paths for this cell to 0
                    dp[i][j] = 0;
                }
                // Check if it's the starting cell (top-left corner)
                else if(i == 0 && j == 0) {
                    // If it's the starting cell, set the number of paths to 1
                    dp[i][j] = 1;
                }
                else {
                    // Calculate the number of paths for the current cell
                    int up = 0, left = 0;

                    // Check if there's a cell above the current cell
                    if(i > 0) up = dp[i-1][j];

                    // Check if there's a cell to the left of the current cell
                    if(j > 0) left = dp[i][j-1];

                    // Set the number of paths for the current cell as the sum of paths from above and left
                    dp[i][j] = up + left;
                }
            }
        }

        // Return the number of unique paths for the last cell in the obstacleGrid
        return dp[m-1][n-1];
    }
};

```
