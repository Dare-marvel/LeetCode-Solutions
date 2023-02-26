# Link to the problem : https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize a dictionary to keep track of the last position of each character
        char_dict = {}
        # Initialize the starting index and maximum length of the current substring
        start, max_length = 0, 0
        # Iterate over each character in the string
        for i in range(len(s)):
            # If the character is already in the dictionary and its last position is within the current substring,
            # update the starting index to skip over the repeated character
            if s[i] in char_dict and char_dict[s[i]] >= start:
                start = char_dict[s[i]] + 1
            # Otherwise, update the maximum length of the current substring
            max_length = max(max_length, i - start + 1)
            # Update the last position of the current character in the dictionary
            char_dict[s[i]] = i
        # Return the maximum length of any substring without repeating characters
        return max_length
