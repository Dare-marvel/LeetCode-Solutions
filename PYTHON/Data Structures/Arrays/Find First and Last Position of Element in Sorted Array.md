### [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/)

## Explanation:
1. **Function Definition**: The function `searchRange` is defined with two parameters: `nums` (a list of integers) and `target` (an integer).

2. **Frequency Dictionary**: A dictionary `freq` is created to store the frequency of each number in the `nums` list. This is done by iterating over the `nums` list and for each number, if it is not already in `freq`, it is added with a count of 1. If it is already in `freq`, its count is incremented by 1.

3. **Target Check**: If the `target` is not in `freq`, it means the `target` is not present in the `nums` list. In this case, the function returns `[-1, -1]` indicating that the `target` is not found.

4. **Start Position Calculation**: If the `target` is present in `freq`, the start position of the `target` in the sorted array is calculated. This is done by initializing a variable `start` to 0 and then iterating over the keys of `freq`. For each key that is less than the `target`, its frequency is added to `start`. This gives the starting position of the `target` in the sorted array.

5. **End Position Calculation**: The end position of the `target` in the sorted array is calculated as `start + freq[target] - 1`. This is because the `target` appears `freq[target]` times in the array, so its end position will be `start + freq[target] - 1`.

6. **Return Statement**: Finally, the function returns a list containing the start and end positions of the `target` in the sorted array.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of the code is O(n), where n is the length of the `nums` list. This is because the code iterates over the `nums` list once to build the `freq` dictionary, and then iterates over the keys of `freq` once to calculate the start position.

### `Space Complexity`:
The space complexity of the code is O(n), where n is the length of the `nums` list. This is because the `freq` dictionary can potentially store n key-value pairs in the worst-case scenario where all numbers in the `nums` list are distinct.

## Code:
```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Initialize a dictionary to store the frequency of each number in the input list
        freq = {}
        
        # Iterate through the input list
        for i in range(len(nums)):
            # If the number is not already in the frequency dictionary, add it with a frequency of 1
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                # If the number is already in the dictionary, increment its frequency
                freq[nums[i]] += 1

        # If the target number is not in the frequency dictionary, it means it's not present in the input list
        # So return [-1, -1] to indicate that
        if target not in freq:
            return [-1, -1]

        # Initialize a variable to keep track of the starting index of the target number in the sorted list
        start = 0
        
        # Iterate through the keys of the frequency dictionary
        for num in freq.keys():
            # If the current number is less than the target, increment the starting index by the frequency of the current number
            if num < target:
                start += freq[num]

        # Return the range of indices where the target number occurs in the input list
        return [start, start + freq[target] - 1]

```
