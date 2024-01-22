### [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/description/)

## Explanation:

## Code:
```cpp

```

## Code:
```cpp

```

## Memoization:
```cpp
class Solution {
public:
    int LISHelp(int ind,int prev_ind,vector<int>& nums, vector<vector<int>> &dp){
        if(ind == nums.size()){
            return 0;
        }

        if(dp[ind][prev_ind+1] != -1){
            return dp[ind][prev_ind+1];
        }

        int len = LISHelp(ind+1,prev_ind,nums,dp);
        if(prev_ind == -1 || nums[ind] > nums[prev_ind]){
            len = max(len,1+LISHelp(ind+1,ind,nums,dp));
        }

        return dp[ind][prev_ind+1] = len;
    }
    int lengthOfLIS(vector<int>& nums) {

        vector<vector<int>> dp(nums.size(),vector<int>(nums.size()+1,-1));
        return LISHelp(0,-1,nums,dp);
    }
};
```

## Recursion (22/55 testcases passed):
```cpp
class Solution {
public:
    int LISHelp(int ind,int prev_ind,vector<int>& nums){
        if(ind == nums.size()){
            return 0;
        }

        int len = LISHelp(ind+1,prev_ind,nums);
        if(prev_ind == -1 || nums[ind] > nums[prev_ind]){
            len = max(len,1+LISHelp(ind+1,ind,nums));
        }

        return len;
    }
    int lengthOfLIS(vector<int>& nums) {
        return LISHelp(0,-1,nums);
    }
};
```
