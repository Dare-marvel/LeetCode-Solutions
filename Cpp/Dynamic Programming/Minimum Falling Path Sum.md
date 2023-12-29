### [Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/description/)

## Explanation:

## Time and Space Complexity:
### `Time Complexity`:

### `Space Complexity`:

## Code:
```cpp
class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size();
        vector<vector<int>> dp(n,vector<int>(m,0));

        for(int j=0;j<m;j++){
            dp[0][j] = matrix[0][j];
        }

        for(int i=1;i<n;i++){
            for(int j=0;j<m;j++){
                int s = matrix[i][j] + dp[i-1][j];

                int ld = matrix[i][j];
                if(j-1>=0) ld += dp[i-1][j-1];
                else ld+= 1e8;

                int rd = matrix[i][j];
                if(j+1<m) rd += dp[i-1][j+1];
                else rd+= 1e8;

                dp[i][j] = min(s,min(ld,rd));
            }
        }

        int minElement = *std::min_element(dp[n-1].begin(), dp[n-1].end());

        return minElement;
    }
};
```
