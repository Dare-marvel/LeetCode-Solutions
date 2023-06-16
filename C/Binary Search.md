### [Binary Search](https://leetcode.com/problems/binary-search/)

## Explanation:
This code defines a function `binarySearch` that takes in an array `nums` of `n` integers and an integer `key` and returns the index of `key` in the array if it is present, or -1 if it is not present. Here's the main logic of the code in points:
1. The code initializes variables `st`, `end`, and `mid` to represent the start, end, and middle indices of the search range.
2. The code enters a loop that continues until the start index is greater than the end index.
3. In each iteration of the loop, the code checks if the element at the middle index is equal to the key. If it is, the middle index is returned.
4. If the element at the middle index is greater than the key, the end index is updated to be one less than the middle index.
5. If the element at the middle index is less than the key, the start index is updated to be one more than the middle index.
6. The middle index is recalculated as the average of the start and end indices.
7. If the loop exits without finding the key, -1 is returned to indicate that the key is not present in the array.

## Time and Space Compexity:
### `Time Complexity`:
The time complexity of this code is O(log(n)), where n is the number of elements in `nums`. This is because in each iteration of the loop, the search range is halved.

### `Space Complexity`:
The space complexity of this code is O(1), because only a constant amount of additional memory is used.

## Code :
```c
int binarySearch(int nums[], int n, int key) {
    int st = 0, end = n - 1, mid = (st + end) / 2;
    while (st <= end) {
        if (nums[mid] == key) {
            return mid;
        }
        else if (nums[mid] > key) {
            end = mid - 1;
        }
        else {
            st = mid + 1;
        }
        mid = (st + end) / 2;
    }
    return -1;
}
```
