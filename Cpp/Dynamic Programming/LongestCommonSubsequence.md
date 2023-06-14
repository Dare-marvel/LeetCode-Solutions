### [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/description/?envType=study-plan-v2&envId=dynamic-programming)

## Method 1 : Tabulated implementation
<hr>

## Explanation:
This code is an implementation of the Longest Common Subsequence (LCS) problem using dynamic programming with an iterative bottom-up approach. Here's a brief explanation of how it works:

- The function takes two input strings `X` and `Y` and calculates their lengths `m` and `n`, respectively.
- A 2D matrix `L` of size `(m+1)*(n+1)` is initialized to store the intermediate results of the dynamic programming algorithm.
- The matrix is filled in a bottom-up manner using two nested loops that iterate over the rows and columns of the matrix.
- If either `i` or `j` is 0, the value of `L[i][j]` is set to 0.
- If the characters at positions `i-1` in `X` and `j-1` in `Y` are equal, the value of `L[i][j]` is set to the value of `L[i-1][j-1] + 1`.
- Otherwise, the value of `L[i][j]` is set to the maximum of `L[i-1][j]` and `L[i][j-1]`.
- The final result, which is the length of the longest common subsequence, is stored in `L[m][n]`.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(m * n), where m and n are the lengths of the two input strings. This is because the algorithm uses two nested loops to fill the 2D matrix `L` of size `(m+1)*(n+1)`.

### `Space Complexity`:
The space complexity of this code is also O(m * n) because it uses a 2D matrix `L` of size `(m+1)*(n+1)` to store the intermediate results of the dynamic programming algorithm.

## Code:
```cpp
class Solution {
public:
    int longestCommonSubsequence(string X, string Y)
    {
        // Get the lengths of the input strings
        int m, n;
        m = X.length();
        n = Y.length();
        
        // Initializing a matrix of size (m+1)*(n+1)
        int L[m + 1][n + 1];
     
        // Following steps build L[m+1][n+1] in bottom-up
        // fashion. Note that L[i][j] contains the length of LCS of
        // X[0..i-1] and Y[0..j-1]
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                // If either string is empty, LCS length is 0
                if (i == 0 || j == 0)
                    L[i][j] = 0;
     
                // If characters at the corresponding positions are equal,
                // increment LCS length by 1
                else if (X[i - 1] == Y[j - 1])
                    L[i][j] = L[i - 1][j - 1] + 1;
     
                // If characters at the corresponding positions are different,
                // take the maximum LCS length from the previous row or column
                else
                    L[i][j] = max(L[i - 1][j], L[i][j - 1]);
            }
        }
     
        // L[m][n] contains the length of LCS for X[0..n-1]
        // and Y[0..m-1]
        return L[m][n];
    }
};
```
