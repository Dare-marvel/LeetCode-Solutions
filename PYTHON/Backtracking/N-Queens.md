### [N-Queens](https://leetcode.com/problems/n-queens/description/)

### [Articles to refer](https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/)

## Explanation of the code:
* This code is an implementation of the N-Queens problem. The N-Queens problem is the problem of placing n queens on an n x n chessboard such that no two queens attack each other. A solution to this problem exists for all natural numbers n with the exception of n = 2 and n = 3.

* The `IsSafe` function checks if a queen can be placed on `board[row][column]` without being attacked by any other queen already placed on the board. It does this by checking if there is any queen in the same row or in the same diagonal as `board[row][column]`. If there is any such queen, then it returns `False`, otherwise it returns `True`.

* The `solveQueens` function is a recursive function that tries to place queens on the board one by one in different columns. It starts from the leftmost column and moves to the right. For each column, it tries to place a queen in all rows one by one. If a queen can be placed in a row (i.e., the `IsSafe` function returns `True`), then it places the queen on `board[row][column]` and recursively calls itself to place the rest of the queens.

* The base case of the `solveQueens` function is when all queens have been placed on the board (i.e., when `column == n`). In this case, the current configuration of the board is added to the result list.

* The `solveNQueens` function initializes the board with all cells as `"."` and creates an empty result list. It then calls the `solveQueens` function with the initial column as 0 to solve the N-Queens problem. The final result is a list of all possible configurations of the board where n queens can be placed without attacking each other.

* Each configuration in the result list is represented as a list of strings, where each string represents a row of the board. A `"Q"` in a string represents a queen and a `"."` represents an empty cell.


## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is `O(n!)`, where n is the number of queens (or the size of the board). This is because for each queen, there are n possible positions to place it on the board. Since there are n queens, the total number of possibilities is n^n. However, due to the pruning of invalid positions by the IsSafe function, the actual number of possibilities is much smaller than n^n, and is closer to n!.

### `Space Complexity`:
The space complexity of this code is O(n^2), where n is the number of queens (or the size of the board). This is because a 2D array of size n x n is used to represent the board.


## Code:
```py
class Solution:
    # Function to check if a queen can be placed on board[row][column]
    def IsSafe(self,row,column,n,board):
        # Check this row on left side
        for i in range(column):
            if board[row][i] == "Q":
                return False
        # Check upper diagonal on left side
        i,j = row,column
        while(i>=0 and j>=0):
            if(board[i][j] == "Q"):
                return False
            i -= 1
            j -= 1
        # Check lower diagonal on left side
        i,j = row,column
        while(i<n and j>=0):
            if(board[i][j] == "Q"):
                return False
            i += 1
            j -= 1
        return True
    
    # Recursive function to solve N-Queens problem
    def solveQueens(self,column,n,board,result):
        # Base case: If all queens are placed then return True
        if column == n:
            result.append(["".join(i) for i in board])
            return
        
        # Consider this column and try placing this queen in all rows one by one
        for row in range(n):
            if(self.IsSafe(row,column,n,board)):
                # Place this queen in board[row][column]
                board[row][column] = "Q"
                
                # recur to place rest of the queens
                self.solveQueens(column+1,n,board,result)
                
                # If placing queen in board[row][column] doesn't lead to a solution then remove queen from board[row][column]
                board[row][column] = "."
        return
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Initialize the board with all cells as "."
        board = [["." for i in range(n)] for i in range(n)]
        
        result = []
        
        # Call the recursive function to solve N-Queens problem
        self.solveQueens(0,n,board,result)
        
        return result

```
