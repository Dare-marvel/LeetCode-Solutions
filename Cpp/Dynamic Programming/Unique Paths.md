### [Unique Paths](https://leetcode.com/problems/unique-paths/description/)

## Explanation:
This C++ code is a solution to the problem of finding the number of unique paths from the top-left corner to the bottom-right corner of a grid. The solution uses dynamic programming to optimize the process. Here's a detailed explanation:

1. **Including Libraries**: The code begins with `#include <bits/stdc++.h>`, which is a header file in C++ that includes most standard library files.

2. **uniquePaths Function**: The `uniquePaths` function is defined, which takes two integers `m` and `n`, and a reference to a 2D vector `dp`. This function calculates the number of unique paths from the top-left corner to each cell in a `m` by `n` grid.

3. **Initialization**: Inside the function, a nested loop is used to iterate over each cell in the grid. If the cell is the top-left corner (i.e., `i` and `j` are both 0), `dp[i][j]` is set to 1, because there is only one path to the top-left corner itself.

4. **Dynamic Programming**: For each other cell, the function calculates the number of unique paths to that cell as the sum of the number of unique paths to the cell above it and the cell to its left. This is because a path to a cell can only come from the cell above it or the cell to its left. The number of unique paths to the cell is then stored in `dp[i][j]`.

5. **Return Statement**: The function returns `dp[m-1][n-1]`, which is the number of unique paths to the bottom-right corner of the grid.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of the code is **O(m*n)**, because each cell in the `m` by `n` grid is visited once, and the number of unique paths to each cell is calculated once.

### `Space Complexity`:
The space complexity is also **O(m*n)**, because a 2D vector of size `m` by `n` is used to store the number of unique paths to each cell.

## Code:
```cpp
class Solution {
public:
    // Function to find the number of unique paths in a grid of size m x n
    int uniquePaths(int m, int n) {

        // Create a memoization table initialized with -1
        vector<vector<int>> dp(m, vector<int>(n, -1));
        
        // Iterate through each cell in the grid
        for(int i=0; i < m; i++) {
            for(int j=0; j < n; j++) {
                // Base case: Top-left cell has only one way to reach (itself)
                if(i == 0 && j == 0) {
                    dp[i][j] = 1;
                    continue;
                }

                int up = 0, left = 0;

                // Check if moving up is a valid move
                if(i > 0)
                    up = dp[i - 1][j];

                // Check if moving left is a valid move
                if(j > 0)
                    left = dp[i][j - 1];

                // Calculate and store the number of ways to reach the current cell
                dp[i][j] = up + left;
            }
        }

        // Return the number of unique paths to the bottom-right cell
        return dp[m-1][n-1];
    }
};

```
