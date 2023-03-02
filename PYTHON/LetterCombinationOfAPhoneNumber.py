# Link to the problem : https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Method - 1
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
        
        

  # Method - 2
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
