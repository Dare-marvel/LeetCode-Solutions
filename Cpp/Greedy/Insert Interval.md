### [Insert Interval](https://leetcode.com/problems/insert-interval/description/)

## Approach and Intuition

The problem at hand is to insert a new interval into a list of non-overlapping intervals and merge any necessary intervals to maintain the list's non-overlapping property. Here's a detailed explanation of the approach and intuition behind the given code:

1. **Initialization**:
    - A result vector `res` is initialized to store the final merged intervals.
    - The size `n` of the input intervals vector is stored in `n`.
    - An index variable `i` is initialized to 0, which will be used to iterate through the intervals.

2. **Adding Non-Overlapping Intervals Before the New Interval**:
    - The first while loop iterates through the intervals until it finds an interval that might overlap with the `newInterval`.
    - The condition `intervals[i][1] < newInterval[0]` checks if the current interval ends before the new interval starts.
    - If true, the current interval is added to the result as it doesn't overlap with the new interval.
    - This process continues until an overlapping or adjacent interval is found.

3. **Merging Overlapping Intervals**:
    - The second while loop handles the merging of overlapping intervals.
    - The condition `intervals[i][0] <= newInterval[1]` checks if the current interval starts before or at the same time the new interval ends.
    - If true, the intervals overlap, and the new interval is updated to the minimum start and maximum end of the overlapping intervals.
    - This merging process ensures that all overlapping intervals are combined into a single interval.

4. **Adding the Merged Interval**:
    - Once all overlapping intervals are merged, the resulting new interval is added to the result vector.

5. **Adding Remaining Non-Overlapping Intervals**:
    - The final while loop adds any remaining intervals that come after the merged interval to the result.
    - These intervals do not overlap with the new interval as they start after the new interval ends.

6. **Return the Result**:
    - The merged intervals are returned as the final result.

### Points Summary

1. **Initialize result vector and iterator**:
    - `vector<vector<int>> res;`
    - `int n = intervals.size();`
    - `int i = 0;`

2. **Add intervals that end before the new interval starts**:
    - While loop with condition `intervals[i][1] < newInterval[0]`.
    - Add these intervals directly to `res`.

3. **Merge overlapping intervals**:
    - While loop with condition `intervals[i][0] <= newInterval[1]`.
    - Adjust `newInterval` to cover the range of overlapping intervals.

4. **Add the merged interval**:
    - Push the merged `newInterval` to `res`.

5. **Add remaining intervals**:
    - While loop to add intervals starting after the new merged interval.

6. **Return the result**:
    - `return res;`.

This approach ensures that all intervals are processed in a single pass, efficiently merging overlapping intervals while maintaining the non-overlapping property of the list.

## Time and Space Complexity:
### Time Complexity

The time complexity of the algorithm is \(O(n)\), where \(n\) is the number of intervals in the input list. Here’s the breakdown:

- The first while loop runs until it finds the first overlapping interval, which in the worst case can take \(O(n)\) iterations.
- The second while loop processes all overlapping intervals, and in the worst case, it might also run \(O(n)\) iterations if all intervals overlap with the new interval.
- The final while loop runs for the remaining intervals, which can again be \(O(n)\) in the worst case.
- Since each interval is processed at most twice (once in the first loop and once in the second or third loops), the overall complexity remains \(O(n)\).

### Space Complexity

The space complexity of the algorithm is \(O(n)\) as well. Here’s why:

- The result vector `res` stores the merged intervals, and in the worst case, it contains all the original intervals plus the new one.
- No additional space proportional to the input size is used except for the output vector.

## Code:
```cpp
class Solution {
public:
    // Function to insert a new interval into a list of intervals
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        // Resultant list of intervals after insertion
        vector<vector<int>> res;
        // Total number of intervals
        int n = intervals.size();

        // Initialize the index
        int i = 0;
        // Traverse through the intervals until the end of the interval is less than the start of the new interval
        while(i < n && intervals[i][1] < newInterval[0]){
            // Add the interval to the result
            res.push_back(intervals[i]);
            // Increment the index
            i++;
        }
        // Traverse through the intervals until the start of the interval is less than or equal to the end of the new interval
        while(i<n && intervals[i][0] <= newInterval[1]){
            // Update the start of the new interval to the minimum of the current interval start and the new interval start
            newInterval[0] = min(intervals[i][0],newInterval[0]);
            // Update the end of the new interval to the maximum of the current interval end and the new interval end
            newInterval[1] = max(intervals[i][1],newInterval[1]);
            // Increment the index
            i++;
        }
        // Add the new interval to the result
        res.push_back(newInterval);

        // Add the remaining intervals to the result
        while(i<n){
            res.push_back(intervals[i]);
            i++;
        }

        // Return the resultant list of intervals
        return res;
    }
};
```
