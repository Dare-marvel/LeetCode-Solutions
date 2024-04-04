### [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/description/)

## Explanation:
Sure, let's break down the logic of this code:

1. **Initialization**: The code starts by checking if the input list `strs` is empty. If it is, the function returns an empty string as there is no common prefix among zero strings. Then, it initializes `oldL` as a list of characters from the first string in `strs`.

2. **Iteration over the strings**: The code then enters a loop that iterates over the rest of the strings in `strs` (from the second string to the last). For each string, it does the following:

    - **Reset the new prefix**: It initializes `newL` as an empty list. This list will hold the characters of the new common prefix.

    - **Comparison of characters**: It enters another loop where it compares the characters of the current string and `oldL` (the common prefix found so far). The comparison is done character by character, from the first to the last character of the current string.

    - **Character matching**: If the current character of the current string matches the corresponding character in `oldL`, it appends the character to `newL`.

    - **Character mismatch or end of string**: If the characters don't match, or if the end of the current string or `oldL` is reached, it breaks the loop. This is because a mismatch means that the current character cannot be part of the common prefix, and reaching the end of a string means that there are no more characters to compare.

    - **Update the old prefix**: After the loop, it updates `oldL` to be `newL`. This means that the common prefix found so far is updated to be the common prefix found in the current iteration.

3. **Return the common prefix**: After all strings have been processed, the code returns the common prefix found as a string. This is done by joining all characters in `oldL` together.

## Time and Space Complexity:
### `Time Complexity`:
In terms of time complexity, this code has a time complexity of **O(NM)**, where **N** is the number of strings in `strs` and **M** is the maximum length of a string in `strs`. This is because in the worst-case scenario, the code needs to compare all characters of all strings.

### `Space Complexity`:
The space complexity of this code is **O(M)**, where **M** is the length of the first string in `strs`. This is because the code uses two lists, `oldL` and `newL`, to store the characters of the strings, and the maximum number of characters stored is the number of characters in the first string.

## Code:
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Check if the input list of strings is empty. If it is, return an empty string.
        if not strs:
            return ""
        
        # Convert the first string into a list of characters
        oldL = list(strs[0])

        # Iterate through the remaining strings in the list
        for i in range(1,len(strs)):
            newL = []  # Create an empty list to store common characters
            k = 0  # Initialize an index to track characters comparison
            
            # Iterate through characters of oldL and current string simultaneously
            # Break the loop if either oldL or current string runs out or characters don't match
            while k < len(oldL) and k < len(strs[i]) and oldL[k] == strs[i][k]:
                newL.append(oldL[k])  # Append matching character to newL
                k += 1  # Move to the next character
                
            oldL = newL  # Update oldL to store the common characters found so far

        # Join the list of common characters and return as the longest common prefix
        return ''.join(oldL)

```
