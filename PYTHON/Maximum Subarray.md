### [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)

## Brief Description:
This solution is implemented using Kadane's algorithm

## Key Insights:
### [Articles to refer](https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/)

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of the above approach is O(n), where n is the length of the input list nums. This is because we are iterating over the entire list exactly once.

### `Space Complexity`:
The space complexity of the above approach is O(1), because we are only using two extra variables (maxSoFar and maxEndHere) to keep track of the maximum subarray sum seen so far and the maximum subarray sum ending at the current index, respectively. We are not using any data structures or arrays that depend on the input size, so the space used is constant.

## Code:
```python
# Importing the maxsize constant from the sys module
from sys import maxsize

# Defining a class Solution
class Solution:
    
    # Defining a method maxSubArray that takes in an argument of a list of integers and returns an integer
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Initializing two variables: maxSoFar and maxEndHere
        # maxSoFar is initialized to a value smaller than the minimum possible value that could be in the list
        # maxEndHere is initialized to 0 because we haven't seen any numbers yet
        maxSoFar = -maxsize - 1
        maxEndHere = 0
        
        # Looping through the list of numbers
        for number in nums:
            
            # Adding the current number to maxEndHere
            maxEndHere += number
            
            # If maxSoFar is less than maxEndHere, set maxSoFar to maxEndHere
            if maxSoFar < maxEndHere:
                maxSoFar = maxEndHere
            
            # If maxEndHere is negative, set it to 0
            # This means we're starting a new subarray because the sum of the previous subarray was negative
            if maxEndHere < 0:
                maxEndHere = 0
        
        # Return the maximum sum found in the list
        return maxSoFar

```
