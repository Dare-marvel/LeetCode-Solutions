#Link to the problem : https://leetcode.com/problems/zigzag-conversion/

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
