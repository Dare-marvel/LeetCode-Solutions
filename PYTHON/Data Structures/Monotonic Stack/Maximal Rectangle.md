### [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/description/)

## Approach and Intuition:

**Approach:**

- **Problem Statement**: The problem asks us to find the maximum area rectangle that can be formed in a binary matrix where each cell represents whether it is filled with '1' or not.
  
- **Approach Overview**: This problem can be solved using the concept of histograms. We can convert each row of the matrix into a histogram, where each bar's height represents the number of consecutive '1's encountered so far in that column.
  
- **Histogram Method**: We iterate through each row of the matrix and update the histogram heights accordingly. Then, we use a stack to find the maximum area rectangle that can be formed based on the heights of the histogram bars.

**Intuition:**

1. **Initialization**: Initialize variables for rows, columns, histogram heights, and maximum area.
  
2. **Iterating Through Rows**: We iterate through each row of the matrix.
   
3. **Updating Histogram Heights**: For each row, we update the heights of histogram bars based on the consecutive '1's encountered in that row.
   
4. **Calculating Maximum Area**: After updating histogram heights, we use a stack to find the maximum area rectangle. We iterate through the histogram heights and maintain a stack of indices. At each step, we compare the current height with the height at the top of the stack. If the current height is less than the height at the top of the stack, we pop the top element from the stack and calculate the area of the rectangle using the popped height. We continue this process until the current height is greater than or equal to the height at the top of the stack. While popping elements, we calculate the width of the rectangle as the difference between the current index and the index at the top of the stack minus one. We update the maximum area if the calculated area is greater than the current maximum area.

5. **Returning Maximum Area**: Finally, we return the maximum area calculated.

## Time and Space Complexity:
### `Time Complexity`:
- The time complexity of the algorithm is O(rows * cols), where rows is the number of rows in the matrix and cols is the number of columns. This is because we iterate through each cell of the matrix once to update the histogram heights.
 
### `Space Complexity`:
- The space complexity of the algorithm is O(cols), where cols is the number of columns in the matrix. This is because we maintain a histogram of heights with one extra element for easier calculation, which requires space proportional to the number of columns.
 
## Code:
```python
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Check if the matrix is empty
        if not matrix:
            return 0
        
        # Get the number of rows and columns in the matrix
        rows, cols = len(matrix), len(matrix[0])
        
        # Initialize a list to store the heights of the histogram bars,
        # initialized with zeros, and add an extra element for easier calculation
        heights = [0] * (cols + 1)
        
        # Initialize the variable to store the maximum area
        max_area = 0
        
        # Iterate through each row in the matrix
        for row in matrix:
            # Update the heights of histogram bars based on the current row
            for i in range(cols):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            
            # Calculate the maximum area using the histogram method
            stack = []  # Initialize an empty stack to store indices
            for i in range(len(heights)):
                # While the stack is not empty and the current height is less than the height at the top of the stack
                while stack and heights[i] < heights[stack[-1]]:
                    # Pop the index from the stack and calculate the area of the rectangle
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    # Update the maximum area if the calculated area is greater
                    max_area = max(max_area, h * w)
                # Append the current index to the stack
                stack.append(i)
        
        # Return the maximum area
        return max_area 
```
