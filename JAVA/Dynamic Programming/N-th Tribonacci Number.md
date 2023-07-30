### [N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/description/?envType=study-plan-v2&envId=dynamic-programming)

## Explanation:
This code is an implementation of an iterative solution to the Tribonacci sequence problem. The goal of the problem is to find the n-th number in the Tribonacci sequence, where the sequence is defined as follows: `T(0) = 0`, `T(1) = 1`, `T(2) = 1`, and `T(n) = T(n-1) + T(n-2) + T(n-3)` for `n > 2`.

Here's a detailed explanation of the main logic of the code, broken down into points:

1. The code defines a `Solution` class that contains a single method: `tribonacci`.
2. The `tribonacci` method takes as input an integer `n` and returns the n-th number in the Tribonacci sequence.
3. The method first initializes four variables: `a`, `b`, `c`, and `i`. The variables `a`, `b`, and `c` are used to keep track of the last three numbers in the Tribonacci sequence, while `i` is used as a loop counter.
4. The method then checks if `n` is 0, 1, or 2. If it is, it returns the corresponding base case value for the Tribonacci sequence.
5. If `n` is greater than 2, the method enters a while loop that iterates until `i` is equal to `n - 2`. In each iteration of the loop, the method calculates the next number in the Tribonacci sequence by adding together the values of `a`, `b`, and `c`. It then updates the values of these variables to move them one position forward in the sequence and increments `i`.
6. After all iterations of the while loop are complete, the variable `c` contains the n-th number in the Tribonacci sequence.
7. The method then returns the value of `c`, which is the final result.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(n), since it uses a while loop to iteratively calculate each number in the Tribonacci sequence up to the n-th number.

### `Space Complexity`:
The space complexity of this code is O(1), since it uses a constant amount of memory to store intermediate results.

## Code:
```java
class Solution {
    public int tribonacci(int n) {
        // initialize 3 numbers
        int a = 0;
        int b = 1;
        int c = 1;
        int i = 0;
        
        // Base cases for n = 0, 1, and 2
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 1;
        }
        
        // Loop to calculate the nth tribonacci number
        while (i < n - 2) {
            int d = a + b + c;
            a = b;
            b = c;
            c = d;
            i++;
        }
        
        // Return the result for the nth tribonacci number.
        return c;
    }
}
```
