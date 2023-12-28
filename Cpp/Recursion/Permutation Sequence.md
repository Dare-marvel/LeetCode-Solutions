### [Permutation Sequence](https://leetcode.com/problems/permutation-sequence/description/)

## Explanation:
This C++ code is a solution to find the kth permutation sequence of the first n natural numbers. Here's a detailed explanation:

1. **Class and Function Definition**: The code begins with the definition of a `class` named `Solution`. Inside this class, a `public` function named `getPermutation` is defined. This function takes two `int` parameters, `n` and `k`, and returns a `std::string`. The purpose of this function is to generate the kth permutation of the first n natural numbers.

2. **Initialization**: Inside the function, an `int` variable `fact` is initialized to 1. This variable will be used to store the factorial of each number from 1 to `n-1`. A `std::vector<int>` named `numbers` is also initialized. This vector will store the first n natural numbers.

3. **Factorial Calculation and Number Storage**: A `for` loop is used to calculate the factorial of `n-1` and to fill the `numbers` vector with the first n natural numbers. The loop variable `i` starts at 1 and increments by 1 in each iteration until it reaches `n`. Inside the loop, `fact` is multiplied by `i`, and `i` is added to `numbers` using the `push_back` function.

4. **Answer String and Index Adjustment**: After the loop, a `std::string` named `ans` is initialized as an empty string. This string will be used to build the kth permutation sequence. The variable `k` is then decremented by 1. This is done to adjust for the fact that indexing in C++ starts at 0, not 1.

5. **Permutation Generation**: A `while` loop is used to generate the kth permutation sequence. The loop continues until `numbers` is empty. In each iteration, the number at index `k / fact` in `numbers` is converted to a string using the `std::to_string` function and added to `ans`. This number is then removed from `numbers` using the `erase` function. After this, `k` is updated to `k % fact`, and `fact` is updated to `fact / numbers.size()`. These updates ensure that the correct number is selected and removed in each iteration.

6. **Return Statement**: Once `numbers` is empty, the `while` loop breaks, and the function returns `ans`. At this point, `ans` contains the kth permutation sequence of the first n natural numbers.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of the code is **O(n^2)**. This is because the `erase` function, which is used inside the while loop, has a time complexity of O(n). Since this function is potentially called n times (in the worst-case scenario), the overall time complexity becomes O(n^2).

### `Space Complexity`:
The space complexity of the code is **O(n)**. This is due to the `numbers` vector, which stores n elements. No other data structures in the code depend on `n`, so the space complexity is linear.

## Code:
```cpp
#include <vector>
#include <string>

class Solution {
public:
    // Function to generate the kth permutation of the first n natural numbers
    std::string getPermutation(int n, int k) {
        int fact = 1;  // Variable to store the factorial value
        std::vector<int> numbers;  // Vector to store the numbers 1 to n

        // Calculate (n-1)! and populate the vector with numbers 1 to n
        for (int i = 1; i < n; ++i) {
            fact *= i;
            numbers.push_back(i);
        }

        // Add the last number (n) to the vector
        numbers.push_back(n);

        std::string ans = "";  // String to store the resulting permutation

        k -= 1;  // Adjust k to work with zero-based indexing

        // Generate the permutation
        while (true) {
            // Append the selected number to the result
            ans += std::to_string(numbers[k / fact]);
            
            // Remove the selected number from the vector
            numbers.erase(numbers.begin() + k / fact);

            // Break if all numbers are used
            if (numbers.size() == 0) 
                break;

            // Update k for the next iteration and recalculate factorial
            k %= fact;
            fact /= numbers.size();
        }

        return ans;  // Return the final permutation
    }
};

```
