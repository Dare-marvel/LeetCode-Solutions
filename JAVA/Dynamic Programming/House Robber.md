### [House Robber](https://leetcode.com/problems/house-robber/description/)

## Explanation:
This is a Java implementation of a solution to the House Robber problem. The problem statement is: Given an array of non-negative integers representing the amount of money in each house, determine the maximum amount of money you can rob without robbing two adjacent houses.

Here's a detailed explanation of the main logic of the code:
1. The `memo` array is initialized with a length of `nums.length + 1` and filled with `-1` to indicate that no values have been calculated yet.
2. The `rob` function is called with `nums` and `nums.length - 1` as arguments.
3. The `rob` function checks if `i` is less than 0. If it is, it returns 0.
4. The function then checks if the value for the current `i` is already stored in the `memo` array. If it is, it returns that value.
5. Otherwise, the function calculates the maximum amount of money that can be robbed by either robbing the current house and skipping the next one or skipping the current house and moving to the next one.
6. The result is stored in the `memo` array and returned.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this solution is O(n), where n is the length of the input array, since each element in the array is visited once.

### `Space Complexity`:
The space complexity is also O(n), since an additional array of size n+1 is used for memoization.

## Code:
```java
class Solution {
    int[] memo; // Array to store previously computed results
    
    public int rob(int[] nums) {
        memo = new int[nums.length + 1]; // Initialize the memo array with a length of nums.length + 1
        Arrays.fill(memo, -1); // Fill the memo array with -1 to indicate that no results have been computed yet
        return rob(nums, nums.length - 1); // Call the private helper function to start the recursive computation
    }

    private int rob(int[] nums, int i) {
        if (i < 0) {
            return 0; // Base case: If the index becomes less than 0, return 0 since there are no more houses to consider
        }
        if (memo[i] >= 0) {
            return memo[i]; // If the result for the current index is already computed and stored in memo, return it
        }
        
        // Compute the maximum amount of money that can be stolen by considering two choices:
        // 1. Rob the current house and add its value to the result obtained by robbing two houses ago (i - 2)
        // 2. Skip the current house and obtain the result obtained by robbing the previous house (i - 1)
        int result = Math.max(rob(nums, i - 2) + nums[i], rob(nums, i - 1));
        
        memo[i] = result; // Store the computed result in the memo array for future use
        
        return result; // Return the computed result
    }
}
```
