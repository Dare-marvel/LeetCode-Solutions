### [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/)

## [Explanation](https://takeuforward.org/data-structure/buy-and-sell-stocks-with-cooldown-dp-39/):

## Tabulation:
```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        vector<vector<long>> dp(prices.size()+2,vector<long>(2,0));

        long profit = 0;

        for(int i=prices.size()-1;i>=0;i--){
            for(int j=0;j<=1;j++){
                if(j) {
                    profit = max(dp[i+1][0]-prices[i],dp[i+1][1]);
                }
                else{
                    profit = max(dp[i+2][1]+prices[i],dp[i+1][0]);
                }

                dp[i][j] = profit;
            }
        }
        return (int)dp[0][1];
    }
};
```

## Memoization:
```cpp
class Solution {
public:
    int maxProfitHelper(int ind, int buy,vector<int> &prices,vector<vector<int>> &dp){
        if(ind >= prices.size()) return 0;
        
        if(dp[ind][buy] != -1) return dp[ind][buy];

        long profit = 0;
        if(buy) {
            profit = max(maxProfitHelper(ind+1,0,prices,dp)-prices[ind],maxProfitHelper(ind+1,1,prices,dp));
        }
        else{
            profit = max(maxProfitHelper(ind+2,1,prices,dp)+prices[ind],maxProfitHelper(ind+1,0,prices,dp));
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
        if(ind >= prices.size()) return 0;
        
        long profit = 0;
        if(buy) {
            profit = max(maxProfitHelper(ind+1,0,prices)-prices[ind],maxProfitHelper(ind+1,1,prices));
        }
        else{
            profit = max(maxProfitHelper(ind+2,1,prices)+prices[ind],maxProfitHelper(ind+1,0,prices));
        }

        return profit;
    }
    int maxProfit(vector<int>& prices) {
        return maxProfitHelper(0,1,prices);
    }
};
```
