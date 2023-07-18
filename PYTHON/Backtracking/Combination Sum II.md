### [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/description/)

## Explanation:
This Python code finds all unique combinations of numbers in a list of candidates that add up to a given target using a backtracking approach. Here's how it works:

1. The `combinationSum2` method is called with the list of candidates and the target as arguments.
2. A `backtrack` function is defined inside the `combinationSum2` method.
3. The `backtrack` function takes three arguments: `start`, `remaining`, and `path`.
4. If the remaining value is 0, the current path is added to the result and the function returns.
5. A for loop iterates over the candidates from the `start` index to the end of the list.
6. If the current candidate is equal to the previous candidate, it is skipped to avoid duplicates.
7. If the current candidate is greater than the remaining value, the loop breaks as no further candidates can be used.
8. The `backtrack` function is called recursively with the next index, the remaining value minus the current candidate, and the current path plus the current candidate as arguments.
9. An empty result list is initialized.
10. The list of candidates is sorted in ascending order.
11. The `backtrack` function is called with 0 as the start index, the target as the remaining value, and an empty path.
12. The result list is returned.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this solution is O(2^n), where n is the number of candidates. This is because in the worst case, all possible combinations of candidates are explored.

### `Space Complexity`:
The space complexity is O(n), as there are at most n recursive calls on the call stack.

## Code:
```py
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Define the backtrack function to find combinations
        def backtrack(start, remaining, path):
            # If remaining sum is 0, we have found a valid combination
            if remaining == 0:
                result.append(path)
                return
            # Explore all possible candidates starting from the given index
            for i in range(start, len(candidates)):
                # Skip duplicates to avoid duplicate combinations
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                # If the candidate is greater than the remaining sum, stop exploring
                if candidates[i] > remaining:
                    break
                # Recursive call to explore the next candidate
                # Update the remaining sum and the path
                backtrack(i+1, remaining - candidates[i], path + [candidates[i]])
        
        # Initialize the result list to store valid combinations
        result = []
        # Sort the candidates list in ascending order
        candidates.sort()
        # Start the backtrack process from index 0 with the target sum and an empty path
        backtrack(0, target, [])
        # Return the list of valid combinations
        return result

```
