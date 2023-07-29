### [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

## Explanation:
This Java program defines a `Solution` class with a `merge` method. The `merge` method takes two sorted integer arrays, `nums1` and `nums2`, and their respective lengths, `m` and `n`, as arguments. It merges the elements of `nums2` into `nums1`, starting from the last element of each array, and overwriting the elements of `nums1` from the end. The result is a sorted array that contains all the elements of both input arrays.

Here is the main logic of the code in detail:

1. The `merge` method initializes three indices: `i`, `j`, and `k`. Index `i` points to the last element of the first `m` elements of `nums1`, index `j` points to the last element of `nums2`, and index `k` points to the last element of `nums1`.
2. The method enters a loop that continues until either index `i` or index `j` becomes negative, indicating that all elements from one of the input arrays have been processed.
3. Inside the loop, the method compares the elements of `nums1` and `nums2` pointed to by indices `i` and `j`, respectively.
4. If the element of `nums1` is greater than the element of `nums2`, the method copies it to the position in `nums1` pointed to by index `k`, decrements index `i`, and decrements index `k`.
5. Otherwise, the method copies the element of `nums2` to the position in `nums1` pointed to by index `k`, decrements index `j`, and decrements index `k`.
6. After exiting the loop, if there are any remaining elements in `nums2`, the method enters another loop to copy them to the remaining positions in `nums1`.
7. Inside this loop, the method copies the element of `nums2` pointed to by index `j` to the position in `nums1` pointed to by index `k`, and decrements both indices.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(m + n), because it processes each element of both input arrays once.

### `Space Complexity`:
The space complexity is O(1), because it uses a constant amount of additional memory (i.e., memory usage does not depend on the size of either input array).

## Code:
```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        // Initialize indices for the last elements of nums1, nums2, and the merged array
        int i = m - 1;
        int j = n - 1;
        int k = m + n - 1;
        
        // Merge elements from nums1 and nums2 into nums1 from the end
        while (i >= 0 && j >= 0) {
            if (nums1[i] > nums2[j]) {
                // If the current element of nums1 is greater, copy it to the merged array
                nums1[k] = nums1[i];
                i--;
            } else {
                // Otherwise, copy the current element of nums2 to the merged array
                nums1[k] = nums2[j];
                j--;
            }
            k--;
        }
        
        // If there are remaining elements in nums2, copy them to nums1
        while (j >= 0) {
            nums1[k] = nums2[j];
            k--;
            j--;
        }
    }
}

```
