### [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/description/)

## [Explanation](https://takeuforward.org/data-structure/wildcard-matching-dp-34/):

## Tabulation:
```cpp

```

## Memoization (passes all testcases):
```cpp
class Solution {
public:
    bool isMatchHelp(int i,int j,string &p,string &s,vector<vector<int>> &dp){
        if(i<0 && j<0) return true;
        if(i<0 && j>=0) return false;
        if(j<0 && i>=0) {
            for(int ind=0;ind<=i;ind++){
                if(p[ind] != '*') return false;
            }
            return true;
        }

        if(dp[i][j] != -1) return dp[i][j];

        if(p[i] == s[j] || p[i] == '?'){
            return dp[i][j] = isMatchHelp(i-1,j-1,p,s,dp);
        }

        if(p[i] == '*'){
            return dp[i][j] = isMatchHelp(i-1,j,p,s,dp) || isMatchHelp(i,j-1,p,s,dp);
        }

        return false;
    }
    bool isMatch(string s, string p) {
        int n = p.size();
        int m = s.size();
        vector<vector<int>> dp(n,vector<int>(m,-1));

        return isMatchHelp(n-1,m-1,p,s,dp);
    }
};
```

## Recursion (passed 1639/1811 testcases):
```cpp
class Solution {
public:
    bool isMatchHelp(int i,int j,string &p,string &s){
        if(i<0 && j<0) return true;
        if(i<0 && j>=0) return false;
        if(j<0 && i>=0) {
            for(int ind=0;ind<=i;ind++){
                if(p[ind] != '*') return false;
            }
            return true;
        }

        if(p[i] == s[j] || p[i] == '?'){
            return isMatchHelp(i-1,j-1,p,s);
        }

        if(p[i] == '*'){
            return isMatchHelp(i-1,j,p,s) || isMatchHelp(i,j-1,p,s);
        }

        return false;
    }
    bool isMatch(string s, string p) {
        int n = p.size();
        int m = s.size();

        return isMatchHelp(n-1,m-1,p,s);
    }
};
```
