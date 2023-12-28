### [House Robber II](https://leetcode.com/problems/house-robber-ii/description/)

## Explanation:
This Java code is a solution to the problem of finding the maximum amount of money a robber can rob from houses arranged in a circle, where adjacent houses have security systems connected and cannot be robbed together. The solution uses dynamic programming to optimize the process. Here's a detailed explanation:

1. **Class and Function Definitions**: The code begins with the definition of a `class` named `Solution`. Inside this class, two `public` functions named `helper` and `rob` are defined.

2. **Helper Function**: The `helper` function takes an array of integers `nums` and calculates the maximum amount of money that can be robbed from a linear arrangement of houses. It uses two variables, `prevMax` and `currMax`, to keep track of the maximum amount of money that can be robbed up to the previous house and the current house, respectively. For each house in `nums`, it calculates the maximum of `prevMax + num` and `currMax`, where `num` is the amount of money in the current house. This is because the robber can either rob the current house and the houses up to two houses before, or not rob the current house and keep the maximum amount robbed up to the previous house. The function returns `currMax`, which is the maximum amount that can be robbed from all the houses.

3. **Rob Function**: The `rob` function takes an array of integers `nums`, which represents the amount of money in each house arranged in a circle, and calculates the maximum amount of money that can be robbed. It first checks if there is only one house, in which case it returns the amount in that house. If there are more than one houses, it creates two new arrays, `temp1` and `temp2`, and copies the amounts from `nums` to `temp1` and `temp2` such that `temp1` excludes the last house and `temp2` excludes the first house. This is because the first and last houses cannot be robbed together as they are adjacent in the circular arrangement. It then returns the maximum of the maximum amounts that can be robbed from `temp1` and `temp2`, which is calculated using the `helper` function.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of the code is **O(n)**, because each house is visited once, and the maximum amount that can be robbed from each house is calculated once.

### `Space Complexity`:
The space complexity is also **O(n)**, because two new arrays of size `n` are used to store the amounts in the houses.

## Code:
```java
class Solution {
    // Helper function to calculate the maximum sum of non-adjacent elements
    public int helper(int[] nums) {
        int prevMax = 0; // Variable to store the maximum sum excluding the current element
        int currMax = 0; // Variable to store the maximum sum including the current element

        // Iterate through each element in the array
        for (int num : nums) {
            int temp = currMax; // Temporary variable to store the currentMax before updating it
            currMax = Math.max(prevMax + num, currMax); // Update currMax based on the current element
            prevMax = temp; // Update prevMax for the next iteration
        }

        return currMax; // Return the final maximum sum
    }

    // Function to calculate the maximum amount of money that can be robbed
    public int rob(int[] nums) {
        int n = nums.length;
        int[] temp1 = new int[n]; // Temporary array to store the input array, excluding the last element
        int[] temp2 = new int[n]; // Temporary array to store the input array, excluding the first element

        if (n == 1)
            return nums[0]; // If there is only one element, return that element

        // Populate temp1 and temp2 arrays
        for (int i = 0; i < n; i++) {
            if (i != 0)
                temp1[i] = nums[i]; // Exclude the first element
            if (i != n - 1)
                temp2[i] = nums[i]; // Exclude the last element
        }

        // Return the maximum amount of money that can be robbed by considering both cases
        return Math.max(helper(temp1), helper(temp2));
    }
}

```
