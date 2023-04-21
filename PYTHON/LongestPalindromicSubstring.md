### [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

## Brief Description:
The given code implements a solution to find the longest palindromic substring in a given string 's'.<br> 
A palindromic substring is a substring that reads the same backward as forward. For example, "racecar" is a palindromic substring.<br>

## Key Insights:
The algorithm used in this solution is based on the idea of expanding around the center. The algorithm works as follows:

Initialize an empty string 'LongSub' to hold the longest palindromic substring found so far.
Determine the length of the input string 's'.
Initialize a variable 'length' to hold the length of the longest palindromic substring found so far.
Loop through each character in the input string 's'.
Check for even length palindromic sequences around the current character. The center of an even length palindromic substring can be two characters. So, we take the current character as the center of the palindromic substring and expand on both sides until the characters do not match. We keep track of the length of the palindromic substring found and update the 'LongSub' variable if the current palindromic substring is longer than the previously found palindromic substring.
Check for odd length palindromic sequences around the current character. The center of an odd length palindromic substring can be one character. So, we take the current character as the center of the palindromic substring and expand on both sides until the characters do not match. We keep track of the length of the palindromic substring found and update the 'LongSub' variable if the current palindromic substring is longer than the previously found palindromic substring.
Return the longest palindromic substring found.

## Time and Space Complexity:

`Time Complexity`:
The time complexity of this algorithm is O(n^2) because we are expanding around the center of each character in the input string 's'. 

`Space Complexity`:
The space complexity of this algorithm is O(1) because we are only using constant space to hold the longest palindromic substring found so far.

## Code:
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Initialize an empty string to hold the longest palindromic substring.
        LongSub = ""
        # Determine the length of the input string.
        n = len(s)
        # Initialize a variable to hold the length of the longest palindromic substring found so far.
        length = 0
        # Loop through each character in the input string.
        for i in range(n):
            # Check for even length palindromic sequences around the current character.
            l, r = i, i + 1
            while (l >= 0 and r < n) and s[l] == s[r]:
                # If a longer palindromic substring is found, update the length and LongSub variables.
                if r - l + 1 > length:
                    length = r - l + 1
                    LongSub = s[l:r + 1]
                # Move to the next pair of characters.
                l, r = l - 1, r + 1
            # Check for odd length palindromic sequences around the current character.
            l, r = i, i
            while (l >= 0 and r < n) and s[l] == s[r]:
                # If a longer palindromic substring is found, update the length and LongSub variables.
                if r - l + 1 > length:
                    length = r - l + 1
                    LongSub = s[l:r + 1]
                # Move to the next pair of characters.
                l, r = l - 1, r + 1
        # Return the longest palindromic substring found.
        return LongSub
```
