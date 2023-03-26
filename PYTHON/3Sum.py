# Link to the problem : https://leetcode.com/problems/3sum/description/

# Brute force approach : Exceeding time limit
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

# Key Insight : iterate through the sorted array and for each element,
# we use two pointers to find the other two elements that can form a triplet whose sum is equal to zero. 
# We can set one pointer at the next element after the current element and the other pointer at the end of the array. 

# Optimal Solution using two pointer approach:
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
