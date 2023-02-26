# Link to the problem : https://leetcode.com/problems/longest-palindromic-substring/

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
