### [Single Number III](https://leetcode.com/problems/single-number-iii/)

## Explanation:
1. **Problem Statement**: The problem this code is trying to solve is to find two numbers that appear only once in an array, while all other numbers appear twice.

2. **XOR Operation**: The XOR operation is a binary operation that takes two bits and returns 1 if the two bits are different; otherwise, it returns 0. In the context of this problem, the XOR operation is used to find the two numbers that appear only once in the array.

3. **First Loop**: The first for loop in the `singleNumber` function goes through each number in the input array `nums` and performs an XOR operation with the `ans` variable. Since XOR of all numbers that appear twice will be 0 and XOR of a number with 0 is the number itself, at the end of this loop, `ans` will be the XOR of the two numbers that appear only once.

4. **Bit Manipulation**: The line `ans = ans & ~(ans-1);` is a bit manipulation trick to get the rightmost set bit of `ans`. This set bit is in the position where the two single numbers differ.

5. **Second Loop**: The second for loop divides all numbers into two groups, one with the rightmost set bit of `ans` and one without it. It then performs XOR operations within each group. Since all numbers appearing twice will XOR to 0 within their group, `num1` and `num2` will be the two single numbers at the end of this loop.

6. **Result Preparation**: The two single numbers are then added to the result vector, sorted, and returned.

This code is a great example of how bit manipulation can be used to solve problems efficiently. It cleverly uses the properties of the XOR operation and bit manipulation to find the two single numbers in one pass through the array. However, it also assumes that there are exactly two single numbers in the array, which might not always be the case. Therefore, it's important to understand the problem constraints and assumptions when implementing and using this code. I hope this explanation helps you understand the code better! Let me know if you have any other questions.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(n), where n is the size of the input array. This is because the code goes through the array twice, once to find the XOR of the two single numbers and once to find the two single numbers.

### `Space Complexity`:
The space complexity of this code is O(1), as it uses a constant amount of space to store the two single numbers and the XOR result, regardless of the size of the input array.
## Code:
```cpp
// This class provides a solution to find two non-repeating numbers in an array.
class Solution {
public:
    // Function to find two non-repeating numbers.
    vector<int> singleNumber(vector<int>& nums) {
        long long ans = 0;

        // XOR all elements in the array to find the XOR of the two non-repeating numbers.
        for(int i=0; i<nums.size(); i++){
            ans ^= nums[i];
        }

        // Find the rightmost set bit in the XOR result.
        ans = ans & ~(ans-1);

        // Initialize two variables to store the non-repeating numbers.
        int num1 = 0, num2 = 0;

        // Iterate through the array again to separate the two non-repeating numbers based on the set bit.
        for(int i=0; i<nums.size(); i++){
            if(ans & nums[i]) 
                num1 ^= nums[i];
            else 
                num2 ^= nums[i];
        }

        // Create a vector to store the results and sort it.
        vector<int> result;
        result.push_back(num1);
        result.push_back(num2);
        sort(result.begin(), result.end());

        // Return the vector containing the two non-repeating numbers.
        return result;
    }
};
```
