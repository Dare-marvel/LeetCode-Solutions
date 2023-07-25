### [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Explanation:
This code defines a class `Solution` with a method `lengthOfLongestSubstring` that takes in a string `s` and returns the length of the longest substring without repeating characters. Here's the main logic of the code in points:
1. The code initializes a dictionary `char_dict` to keep track of the last position of each character in the string.
2. The code initializes variables `start` and `max_length` to represent the starting index and maximum length of the current substring without repeating characters, respectively.
3. The code iterates over each character in the string. For each character, it checks if it is already present in `char_dict` and if its last position is within the current substring. If it is, it updates `start` to skip over the repeated character. Otherwise, it updates `max_length` with the maximum length of the current substring.
4. The code updates the last position of the current character in `char_dict`.
5. After all characters have been processed, the final value of `max_length` is returned.

## Time and Space Compexity:
### `Time Complexity`:
The time complexity of this code is O(n), where n is the length of `s`. This is because each character in `s` is processed once.

### `Space Complexity`:
The space complexity of this code is O(k), where k is the size of the character set. This is because memory is allocated for a dictionary that can have at most k entries.

## Code:
```py
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
```
