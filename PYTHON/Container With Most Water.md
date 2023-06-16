### [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

## Explanation:
This code defines a class `Solution` with a method `maxArea` that takes in a list of integers `height` representing the heights of lines and returns the maximum area of water that can be contained between any two lines. Here's the main logic of the code in points:
1. The code initializes variables `left` and `right` to represent the leftmost and rightmost lines, respectively, and a variable `max_area` to keep track of the maximum area found so far.
2. The code enters a loop that continues until the left index is greater than or equal to the right index.
3. In each iteration of the loop, the code calculates the area of water that can be contained between the leftmost and rightmost lines and updates `max_area` if it is greater than its current value.
4. If the height of the leftmost line is less than the height of the rightmost line, the left index is incremented. Otherwise, the right index is decremented.
5. After all pairs of lines have been considered, the final value of `max_area` is returned.

## Time and Space Compexity:
### `Time Complexity`:
The time complexity of this code is O(n), where n is the number of elements in `height`. This is because each element in `height` is processed once.
### `Space Complexity`:
The space complexity of this code is O(1), because only a constant amount of additional memory is used.


## Code:
### Optimized Solution - with two pointers approach
```py
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
```

<hr>
## Explanation:
Checks each and every area 

## Code:
### Brute force approach ( Exceeding Time Limit)
class Solution:
    def maxArea(self, height: list[int]) -> int:
        end,max_area = len(height),0
        for i in range(end):
            j=0
            while j<end and j!=i:
                max_area=max(max_area,abs(i-j)*min(height[i],height[j]))
                j=j+1
        return max_area
      

