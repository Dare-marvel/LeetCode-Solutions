### [Letter Combination of A Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

## Method - 1
## Explanation:
This code defines a class `Solution` with a method `letterCombinations` that takes in a string `digits` representing a sequence of digits and returns a list of strings representing all possible letter combinations that the number could represent. Here's the main logic of the code in points:
1. The code checks if `digits` is empty and returns an empty list if it is.
2. The code creates a dictionary `dialpad` that maps digits to their respective characters on a dialpad.
3. The code uses the `itertools.product()` function to generate all possible combinations of characters for the given input digits. It passes a list comprehension as an argument to the function that extracts the characters for each digit from the `dialpad` dictionary.
4. The code joins each combination of characters and returns them as a list.

## Time and Space Compexity:
### `Time Complexity`:
The time complexity of this code is O(n * 4^n), where n is the length of `digits`. This is because there can be at most 4^n combinations of characters for n digits and each combination has n characters.

### `Space Complexity`:
The space complexity of this code is O(n * 4^n), where n is the length of `digits`. This is because memory is allocated for a list that can have at most 4^n elements and for strings that can have at most n * 4^n characters.

## Code:
```py
import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        # Creating a dictionary to map digits to their respective characters on dialpad
        dialpad = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    
        # Using itertools.product() to generate all possible combinations of characters
        # for the given input digits
        combinations = itertools.product(*[dialpad[digit] for digit in digits])
        # Joining the combinations and returning them as a list
        return [''.join(combination) for combination in combinations]
 ```       
        

## Method - 2

## Explanation:
This code defines a class `Solution` with a method `letterCombinations` that takes in a string `digits` representing a sequence of digits and returns a list of strings representing all possible letter combinations that the number could represent. Here's the main logic of the code in points:
1. The code checks if `digits` is empty and returns an empty list if it is.
2. The code creates a dictionary `dialpad` that maps digits to their respective characters on a dialpad.
3. The code defines a recursive function `dfs` that takes in an index and a path and generates all possible combinations of characters for the given input digits. For each digit in `digits`, it iterates over its characters and recursively calls itself with the next index and an updated path that includes the current character. When it reaches the end of `digits`, it adds the current path to a results list.
4. The code initializes an empty results list and calls the `dfs` function with initial index and path values.
5. After all combinations have been generated, the final value of the results list is returned.

## Time and Space Compexity:
### `Time Complexity`:
The time complexity of this code is O(n * 4^n), where n is the length of `digits`. This is because there can be at most 4^n combinations of characters for n digits and each combination has n characters.

### `Space Complexity`:
The space complexity of this code is O(n * 4^n), where n is the length of `digits`. This is because memory is allocated for a list that can have at most 4^n elements, for strings that can have at most n * 4^n characters, and for the call stack which can have at most n frames.

## Code:
```py
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Return empty list if digits string is empty
        if not digits:
            return []
        
        # Define a dialpad dictionary mapping digits to a list of corresponding letters
        dialpad = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        # Define a recursive function to generate all combinations
        def dfs(index, path):
            # If we have reached the end of the digits string, add the current path to the results list and return
            if index == len(digits):
                res.append(path)
                return
            # For each letter corresponding to the current digit, recursively call the function with the next index and updated path
            for char in dialpad[digits[index]]:
                dfs(index+1, path+char)
        
        # Initialize an empty results list and call the dfs function with initial index and path values
        res = []
        dfs(0, '')
        # Return the results list
        return res
```
