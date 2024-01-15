### [Target Sum](https://leetcode.com/problems/target-sum/description/)

## Explanation:
Sure, here's an explanation of the code:

1. **Class and Function Structure**: The code is encapsulated within a class named `Solution`. It contains three public functions: `findWays`, `countPartitions`, and `findTargetSumWays`.

2. **Function - findWays**: This function takes a vector of integers (`num`) and an integer (`k`) as input. It returns the number of subsets of `num` that sum up to `k`. It uses a dynamic programming (DP) approach to solve the problem.

3. **Dynamic Programming Table**: A 2D DP table `dp` is created with dimensions `n x (k+1)`, where `n` is the size of the input vector `num`. The DP table is initialized with zeros.

4. **DP Table Initialization**: The first row of the DP table is initialized based on the first element of the array. If the first element is zero, `dp[0][0]` is set to 2, otherwise it's set to 1. If the first element is not zero and less than or equal to `k`, `dp[0][num[0]]` is set to 1.

5. **DP Table Update**: The DP table is filled using a bottom-up approach. For each element in the array (from the second element onwards), and for each target sum from 0 to `k`, the DP table is updated. If the current element doesn't exceed the target, it can be included in the subset. The number of ways to reach the target sum is the sum of the number of ways without including the current element (`notTaken`) and the number of ways including the current element (`taken`).

6. **Function - countPartitions**: This function takes the size of the array (`n`), a target sum (`d`), and a vector of integers (`arr`) as input. It calculates the total sum of the elements in `arr`. If the difference between the total sum and `d` is negative or odd, it returns 0. Otherwise, it calls the `findWays` function with `arr` and half of the difference between the total sum and `d` as arguments.

7. **Function - findTargetSumWays**: This function is the main function that gets called. It takes a vector of integers (`nums`) and a target sum (`target`) as input. It calls the `countPartitions` function with the size of `nums`, `target`, and `nums` as arguments.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of the code is O(n*k), where `n` is the size of the input array and `k` is the target sum. This is because the code iterates over each element of the array for each target sum from 0 to `k`.

### `Space Complexity`:
The space complexity of the code is also O(n*k), due to the 2D DP table that is created with dimensions `n x (k+1)`. The space required for the DP table is directly proportional to the size of the input array and the target sum.

## Code:
```cpp
class Solution {
public:
    // Function to count the number of subsets with a given sum
    int findWays(vector<int>& num, int k) {
        int n = num.size();

        // Create a 2D DP table with dimensions n x k+1, initialized with zeros
        vector<vector<int>> dp(n, vector<int>(k + 1, 0));

        // Handling the base case when the first element is 0
        if (num[0] == 0) 
            dp[0][0] = 2;  // Two subsets: one with the element, one without
        else 
            dp[0][0] = 1;  // Only one subset without the element

        // Initialize the first row based on the first element of the array
        if (num[0] != 0 && num[0] <= k) {
            dp[0][num[0]] = 1;
        }

        // Fill in the DP table using a bottom-up approach
        for (int ind = 1; ind < n; ind++) {
            for (int target = 0; target <= k; target++) {
                // Exclude the current element
                int notTaken = dp[ind - 1][target];

                // Include the current element if it doesn't exceed the target
                int taken = 0;
                if (num[ind] <= target) {
                    taken = dp[ind - 1][target - num[ind]];
                }

                // Update the DP table
                dp[ind][target] = (notTaken + taken);
            }
        }

        // The final result is in the last cell of the DP table
        return dp[n - 1][k];
    }

    // Function to count the number of ways to partition an array into two subsets
    int countPartitions(int n, int d, vector<int> &arr) {
        // Calculate the total sum of the array
        int totSum = 0;
        for (auto &it : arr) 
            totSum += it;

        // Check if it's possible to achieve the desired difference
        if (totSum - d < 0 || (totSum - d) % 2) 
            return 0;  // If not, return 0

        // Call the findWays function to count subsets with the required sum
        return findWays(arr, (totSum - d) / 2);
    }

    // Function to find the number of ways to reach a target sum using given numbers
    int findTargetSumWays(vector<int>& nums, int target) {
        return countPartitions(nums.size(), target, nums);
    }
};
```
