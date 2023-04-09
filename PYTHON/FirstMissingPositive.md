### [First Missing Positive](https://leetcode.com/problems/first-missing-positive/description/)

## Key Insight : 
Remove the non-positive integers and then loop over the dictionary from 1 upto a number greater than the maximum of the dictionary and<br> 
return the element which is not present<br>
If a question arises in your mind that, why have we used a dictionary instead of looping of over the list which would also have been <br>
the same , then the answer to it is.....<br>
When we search for an element in a dictionary in python the time-complexity is O(1) , so we speed up the code<br> 
If we had used `not in` operator with a list it would have resulted in a time-complexity of O(n) and the resultant time-complexity of<br> 
the code would have become O(n^2)<br>

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
