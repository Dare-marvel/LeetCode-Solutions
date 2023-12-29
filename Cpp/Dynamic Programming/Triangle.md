### [Triangle](https://leetcode.com/problems/triangle/description/)

## Explanation:

## Time and Space Complexity:
### `Time Complexity`:

### `Space Complexity`:

## Recursion ( 42/44 testcases passed ):
```cpp
class Solution {
public:
    int helper(int i, int j, vector<vector<int>>& triangle) {
        int n = triangle.size();

        // Check if the current path is invalid
        if(j > i) {
            return INT_MAX;
        }

        // Base case: return the value of the current cell
        if(i == n-1) {
            return triangle[i][j];
        }

        // Recursive case: return the minimum path sum
        int fs = triangle[i][j] + helper(i+1, j, triangle);
        int ss = triangle[i][j] + helper(i+1, j+1, triangle);
        return min(fs, ss);
    }

    int minimumTotal(vector<vector<int>>& triangle) {
        return helper(0, 0, triangle);
    }
};

```

## Memoization ( All test-cases passed ):
```cpp
class Solution {
public:
    int computeMinPathSum(int row, int col, vector<vector<int>>& triangle, vector<vector<int>>& dp) {
        int n = triangle.size();

        // Check if the current path is invalid
        if (col > row) {
            return INT_MAX;
        }

        // Base case: return the value of the current cell
        if (row == n - 1) {
            return triangle[row][col];
        }

        if (dp[row][col] != -1) {
            return dp[row][col];
        }

        // Recursive case: return the minimum path sum
        int fromBelow = triangle[row][col] + computeMinPathSum(row + 1, col, triangle, dp);
        int fromBelowRight = triangle[row][col] + computeMinPathSum(row + 1, col + 1, triangle, dp);
        
        return dp[row][col] = min(fromBelow, fromBelowRight);
    }

    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<vector<int>> dp(n, vector<int>(n, -1));
        return computeMinPathSum(0, 0, triangle, dp);
    }
};

```

## Tabulization:
```cpp
// Definition of the Solution class
class Solution {
public:
    // Function to find the minimum total of a triangle
    int minimumTotal(vector<vector<int>>& triangle) {
        // Get the number of rows in the triangle
        int n = triangle.size();
        
        // Create a 2D vector to store intermediate results with default value 0
        vector<vector<int>> dp(n, vector<int>(n, 0));

        // Initialize the top-left cell of dp with the value of the triangle's top-left cell
        dp[0][0] = triangle[0][0];

        // Iterate through each row of the triangle
        for(int i = 1; i < n; i++) {
            // Iterate through each element in the current row
            for(int j = 0; j <= i; j++) {
                // Initialize variables for the minimum values from below and below-right
                int fromBelow = INT_MAX, fromBelowRight = INT_MAX;

                // Check if there's a cell below the current cell
                if (i > 0 && i-1 >= j) 
                    fromBelow = triangle[i][j] + dp[i-1][j];

                // Check if there's a cell below and to the right of the current cell
                if (j > 0) 
                    fromBelowRight = triangle[i][j] + dp[i-1][j-1];

                // Update the current cell with the minimum value from below or below-right
                dp[i][j] = min(fromBelow, fromBelowRight);
            }
        }

        // Find the minimum element in the last row of the dp table
        int minElement = *std::min_element(dp[n-1].begin(), dp[n-1].end());

        // Return the minimum total
        return minElement;
    }
};

```

## From Bottom to Up:
```cpp
// Definition of the Solution class
class Solution {
public:
    // Function to find the minimum path sum in a triangle
    int minimumPathSum(vector<vector<int>>& triangle, int n) {
        // Create a 2D DP (dynamic programming) array to store minimum path sums
        vector<vector<int>> dp(n, vector<int>(n, 0));

        // Initialize the bottom row of dp with the values from the triangle
        for (int j = 0; j < n; j++) {
            dp[n - 1][j] = triangle[n - 1][j];
        }

        // Iterate through the triangle rows in reverse order
        for (int i = n - 2; i >= 0; i--) {
            for (int j = i; j >= 0; j--) {
                // Calculate the minimum path sum for the current cell
                int down = triangle[i][j] + dp[i + 1][j];
                int diagonal = triangle[i][j] + dp[i + 1][j + 1];

                // Store the minimum of the two possible paths in dp
                dp[i][j] = min(down, diagonal);
            }
        }

        // The top-left cell of dp now contains the minimum path sum
        return dp[0][0];
    }

    // Main function to find the minimum total of a triangle
    int minimumTotal(vector<vector<int>>& triangle) {
        return minimumPathSum(triangle, triangle.size());
    }
};

```
