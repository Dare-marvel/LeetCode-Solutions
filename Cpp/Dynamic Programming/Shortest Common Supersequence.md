### [Shortest Common Supersequence](https://leetcode.com/problems/shortest-common-supersequence/description/)

## Explanation:
1. **Class Definition**: The code defines a class named `Solution` that contains a public method: `shortestCommonSupersequence`.

2. **Shortest Common Supersequence (SCS)**: The `shortestCommonSupersequence` method calculates the shortest common supersequence of two strings `str1` and `str2`. A supersequence of two strings is a sequence that contains both strings as subsequences.

3. **Dynamic Programming (DP)**: The method uses a dynamic programming approach to solve the problem. A 2D DP table `dp` is created with dimensions `(n+1) x (m+1)`, where `n` and `m` are the sizes of `str1` and `str2` respectively.

4. **Base Cases**: The base cases are initialized by setting the first row and the first column of the DP table to `0`. This represents the scenario where one of the strings is empty.

5. **DP Table Filling**: The DP table is filled by iterating over each character of `str1` and `str2`. If the characters at the current indices of `str1` and `str2` match, the value of the cell in the DP table is set to `1` plus the value of the cell diagonally above and to the left. If the characters don't match, the value of the cell is set to the maximum of the cell directly above or to the left.

6. **Building the SCS**: The SCS is built by starting from the bottom-right cell of the DP table and moving towards the top-left cell. If the characters at the current indices of `str1` and `str2` match, the character is added to the SCS and the indices are decremented. If the characters don't match, the character from the string with the larger DP value is added to the SCS and the corresponding index is decremented. If the DP values are equal, the character from either string can be added to the SCS.

7. **Adding Remaining Characters**: If there are any remaining characters in `str1` or `str2` after reaching the first row or column of the DP table, they are added to the SCS.

8. **Reversing the SCS**: Since the SCS was built in reverse order, it is reversed to get the final SCS.

9. **Return SCS**: The method returns the SCS.

## Time and Space Complexity:
### `Time Complexity`:
In terms of **time complexity**, the method has a time complexity of **O(n*m)**, where `n` and `m` are the sizes of the input strings. This is because each cell in the DP table needs to be filled once.

### `Space Complexity`:
The **space complexity** is also **O(n*m)** due to the space required for the DP table.

## Code:
```cpp
class Solution {
public:
    // Function to find the shortest common supersequence of two strings
    string shortestCommonSupersequence(string str1, string str2) {
        int n = str1.size();
        int m = str2.size();

        // Create a 2D DP table to store the length of the Longest Common Subsequence (LCS)
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, -1)); // Initialize with -1
    
        // Initialize the base cases: LCS with an empty string is 0
        for (int i = 0; i <= n; i++) {
            dp[i][0] = 0;
        }
        for (int i = 0; i <= m; i++) {
            dp[0][i] = 0;
        }

        // Fill in the DP table to calculate the length of LCS
        for (int ind1 = 1; ind1 <= n; ind1++) {
            for (int ind2 = 1; ind2 <= m; ind2++) {
                if (str1[ind1 - 1] == str2[ind2 - 1])
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]; // Characters match, increment LCS length
                else
                    dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1]); // Characters don't match, consider the maximum from left or above
            }
        }

        string ans = "";
        int i = n, j = m;

        // Reconstruct the shortest common supersequence using the LCS information
        while (i > 0 && j > 0) {
            if (str1[i - 1] == str2[j - 1]) {
                ans += str1[i - 1];
                i--, j--;
            } else if (dp[i - 1][j] > dp[i][j - 1]) {
                ans += str1[i - 1];
                i--;
            } else {
                ans += str2[j - 1];
                j--;
            }
        }

        // Add the remaining characters from both strings, if any
        while (i > 0) {
            ans += str1[i - 1];
            i--;
        }
        while (j > 0) {
            ans += str2[j - 1];
            j--;
        }

        // Reverse the constructed supersequence to get the correct order
        reverse(ans.begin(), ans.end());

        return ans;
    }
};
```
