### [Total Hamming Distance](https://leetcode.com/problems/total-hamming-distance/description/)

## Explanation:
1. **Class Definition**: The code is written in C++ and defines a class named `Solution`.

2. **Function Definition**: Inside this class, a public function `totalHammingDistance` is defined. This function takes a vector of integers (`nums`) as input and returns an integer.

3. **Variable Initialization**: Inside the function, two variables `ans` and `i` are initialized. `ans` is used to store the total Hamming distance, and `i` is used as a counter in the first for loop.

4. **First For Loop**: The first for loop runs 32 times. This is because the maximum number of bits required to represent an integer in binary form is 32.

5. **Counters**: Inside the first loop, two counters `count0` and `count1` are initialized to count the number of 0s and 1s in the `i`th bit position of all numbers in the `nums` vector.

6. **Second For Loop**: The second for loop iterates over the `nums` vector. For each number in the vector, it checks if the `i`th bit is 0 or 1. If it's 0, `count0` is incremented; if it's 1, `count1` is incremented.

7. **Hamming Distance Calculation**: After counting the number of 0s and 1s in the `i`th bit position of all numbers, the product of `count0` and `count1` is added to `ans`. This is based on the principle that the Hamming distance between two binary numbers is the number of bit positions at which the corresponding bits are different. Since `count0` and `count1` represent the count of numbers having `i`th bit as 0 and 1 respectively, their product will give the count of pairs having different bits at `i`th position.

8. **Return Statement**: After all bit positions have been checked, the function returns `ans`, which represents the total Hamming distance for all pairs of numbers in the `nums` vector.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of the code is O(32n), where n is the size of the `nums` vector. This is because there are two nested loops: the outer loop runs 32 times, and the inner loop runs `n` times. However, since 32 is a constant, we can simplify the time complexity to O(n).

### `Space Complexity`:
The space complexity of the code is O(1), as the space required does not increase with the size of the input vector. The code only uses a fixed amount of space to store variables and counters, regardless of the size of the input.

## Code:
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    // Function to calculate the total Hamming distance among all pairs of integers in the given vector
    int totalHammingDistance(vector<int>& nums) {
        long long ans = 0;  // Initialize the result

        // Iterate through each bit position (0 to 31)
        for (int i = 0; i < 32; i++) {
            long long count0 = 0, count1 = 0;  // Initialize counts for 0s and 1s at the current bit position

            // Iterate through each integer in the vector
            for (int j = 0; j < nums.size(); j++) {
                // Check if the current bit is 0
                if (((1 << i) & nums[j]) == 0)
                    count0++;  // Increment count0 if the bit is 0
                else
                    count1++;  // Increment count1 if the bit is 1
            }

            // Add the product of count0 and count1 to the result
            ans += count0 * count1;
        }

        return ans;  // Return the total Hamming distance
    }
};
```
