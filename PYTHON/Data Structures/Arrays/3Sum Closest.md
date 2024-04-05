### [3Sum Closest](https://leetcode.com/problems/3sum-closest/description/)

## Explanation:
1. **Function Definition**: The function `threeSumClosest` is defined with two parameters: `nums`, a list of integers, and `target`, an integer.

2. **Initialization**: The length of `nums` is stored in `n`. Four variables are initialized: `curDiff`, `actSum`, `minDiff`, and `curSum`. `curDiff` and `actSum` are set to 0, `minDiff` is set to a large number (10e9), and `curSum` is also set to 0.

3. **Sorting**: The list `nums` is sorted in ascending order. This is crucial for the two-pointer technique used later.

4. **Outer Loop**: A `for` loop is used to iterate over the elements of `nums` up to the third last element. If the current element is the same as the previous one, it is skipped to avoid duplicate solutions.

5. **Two-Pointer Technique**: Two pointers, `lf` and `rt`, are initialized to point to the next element and the last element of `nums` respectively. These pointers are moved towards each other until they meet.

6. **Inner Loop**: Inside the `while` loop, `curSum` is calculated as the sum of the elements pointed to by `i`, `lf`, and `rt`. `curDiff` is the absolute difference between `curSum` and `target`.

7. **Updating Minimum Difference**: If `curDiff` is less than `minDiff`, `minDiff` and `actSum` are updated to `curDiff` and `curSum` respectively.

8. **Moving Pointers**: If `curSum` is less than `target`, `lf` is incremented to increase `curSum`. If `curSum` is greater than `target`, `rt` is decremented to decrease `curSum`. If `curSum` equals `target`, `actSum` is set to `curSum` and returned immediately as the closest sum.

9. **Return Value**: If no three numbers sum up exactly to `target`, `actSum` is returned after the loop ends.

## Time and Space Complexity:
### `Time Complexity`:
The **time complexity** of the code is **O(n^2)**, where `n` is the length of `nums`. This is because the code involves a nested loop: the outer `for` loop runs `n` times, and for each iteration, the inner `while` loop can run up to `n` times.

### `Space Complexity`:
The **space complexity** of the code is **O(log n)** if we consider the space required for the recursion stack during the sorting of `nums`, or **O(1)** if we don't consider it. This is because the amount of extra space used does not grow with `n`, and is therefore constant.

## Code:
```py
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Initialize variables
        n = len(nums)  # Length of the input list
        curDiff, actSum, minDiff, curSum = 0, 0, 10e9, 0  # Variables to track differences and sums

        # Sort the input list
        nums.sort()

        # Iterate through the list
        for i in range(n-2):
            # Skip duplicate elements to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Two-pointer approach for finding the other two elements
            lf, rt = i+1, n-1  # Left and right pointers
            while lf < rt:
                # Calculate current sum and absolute difference from the target
                curSum = nums[i] + nums[lf] + nums[rt]
                curDiff = abs(target-curSum)

                # Update the actual sum and minimum difference if the current difference is smaller
                if curDiff < minDiff:
                    actSum = curSum
                    minDiff = curDiff

                # Move pointers based on the current sum
                if curSum < target:
                    lf += 1  # Increment left pointer if the sum is less than the target
                elif curSum > target:
                    rt -= 1  # Decrement right pointer if the sum is greater than the target
                else:
                    actSum = curSum  # If the sum is equal to the target, return the sum
                    return actSum

        return actSum  # Return the sum closest to the target
```
