## [3 Sum](https://leetcode.com/problems/3sum/description/)

## Key Insights:
The approach taken is to use three nested loops to iterate through all possible combinations of three elements in the array. Then, the sum of each triplet is checked, and if it equals zero, the triplet is added to the solution list.<br>

However, since the problem requires finding unique solutions, the final step is to remove duplicates from the solution list. This is done by converting the solution list to a set of tuples, where each tuple contains the sorted elements of a triplet. Since sets can only contain unique elements, this automatically removes duplicates. Finally, the set of tuples is converted back to a list of lists and returned as the final solution.

### Time Complexity: O(n<sup>3</sup>)

## Code :
#### Brute force approach : Exceeding time limit
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create an empty list to store solutions
        solution_list = []
        # get the length of the array
        n = len(nums)
        
        # iterate through the array
        for i in range(n):
            # iterate through the remaining elements in the array
            for j in range(i+1,n):
                # iterate through the remaining elements in the array
                for k in range(j+1,n):
                    # check if the three numbers sum to zero
                    if nums[i] + nums[j] + nums[k] == 0:
                        # if so, add the triplet to the solution list
                        solution_list.append([nums[i],nums[j],nums[k]])
        
        # remove duplicates from the solution list using set
        unique_solutions = set(map(lambda x: tuple(sorted(x)), solution_list))
        # convert the set of tuples back to a list of lists
        return list(map(list, unique_solutions)))
```

## Key Insight : 
Iterate through the sorted array and for each element,<br>
we use two pointers to find the other two elements that can form a triplet whose sum is equal to zero.<br> 
We can set one pointer at the next element after the current element and the other pointer at the end of the array.<br> 

## Time and Space Complexity:
`Time Complexity`:
The time complexity of this solution is O(n^2), where n is the length of the input array. This is because the solution uses a nested loop to iterate through all possible pairs of numbers in the array, and then uses two pointers to search for a third number that completes the triplet.

`Space Complexity`:
The space complexity of this solution is O(1), as the only extra space used is the result list to store the triplets that sum up to zero. No additional data structures or memory allocations are made, and the input array is sorted in place, so the space used by the algorithm is constant with respect to the size of the input array.

#### Optimal Solution using two pointer approach:
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create an empty list to store the solutions
        result = []
        n = len(nums) 

        # sort the input array in ascending order
        nums.sort()
        
        # iterate through the input array
        for i in range(n-2):
            # skip any duplicate values
            if i>0 and nums[i] == nums[i-1]:
                continue

            # use two pointers to find the other two numbers that add up to the target sum
            lf , rt = i+1 , n-1
            while lf < rt :
                s = nums[i] + nums[lf] + nums[rt]
                
                # if the sum is less than zero, move the left pointer
                if s < 0:
                    lf += 1
                # if the sum is greater than zero, move the right pointer
                elif s > 0:
                    rt -= 1
                # if the sum is zero, add the triplet to the result list
                else:
                    result.append([nums[i],nums[lf],nums[rt]])
                    # skip any duplicate values
                    while lf < rt and (nums[lf]==nums[lf+1]):
                        lf+=1
                    while lf < rt and (nums[rt]==nums[rt-1]):
                        rt-=1
                    # move both pointers to continue searching for triplets
                    lf+=1
                    rt-=1
        # return the result list
        return result
```
