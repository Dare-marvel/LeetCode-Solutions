### [Binary Search](https://leetcode.com/problems/binary-search/)

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
