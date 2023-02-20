#Brute force approach ( Exceeding Time Limit)
class Solution:
    def maxArea(self, height: list[int]) -> int:
        end,max_area = len(height),0
        for i in range(end):
            j=0
            while j<end and j!=i:
                max_area=max(max_area,abs(i-j)*min(height[i],height[j]))
                j=j+1
        return max_area
      
#Optimized Solution
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
