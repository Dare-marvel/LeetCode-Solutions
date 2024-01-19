### [Count Good Numbers](https://leetcode.com/problems/count-good-numbers/description/)

## Explanation:
[Binary Exponentiation](https://www.geeksforgeeks.org/binary-exponentiation-for-competitive-programming/)

**Count Good Numbers Function**: The `countGoodNumbers` function calculates the count of good numbers of length `n`. It first calculates the count of odd and even indexed digits . A good digit string has five possible digits at each even index and four possible digits at each odd index. Then it calculates the count of good numbers as `(5^even * 4^odd) % MOD`.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is **O(log n)** because the power function runs in logarithmic time and it's called a constant number of times.

### `Space Complexity`:
The space complexity of this code is **O(log n)** because the power function uses recursive calls which are stored on the call stack, and in the worst case, it can go up to log n levels deep.

## Code:
```cpp
class Solution {
public:
    // Constant representing the modulo value
    const int MOD = 1000000007;

    // Recursive function to calculate x^y modulo MOD
    long long int power(long long int x, long long int y) {
        // Base case: if y is 0, return 1
        if (y == 0) return 1;

        // Recursively calculate x^(y/2)
        long long int res = power(x, y / 2);
        
        // Square the result to calculate x^y
        res = (res * res) % MOD;

        // If y is odd, multiply the result by x once more
        if (y % 2 == 1) res = (res * x) % MOD;
        
        // Return the calculated result
        return res;
    }

    // Function to count good numbers based on the given logic
    int countGoodNumbers(long long n) {
        // Calculate the number of odd and even positions
        long long int odd = n / 2;
        long long int even = n - odd;

        // Calculate and return the count of good numbers
        return (power(5, even) * power(4, odd)) % MOD;
    }
};
```
