### [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/description/)

## Explanation:
1. **Class Definition**: The code defines a class named `Solution`. This class encapsulates the methods needed to solve a Sudoku puzzle.

2. **solveSudoku Method**: This is the public method that is called to solve the Sudoku. It takes a 2D vector (the Sudoku board) as input and calls the `solve` method on it.

3. **solve Method**: This method uses a recursive approach (backtracking) to solve the Sudoku. It iterates over each cell in the Sudoku board. If it finds an empty cell (denoted by '.'), it tries to fill it with a number from '1' to '9'. For each number, it checks if placing that number in the current empty cell is valid using the `isValid` method.

    - **Backtracking**: If placing a certain number in the current empty cell is valid, the `solve` method then recursively calls itself. If the recursive call returns true, it means the Sudoku is solved and it returns true. If not, it means the number it placed in the current empty cell leads to an unsolvable Sudoku, so it changes the cell back to empty and tries the next number. If it has tried all numbers from '1' to '9' and none of them leads to a solution, it returns false to backtrack to the previous empty cell.

4. **isValid Method**: This method checks if we can place a number in a certain cell. It checks the current row, column, and the 3x3 box the cell belongs to, to see if the number already exists in any of these. If it does, it returns false; otherwise, it returns true.

    - **Row and Column Check**: The method iterates over all the cells in the given row and column. If it finds the number in any of these cells, it returns false.

    - **3x3 Box Check**: Sudoku has 9 3x3 boxes. The method identifies which 3x3 box the current cell belongs to, and checks all the cells in this box. If it finds the number in any of these cells, it returns false.

## Time and Space Complexity:
### `Time Complexity`: The time complexity is $$O(9^{m})$$, where $$m$$ is the number of empty cells in the Sudoku. In the worst case, we have to try 9 numbers for each empty cell.

### `Space Complexity`: The space complexity is $$O(m)$$ because in the worst case, if we can't find a valid number for a cell, we will go back (backtrack) and try the next number. This requires system stack space and in the worst case it will be the number of empty cells $$m$$. 

## Code:
```cpp
class Solution {
public:
    // Public function to solve the Sudoku puzzle
    void solveSudoku(vector<vector<char>>& board) {
        // Call the recursive solve function to fill in the Sudoku puzzle
        solve(board);
    }

    // Recursive function to solve the Sudoku puzzle
    bool solve(vector<vector<char>> &board){
        // Iterate through each cell in the Sudoku board
        for(int i=0; i<board.size(); i++){
            for(int j=0; j<board[0].size(); j++){
                // Check if the cell is empty
                if(board[i][j] == '.' ){
                    // Try placing digits '1' to '9' in the empty cell
                    for(char c='1'; c<='9'; c++){
                        // Check if placing the current digit is valid
                        if(isValid(board, i, j, c) == true){
                            // Place the current digit in the cell
                            board[i][j] = c;
                            
                            // Recursively try to solve the updated board
                            if(solve(board) == true){
                                return true;  // If a solution is found, return true
                            }
                            else{
                                // If placing the current digit does not lead to a solution, backtrack
                                board[i][j] = '.';  // Reset the cell
                            }
                        }
                    }
                    return false;  // If no valid digit can be placed in the cell, backtrack
                }
            }
        }
        return true;  // If the entire board is filled, return true
    }

    // Function to check if placing a digit at a specific position is valid
    bool isValid(vector<vector<char>> &board, int row, int col, char c){
        // Check the current row and column for the digit
        for(int i=0; i<9; i++){
            if(board[i][col] == c || board[row][i] == c){
                return false;  // If the digit is found in the row or column, it's not valid
            }
        }
        
        // Check the 3x3 subgrid for the digit
        for(int i=0; i<9; i++){
            if(board[3*(row/3) + i/3][3*(col/3) + i%3] == c){
                return false;  // If the digit is found in the subgrid, it's not valid
            }
        }
        return true;  // If the digit can be placed at the given position, it's valid
    }
};

```
