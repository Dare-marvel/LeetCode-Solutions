### [Jump Game](https://leetcode.com/problems/jump-game/description/)

## Explanation:
Sure, here's an elaborate explanation of the code:

1. **Class Definition**: The code defines a class named `Solution`. This is a common practice in C++ to encapsulate related data and functions.

2. **Function Definition**: Inside the `Solution` class, there's a public function named `canJump`. This function takes a vector of integers (`nums`) as an argument and returns a boolean value.

3. **Variable Initialization**: Inside the `canJump` function, two integer variables `n` and `lastPos` are initialized. `n` is the size of the input vector `nums`, and `lastPos` is initially set to the last index of `nums`.

4. **Loop Structure**: A `for` loop is used to iterate over the `nums` vector in reverse order, starting from the last index (`n - 1`) and going down to the first index (`0`).

5. **Condition Check**: Inside the loop, an `if` condition checks whether the sum of the current index `i` and the value at that index in `nums` (`nums[i]`) is greater than or equal to `lastPos`.

6. **Updating lastPos**: If the condition is true, `lastPos` is updated to the current index `i`. This means that it's possible to reach `lastPos` from `i` within the jumps allowed by `nums[i]`.

7. **Return Statement**: After the loop, the function returns whether `lastPos` is `0`. If it is, this means it's possible to reach the first index from all later indices within the jumps allowed by their respective values in `nums`, so a jump to the end of the array is possible from the first index.

This code is an example of a **greedy algorithm**, where the optimal decision is made at each stage with the hope that these local optimums will lead to a global optimum. In this case, the algorithm greedily jumps as far as possible at each step, which leads to the minimum total number of jumps to reach the end of the array. The `lastPos` variable is used to keep track of the farthest reachable index at each step.

## Time and Space Complexity:
### `Time Complexity`:
The **time complexity** of this code is **O(n)**, where `n` is the size of the input vector. This is because each element in the `nums` vector is visited once in the `for` loop.

### `Space Complexity`:
The **space complexity** of this code is **O(1)**. This is because the space used does not grow with the size of the input vector - only a constant amount of space is used for variables.

## Code:
```cpp
class Solution {
public:
    // Function to check if it's possible to jump through the array
    bool canJump(vector<int>& nums) {
        // Get the size of the array
        int n = nums.size();
        
        // Initialize the last position to be reached as the last index of the array
        int lastPos = n - 1;
        
        // Iterate through the array in reverse order
        for (int i = n - 1; i >= 0; i--) {
            // Check if the current position can reach the last position or beyond
            if (i + nums[i] >= lastPos) {
                // If true, update the last position to the current index
                lastPos = i;
            }
        }
        
        // Check if the last position reached is the beginning of the array
        return lastPos == 0;
    }
};


```

## Memoization:
```cpp
class Solution {
    vector<int> dp;
public:
    bool canJumpUtil(vector<int>& nums, int ind) {
        if (ind == nums.size() - 1) {
            return true;
        }

        if (dp[ind] != -1) {
            return dp[ind];
        }

        int reach = min(ind + nums[ind], (int)nums.size() - 1);

        for (int k = ind + 1; k <= reach; k++) {
            if (canJumpUtil(nums, k)) {
                return dp[ind] = true;
            }
        }
        return dp[ind] = false;
    }

    bool canJump(vector<int>& nums) {
        dp.assign(nums.size(), -1);
        return canJumpUtil(nums, 0);
    }
};

```
