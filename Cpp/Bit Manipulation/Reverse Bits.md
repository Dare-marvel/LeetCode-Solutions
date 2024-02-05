### [Reverse Bits](https://leetcode.com/problems/reverse-bits/description/)

## Explanation:
1. **Class Definition**: The code is encapsulated within a class named `Solution`. This is a common practice in C++ to organize related functions and data.

2. **Function `findifKthBitSet(int k,uint32_t A)`**: This function checks if the `k`-th bit of the number `A` is set (i.e., if it's 1).

    - **Bitwise Shift**: `1<<(k-1)` shifts 1 to the left `k-1` times. This operation effectively creates a number that has its `k`-th bit set.
    
    - **Bitwise AND**: The bitwise AND operation `&` is then used to check if the `k`-th bit of `A` is set. If it is, the result will be non-zero (true), otherwise, it will be zero (false).

3. **Function `reverseBits(uint32_t n)`**: This function reverses the bits of the number `n`.

    - **Initialization**: The variable `ans` is initialized to 0. This will hold the final result.

    - **Loop**: A for loop runs from 1 to 32, inclusive. For each `i`, it checks if the `i`-th bit of `n` is set using the `findifKthBitSet(i,n)` function.

    - **Bit Manipulation**: If the `i`-th bit is set, it sets the `(32-i)`-th bit of `ans`. This is done using the bitwise OR operation `|` and the bitwise shift operation `<<`. This effectively reverses the bits of `n`.

    - **Return Value**: Finally, `ans` is returned. This is the number `n` with its bits reversed.



## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(1). This is because the number of bits in `n` is fixed (32 bits), so the loop in `reverseBits` always iterates 32 times.

### `Space Complexity`:
The space complexity of this code is also O(1). This is because a fixed amount of space is used. The space does not increase with the size of the input number `n`.

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
