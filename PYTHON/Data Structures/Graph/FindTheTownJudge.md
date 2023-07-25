### [Find The Town Judge](https://leetcode.com/problems/find-the-town-judge/description/)

## Brief Description:
The problem statement asks us to find the town judge among a group of 'n' people. The judge is defined as a person who is trusted by everyone else, but trusts nobody himself/herself.

## Key Insights:
To solve the problem, the given code uses a list trustCount to keep track of how many people trust each person. The index of the list represents a person, and the value at the index represents how many people trust that person. Initially, all values in trustCount are set to 0, since no one has been trusted yet.

The code then iterates through the list of pairs in trust. For every pair, the code increments the trust count of the second person (i.e., the person being trusted) and decrements the trust count of the first person (i.e., the person doing the trusting). This is done using the following two lines of code:
```python
trustCount[trustPair[0]] -= 1
trustCount[trustPair[1]] += 1
```

After the trust counts have been updated for all pairs in trust, the code checks each person's trust count in the list trustCount. The judge is the person whose trust count is equal to n-1, since everyone trusts the judge except the judge himself/herself. The code returns the index of the judge (i.e., the person whose trust count is n-1) if such a person is found. If no such person is found, the code returns -1.

The code uses a loop to iterate over the list trustCount to find the judge. The loop starts from index 1 (since the index 0 is not used) and goes up to index n. If the trust count of a person is equal to n-1, the code returns the index of that person (which represents the person number), as shown below:

```python
for i in range(1, n+1):
    if trustCount[i] == n-1:
        return i
```
If the loop completes without finding the judge, the code returns -1, as shown below:
```python
return -1
```

## Time and Space Complexity:
`Time Complexity`:
The time complexity of this approach is O(T + P), where T is the number of trust relationships and P is the number of people. This is because we loop through all trust relationships to update the trust count list, and then loop through all people to find the one with trust count n-1.

`Space Complexity`:
The space complexity of this approach is O(P), where P is the number of people. This is because we create a trust count list with size P+1 to store the trust counts for each person.

## Code:
#### Approach 1
```python
from typing import List
from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Initialize the trust count list with 0 for all people
        trustCount = [0] * (n+1)
        
        # Loop through all trust relationships and update the trust count list
        for trustPair in trust:
            trustCount[trustPair[0]] -= 1
            trustCount[trustPair[1]] += 1
        
        # Loop through all people and find the one whose trust count is n-1
        for i in range(1, n+1):
            if trustCount[i] == n-1:
                # This person is trusted by everyone, but trusts no one
                return i
        
        # If no such person is found, return -1
        return -1

```
--------------------------------------------------------------------------------------------------------------------------------------------------
#### Approach 2
```python
from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Create a dictionary to keep track of the number of incoming edges (trusts)
        inDeg = defaultdict(int)
        # Create a dictionary to keep track of the number of outgoing edges (trusted by)
        outDeg = defaultdict(int)
        
        # If there is only one person, they are the judge (they trust no one and everyone trusts them)
        if n == 1:
            return 1
        
        # Loop through all trust relationships and update the incoming and outgoing edge counts
        for per1, per2 in trust:
            outDeg[per1] += 1
            inDeg[per2] += 1
        
        # Check if there is a person who is trusted by everyone (n-1 incoming edges) and trusts no one (0 outgoing edges)
        found = False
        judge = 0
        for per1, per2 in trust:
            if inDeg[per2] == n - 1 and outDeg[per2] == 0:
                found = True
                judge = per2
        
        # If such a person exists, return their ID. Otherwise, return -1.
        if found:
            return judge
        else:
            return -1

```
