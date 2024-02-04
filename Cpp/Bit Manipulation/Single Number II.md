### [Single Number II](https://leetcode.com/problems/single-number-ii/)

## Explanation:

## Time and Space Complexity:
### `Time Complexity`:

### `Space Complexity`:

## Code:
```cpp
// This class provides a solution to find the single number occurring only once in an array.
class Solution {
public:
    // Function to find the single number.
    int singleNumber(vector<int>& nums) {
        int ans = 0;

        // Iterate through each bit of a 32-bit integer.
        for(int i=0; i<32; i++){
            int countodd = 0;

            // Count the number of occurrences of set bits at the i-th position in all array elements.
            for(int j=0; j<nums.size(); j++){
                if((1<<i) & nums[j]) 
                    countodd++;
            }

            // If the count of set bits is not a multiple of 3, set the corresponding bit in the result.
            if(countodd % 3) 
                ans = ans | (1<<i);
        }

        // The result contains the 32-bit integer representing the single number.
        return ans;
    }
};
```
