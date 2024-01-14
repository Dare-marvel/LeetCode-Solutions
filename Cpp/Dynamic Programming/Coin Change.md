### [Coin Change](https://leetcode.com/problems/coin-change/description/)

## [Explanation](https://takeuforward.org/data-structure/minimum-coins-dp-20/):

## Tabulation:
```cpp

```

## Memoization:
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

## Recursion:
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
