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
            return dp[row][col] = triangle[row][col];
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

```
