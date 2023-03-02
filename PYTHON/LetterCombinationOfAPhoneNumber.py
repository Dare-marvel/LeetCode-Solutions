# Link to the problem : https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Method - 1
import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
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
        
        combinations = itertools.product(*[dialpad[digit] for digit in digits])
        return [''.join(combination) for combination in combinations]

  # Method - 2
  class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
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
        
        def dfs(index, path):
            if index == len(digits):
                res.append(path)
                return
            for char in dialpad[digits[index]]:
                dfs(index+1, path+char)
        
        res = []
        dfs(0, '')
        return res
