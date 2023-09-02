### [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/description/)

## Explanation:
This code is a solution to the problem of trapping rainwater. The main logic of the code is as follows:
1. The code uses two pointers, `left` and `right`, to traverse the array from both ends towards the center.
2. The variable `res` is used to store the final result, which is the total amount of trapped water.
3. The variables `leftmax` and `rightmax` are used to keep track of the maximum height of the bars on the left and right sides, respectively.
4. The code uses a while loop to iterate until the two pointers meet.
5. Inside the loop, the code checks if the height of the bar at the left pointer is less than or equal to the height of the bar at the right pointer.
6. If this condition is true, then the code checks if the height of the bar at the left pointer is greater than or equal to `leftmax`. If it is, then `leftmax` is updated to be equal to the height of this bar. Otherwise, the difference between `leftmax` and the height of this bar is added to `res`.
7. The left pointer is then incremented.
8. If the condition in step 5 is false, then similar steps are performed for the right pointer, with `rightmax` being updated instead of `leftmax`.
9. The right pointer is then decremented.
10. This process continues until the two pointers meet, at which point the final result is stored in `res`.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is **O(n)**, where **n** is the length of the input array, since each element in the array is visited once.

### `Space Complexity`:
The space complexity is **O(1)**, since only a constant amount of extra space is used.

## Code:
```java
class Solution {
    public int trap(int[] height) {
        // Initialize two pointers, 'left' and 'right,' to the start and end of the height array.
        int left = 0, right = height.length - 1;

        // Initialize a variable 'res' to store the result (total trapped water).
        int res = 0;

        // Initialize variables 'leftmax' and 'rightmax' to track the maximum height encountered from the left and right sides.
        int leftmax = 0, rightmax = 0;

        // Iterate through the array while the 'left' pointer is less than or equal to the 'right' pointer.
        while (left <= right) {
            // If the height at the 'left' pointer is less than or equal to the height at the 'right' pointer.
            if (height[left] <= height[right]) {
                // Check if the current height is greater than or equal to 'leftmax.'
                if (height[left] >= leftmax)
                    leftmax = height[left]; // Update 'leftmax' if the current height is greater.
                else
                    res += leftmax - height[left]; // Calculate and add trapped water to 'res.'

                // Move the 'left' pointer to the right.
                left++;
            } else { // If the height at the 'right' pointer is greater than the height at the 'left' pointer.
                // Check if the current height is greater than or equal to 'rightmax.'
                if (height[right] >= rightmax)
                    rightmax = height[right]; // Update 'rightmax' if the current height is greater.
                else
                    res += rightmax - height[right]; // Calculate and add trapped water to 'res.'

                // Move the 'right' pointer to the left.
                right--;
            }
        }

        // Return the total trapped water.
        return res;
    }
}
```
