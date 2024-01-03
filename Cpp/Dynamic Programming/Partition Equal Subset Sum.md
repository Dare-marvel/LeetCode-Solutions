### [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/description/)

## Explanation:

## Time and Space Complexity:
### `Time Complexity`:

### `Space Complexity`:

## Tabulization:
```cpp

```

## Recursion ( Passing 36/141 test cases ):
```cpp
class Solution {
public:
    bool subsetUtil(int ind, int target, vector<int> &arr) {
        // Base case: if the target sum is 0, the subset is found
        if (target == 0) return true;

        // Base case: if we have reached the first element and it is equal to the target, return true
        if (ind == 0) return arr[ind] == target;

        // Recursive case: Try not taking the current element in the subset
        bool notTake = subsetUtil(ind - 1, target, arr);

        // Recursive case: Try taking the current element in the subset if it is less than or equal to the target
        bool take = false;
        if (target >= arr[ind]) {
            take = subsetUtil(ind - 1, target - arr[ind], arr);
        }

        // Return true if either notTake or take is true
        return take || notTake;
    }
    bool canPartition(vector<int>& nums) {
        int totSum = 0;
        for(int i=0;i<nums.size();i++) totSum += nums[i];

        if(totSum % 2) return false;

        int target = totSum / 2;
        return subsetUtil(nums.size()-1,target,nums);
    }
};
```
