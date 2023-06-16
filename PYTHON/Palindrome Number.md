### [Palindrome Number](https://leetcode.com/problems/palindrome-number/description/)

## Brief Description:
We just reverse the string and check whether the original string and reversed strings are equal or not

## Explanation:
This code defines a class `Solution` with a method `isPalindrome` that takes in an integer `x` and returns a boolean value indicating whether `x` is a palindrome. Here's the main logic of the code in points:
1. The code checks if `x` is negative and returns `False` if it is because negative numbers cannot be palindromes.
2. The code converts `x` to a string so that it can easily check if it is a palindrome.
3. The code checks if the string representation of `x` is equal to its reverse. If it is, then `x` is a palindrome and the method returns `True`.
4. If the string representation of `x` is not equal to its reverse, then `x` is not a palindrome and the method returns `False`.

## Time and Space Compexity:
### `Time Complexity`:
The time complexity of this code is O(n), where n is the number of digits in `x`. This is because the string representation of `x` is created and reversed, both of which take O(n) time.

### `Space Complexity`:
The space complexity of this code is O(n), where n is the number of digits in `x`. This is because memory is allocated for the string representation of `x` and its reverse, both of which can have at most n characters.

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
