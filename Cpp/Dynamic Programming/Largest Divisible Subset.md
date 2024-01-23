### [Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset/?show=1)

## Explanation:
Sure, let's break down the code:

1. **Class and Function Declaration**: The code is written in C++ and defines a class `Solution` with a public function `largestDivisibleSubset`. This function takes a vector `nums` of integers as input.

2. **Initialization**: The function first determines the size `n` of the input vector. It then initializes two vectors, `dp` and `hash`, of size `n`. `dp` is filled with 1s, representing the length of the largest divisible subset ending at each index. `hash` is used to keep track of the previous index in the largest divisible subset. The variables `maxi` and `lastIndex` are initialized to keep track of the maximum length of the largest divisible subset and the last index of this subset.

3. **Sorting**: The input vector `nums` is sorted in ascending order. This is a crucial step because it ensures that every subset of `nums` is in non-decreasing order, which is a necessary condition for a subset to be divisible.

4. **Main Logic**: The main logic of the function is implemented using two nested loops. The outer loop iterates over the array from left to right. For each element, the inner loop checks all previous elements.

    - If the current element is divisible by a previous element (i.e., `nums[i] % nums[prev] == 0`) and the length of the largest divisible subset ending at the previous element plus one is greater than the current largest divisible subset length, then update the `dp` and `hash` arrays.
    - The `hash` array stores the index of the previous element in the largest divisible subset.
    - If the length of the largest divisible subset ending at the current index is greater than the maximum length found so far, update the maximum length and the last index of the largest divisible subset.

5. **Building the Largest Divisible Subset**: After finding the last index of the largest divisible subset, the code constructs the subset in reverse order by following the indices stored in the `hash` array. The subset is then returned as the result.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of the code is **O(n^2)**, where `n` is the size of the input array. This is because there are two nested loops iterating over the array.

### `Space Complexity`:
The space complexity of the code is **O(n)**, where `n` is the size of the input array. This is due to the additional space required for the `dp` and `hash` arrays.

## Code:
```cpp
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, 1), hash(n);
        int maxi = 1;
        int lastIndex = 0;
        sort(nums.begin(),nums.end());

        // Loop through each element in the array
        for (int i = 0; i < n; i++) {
            hash[i] = i;

            // Check previous elements to find the longest increasing subsequence
            for (int prev = 0; prev < i; prev++) {
                if (nums[i] % nums[prev] == 0 && 1 + dp[prev] > dp[i]) {
                    dp[i] = 1 + dp[prev];
                    hash[i] = prev;
                }
            }

            // Update the maximum length and last index
            if (dp[i] > maxi) {
                maxi = dp[i];
                lastIndex = i;
            }
        }

        // Reconstruct the longest increasing subsequence
        vector<int> temp;
        temp.push_back(nums[lastIndex]);

        // Trace back through the 'hash' array to find the entire subsequence
        while (hash[lastIndex] != lastIndex) {
            lastIndex = hash[lastIndex];
            temp.push_back(nums[lastIndex]);
        }

        return temp;
    }
};
```
