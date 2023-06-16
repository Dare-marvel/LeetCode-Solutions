### [Valid Number](https://leetcode.com/problems/valid-number/description/)

## Explanation of the code:
This solution uses a deterministic approach to check if a given string is a valid number. Here's an explanation of how it works:

1. The function starts by stripping any leading or trailing white spaces from the input string `s`.
2. It then checks if the resulting string is empty. If it is, the function returns `False` since an empty string is not a valid number.
3. The function then initializes three boolean variables: `seenNum`, `seenDot`, and `seenE`. These variables are used to keep track of whether the function has seen a digit, a dot, or an 'e'/'E' character while iterating through the string.
4. The function then enters a loop that iterates through each character in the string.
5. For each character, the function checks if it is a dot ('.'). If it is, the function checks if it has already seen a dot or an 'e'/'E' character. If it has, the function returns `False` since a valid number can only have one dot and it cannot appear after an 'e'/'E' character. Otherwise, the function sets `seenDot` to `True`.
6. If the character is not a dot, the function checks if it is an 'e' or 'E'. If it is, the function checks if it has already seen an 'e'/'E' character or if it has not seen any digits yet. If either of these conditions is true, the function returns `False` since a valid number can only have one 'e'/'E' character and it must appear after at least one digit. Otherwise, the function sets `seenE` to `True` and `seenNum` to `False`.
7. If the character is not an 'e' or 'E', the function checks if it is a '+' or '-'. If it is, the function checks if it appears at the beginning of the string or immediately after an 'e'/'E' character. If neither of these conditions is true, the function returns `False` since a '+' or '-' can only appear at these positions in a valid number. The function then sets `seenNum` to `False`.
8. If the character is none of these special characters, the function checks if it is a digit. If it is not, the function returns `False` since all other characters are invalid in a valid number. Otherwise, the function sets `seenNum` to `True`.
9. After iterating through all characters in the string, the function checks if it has seen at least one digit by checking the value of `seenNum`. If it has not seen any digits, the function returns `False`. Otherwise, it returns `True`.

I hope this explanation helps you understand how this solution works!

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(n), where n is the length of the input string s. This is because the code iterates through each character in the string once, performing a constant amount of work for each character.

### `Space Complexity`:
The space complexity of this code is O(1), because it uses a constant amount of extra space to store the boolean variables seenNum, seenDot, and seenE, regardless of the size of the input string.

## Code:
```py
class Solution:
    def isNumber(self, s: str) -> bool:
        # Strip leading and trailing white spaces
        s = s.strip()
        
        # If the resulting string is empty, return False
        if not s:
            return False

        # Initialize variables to keep track of whether we have seen a digit, a dot, or an 'e'/'E' character
        seenNum = False
        seenDot = False
        seenE = False

        # Iterate through each character in the string
        for i, c in enumerate(s):
            # If the character is a dot
            if c == '.':
                # If we have already seen a dot or an 'e'/'E' character, return False
                if seenDot or seenE:
                    return False
                # Set seenDot to True
                seenDot = True
            # If the character is an 'e' or 'E'
            elif c == 'e' or c == 'E':
                # If we have already seen an 'e'/'E' character or have not seen any digits yet, return False
                if seenE or not seenNum:
                    return False
                # Set seenE to True and seenNum to False
                seenE = True
                seenNum = False
            # If the character is a '+' or '-'
            elif c in '+-':
                # If it does not appear at the beginning of the string or immediately after an 'e'/'E' character, return False
                if i > 0 and s[i - 1] not in 'eE':
                    return False
                # Set seenNum to False
                seenNum = False
            # If the character is none of these special characters
            else:
                # If it is not a digit, return False
                if not c.isdigit():
                    return False
                # Set seenNum to True
                seenNum = True

        # After iterating through all characters in the string, check if we have seen at least one digit. If not, return False. Otherwise, return True.
        return seenNum


```
