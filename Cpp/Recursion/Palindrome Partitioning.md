### [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/description/)

## Explanation:
The code you've shared is a solution to the problem of partitioning a string into all possible palindromic substrings. Here's a detailed explanation of the logic:

1. **partition Function**: This is the main function that takes a string `s` as input and returns all possible palindromic partitioning of `s`. It initializes an empty result array `res` and an empty path array `path`, and then calls the helper function `func`.

2. **func Function**: This is a recursive helper function that generates all possible palindromic partitions. It takes an index, the string `s`, the current `path`, and the result array `res` as inputs.
    - If the index equals the size of the string, it means we've reached the end of the string, so it adds the current `path` to the `res` and returns.
    - Otherwise, it iterates from the current index to the end of the string. For each character, it checks if the substring from the current index to this character forms a palindrome (using the `isPalindrome` function). If it does, it adds this substring to `path`, recursively calls `func` with the next index, and then removes this substring from `path`.

3. **isPalindrome Function**: This function checks if a given substring (specified by start and end indices) is a palindrome. It does this by comparing characters from both ends of the substring towards the center. If all pairs of characters are equal, it returns true; otherwise, it returns false.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity is **O(n * 2^n)** where 'n' is size of string. This is because in worst case scenario, every prefix could be a palindrome and we have to check all partitions.

### `Space Complexity`:
The space complexity is **O(n^2)** because in worst case (when all partitions are palindrome), we end up storing all partitions in memory.

## Code:
```cpp
// This class Solution contains methods to partition a given string into palindromic substrings.
class Solution {
public:
    // The main function to partition the input string into palindromic substrings.
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res; // Initialize a vector of vectors to store the partitioned palindromic substrings.
        vector<string> path; // Initialize a vector to store the current partition path.
        func(0, s, path, res); // Call the recursive function to find all palindromic partitions.
        return res; // Return the resulting vector of vectors containing palindromic partitions.
    }

    // Recursive function to find palindromic partitions starting from a given index.
    void func(int index, string s, vector<string> &path, vector<vector<string>> &res) {
        // If the current index reaches the end of the string, add the current partition to the result.
        if (index == s.size()) {
            res.push_back(path);
            return;
        }

        // Iterate through the string starting from the current index.
        for (int i = index; i < s.size(); i++) {
            // If the substring from the current index to i is a palindrome, add it to the current partition path.
            if (isPalindrome(s, index, i)) {
                path.push_back(s.substr(index, i + 1 - index));
                // Recur for the next index after i.
                func(i + 1, s, path, res);
                // Backtrack: remove the last added substring to explore other possibilities.
                path.pop_back();
            }
        }
    }

    // Helper function to check if a substring of the input string is a palindrome.
    bool isPalindrome(string s, int start, int end) {
        // Check if the substring from start to end is a palindrome by comparing characters from both ends.
        while (start <= end) {
            if (s[start++] != s[end--]) {
                return false; // If characters don't match, the substring is not a palindrome.
            }
        }
        return true; // If all characters match, the substring is a palindrome.
    }
};
```
