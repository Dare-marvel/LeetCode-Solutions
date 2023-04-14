### [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/description/) 

## Intuition
The rowChecker method checks each row in the board by iterating through each element in each row, counting the frequency of each digit, and returning False if any digit appears more than once in a row.

The colChecker method checks each column in the board by iterating through each element in each column, counting the frequency of each digit, and returning False if any digit appears more than once in a column.

The boxChecker method checks a 3x3 sub-grid in the board by iterating through each element in the sub-grid, counting the frequency of each digit, and returning False if any digit appears more than once in the sub-grid.

## Approach
This approach can be named as the "Validity Checking Approach" for solving Sudoku puzzles. It checks the validity of a given Sudoku board by verifying if each row, column, and 3x3 sub-grid contains no duplicate digits from 1-9.


## Complexity
- `Time complexity`:
The time complexity of the approach is `O(N^2)`, where N is the size of the input board. This is because the solution iterates over each cell in the board twice - once for row and column checks, and once for sub-grid checks

- `Space complexity`:
The space complexity of the approach is `O(N)`, where N is the size of the input board. This is because the solution uses a dictionary to store the frequency of each digit in each sub-grid.

## Code
```python
from typing import List

class Solution:
    def rowChecker(self, board: List[List[str]]) -> bool:
        """
        Check if each row in the board contains no duplicate digits from 1-9.
        Returns True if all rows are valid, False otherwise.
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                # If the current element is a digit and appears more than once in its row, the row is invalid
                if board[i][j].isnumeric() and board[i].count(board[i][j]) > 1:
                    return False
        return True
    
    def colChecker(self, board: List[List[str]]) -> bool:
        """
        Check if each column in the board contains no duplicate digits from 1-9.
        Returns True if all columns are valid, False otherwise.
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                # If the current element is a digit and appears more than once in its column, the column is invalid
                if board[j][i].isnumeric() and [board[k][i] for k in range(len(board))].count(board[j][i]) > 1:
                    return False    
        return True
    
    def boxChecker(self, board: List[List[str]], row: int, col: int) -> bool:
        """
        Check if a 3x3 box in the board contains no duplicate digits from 1-9.
        Returns True if the box is valid, False otherwise.
        """
        freq_dict = {}  # dictionary to count the frequency of each digit in the box
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                # If the current element is a digit, increment its count in the freq_dict
                if board[i][j].isnumeric():
                    freq_dict[board[i][j]] = freq_dict.get(board[i][j], 0) + 1
        
        # If any digit appears more than once in the box, the box is invalid
        for val in freq_dict.values():
            if val > 1:
                return False
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Check if a 9x9 Sudoku board is valid.
        Returns True if the board is valid, False otherwise.
        """
        # Check each 3x3 box in the board for validity
        for row in range(0, len(board), 3):
            for col in range(0, len(board[row]), 3):
                if not self.boxChecker(board, row, col):
                    return False
        
        # Check each row and column in the board for validity
        return self.rowChecker(board) and self.colChecker(board)
```
