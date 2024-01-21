### [Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/)

## Explanation:

## Space Optimization:
```cpp
class Solution {
public:
    int maxProfit(int k,vector<int>& prices) {
        vector<vector<long>> after(2,vector<long>(k+1,0));
        vector<vector<long>> cur(2,vector<long>(k+1,0));

        for(int i=prices.size()-1;i>=0;i--){
            for(int j=0;j<=1;j++){
                for(int cap=1;cap<=k;cap++){
                    long profit = 0;
                    if(j) {
                        profit = max(after[0][cap]-prices[i],after[1][cap]);
                    }
                    else{
                        profit = max(after[1][cap-1]+prices[i],after[0][cap]);
                    }
                    cur[j][cap] = profit;
                }
            }
            after = cur;
        }

        return (int)after[1][k];
    }
};
```

## Tabulation:
```cpp
class Solution {
public:
    int maxProfit(int k,vector<int>& prices) {
        vector<vector<vector<long>>> dp(prices.size()+1,vector<vector<long>>(2,vector<long>(k+1,0)));

        for(int i=prices.size()-1;i>=0;i--){
            for(int j=0;j<=1;j++){
                for(int cap=1;cap<=k;cap++){
                    long profit = 0;
                    if(j) {
                        profit = max(dp[i+1][0][cap]-prices[i],dp[i+1][1][cap]);
                    }
                    else{
                        profit = max(dp[i+1][1][cap-1]+prices[i],dp[i+1][0][cap]);
                    }
                    dp[i][j][cap] = profit;
                }
            }
        }

        return (int)dp[0][1][k];
    }
};
```

## Memoization:
```cpp
class Solution {
public:
    int maxProfitHelper(int ind, int buy,vector<int> &prices,vector<vector<vector<int>>> &dp,int cap){
        if(ind == prices.size()) return 0;

        if(cap == 0) return 0;
        
        if(dp[ind][buy][cap] != -1) return dp[ind][buy][cap];

        long profit = 0;
        if(buy) {
            profit = max(maxProfitHelper(ind+1,0,prices,dp,cap)-prices[ind],maxProfitHelper(ind+1,1,prices,dp,cap));
        }
        else{
            profit = max(maxProfitHelper(ind+1,1,prices,dp,cap-1)+prices[ind],maxProfitHelper(ind+1,0,prices,dp,cap));
        }

        return dp[ind][buy][cap] = profit;
    }
    int maxProfit(int k,vector<int>& prices) {
        vector<vector<vector<int>>> dp(prices.size()+1,vector<vector<int>>(2,vector<int>(k+1,-1)));

        return maxProfitHelper(0,1,prices,dp,k);
    }
};
```

## Recursion ( 206 / 210 testcases passed ):
```cpp
class Solution {
public:
    int maxProfitHelper(int ind, int buy,vector<int> &prices,int cap){
        if(ind == prices.size()) return 0;

        if(cap == 0) return 0;
        
        long profit = 0;
        if(buy) {
            profit = max(maxProfitHelper(ind+1,0,prices,cap)-prices[ind],maxProfitHelper(ind+1,1,prices,cap));
        }
        else{
            profit = max(maxProfitHelper(ind+1,1,prices,cap-1)+prices[ind],maxProfitHelper(ind+1,0,prices,cap));
        }

        return profit;
    }
    int maxProfit(int k, vector<int>& prices) {
        return maxProfitHelper(0,1,prices,k);
    }
};
```
