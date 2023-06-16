### [ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)

## Explanation of the code:
The code takes two inputs: a string and an integer. The string is the input to be converted, and the integer is the number of rows in the output.
The code first checks if the number of rows is 1. If it is, the code simply returns the input string.
Otherwise, the code initializes a few variables:
* res: This is the variable that will store the output string.
* length: This is the length of the input string.
* step: This is the step size for the zigzag pattern.
The code then iterates over each row of the zigzag pattern. For each row, the code iterates over each character in the row and adds the character to the output string.
If the current row is not the first or last row, the code also adds the corresponding character from the next row to the output string.
The code then returns the output string.

## Time and Space Complexity
### `Time Complexity`:
The time complexity of the convert method is O(n), where n is the length of the input string s.<br>  
This is because the method iterates over each character in the input string once.

### `Space Complexity`:
The space complexity of the convert method is also O(n), where n is the length of the input string s.<br> 
This is because the method creates a result string res that has the same length as the input string.

## Code:
```py
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if numRows is 1, the result is the input string
        if numRows == 1:
            return s
        
        # Initialize variables
        res = ""         # result string
        length = len(s)  # length of input string
        step = 2 * numRows - 2  # step size for zigzag pattern
        
        # Iterate over each row of the zigzag pattern
        for i in range(numRows):
            # Iterate over each character in the current row
            for j in range(i, length, step):
                # Add the character at index j to the result string
                res += s[j]
                # If the current row is not the first or last row,
                # and there is a corresponding character in the next row,
                # add that character to the result string as well
                if i != 0 and i != numRows - 1 and j + step - 2 * i < length:
                    res += s[j + step - 2 * i]
        
        # Return the result string
        return res
```
