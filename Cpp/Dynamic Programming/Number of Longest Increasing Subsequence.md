### [Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/)

## Approach and Intuition

The problem of finding the number of longest increasing subsequences (LIS) in a given array can be approached effectively using dynamic programming. Here's a detailed explanation of the logic and intuition behind the solution:

#### 1. **Initialization**
- **Array Definitions**:
  - `lengths`: This array stores the length of the longest increasing subsequence ending at each index. Initialized to 1 for all elements, because the minimum length of LIS that ends at each element is the element itself.
  - `counts`: This array stores the count of longest increasing subsequences ending at each index. Initialized to 1 for all elements, because there is at least one subsequence (the element itself) ending at each index.

#### 2. **Iterate Over the Array**
- Use a nested loop to compare each pair of elements `(nums[i], nums[j])` where `i > j`. This helps to build the subsequences by considering all previous elements before the current element.

#### 3. **Update `lengths` and `counts` Arrays**
- **Condition**: Check if `nums[i] > nums[j]` to ensure the subsequence remains increasing.
- **Updating `lengths`**:
  - If `lengths[j] + 1 > lengths[i]`: This means we've found a longer increasing subsequence ending at `i`. Update `lengths[i]` to `lengths[j] + 1`.
  - If `lengths[j] + 1 == lengths[i]`: This means there is another subsequence of the same length ending at `i`. Add the count of subsequences ending at `j` to `counts[i]`.
- **Updating `counts`**:
  - When `lengths[j] + 1 > lengths[i]`, reset `counts[i]` to `counts[j]`.
  - When `lengths[j] + 1 == lengths[i]`, increment `counts[i]` by `counts[j]`.

#### 4. **Determine the Maximum Length**
- Track the maximum value in the `lengths` array, which represents the length of the longest increasing subsequence.

#### 5. **Count Subsequences of Maximum Length**
- Iterate through the `lengths` array and sum up the values in `counts` for indices where the value in `lengths` equals the maximum length. This gives the total number of longest increasing subsequences.

## Time and Space Complexity

### Time Complexity
- The solution uses a nested loop to compare each pair of elements.
- The outer loop runs `n` times, and the inner loop runs up to `n` times.
- This gives a time complexity of \(O(n^2)\).

### Space Complexity
- Two arrays `lengths` and `counts` of size `n` are used.
- The space complexity is \(O(n)\).

### Summary

1. **Initialize `lengths` and `counts` arrays** to store the lengths and counts of LIS ending at each index.
2. **Iterate over each element** in the array to build and extend increasing subsequences.
3. **Update the `lengths` and `counts` arrays** based on the conditions to maintain increasing subsequences.
4. **Track the maximum length** of the increasing subsequences.
5. **Sum up the counts** of subsequences of maximum length to get the final result.

### Example Walkthrough

Consider an example `nums = [1, 3, 5, 4, 7]`:

- Initially, `lengths = [1, 1, 1, 1, 1]` and `counts = [1, 1, 1, 1, 1]`.
- As we iterate:
  - For `i = 1`, comparing with `j = 0`, since `3 > 1`, `lengths[1] = lengths[0] + 1 = 2` and `counts[1] = counts[0] = 1`.
  - For `i = 2`, comparing with `j = 0` and `j = 1`, since `5 > 3` and `5 > 1`, `lengths[2] = lengths[1] + 1 = 3` and `counts[2] = counts[1] = 1`.
  - For `i = 3`, comparing with `j = 0`, `j = 1`, and `j = 2`, since `4 > 1` and `4 > 3`, `lengths[3] = lengths[1] + 1 = 3` and `counts[3] = counts[1] = 1`, then `lengths[3]` remains 3 and `counts[3]` becomes `1 + 1 = 2`.
  - For `i = 4`, comparing with `j = 0`, `j = 1`, `j = 2`, and `j = 3`, since `7 > 5` and `7 > 4`, `lengths[4] = lengths[2] + 1 = 4` and `counts[4] = counts[2] = 1`, then `lengths[4]` remains 4 and `counts[4]` becomes `1 + 2 = 3`.
- The maximum length of LIS is 4, and there are 3 such subsequences.

## Code:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        // Get the size of the input vector
        int n = nums.size();
        
        // If the vector is empty, return 0
        if (n == 0) return 0;
        
        // Initialize vectors to store lengths and counts of LIS ending at each index
        vector<int> lengths(n, 1); // All lengths are initially 1
        vector<int> counts(n, 1); // All counts are initially 1
        
        int maxLength = 1; // Initialize maxLength to 1
        
        // Iterate through the vector
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                // If the current element is greater than the previous element
                if (nums[i] > nums[j]) {
                    // If the length of the LIS ending at j + 1 is greater than the current length
                    if (lengths[j] + 1 > lengths[i]) {
                        // Update the length and count
                        lengths[i] = lengths[j] + 1;
                        counts[i] = counts[j];
                    } 
                    // If the length is the same as the current length
                    else if (lengths[j] + 1 == lengths[i]) {
                        // Add the count to the current count
                        counts[i] += counts[j];
                    }
                }
            }
            // Update the maximum length
            maxLength = max(maxLength, lengths[i]);
        }
        
        int numOfLIS = 0;
        // Iterate through the lengths vector
        for (int i = 0; i < n; ++i) {
            // If the length is equal to the maximum length
            if (lengths[i] == maxLength) {
                // Add the count to the total number of LIS
                numOfLIS += counts[i];
            }
        }
        
        // Return the total number of LIS
        return numOfLIS;
    }
};
```
