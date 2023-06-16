### [First Missing Positive](https://leetcode.com/problems/first-missing-positive/description/)

## Key Insight : 
Remove the non-positive integers and then loop over the dictionary from 1 upto a number greater than the maximum of the dictionary<br> 
and return the element which is not present<br>
If a question arises in your mind that, why have we used a dictionary instead of looping of over the list which would also have been <br>
the same , then the answer to it is.....<br>
When we search for an element in a dictionary in python the time-complexity is O(1) , so we speed up the code<br> 
If we had used `not in` operator with a list it would have resulted in a time-complexity of O(n) and the resultant time-complexity of<br> 
the code would have become O(n^2)<br>

## Explanation:
This code defines a class `Solution` with a method `firstMissingPositive` that takes in a list of integers `nums` and returns the first missing positive integer. Here's the main logic of the code in points:
1. The code removes all non-positive integers from the input list `nums`.
2. The code creates a dictionary `freq` to track the presence of positive integers in the list. For each positive integer in the list, it adds an entry to the dictionary with a key equal to the integer and a value of 1.
3. The code enters a loop that iterates from 1 to `len(nums)+1`. In each iteration, it checks if the current integer is present in the dictionary. If it is not present, it is returned as the first missing positive integer.

## Time and Space Compexity:
### `Time Complexity`:
The time complexity of this code is O(n), where n is the number of elements in `nums`. This is because each element in `nums` is processed once when creating the dictionary and once when checking for the first missing positive integer.

### `Space Complexity`:
The space complexity of this code is O(n), where n is the number of elements in `nums`. This is because memory is allocated for a dictionary that can have at most n entries.

#### Optimized Solution :
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Step 1: Remove non-positive integers from the list
        nums = [num for num in nums if num > 0]
        
        # Step 2: Create a dictionary to track the presence of positive integers
        freq = {}
        for num in nums:
            freq[num] = 1
        
        # Step 3: Find the first missing positive integer
        for i in range(1, len(nums)+2):
            if i not in freq:
                return i
```

<hr> 

#### Time limit Exceeding :
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Step 1: Remove non-positive integers from the list
        nums = [num for num in nums if num > 0]
        
        # Step 2: Find the first missing positive integer
        for i in range(1, len(nums)+2):
            if i not in nums:
                return i
 ```
 

