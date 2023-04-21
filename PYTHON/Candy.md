### [Candy](https://leetcode.com/problems/candy/description/)

## Brief Description:
In the first pass, we give candies to children with higher ratings than their left neighbor.<br> 
In the second pass, we give candies to children with higher ratings than their right neighbor.<br> 
Finally, we return the sum of candies.<br>

## Key Insights:
The approach taken is a two-pass algorithm that uses an array candies to keep track of the number of candies assigned to each child. In the first pass, the algorithm assigns candies to each child based on their rating and the rating of their left neighbor. If a child has a higher rating than their left neighbor, they receive one more candy than their neighbor. This ensures that children with higher ratings receive more candies than their neighbors on the left.

In the second pass, the algorithm assigns candies to each child based on their rating and the rating of their right neighbor. If a child has a higher rating than their right neighbor and has already received fewer candies than their neighbor, they receive additional candies to match their neighbor's count. This ensures that children with higher ratings receive more candies than their neighbors on the right.

## Time and Space Complexity:
`Time Complexity`:
The time complexity of this solution is O(n), where n is the length of the input ratings array, because each child is visited twice at most.

`Space Complexity`:
The space complexity of this solution is also O(n), as an array of size n is used to store the number of candies assigned to each child.

## Code:
```python
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
```
