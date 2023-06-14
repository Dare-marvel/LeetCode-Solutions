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
<hr>

## Method 2 : Memoized approach
<hr>

## Explanation:
This code is an implementation of the Longest Common Subsequence (LCS) problem using dynamic programming with memoization. Here's a brief explanation of how it works:

- The `longestCommonSubsequence` function takes two input strings `text1` and `text2` and calculates their lengths `len1` and `len2`, respectively.
- A 2D vector `dp` of size `(len1 + 1) * (len2 + 1)` is initialized with all values set to -1. This vector is used to store the intermediate results of the dynamic programming algorithm.
- The function calls the helper function `lcsHelper` with the input strings, their lengths, and the `dp` vector as arguments.
- The `lcsHelper` function is a recursive function that uses memoization to avoid recomputing subproblems.
- If either `len1` or `len2` is 0, the function returns 0 because there cannot be any common subsequence if one of the input strings is empty.
- If the characters at positions `len1-1` in `text1` and `len2-1` in `text2` are equal, the function recursively calls itself with the strings reduced by one character (`len1-1` and `len2-1`) and increments the result by 1. The result is stored in `dp[len1][len2]`.
- If the result for the subproblem with lengths `len1` and `len2` has already been computed and stored in `dp[len1][len2]`, the stored result is returned immediately without further computation.
- Otherwise, the function recursively calls itself twice with different arguments and returns the maximum of the two results.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(len1 * len2), where len1 and len2 are the lengths of the two input strings. This is because the algorithm uses dynamic programming with memoization to avoid recomputing subproblems, which reduces the number of recursive calls to the lcsHelper function.

### `Space Complexity`:
The space complexity of this code is O(len1 * len2) because it uses a 2D vector dp of size (len1 + 1) * (len2 + 1) to store the intermediate results of the dynamic programming algorithm. Additionally, there is also space overhead due to the recursive calls to the lcsHelper function, which can be significant if the input strings are very long.


## Code:(Exceeding time limit of leetcode)
```cpp
#include<iostream>
#include<vector>
#include<string>
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lcsHelper(string text1, string text2,int len1, int len2,vector<vector<int> >& dp){
        // This condition checks if either m or n is zero, which means one of the input arrays is empty. In that case, there cannot be any common subsequence, so the function returns 0.
        if (len1 == 0 || len2==0)
            return 0;
        
        // This condition checks if the last characters of both arrays (X[m - 1] and Y[n - 1]) are equal. If they are, it means we have found a matching character for the common subsequence. The function recursively calls lcs with the arrays reduced by one character (m - 1 and n - 1) and increments the result by 1. The result is stored in dp[m][n] and also returned.
        if(text1[len1-1] == text2[len2-1])
            return dp[len1][len2] = 1 + lcsHelper(text1,text2,len1-1,len2-1,dp);

        // This condition checks if the result for the subproblem with length m and n has already been computed and stored in dp[m][n]. If it has, the stored result is returned immediately without further computation.
        if(dp[len1][len2] != -1)
            return dp[len1][len2];

        // If none of the above conditions are satisfied, it means the last characters of X and Y are not equal. In this case, the function recursively calls lcs twice
        return dp[len1][len2] = max(lcsHelper(text1,text2,len1,len2-1,dp),lcsHelper(text1,text2,len1-1,len2,dp));

    }
    int longestCommonSubsequence(string text1, string text2) {
        int len1, len2;
        len1 = text1.length();
        len2 = text2.length();

        vector<vector<int> > dp(len1 + 1, vector<int>(len2 + 1, -1));
        return lcsHelper(text1, text2, len1, len2, dp);

    }
};
```
