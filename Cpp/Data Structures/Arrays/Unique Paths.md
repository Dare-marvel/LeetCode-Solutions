### [Unique Paths](https://leetcode.com/problems/unique-paths/description/)

## Explanation:
1. **Variables**: The code uses several variables:
    - `m` and `n` are the dimensions of the grid.
    - `N` is the total number of steps you need to take to reach the destination.
    - `r` is the number of down steps you need to take.
    - `res` is used to calculate the result.

2. **Calculation**: The code calculates the number of unique paths using a mathematical formula which is a combination formula: `C(N, r)`. This formula calculates the number of ways you can choose `r` elements from a set of `N` elements.

3. **For Loop**: The for loop calculates the combination `C(N, r)` using a product formula. It multiplies `res` with `(N - r + i)/i`.

4. **Return Statement**: Finally, it returns the result as an integer.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is **O(min(m, n))** because it runs a loop min(m, n) times.

### `Space Complexity`:
The space complexity of this code is **O(1)** because it uses a constant amount of space to store variables and does not use any data structures like arrays or matrices.

## Code:
```cpp
class Solution {
public:
    // Function to calculate the number of unique paths from top-left to bottom-right in a grid of size m x n.
    int uniquePaths(int m, int n) {
        // Total number of steps required to reach the destination (bottom-right corner).
        int N  = n + m - 2;
        // Number of steps required to move vertically.
        int r = m - 1;
        // Variable to store the result. Initialized to 1 as there is at least one path.
        double res = 1;

        // Loop to calculate N! / (r! * (N-r)!) where N! represents N factorial.
        for(int i = 1; i <= r; i++){
            // Using the formula: n! / (r! * (n-r)!)
            // Note: Calculating the result as a double to handle large numbers without overflowing.
            res = res * (N - r + i) / i;
        }

        // Casting the result to an integer and returning it.
        return int(res);
    }
};
```
