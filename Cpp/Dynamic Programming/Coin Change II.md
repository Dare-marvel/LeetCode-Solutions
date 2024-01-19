### [Coin Change II](https://leetcode.com/problems/coin-change-ii/description/)

## [Explanation](https://takeuforward.org/data-structure/coin-change-2-dp-22/)
1. **Class and Function Structure**: The code is encapsulated within a class named `Solution`. It contains two public functions: `countWaysToMakeChange` and `change`.

2. **Function - countWaysToMakeChange**: This function takes a vector of integers (`arr`), an integer (`n`), and a target sum (`T`) as input. It returns the number of ways to make change for `T` using the coins in `arr`. It uses a dynamic programming (DP) approach to solve the problem.

3. **Dynamic Programming Table**: A 2D DP table `dp` is created with dimensions `n x (T+1)`, where `n` is the size of the input vector `arr`. The DP table is initialized with zeros.

4. **DP Table Initialization**: The first row of the DP table is initialized based on the first element of the array. If the first element is a divisor of `i`, `dp[0][i]` is set to 1. This is because there is one way to make change for `i` using multiples of the first coin.

5. **DP Table Update**: The DP table is filled using a bottom-up approach. For each coin in the array (from the second coin onwards), and for each target sum from 0 to `T`, the DP table is updated. If the current coin doesn't exceed the target, it can be used to make change. The number of ways to make change for the target sum is the sum of the number of ways without using the current coin (`notTaken`) and the number of ways using the current coin (`taken`).

6. **Function - change**: This function is the main function that gets called. It takes a target amount (`amount`) and a vector of integers (`coins`) as input. It calls the `countWaysToMakeChange` function with `coins`, the size of `coins`, and `amount` as arguments.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of the code is O(n*T), where `n` is the size of the input array and `T` is the target sum. This is because the code iterates over each coin in the array for each target sum from 0 to `T`.

### `Space Complexity`:
The space complexity of the code is also O(n*T), due to the 2D DP table that is created with dimensions `n x (T+1)`. The space required for the DP table is directly proportional to the size of the input array and the target sum.

## Tabulation:
```cpp
class Solution {
public:
    // Function to count the ways to make change for a given amount using given coins
    long countWaysToMakeChange(vector<int>& arr, int n, int T) {
        // Create a DP table with dimensions n x T+1, initialized with zeros
        vector<vector<long>> dp(n, vector<long>(T + 1, 0));

        // Initializing base condition for the first coin
        for (int i = 0; i <= T; i++) {
            if (i % arr[0] == 0)
                dp[0][i] = 1;  // If divisible, there is one way to make change
            // Else condition is automatically fulfilled,
            // as the dp array is initialized to zero
        }

        // Fill in the DP table using a bottom-up approach
        for (int ind = 1; ind < n; ind++) {
            for (int target = 0; target <= T; target++) {
                // Exclude the current coin
                long notTaken = dp[ind - 1][target];

                // Include the current coin if it doesn't exceed the target
                long taken = 0;
                if (arr[ind] <= target)
                    taken = dp[ind][target - arr[ind]];

                // Update the DP table
                dp[ind][target] = notTaken + taken;
            }
        }

        // The final result is in the last cell of the DP table
        return dp[n - 1][T];
    }

    // Function to find the number of ways to make change for a given amount
    int change(int amount, vector<int>& coins) {
        // Call the countWaysToMakeChange function to get the result
        return countWaysToMakeChange(coins, coins.size(), amount);
    }
};
```

## Memoization:
```cpp
#include <bits/stdc++.h>
using namespace std;

// Function to count the number of ways to make change for a given target sum
long countWaysToMakeChangeUtil(vector<int>& arr, int ind, int T, vector<vector<long>>& dp) {
    // Base case: if we're at the first element
    if (ind == 0) {
        // Check if the target sum is divisible by the first element
        return (T % arr[0] == 0);
    }
    
    // If the result for this index and target sum is already calculated, return it
    if (dp[ind][T] != -1)
        return dp[ind][T];
        
    // Calculate the number of ways without taking the current element
    long notTaken = countWaysToMakeChangeUtil(arr, ind - 1, T, dp);
    
    // Calculate the number of ways by taking the current element
    long taken = 0;
    if (arr[ind] <= T)
        taken = countWaysToMakeChangeUtil(arr, ind, T - arr[ind], dp);
        
    // Store the sum of ways in the DP table and return it
    return dp[ind][T] = notTaken + taken;
}

// Function to count the number of ways to make change for the target sum
long countWaysToMakeChange(vector<int>& arr, int n, int T) {
    vector<vector<long>> dp(n, vector<long>(T + 1, -1)); // Create a DP table
    
    // Call the utility function to calculate the answer
    return countWaysToMakeChangeUtil(arr, n - 1, T, dp);
}
```
