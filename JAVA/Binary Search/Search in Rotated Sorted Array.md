### [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)

## Explanation:
1. `int low = 0, high = nums.length - 1;`: Initialize two pointers, `low` and `high`, which represent the range of the array where the search will be performed.

2. `while (low <= high) {`: Start a binary search loop that continues as long as the `low` pointer is less than or equal to the `high` pointer, indicating that there's a valid search space.

3. `int mid = (low + high) >> 1;`: Calculate the middle index `mid` of the current search space using bitwise right shift (`>> 1`) for integer division.

4. `if (nums[mid] == target) { return mid; }`: Check if the middle element is equal to the `target`. If it is, return the index `mid` as the target has been found.

5. `if (nums[low] <= nums[mid]) {`: Check if the left subarray (from `low` to `mid`) is sorted.

   a. `if (target <= nums[mid] && target >= nums[low]) { high = mid - 1; }`: If the target is within the sorted left subarray, adjust the `high` pointer to `mid - 1`, effectively narrowing the search to the left subarray.

   b. `else { low = mid + 1; }`: If the target is not in the left subarray, adjust the `low` pointer to `mid + 1`, effectively shifting the search to the right subarray.

6. `else {`: If the right subarray (from `mid` to `high`) is sorted.

   a. `if (target <= nums[high] && target >= nums[mid]) { low = mid + 1; }`: If the target is within the sorted right subarray, adjust the `low` pointer to `mid + 1`, narrowing the search to the right subarray.

   b. `else { high = mid - 1; }`: If the target is not in the right subarray, adjust the `high` pointer to `mid - 1`, shifting the search to the left subarray.

7. The loop continues until `low` is greater than `high`, indicating that the search space is exhausted, or the target is found and its index is returned.

8. If the target is not found in the array, the function returns `-1`.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(log N), where N is the number of elements in the `nums` array. This is because the binary search algorithm efficiently reduces the search space by half in each iteration.

### `Space Complexity`:
The space complexity is O(1), as the code only uses a constant amount of additional space for the `low`, `high`, and `mid` variables, regardless of the size of the input array.

## Code:
```java
class Solution {
    public int search(int[] nums, int target) {
        // Initialize low and high pointers for binary search.
        int low = 0, high = nums.length - 1;

        // Perform binary search until the low pointer is less than or equal to the high pointer.
        while (low <= high) {
            // Calculate the middle index.
            int mid = (low + high) >> 1;

            // If the middle element is equal to the target, return its index as it's found.
            if (nums[mid] == target) {
                return mid;
            }

            // Check if the left subarray (low to mid) is sorted.
            if (nums[low] <= nums[mid]) {
                // If target is within the sorted left subarray, adjust the high pointer to mid - 1.
                if (target <= nums[mid] && target >= nums[low]) {
                    high = mid - 1;
                } else {
                    // If target is not in the left subarray, adjust the low pointer to mid + 1.
                    low = mid + 1;
                }
            } else {
                // If the right subarray (mid to high) is sorted.
                // Check if the target is within the sorted right subarray.
                if (target <= nums[high] && target >= nums[mid]) {
                    // Adjust the low pointer to mid + 1.
                    low = mid + 1;
                } else {
                    // If target is not in the right subarray, adjust the high pointer to mid - 1.
                    high = mid - 1;
                }
            }
        }

        // If the target is not found in the array, return -1.
        return -1;
    }
}
```
