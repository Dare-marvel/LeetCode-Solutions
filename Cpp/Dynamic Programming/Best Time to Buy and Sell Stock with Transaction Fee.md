### [Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/)

## [Explanation](https://takeuforward.org/data-structure/buy-and-sell-stocks-with-transaction-fees-dp-40/)

## Space Optimization:
```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices,int fee) {
        vector<long> ahead(2,0), cur(2,0);

        for(int i=prices.size()-1;i>=0;i--){
            for(int j=0;j<=1;j++){
                long profit = 0;
                if(j) {
                    profit = max(ahead[0]-prices[i],ahead[1]);
                }
                else{
                    profit = max(ahead[1]+prices[i]-fee,ahead[0]);
                }

                cur[j] = profit;
            }
            ahead = cur;
        }
        return (int)ahead[1];
    }
};
```

## Tabulation:
```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices,int fee) {
        vector<vector<long>> dp(prices.size()+1,vector<long>(2,0));

        long profit = 0;

        for(int i=prices.size()-1;i>=0;i--){
            for(int j=0;j<=1;j++){
                if(j) {
                    profit = max(dp[i+1][0]-prices[i],dp[i+1][1]);
                }
                else{
                    profit = max(dp[i+1][1]+prices[i]-fee,dp[i+1][0]);
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
    int maxProfitHelper(int ind, int buy,vector<int> &prices,vector<vector<int>> &dp,int fee){
        if(ind == prices.size()) return 0;
        
        if(dp[ind][buy] != -1) return dp[ind][buy];

        long profit = 0;
        if(buy) {
            profit = max(maxProfitHelper(ind+1,0,prices,dp,fee)-prices[ind],maxProfitHelper(ind+1,1,prices,dp,fee));
        }
        else{
            profit = max(maxProfitHelper(ind+1,1,prices,dp,fee)+prices[ind]-fee,maxProfitHelper(ind+1,0,prices,dp,fee));
        }

        return dp[ind][buy] = profit;
    }
    int maxProfit(vector<int>& prices,int fee) {
        vector<vector<int>> dp(prices.size()+1,vector<int>(2,-1));
        return maxProfitHelper(0,1,prices,dp,fee);
    }
};
```

## Recursion ( 19 / 44 testcases passed ):
```cpp
class Solution {
public:
    int maxProfitHelper(int ind, int buy,vector<int> &prices,int fee){
        if(ind == prices.size()) return 0;
        long profit = 0;
        if(buy) {
            profit = max(maxProfitHelper(ind+1,0,prices,fee)-prices[ind],maxProfitHelper(ind+1,1,prices,fee));
        }
        else{
            profit = max(maxProfitHelper(ind+1,1,prices,fee)+prices[ind]-fee,maxProfitHelper(ind+1,0,prices,fee));
        }

        return profit;
    }
    int maxProfit(vector<int>& prices,int fee) {
        return maxProfitHelper(0,1,prices,fee);
    }
};
```
