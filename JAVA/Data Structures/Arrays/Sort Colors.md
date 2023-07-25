### [Sort Colors](https://leetcode.com/problems/sort-colors/)

## Explanation:
To sort an array of size N in ascending order iterate over the array and compare the current element (key) to its predecessor, if the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

## Time and Space Complexity:
### `Time Complexity`:
O(N^2) 
### `Space Complexity`:
O(1)

## Code:
```java
class Solution {
    public void sortColors(int[] nums) {
        int n = nums.length;
        for (int i = 1; i < n; ++i) {
            int key = nums[i];
            int j = i - 1;
 
            /* Move elements of nums[0..i-1], that are
               greater than key, to one position ahead
               of their current position */
            while (j >= 0 && nums[j] > key) {
                nums[j + 1] = nums[j];
                j = j - 1;
            }
            nums[j + 1] = key;
        }

    }
}
```

<hr>

## Explanation:
This code implements a variation of the Dutch National Flag algorithm to sort an array of integers that only contains 0s, 1s, and 2s. Here is the main logic of the code explained in detail:

1. The code initializes three pointers: `low`, `mid`, and `high`. The `low` pointer points to the first element of the array, the `mid` pointer points to the first element of the array, and the `high` pointer points to the last element of the array.
2. The code uses a `while` loop to iterate through the array using the `mid` pointer. The loop continues until the `mid` pointer is greater than the `high` pointer.
3. If the current element pointed to by the `mid` pointer is 0, the code swaps it with the element pointed to by the `low` pointer, then moves both the `low` and `mid` pointers forward by one position.
4. If the current element pointed to by the `mid` pointer is 1, the code just moves the `mid` pointer forward by one position.
5. If the current element pointed to by the `mid` pointer is 2, the code swaps it with the element pointed to by the `high` pointer, then moves the `high` pointer backward by one position.
6. After all elements of the array have been processed, the array is sorted in ascending order.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(`nums.length`) because it uses a single loop to iterate through all elements of the array.

### `Space Complexity`:
The space complexity of this code is O(1) because it uses a constant amount of extra memory to store temporary variables.

## Code:
### Dutch National Flag Algorithm
```java
class Solution {
    public void sortColors(int[] nums) {
        // Initialize three pointers: low, mid, and high
        int low = 0, mid = 0, high = nums.length - 1;
        
        // Use the mid pointer to iterate through the array
        while (mid <= high) {
            // If the current element is 0, swap it with the element at the low pointer and move both the low and mid pointers forward
            if (nums[mid] == 0) {
                swap(nums, low, mid);
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                // If the current element is 1, just move the mid pointer forward
                mid++;
            } else {
                // If the current element is 2, swap it with the element at the high pointer and move the high pointer backward
                swap(nums, mid, high);
                high--;
            }
        }
    }
    
    // Helper function to swap two elements in an array
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}

```


