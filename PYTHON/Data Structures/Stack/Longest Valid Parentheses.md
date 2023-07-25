### [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/description/)

## Explanation:
- The algorithm uses a stack to keep track of the indices of the parentheses in the string.
- The `longestValidParentheses` function is a method of the `Solution` class. It takes as input a string `S` and returns an integer representing the length of the longest valid parentheses substring.
- The function initializes a stack with `-1` and a variable `ans` to store the maximum length of a valid parentheses substring.
- The function iterates over each character in the string using a `for` loop.
- If the current character is an opening parenthesis `'('`, its index is appended to the stack.
- If the current character is a closing parenthesis `')'`, the function checks if the length of the stack is equal to `1`. If it is, it updates the first element of the stack to be the current index. Otherwise, it pops an element from the stack and updates `ans` to be the maximum value between its current value and `i - stack[-1]`, where `i` is the current index.
- After iterating over all characters in the string, the function returns `ans`, which represents the length of the longest valid parentheses substring in `S`.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of the `longestValidParentheses` function is `O(n)`, where `n` is the length of the input string `S`. 
This is because the function iterates over each character in the string using a `for` loop, which takes `O(n)` time. 
The operations inside the loop, such as checking the current character, 
appending to or popping from the stack, and updating `ans`, all take constant time `O(1)`.
In the worst case, the stack can contain all characters in the string, which would require `O(n)` space.

### `Space Complexity`:
The space complexity of the `longestValidParentheses` function is `O(n)`, because it uses a stack to keep track of the indices of the parentheses in the string.

## Code:
```py
class Solution:
    def longestValidParentheses(self, S: str) -> int:
        # Initialize a stack with -1 and a variable to store the maximum length of a valid parentheses substring
        stack, ans = [-1], 0
        
        # Iterate over each character in the string
        for i in range(len(S)):
            # If the current character is an opening parenthesis
            if S[i] == '(':
                # Append its index to the stack
                stack.append(i)
            # If the current character is a closing parenthesis
            elif len(stack) == 1:
                # Update the first element of the stack to be the current index
                stack[0] = i
            else:
                # Pop an element from the stack
                stack.pop()
                # Update ans to be the maximum value between its current value and i - stack[-1]
                ans = max(ans, i - stack[-1])
        
        # Return the maximum length of a valid parentheses substring
        return ans
```
