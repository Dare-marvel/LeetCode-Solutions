### [Candy](https://leetcode.com/problems/candy/description/)

## Brief Description:
In the first pass, we give candies to children with higher ratings than their left neighbor.<br> 
In the second pass, we give candies to children with higher ratings than their right neighbor.<br> 
Finally, we return the sum of candies.<br>

## Code:
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        
        # First pass: Give candies to children with higher ratings than their left neighbor
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        # Second pass: Give candies to children with higher ratings than their right neighbor
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        # Return the sum of candies
        return sum(candies)
