### [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)

## Explanation:
1. **Problem Statement**: The problem this code is trying to solve is to find the Hamming weight of a number. The Hamming weight of a number is the number of set bits (bits that are 1) in its binary representation.

2. **Function Signature**: The function `hammingWeight` takes an unsigned 32-bit integer `n` as input and returns an integer. The input `n` is the number for which we want to find the Hamming weight.

3. **Initialization**: The variable `count` is initialized to 0. This variable keeps track of the number of set bits in `n`.

4. **While Loop**: The while loop runs as long as `n` is not 0. In each iteration of the loop, the code performs two operations.

5. **Bitwise AND Operation**: The expression `n = n & (n-1)` is a bitwise AND operation that has the effect of flipping the least significant set bit of `n` to 0. This is because `n-1` will have all the bits same as `n` up to the least significant set bit, but the least significant set bit and all the bits after it will be flipped. So, when `n` and `n-1` are ANDed, all bits remain the same except the least significant set bit, which becomes 0.

6. **Count Increment**: After the bitwise AND operation, the code increments `count` by 1. This is because we have just removed a set bit from `n`.

7. **Result**: After the loop, `n` will be 0 because all set bits have been flipped to 0, and `count` will be the number of set bits in the original `n`. So, `count` is returned as the result.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(k), where k is the number of set bits in `n`. This is because the while loop runs once for each set bit in `n`.

### `Space Complexity`:
The space complexity of this code is O(1), as it uses a constant amount of space to store the count of set bits, regardless of the size of the input number.

## Code:
```cpp
// This class provides a solution to calculate the Hamming Weight (number of set bits) of a 32-bit unsigned integer.
class Solution {
public:
    // Function to calculate the Hamming Weight.
    int hammingWeight(uint32_t n) {
        int count = 0;

        // Iterate until all set bits are counted.
        while(n != 0){
            // Use the bitwise trick to unset the rightmost set bit in n and increment the count.
            n = n & (n-1);
            count++;
        }

        // Return the count of set bits in the 32-bit unsigned integer.
        return count;
    }
};
```
