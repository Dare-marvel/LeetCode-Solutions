### [Cherry Pickup II](https://leetcode.com/problems/cherry-pickup-ii/description/)

## Explanation:

## Time and Space Complexity:
### `Time Complexity`:

### `Space Complexity`:

## Tabulization:
```cpp
class Solution {
public:
    int maxCherryUtil(int i, int j1, int j2, int n, int m, vector<vector<int>>& grid, vector<vector<vector<int>>>& dp) {
        if (j1 < 0 || j1 >= m || j2 < 0 || j2 >= m)
            return -1e9;

        if (i == n - 1) {
            if (j1 == j2)
                return grid[i][j1];
            else
                return grid[i][j1] + grid[i][j2];
        }

        if (dp[i][j1][j2] != -1)
            return dp[i][j1][j2];

        int maxi = INT_MIN;

        for (int di = -1; di <= 1; di++) {
            for (int dj = -1; dj <= 1; dj++) {
                int ans;

                if (j1 == j2)
                    ans = grid[i][j1];
                else
                    ans = grid[i][j1] + grid[i][j2];

                if ((j1 + di < 0 || j1 + di >= m) || (j2 + dj < 0 || j2 + dj >= m))
                    ans += -1e9;
                else
                    ans += maxCherryUtil(i + 1, j1 + di, j2 + dj, n, m, grid, dp);

                maxi = max(ans, maxi);
            }
        }

        return dp[i][j1][j2] = maxi;
    }

    int cherryPickup(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(m, vector<int>(m, -1)));
        return max(0, maxCherryUtil(0, 0, m - 1, n, m, grid, dp));
    }
};
```

## Memoization:
```cpp
class Solution {
public:
    int maxCherryUtil(int i, int j1, int j2, int n, int m, vector<vector<int>>& grid, vector<vector<vector<int>>>& dp) {
        if (j1 < 0 || j1 >= m || j2 < 0 || j2 >= m)
            return -1e9;

        if (i == n - 1) {
            if (j1 == j2)
                return grid[i][j1];
            else
                return grid[i][j1] + grid[i][j2];
        }

        if (dp[i][j1][j2] != -1)
            return dp[i][j1][j2];

        int maxi = INT_MIN;

        for (int di = -1; di <= 1; di++) {
            for (int dj = -1; dj <= 1; dj++) {
                int ans;

                if (j1 == j2)
                    ans = grid[i][j1] + maxCherryUtil(i + 1, j1 + di, j2 + dj, n, m, grid, dp);
                else
                    ans = grid[i][j1] + grid[i][j2] + maxCherryUtil(i + 1, j1 + di, j2 + dj, n, m, grid, dp);

                maxi = max(maxi, ans);
            }
        }

        return dp[i][j1][j2] = maxi;
    }

    int cherryPickup(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(m, vector<int>(m, -1)));
        return max(0, maxCherryUtil(0, 0, m - 1, n, m, grid, dp));
    }
};
```

## Recursive ( 17/59 Testcases passed ):
```cpp
class Solution {
public:
    int pickupPath(int i,int j1,int j2,vector<vector<int>>& grid){
        int m = grid.size();
        int n = grid[0].size();
        if(j1 < 0 || j1 >= n || j2 < 0 || j2 >= n){
            return INT_MIN;
        }
        if(i == m-1){
            if(j1 == j2){
            return grid[i][j1];
            }
            else{
                return grid[i][j1] + grid[i][j2];
            }
        }

        int maxi = INT_MIN;
        int ans = 0;
        for(int di=-1;di<=1;di++){
            for(int dj=-1;dj<=1;dj++){
                if(j1 == j2){
                    ans = max(maxi,grid[i][j1]+pickupPath(i+1,j1+di,j2+dj,grid));
                }
                else{
                    ans = max(maxi,grid[i][j1]+ grid[i][j2] + pickupPath(i+1,j1+di,j2+dj,grid));
                }
                maxi = max(maxi,ans);
            }
        }
        
        return maxi;
    }
    int cherryPickup(vector<vector<int>>& grid) {
        int n = grid[0].size();
        return pickupPath(0,0,n-1,grid);
    }
};
```
