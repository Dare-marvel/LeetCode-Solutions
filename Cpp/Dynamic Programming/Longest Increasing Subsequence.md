### [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/description/)

## [Explanation](https://takeuforward.org/data-structure/printing-longest-increasing-subsequence-dp-42/)

## Binary Search:
```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> temp;
        temp.push_back(nums[0]);

        for(int i=0;i<n;i++){
            if(nums[i] > temp.back()){
                temp.push_back(nums[i]);
            }
            else{
                auto it = lower_bound(temp.begin(),temp.end(),nums[i]);
                *it = nums[i];
            }
        }
        return temp.size();
    }
};

```

## Space Optimization:
```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n,1);
        int maxi = 1;

        for(int i=0;i<n;i++){
            for(int prev=0;prev<i;prev++){
                if(nums[prev] < nums[i])
                    dp[i] = max(dp[i],1+dp[prev]);
            }

            maxi = max(dp[i],maxi);
        }

        return maxi;
    }
};
```

## Tabulation:
```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(nums.size()+1,vector<int>(nums.size()+1,0));
        
        for(int ind=n-1;ind>=0;ind--){
            for(int prev=ind-1;prev>=-1;prev--){
                int len = dp[ind+1][prev+1];
                if(prev == -1 || nums[ind] > nums[prev]){
                    len = max(len,1+dp[ind+1][ind+1]);
                }

                dp[ind][prev+1] = len;
            }
        }

        return dp[0][0];
    }
};
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
