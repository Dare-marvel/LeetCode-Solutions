### [Reverse Bits](https://leetcode.com/problems/reverse-bits/description/)

## Explanation:

## Time and Space Complexity:
### `Time Complexity`:

### `Space Complexity`:

## Code:
```cpp
class Solution {
public:
    // Function to check if the kth bit is set in the binary representation of A
    bool findifKthBitSet(int k, uint32_t A) {
        if ((1 << (k - 1)) & A)  // Check if the kth bit is set
            return true;
        return false;
    }

    // Function to reverse the bits in the binary representation of n
    uint32_t reverseBits(uint32_t n) {
        uint32_t ans = 0;  // Initialize the result

        // Iterate through each bit position (1 to 32)
        for (int i = 1; i <= 32; i++) {
            if (findifKthBitSet(i, n)) {  // If the current bit is set in n
                ans = ans | (1 << (32 - i));  // Set the corresponding bit in the result
            }
        }

        return ans;  // Return the reversed bits
    }
};
```
