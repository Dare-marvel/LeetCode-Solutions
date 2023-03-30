# Link : https://leetcode.com/problems/two-sum/description/

# Key Insight :


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
