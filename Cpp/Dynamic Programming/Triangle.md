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

## Memoization:
