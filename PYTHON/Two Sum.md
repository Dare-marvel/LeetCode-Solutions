### [Two Sum](https://leetcode.com/problems/two-sum/description/)

## Optimal Solution

## Key Insight :
Use a dictionary to store the indices of each element in the input list,<br>
and then iterate over the list to check if the complement of each element is already in the dictionary .<br> 
If the complement is found return the indices<br> 

## Explanation:
This code defines a class `Solution` with a method `twoSum` that takes in a list of integers `nums` and an integer `target` and returns a list of two indices such that the elements at those indices add up to `target`. Here's the main logic of the code in points:
1. The code creates an empty dictionary `index_dict` to store the indices of each element in the input list.
2. The code iterates over the input list using the `enumerate()` function to keep track of the indices. For each element, it computes its complement (i.e., the value that is needed to reach `target`) and checks if it is present in `index_dict`. If it is, it returns a list containing the indices of the current element and its complement.
3. If the complement is not present in `index_dict`, the code adds the current element and its index to `index_dict` and continues iterating.
4. If no pair of elements that add up to `target` is found, the code returns an empty list.

## Time and Space Compexity:
### `Time Complexity`:
The time complexity of this code is O(n), where n is the number of elements in `nums`. This is because each element in `nums` is processed once.

### `Space Complexity`:
The space complexity of this code is O(n), where n is the number of elements in `nums`. This is because memory is allocated for a dictionary that can have at most n entries.

## Code:
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
## Working but not a optimal solution

## Explanation:
This code defines a class `Solution` with a method `twoSum` that takes in a list of integers `nums` and an integer `target` and returns a list of two indices such that the elements at those indices add up to `target`. Here's the main logic of the code in points:
1. The code sorts the input list `nums` and stores it in a variable `sorted_nums`.
2. The code initializes variables `left` and `right` to represent pointers to the beginning and end of the sorted list, respectively.
3. The code checks if the length of `nums` is 2 and returns a list containing the indices 0 and 1 if it is.
4. The code enters a loop that continues until the left pointer is greater than or equal to the right pointer. In each iteration of the loop, it checks if the sum of the elements at the left and right pointers is equal to `target`. If it is, it returns a list containing their indices in the original list. If the sum is greater than `target`, it decrements the right pointer. If the sum is less than `target`, it increments the left pointer.

## Time and Space Compexity:
### `Time Complexity`:
The time complexity of this code is O(n log(n)), where n is the number of elements in `nums`. This is because sorting `nums` takes O(n log(n)) time and each element in `sorted_nums` is processed once.

### `Space Complexity`:
The space complexity of this code is O(n), where n is the number of elements in `nums`. This is because memory is allocated for a sorted copy of `nums` that can have at most n elements.

## Code:
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
