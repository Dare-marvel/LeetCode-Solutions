### [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/description/)

## Explanation:
This code generates Pascal's Triangle with the given number of rows. Here is the main logic of the code explained in detail:

1. The code creates a new list `pTriangle` to store the entire Pascal's Triangle.
2. The code uses a `for` loop to iterate through each row of the triangle, from the first row to the `numRows-th` row.
3. For each row, the code creates a new list `individualElements` to store the elements of that row.
4. The code uses another `for` loop to iterate through each element of the current row.
5. If the element is the first or last element of the row, the code adds 1 to the `individualElements` list.
6. Otherwise, the code calculates the value of the current element by adding the values of the two elements above it in the previous row. The values of these two elements are obtained by calling the `get()` method on the `pTriangle` list with the appropriate indexes. The sum of these two values is then added to the `individualElements` list.
7. After all elements of the current row have been generated, the code adds the `individualElements` list to the `pTriangle` list.
8. After all rows of the triangle have been generated, the code returns the `pTriangle` list, which contains the entire Pascal's Triangle.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(`numRows^2`) because it uses a nested loop to generate each element of Pascal's Triangle.

### `Space Complexity`:
The space complexity of this code is also O(`numRows^2`) because it stores all elements of Pascal's Triangle in memory.

## Code:
```java
class Solution {
    public List<List<Integer>> generate(int numRows) {
        // Create a new list to store the entire Pascal's Triangle
        List<List<Integer>> pTriangle = new ArrayList<>();
        
        // Loop through each row of the triangle
        for(int i = 1; i <= numRows; i++) {
            // Create a new list to store the elements of the current row
            List<Integer> individualElements = new ArrayList<>(i);
            
            // Loop through each element of the current row
            for(int j = 1; j <= i; j++) {
                // If the element is the first or last element of the row, add 1 to the row
                if(j == 1 || i == j) {
                    individualElements.add(1);
                } else {
                    // Otherwise, add the sum of the two elements above the current element to the row
                    int val1 = pTriangle.get(i - 2).get(j - 2);
                    int val2 = pTriangle.get(i - 2).get(j - 1);
                    individualElements.add(val1 + val2);
                }
            }
            // Add the current row to the triangle
            pTriangle.add(individualElements);
        }
        // Return the entire Pascal's Triangle
        return pTriangle;
    }
}
```
