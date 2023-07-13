### [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/description/?envType=study-plan-v2&envId=dynamic-programming)

## Explanation:
This code is a Java program that calculates the nth Fibonacci number using recursion. Here is the main logic of the code:

1. The `Solution` class contains a single method `fib` that takes in an integer `n` as an argument.

2. The `fib` method checks if `n` is 0 or 1, and if so, returns `n` as the result.

3. If `n` is greater than 1, the method returns the sum of the results of calling itself with `n-1` and `n-2` as arguments.

4. This recursive process continues until the base case of `n` being 0 or 1 is reached, at which point the final result is returned.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(2^n) due to the exponential growth of recursive calls.

### `Space Complexity`:
The space complexity is O(n) due to the maximum depth of the recursion tree being n.

## Code:
```java
class Solution {
    // Method to calculate the nth Fibonacci number using recursion
    public int fib(int n) {
        // Base case: if n is 0 or 1, return n
        if (n == 0 || n == 1) {
            return n;
        }
        // Recursive case: return the sum of fib(n-1) and fib(n-2)
        return fib(n - 1) + fib(n - 2);
    }
}
```
