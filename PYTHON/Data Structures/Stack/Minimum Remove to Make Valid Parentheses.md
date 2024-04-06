### [Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/)

## Explanation:
1. **Conversion to List**: The string `s` is converted to a list. This is done because strings in Python are immutable, which means they cannot be changed after they are created. By converting the string to a list, we can modify it in-place, which is more efficient.

2. **Initialization of Stack**: A stack is initialized as an empty list. Stacks follow the Last-In-First-Out (LIFO) principle. They are used here to keep track of the indices of the open parentheses.

3. **Iteration over the List**: The list `s` is iterated over using the `enumerate` function, which returns both the index `i` and the character `char` at that index.

4. **Handling Open Parentheses**: If the character `char` is an open parenthesis `'('`, its index `i` is appended to the stack. This is done to keep track of the last unmatched open parenthesis.

5. **Handling Close Parentheses**: If the character `char` is a close parenthesis `')'`, it checks if the stack is not empty and the character at the index at the top of the stack is an open parenthesis. If so, it pops the index from the stack, effectively matching the close parenthesis with the last unmatched open parenthesis. If the stack is empty or the character at the index at the top of the stack is not an open parenthesis, it means the close parenthesis is unmatched, so its index is appended to the stack.

6. **Removal of Unmatched Parentheses**: After the iteration, any indices remaining on the stack represent unmatched parentheses. These are removed by setting the characters at these indices in the list `s` to an empty string `''`.

7. **Conversion Back to String**: Finally, the list `s` is joined back into a string using the `join` method and returned.

## Time and Space Complexity:
### `Time Complexity`:
The **time complexity** of this code is **O(n)**, where **n** is the length of the string. This is because each character in the string is processed once.

### `Space Complexity`:
The **space complexity** is also **O(n)**, for the same reason. In the worst case, every character in the string could be an open parenthesis, in which case every index would be added to the stack.

## Code:
```py
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Convert the input string to a list of characters to allow modification.
        s = list(s)
        
        # Initialize a stack to keep track of indices of parentheses that are currently open or unmatched.
        stack = []
        
        # Iterate through each character in the string along with its index.
        for i, char in enumerate(s):
            # If the current character is an opening parenthesis, push its index onto the stack.
            if char == '(':
                stack.append(i)
            # If the current character is a closing parenthesis:
            elif char == ')':
                # If the stack is not empty and the top of the stack is an opening parenthesis:
                # This means we've found a matching pair.
                if stack and s[stack[-1]] == '(':
                    stack.pop()  # Pop the opening parenthesis' index off the stack.
                else:
                    # If the stack is empty or the top is not an opening parenthesis,
                    # this closing parenthesis is unmatched. Push its index onto the stack.
                    stack.append(i)
        
        # After processing all characters, the stack contains indices of unmatched parentheses.
        # Remove these by setting them to an empty string.
        while stack:
            s[stack.pop()] = ''
        
        # Join the list back into a string, which now excludes the unmatched parentheses, and return it.
        return ''.join(s)

```
