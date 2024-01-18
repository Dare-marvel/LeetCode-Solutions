### [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/description/)

## Explanation:


## Tabulation:
```cpp

```

## Memoization (Passed all testcases):
```cpp
class Solution {
public:
    int distHelper(int i,int j,string &s,string &t,vector<vector<int>> &dp){
        if(j<0) return 1;
        if(i<0) return 0;

        if(dp[i][j] != -1) return dp[i][j];

        if(s[i] == t[j]) return dp[i][j] = distHelper(i-1,j-1,s,t,dp) + distHelper(i-1,j,s,t,dp);
        else return dp[i][j] = distHelper(i-1,j,s,t,dp);
    }
    int numDistinct(string s, string t) {
        vector<vector<int>> dp(s.size(),vector<int>(t.size(),-1));
        return distHelper(s.size()-1,t.size()-1,s,t,dp);
    }
};
```

## Recursion (Time Limit Exceeded):
```cpp
class Solution {
public:
    int distHelper(int i,int j,string &s,string &t){
        if(j<0) return 1;
        if(i<0) return 0;

        if(s[i] == t[j]) return distHelper(i-1,j-1,s,t) + distHelper(i-1,j,s,t);
        else return distHelper(i-1,j,s,t);
    }
    int numDistinct(string s, string t) {
        return distHelper(s.size()-1,t.size()-1,s,t);
    }
};
```
