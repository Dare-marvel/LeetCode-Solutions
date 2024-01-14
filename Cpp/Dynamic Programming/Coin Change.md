### [Coin Change](https://leetcode.com/problems/coin-change/description/)

## [Explanation](https://takeuforward.org/data-structure/minimum-coins-dp-20/):

## Tabulation ( All test cases passed ):
```cpp
class Solution {
public:
    int coinChange(vector<int>& arr, int T) {
        int n = arr.size();
    
    // Create a 2D DP (Dynamic Programming) table with n rows and T+1 columns
    vector<vector<int>> dp(n, vector<int>(T + 1, 0));
    
    // Initialize the first row of the DP table
    for (int i = 0; i <= T; i++) {
        if (i % arr[0] == 0)
            dp[0][i] = i / arr[0];
        else
            dp[0][i] = 1e9; // Set it to a very large value if not possible
    }
    
    // Fill the DP table using a bottom-up approach
    for (int ind = 1; ind < n; ind++) {
        for (int target = 0; target <= T; target++) {
            // Calculate the minimum elements needed without taking the current element
            int notTake = dp[ind - 1][target];
            
            // Calculate the minimum elements needed by taking the current element
            int take = 1e9; // Initialize 'take' to a very large value
            if (arr[ind] <= target)
                take = 1 + dp[ind][target - arr[ind]];
                
            // Store the minimum of 'notTake' and 'take' in the DP table
            dp[ind][target] = min(notTake, take);
        }
    }
    
    // The answer is in the bottom-right cell of the DP table
    int ans = dp[n - 1][T];
    
    // If 'ans' is still very large, it means it's not possible to form the target sum
    if (ans >= 1e9)
        return -1;
    
    return ans;
    }
};
```

## Memoization ( All test cases passed ):
```cpp
class Solution {
public:
    int coinUtil(vector<int> &coins,int remAmt,int ind,vector<vector<int>> &dp){
        if(ind == 0){
            if(remAmt % coins[ind] == 0) return remAmt / coins[ind];
            else return 1e9;
        }

        if(dp[ind][remAmt] != -1) return dp[ind][remAmt];

        int notTake = coinUtil(coins,remAmt,ind-1,dp);
        int take = INT_MAX;
        if(remAmt >= coins[ind]) take = 1 + coinUtil(coins,remAmt-coins[ind],ind,dp);

        return dp[ind][remAmt] = min(take,notTake);
    }
    int coinChange(vector<int>& coins, int amount) {
        vector<vector<int>> dp(coins.size(),vector<int>(amount+1,-1));
        int count = coinUtil(coins,amount,coins.size()-1,dp);

        if(count >= 1e9) return -1;
        return count;
    }
};
```

## Recursion (58/189 testcases passed):
```cpp
class Solution {
public:
    int coinUtil(vector<int> &coins,int remAmt,int ind){
        if(ind == 0){
            if(remAmt % coins[ind] == 0) return remAmt / coins[ind];
            else return 1e9;
        }

        int notTake = coinUtil(coins,remAmt,ind-1);
        int take = INT_MAX;
        if(remAmt >= coins[ind]) take = 1 + coinUtil(coins,remAmt-coins[ind],ind);

        return min(take,notTake);
    }
    int coinChange(vector<int>& coins, int amount) {
        int count = coinUtil(coins,amount,coins.size()-1);

        if(count >= 1e9) return -1;
        else return count;
    }
};
```
