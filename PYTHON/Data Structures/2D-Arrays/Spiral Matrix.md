### [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/description/)

## Explanation:
The `spiralOrder()` function takes in a matrix as input and returns a list of the numbers in the matrix in spiral order. The function works by first initializing two variables, i and j, to the top-left and bottom-right corners of the matrix, respectively. The function then creates an empty list, op, to store the output.

The function then enters a while loop that continues as long as i is less than or equal to j and i is less than the number of rows in the matrix and j is greater than or equal to 0. Inside the while loop, the function performs the following steps:

* Iterates over the top row of the matrix and adds each number to the op list.
* Iterates over the rightmost column of the matrix and adds each number to the op list.
* If there is an inner layer to traverse, the function iterates over the bottom row of the matrix and adds each number to the op list in reverse order.
* If there is an inner layer to traverse, the function iterates over the leftmost column of the matrix and adds each number to the op list in reverse order.

The function then increments i by 1 and decrements j by 1. This ensures that the next iteration of the while loop will start at the next row and column in the matrix.
The function continues iterating through the while loop until i is greater than j. When this happens, the function returns the op list, which contains the numbers in the matrix in spiral order.

Here is an example of how the spiralOrder() function would be used:
* Input:
```
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
* Output:
```
[1, 2, 3, 6, 9, 8, 7, 4, 5]
```

## Time and Space Complexity:
### `Time Complexity`:
The code iterates through each element of the matrix exactly once, visiting each element in a spiral order.
The total number of elements in the matrix is m * n, where m represents the number of rows and n represents the number of columns.
Therefore, the time complexity of the code is `O(m * n)` or `O(N)`, where N is the total number of elements in the matrix.

### `Space Complexity`:
The code uses additional space to store the spiral order elements in the op list.
The size of the op list will be the same as the number of elements in the matrix, which is m * n.
Thus, the space complexity of the code is `O(m * n)` or `O(N)`, where N is the total number of elements in the matrix.

## Code:
```py
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        i, j = 0, len(matrix[0]) - 1
        op = []
        m, n = len(matrix), len(matrix[0])  # Update the dimensions of the matrix

        while i <= j and i < m and j >= 0:  # Fix the while loop condition
            for k in range(i, j + 1):  # Iterate over the top row
                op.append(matrix[i][k])
            for k in range(i + 1, m):  # Iterate over the rightmost column
                op.append(matrix[k][j])
            if i < m - 1 and i < j:  # Check if there is an inner layer to traverse
                for k in range(j - 1, i - 1, -1):  # Iterate over the bottom row
                    op.append(matrix[m - 1][k])
                for k in range(m - 2, i, -1):  # Iterate over the leftmost column
                    op.append(matrix[k][i])
            i += 1
            j -= 1

        return op
```
