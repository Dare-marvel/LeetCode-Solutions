### [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/description/)

## Explanation:
1. **Initialization**: The `low` and `high` counters are initialized to 0. These counters represent the lowest and highest possible number of unmatched left parentheses after processing each character in the string.

2. **Processing the String**: The code iterates over the string `s`. For each character, it checks if it's a left parenthesis `(`, a right parenthesis `)`, or an asterisk `*`.

3. **Left Parenthesis**: If the character is a left parenthesis, both `low` and `high` are incremented by 1. This is because a new left parenthesis has been added, increasing the number of unmatched left parentheses.

4. **Right Parenthesis**: If the character is a right parenthesis, `low` and `high` are decremented by 1. However, `low` is not allowed to go below 0 because it represents the minimum possible number of unmatched left parentheses. This is because a right parenthesis can either match a left parenthesis or an asterisk treated as a left parenthesis.

5. **Asterisk**: If the character is an asterisk, it can be treated as a left parenthesis, a right parenthesis, or an empty string. Therefore, `low` is decremented by 1 (as the asterisk could be a right parenthesis or empty), and `high` is incremented by 1 (as the asterisk could be a left parenthesis).

6. **Checking Validity**: After processing each character, the code checks if `high` is negative. If it is, it means there are more right parentheses than left parentheses and asterisks, so the string is invalid. If `high` is not negative, the code continues to the next character.

7. **Final Check**: After processing all characters, if `low` is 0, it means all left parentheses can be matched with right parentheses or asterisks, so the string is valid. If `low` is not 0, it means there are unmatched left parentheses, so the string is invalid. 

## Time and Space Complexity:
### `Time Complexity`:
The time complexity is O(n), where n is the length of the string. This is because each character in the string is processed once.

### `Space Complexity`:
The space complexity is O(1), as a constant amount of space is used to store the `low` and `high` counters, regardless of the size of the input string.

## Code:
```py
class Solution:
    def checkValidString(self, s: str) -> bool:
        # Track the lowest and highest possible number of open left brackets
        low = high = 0
        for char in s:
            if char == '(':
                # For every open parenthesis, both low and high increase
                low += 1
                high += 1
            elif char == ')':
                # For every closing parenthesis, decrease low (but not below 0) and high
                if low > 0:
                    low -= 1
                high -= 1
            else:  # char == '*'
                # For a star, it can be either an open parenthesis, a closing parenthesis, or a blank
                # So, low can decrease but not below 0 (if star is considered as closing parenthesis or blank)
                if low > 0:
                    low -= 1
                high += 1  # If star is considered as an open parenthesis
                
            # If high becomes negative, it means there are too many closing parentheses
            if high < 0:
                return False

        # If low is 0, all opening parentheses can be matched
        return low == 0
```
