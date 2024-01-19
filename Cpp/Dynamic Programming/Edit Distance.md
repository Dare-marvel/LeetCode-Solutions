### [Edit Distance](https://leetcode.com/problems/edit-distance/description/)

## Explanation:

## Tabulation:
```cpp

```

## Memoization:
```cpp
class Solution {
public:
    vector<vector<int>> dp;
    int minDistHelper(string &word1, string &word2,int i,int j){
        if(i<0) return j+1;
        if(j<0) return i+1;

        if(dp[i][j] != -1) return dp[i][j];

        if(word1[i] == word2[j]) return dp[i][j] = minDistHelper(word1,word2,i-1,j-1);
        else{
            return dp[i][j] = min({1+ minDistHelper(word1,word2,i,j-1),1+ minDistHelper(word1,word2,i-1,j), 1+ minDistHelper(word1,word2,i-1,j-1)});
        }
    }
    int minDistance(string word1, string word2) {
        dp = vector<vector<int>>(word1.size(), vector<int>(word2.size(), -1));
        return  minDistHelper(word1,word2,word1.size()-1,word2.size()-1);
    }
};
```

## Recursion (25/1146 testcases passed):
```cpp
class Solution {
public:
    int minDistHelper(string &word1, string &word2,int i,int j){
        if(i<0) return j+1;
        if(j<0) return i+1;

        if(word1[i] == word2[j]) return minDistHelper(word1,word2,i-1,j-1);
        else{
            return min({1+ minDistHelper(word1,word2,i,j-1),1+ minDistHelper(word1,word2,i-1,j), 1+ minDistHelper(word1,word2,i-1,j-1)});
        }
    }
    int minDistance(string word1, string word2) {
        return  minDistHelper(word1,word2,word1.size()-1,word2.size()-1);
    }
};

```
