### [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

### Explanation of the code:
* The code check_parentheses() takes a string s as input and returns a boolean value indicating whether the parentheses in s are balanced.<br> 
The code works as follows:
* The code defines two strings, opening and closing, that represent opening and closing parentheses, respectively.
* The code creates an empty list to represent a stack.
* The code iterates over each character in the string s.
* If the character is an opening parenthesis, the code pushes it onto the stack.
* If the character is a closing parenthesis, the code does the following:
    * If the stack is empty, the code returns False.
    * If the most recent opening parenthesis matches the closing parenthesis, the code pops the opening parenthesis from the stack.
    * Otherwise, the code returns False.
* If the stack is empty after processing all characters, the code returns True.

Here is an example of how the code works:
#### Test-case 1<br>
```
Input: "(())"
Output: True
```

In this example, the string s contains three parentheses: (, (, and ). The code first pushes the first two parentheses (( and () onto the stack. When the code encounters the third parenthesis ()), it pops the top two parentheses from the stack (i.e., ( and (). 
Since the stack is empty after processing all characters, the code returns True.

#### Test-case 2
```
Input: "(()"
Output: False
```

In this example, the string s contains two parentheses: ( and (. The code first pushes the first parenthesis (() onto the stack. When the code encounters the second parenthesis ()), it pops the top parenthesis from the stack (i.e., (). However, the stack is not empty after processing all characters, so the code returns False.


### Time and Space Complexity:

## Code:
```py
# define the function `check_parentheses` that takes a string `s` as input
def check_parentheses(s):
    # define two strings that represent opening and closing parentheses respectively
    opening = "([{"
    closing = ")]}"
    # create an empty list to represent a stack
    stack = []
    # iterate over each character in the string `s`
    for char in s:
        # if the character is an opening parenthesis, push it onto the stack
        if char in opening:
            stack.append(char)
        # if the character is a closing parenthesis:
        elif char in closing:
            # if the stack is empty, return False (i.e., there is a closing parenthesis without a corresponding opening parenthesis)
            if not stack:
                return False
            # if the most recent opening parenthesis matches the closing parenthesis, pop the opening parenthesis from the stack
            elif opening.index(stack[-1]) == closing.index(char):
                stack.pop()
            # otherwise, return False (i.e., there is a mismatched opening parenthesis)
            else:
                return False
    # if the stack is empty after processing all characters, return True (i.e., all parentheses have been matched)
    return not stack
```
