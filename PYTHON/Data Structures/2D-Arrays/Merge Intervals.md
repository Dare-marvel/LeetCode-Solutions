### [Merge Intervals](https://leetcode.com/problems/merge-intervals/description/)

## Explanation:
This code merges overlapping intervals in a list of intervals. Here is the main logic of the code explained in detail:

1. The code sorts the input list of intervals in ascending order by their start time.
2. The code initializes several variables: `n`, `mergedList`, and `prev`. The `n` variable stores the number of intervals in the input list. The `mergedList` variable is a new list that will store the merged intervals. The `prev` variable is used to keep track of the previous interval.
3. The code uses a `for` loop to iterate through the sorted list of intervals, starting from the second interval.
4. In each iteration, the code checks if the current interval overlaps with the previous interval by comparing their start and end times.
5. If the current interval overlaps with the previous interval, the code merges them by updating the end time of the previous interval to be equal to the maximum of its end time and the end time of the current interval.
6. If the current interval does not overlap with the previous interval, the code adds the previous interval to the `mergedList` and updates the `prev` variable to point to the current interval.
7. After all intervals have been processed, the code adds the last interval to the `mergedList`.
8. Finally, the code returns the `mergedList`, which contains all merged intervals.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(`n log n`) where `n` is the number of intervals in the input list. This is because it uses sorting, which has a time complexity of O(`n log n`), and a single loop that iterates through all intervals, which has a time complexity of O(`n`).

### `Space Complexity`:
The space complexity of this code is O(`n`) because it uses a new list to store all merged intervals.

## Code:
```py
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals by their start time
        intervals.sort()
        
        # Initialize variables
        n = len(intervals)
        mergedList = []
        prev = intervals[0]
        
        # Iterate through the intervals
        for i in range(1,n):
            # If the current interval overlaps with the previous interval, merge them
            if intervals[i][0] <= prev[1] :
                prev[1] = max(prev[1], intervals[i][1])
            else:
                # Otherwise, add the previous interval to the merged list and update the prev variable
                mergedList.append(prev)
                prev = intervals[i]
        
        # Add the last interval to the merged list
        mergedList.append(prev)
        
        # Return the merged list of intervals
        return mergedList

```
