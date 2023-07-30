### [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

## Explanation:
Sure! Here's a detailed explanation of the main logic of the code, broken down into points:

1. The code takes as input a sorted array of integers `nums` and the goal is to remove duplicate elements from the array in-place and return the new length of the array.
2. The code first checks if the input array is empty. If it is, it returns 0, since there are no elements in the array.
3. The code then initializes two pointers, `i` and `j`, to 0 and 1 respectively. These pointers are used to keep track of the unique elements in the array.
4. The code enters a for loop that iterates from `j = 1` to `j = nums.length - 1`. In each iteration of the loop, the code checks if `nums[j]` is different from `nums[i]`.
5. If `nums[j]` is different from `nums[i]`, this means that a new unique element has been found. In this case, the code increments `i` to move it to the next position in the array and sets `nums[i]` to `nums[j]`. This moves the new unique element to its correct position in the front of the array.
6. If `nums[j]` is equal to `nums[i]`, this means that a duplicate element has been found. In this case, the code doesn't do anything and simply moves on to the next iteration of the loop.
7. After all iterations of the for loop are complete, all unique elements have been moved to the front of the array and `i` points to the last unique element in the array.
8. The code then returns `i + 1`, which is the new length of the array after removing duplicates.

## Dry Run:
Let's do a dry run of the code with a larger example input array: `nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]`.

Here's a step-by-step explanation of how the code processes this input:

1. First, the code checks if the input array is empty. If it is, it returns 0. In our example, the input array is not empty, so this check is skipped.
2. The code then initializes two pointers, `i` and `j`, to 0 and 1 respectively. These pointers are used to keep track of the unique elements in the array.
3. The code enters a for loop that iterates from `j = 1` to `j = nums.length - 1`. In each iteration of the loop, the code checks if `nums[j]` is different from `nums[i]`.
4. In the first iteration of the loop, `j = 1`, so `nums[j]` is 0 and `nums[i]` is also 0. Since these values are equal, the code doesn't do anything and moves on to the next iteration of the loop.
5. In the second iteration of the loop, `j = 2`, so `nums[j]` is 1 and `nums[i]` is still 0. Since these values are different, the code increments `i` to 1 and sets `nums[i]` to `nums[j]`, which is 1. At this point, the array `nums` looks like this: `[0, 1, 1, 1, 1, 2, 2, 3, 3, 4]`.
6. The code continues iterating through the for loop in this manner. In each iteration where `nums[j]` is different from `nums[i]`, it increments `i` and sets `nums[i]` to `nums[j]`. This moves all unique elements to the front of the array.
7. After all iterations of the for loop are complete, the final value of `i` is 4 and the array `nums` looks like this: `[0, 1, 2, 3, 4, 2, 2, 3, 3, 4]`.
8. The code then returns `i + 1`, which is 5.

The final result is 5, which is the new length of the array after removing duplicates. The unique elements of the array are `[0, 1, 2, 3, 4]`, which are stored at the front of the input array.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(n), where n is the length of the input array. This is because the code iterates through the entire input array once using a for loop.

### `Space Complexity`:
The space complexity of this code is O(1), since it operates in-place on the input array and doesn't require any additional memory to be allocated.

## Code:
```java
class Solution {
    public int removeDuplicates(int[] nums) {
        // Check if the input array is empty
        if (nums.length == 0) return 0;
        
        // Initialize two pointers, i and j
        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            // If nums[j] is different from nums[i], increment i and set nums[i] to nums[j]
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }
        // Return the new length of the array after removing duplicates
        return i + 1;
    }
}
```
