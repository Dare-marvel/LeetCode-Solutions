### [LinkToProblem](https://leetcode.com/problems/palindrome-number/description/)

## Brief Description:
We just reverse the string and check whether the original string and reversed strings are equal or not

## Code:
```python
# Defining a class Solution
class Solution:
    
    # Defining a method isPalindrome that takes in an integer argument and returns a boolean value
    def isPalindrome(self, x: int) -> bool:
        
        # If x is negative, it can't be a palindrome, so return False
        if x < 0:
            return False
        
        # Convert x to a string so we can check if it's a palindrome easily
        x = str(x)
        
        # Check if the string representation of x is equal to its reverse
        # If it is, then x is a palindrome, so return True
        if x == x[::-1]:
            return True
        
        # If x is not a palindrome, return False
        return False

```
