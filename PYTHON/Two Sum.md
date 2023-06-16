### [Two Sum](https://leetcode.com/problems/two-sum/description/)

## Key Insight :
Use a dictionary to store the indices of each element in the input list,<br>
and then iterate over the list to check if the complement of each element is already in the dictionary .<br> 
If the complement is found return the indices<br> 

## Code:
#### Optimal Solution
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty dictionary to store the indices of each element in the input list
        index_dict = {}
        
        # Iterate over the input list using the enumerate() function to keep track of the indices
        for i , num in enumerate(nums):
            # Compute the complement of the current element (i.e., the value that is needed to reach the target sum)
            complement = target - num
            
            # Check if the complement is already in the dictionary. If it is, we have found a pair of elements that add up to the target sum.
            # Return their indices as a list and exit the loop.
            if complement in index_dict:
                return [index_dict[complement],i]
            
            # If the complement is not in the dictionary, add the current element and its index to the dictionary and continue iterating.
            index_dict[num] = i
        
        # If no pair is found, return an empty list.
        return []
 ```
------------------------------------------------------------------------------------------------------------------------------------------

#### Working but not a optimal solution
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Sort the input list of numbers
        sorted_nums = sorted(nums)
        # Set pointers to the beginning and end of the list
        left , right = 0 , len(nums) - 1
        # If there are only two numbers in the list, return their indices
        if len(nums) == 2:
            return [0,1]
        # Continue iterating until the pointers meet in the middle
        while left < right:
            # If the sum of the left and right pointers is equal to the target, return their indices
            if sorted_nums[left] + sorted_nums[right] == target:
                # If the left and right pointers point to different values, return the indices of those values in the original list
                if sorted_nums[left] != sorted_nums[right]:
                    return [nums.index(sorted_nums[left]),nums.index(sorted_nums[right])]
                # If the left and right pointers point to the same value, return the index of the value twice
                else:
                    return [nums.index(sorted_nums[left]),len(nums) - 1 - nums[::-1].index(sorted_nums[left])]
            # If the sum of the left and right pointers is greater than the target, move the right pointer leftward
            elif sorted_nums[left] + sorted_nums[right] > target:
                right -=1
            # If the sum of the left and right pointers is less than the target, move the left pointer rightward
            else:
                left +=1
```
