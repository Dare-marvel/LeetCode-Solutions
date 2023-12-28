### [House Robber II](https://leetcode.com/problems/house-robber-ii/description/)

## Explanation:

## Time and Space Complexity:
### `Time Complexity`:

### `Space Complexity`:

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
