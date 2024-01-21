### [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/)

## [Explanation]()

## Tabulation:
```cpp

```

## Memoization:
```cpp
class Solution {
public:
    int maxProfitHelper(int ind, int buy,vector<int> &prices,vector<vector<int>> &dp){
        if(ind == prices.size()) return 0;
        
        if(dp[ind][buy] != -1) return dp[ind][buy];

        long profit = 0;
        if(buy) {
            profit = max(maxProfitHelper(ind+1,0,prices,dp)-prices[ind],maxProfitHelper(ind+1,1,prices,dp));
        }
        else{
            profit = max(maxProfitHelper(ind+1,1,prices,dp)+prices[ind],maxProfitHelper(ind+1,0,prices,dp));
        }

        return dp[ind][buy] = profit;
    }
    int maxProfit(vector<int>& prices) {
        vector<vector<int>> dp(prices.size()+1,vector<int>(2,-1));
        return maxProfitHelper(0,1,prices,dp);
    }
};
```

## Recursion:
```cpp
class Solution {
public:
    int maxProfitHelper(int ind, int buy,vector<int> &prices){
        if(ind == prices.size()) return 0;
        long profit = 0;
        if(buy) {
            profit = max(maxProfitHelper(ind+1,0,prices)-prices[ind],maxProfitHelper(ind+1,1,prices));
        }
        else{
            profit = max(maxProfitHelper(ind+1,1,prices)+prices[ind],maxProfitHelper(ind+1,0,prices));
        }

        return profit;
    }
    int maxProfit(vector<int>& prices) {
        return maxProfitHelper(0,1,prices);
    }
};
```
