### [Jump Game II](https://leetcode.com/problems/jump-game-ii/description/)

## Explanation ( Dynamic Programming Approach ):
### Approach and Intuition

1. **Understanding the Problem:**
   - The problem is to find the minimum number of jumps needed to reach the end of an array, starting from the first element. Each element in the array represents the maximum jump length from that position.
   
2. **Recursive Approach with Memoization:**
   - The solution employs a recursive approach to solve the problem. The function `jumpHelper` recursively determines the minimum jumps needed to reach the end of the array from a given index.
   - To avoid redundant calculations and optimize the solution, the approach uses memoization, storing the results of subproblems in a `dp` array.

3. **Base Case:**
   - The base case for the recursion is when the current index (`ind`) reaches the last element of the array (`n-1`). At this point, no further jumps are needed, so the function returns 0.

4. **Memoization Check:**
   - Before performing the recursive calculation for a given index, the function checks if the result is already computed and stored in the `dp` array. If `dp[ind]` is not `-1`, it returns the stored value to avoid redundant computation.

5. **Recursive Calculation:**
   - For each index, the function calculates the minimum jumps required to reach the end by trying all possible jumps (from 1 to the value at the current index `nums[ind]`).
   - It iteratively checks each possible jump from the current position and recursively calls `jumpHelper` for the new position (`ind + i`).
   - It keeps track of the minimum jumps required (`mini`) for each possible jump.

6. **Updating the Memoization Table:**
   - After computing the minimum jumps for the current index, the result is stored in the `dp` array to be used in future calls.

7. **Initialization and Final Call:**
   - The `jump` function initializes the `dp` array with `-1` and calls `jumpHelper` starting from index `0`.

## Time and Space Complexity

1. **Time Complexity:**
   - The time complexity of this solution is **O(n^2)**, where `n` is the length of the `nums` array.
   - This is because, in the worst case, for each index, the function might make up to `nums[ind]` recursive calls, and the maximum value of `nums[ind]` can be `n-1`. Hence, for each index, the recursion depth can go up to `n`, leading to an overall complexity of `O(n^2)`.

2. **Space Complexity:**
   - The space complexity is **O(n)**.
   - This includes the space required for the `dp` array, which is of size `n`.
   - Additionally, the recursion stack can go up to `n` in depth in the worst case, contributing to the space complexity.

### Step-by-Step Walkthrough

1. **Initialize the `dp` Array:**
   - The `jump` function initializes the `dp` array with `-1`, indicating that no subproblem has been solved yet.

2. **Call the Recursive Helper Function:**
   - `jumpHelper(0, nums, nums.size())` is called to start the process from the first index of the array.

3. **Base Case Handling:**
   - If the current index is the last index (`ind == n-1`), return 0 because no further jumps are needed.

4. **Memoization Check:**
   - Before proceeding with recursive calculations, check if the result for the current index is already computed (`dp[ind] != -1`). If so, return the precomputed value.

5. **Calculate Minimum Jumps:**
   - Iterate through all possible jumps from the current position (from 1 to `nums[ind]`).
   - For each possible jump, recursively calculate the minimum jumps needed from the new position (`ind + i`).

6. **Track Minimum Jumps:**
   - Keep track of the minimum jumps required by comparing the current minimum (`mini`) with the result of the recursive call.

7. **Store Result in `dp` Array:**
   - Once the minimum jumps for the current index are determined, store the result in the `dp` array to avoid recomputation in future calls.

8. **Return Final Result:**
   - The `jump` function returns the result of `jumpHelper(0, nums, nums.size())`, which gives the minimum jumps required to reach the end of the array from the first index.

## Code:
```cpp
class Solution {
public:
    // dp vector to store the minimum number of jumps needed to reach the end from each index
    vector<int> dp;

    // Helper function to find the minimum number of jumps to reach the end
    int jumpHelper(int ind, vector<int>& nums, int n){
        // Base case: if we're at the last index, we don't need to jump anymore
        if(ind == n-1){
            return 0;
        }

        // If we've already computed the result for this index, return it
        if(dp[ind] != -1){
            return dp[ind];
        }

        int jump = 0, mini = 1e9;

        // Try all possible jumps from the current index
        for(int i=1; i<=nums[ind]; i++){
            // If the jump leads to a valid index
            if(ind + i < n){
                // Recursively find the minimum number of jumps from the new index
                jump = 1 + jumpHelper(ind+i, nums, n);
                // Update the minimum number of jumps
                mini = min(mini, jump);
            }
        }

        // Store the result for this index in dp and return it
        return dp[ind] = mini;
    }

    // Function to find the minimum number of jumps to reach the end of the array
    int jump(vector<int>& nums) {
        // Initialize dp with -1
        dp.resize(nums.size(), -1);
        // Call the helper function for the first index
        return jumpHelper(0, nums, nums.size());
    }
};

```
