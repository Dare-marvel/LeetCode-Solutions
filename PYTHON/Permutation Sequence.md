### [Permutation Sequence](https://leetcode.com/problems/permutation-sequence/description/)

## Explanation:
This code defines a class `Solution` with a single method `getPermutation`. The purpose of this method is to return the `k`-th permutation of the numbers from 1 to `n` in lexicographic order.

Here is the main logic of the code, explained in detail:

1. The method generates all permutations of the numbers from 1 to `n` using the `itertools.permutations` function. This function returns an iterator, so we convert it to a list using the `list` function. The permutations are generated in lexicographic order.
2. The method then gets the `k`-th permutation from the list of all permutations using indexing. Note that we use `k-1` instead of `k` because Python uses zero-based indexing.
3. Finally, the method converts the permutation from a tuple of integers to a string using `''.join(map(str, kth_permutation))`. This converts each integer in the tuple to a string using the `map` function, and then concatenates all the strings using the `''.join` method.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is `O(n!)`, where `n` is the size of the input. This is because generating all permutations of `n` numbers takes `O(n!)` time.

### `Space Complexity`:
The space complexity of this code is also `O(n!)`, because we need to store all `n!` permutations in memory.

## Code:
```
import itertools  # Import the itertools module

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Generate all permutations of the numbers from 1 to n
        allPer = list(itertools.permutations(range(1, n+1)))
        
        # Get the k-th permutation (using 1-based indexing)
        kth_permutation = allPer[k-1]
        
        # Convert the permutation from a tuple of integers to a string
        result = ''.join(map(str, kth_permutation))
        
        return result
```
