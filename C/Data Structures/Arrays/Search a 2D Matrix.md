### [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/description/)

## Explanation:
This is a C++ function that searches for a target value in a 2D matrix using binary search on each row. Here is the main logic of the code explained in detail:

1. The function performs a row-wise search on the input matrix. For each row, it uses binary search to find the target value.
2. Binary search works by repeatedly dividing the search interval in half. If the target value is less than the value in the middle of the interval, then the search continues in the left half of the interval. Otherwise, the search continues in the right half of the interval.
3. If the target value is found in any row, the function returns `true`. If the target value is not found in any row, the function returns `false`.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this algorithm is O(m log n), where m is the number of rows and n is the number of columns in the matrix. This is because binary search has a time complexity of O(log n) and it is performed m times, once for each row.

### `Space Complexity`:
The space complexity of this algorithm is O(1), as it only uses a few local variables to keep track of the current state of the algorithm and does not allocate any additional memory.

## Code:
```c
bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    // Row-wise search
    for (int i = 0; i < matrixSize; i++) {
        // Initialize binary search variables
        int low = 0, high = *matrixColSize - 1;
        int mid;

        // Binary search on current row
        while (low <= high) {
            // Calculate mid index
            mid = low + (high - low) / 2;
            
            // Check if target value is found
            if (matrix[i][mid] == target) {
                return true;
            } else if (matrix[i][mid] > target) {
                // Target value is in left half
                high = mid - 1;
            } else {
                // Target value is in right half
                low = mid + 1;
            }
        }
    }
    
    // Element not found
    return false;
}
```
