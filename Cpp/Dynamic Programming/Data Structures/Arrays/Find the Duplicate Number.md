### [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/description/)

## Explanation:
This is a C++ implementation of the Floyd's Tortoise and Hare (Cycle Detection) algorithm to solve the problem of finding the duplicate number in an array of integers. Here is the main logic of the code explained in detail:

1. The algorithm uses two pointers, `slow` and `fast`, to traverse the array. The `slow` pointer moves one step at a time, while the `fast` pointer moves two steps at a time.
2. When the two pointers meet, it means that there is a cycle in the array. The `fast` pointer is then reset to the beginning of the array and both pointers move one step at a time until they meet again.
3. The meeting point is the duplicate number.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this algorithm is O(n), where n is the number of elements in the array. This is because both pointers traverse the array at most twice, so the total number of steps taken by both pointers is at most 2n.

### `Space Complexity`:
The space complexity of this algorithm is O(1), as it only uses two pointers and a few variables to keep track of the current state of the algorithm. No additional data structures are used.

## Code:
```cpp
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        // Initialize slow and fast pointers
        int slow = nums[0];
        int fast = nums[0];
        
        // Move slow pointer one step at a time and fast pointer two steps at a time
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);
        
        // Reset fast pointer to the beginning of the array
        fast = nums[0];
        
        // Move both pointers one step at a time until they meet again
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        
        // The meeting point is the duplicate number
        return slow;
    }
};
```
