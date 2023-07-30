### [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/description/?envType=study-plan-v2&envId=dynamic-programming)

## Naive approach:
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

## Dynamic Programming
## Explanation
This code is an implementation of a dynamic programming solution to the Fibonacci sequence problem. The goal of the problem is to find the n-th number in the Fibonacci sequence, where the sequence is defined as follows: `F(0) = 0`, `F(1) = 1`, and `F(n) = F(n-1) + F(n-2)` for `n > 1`.

Here's a detailed explanation of the main logic of the code, broken down into points:

1. The code defines a `Solution` class that contains two methods: `dynProg` and `fib`.
2. The `fib` method takes as input an integer `n` and returns the n-th number in the Fibonacci sequence. This method creates an array `dp` of length `n+1` and fills it with the value `-1`. It then calls the `dynProg` method with arguments `n` and `dp` and returns the result.
3. The `dynProg` method takes as input two arguments: an integer `n` and an array `dp`. This method implements a dynamic programming solution to the Fibonacci sequence problem.
4. The `dynProg` method first checks if `n` is 0 or 1. If it is, it returns `n`, since these are the base cases of the Fibonacci sequence.
5. The method then checks if `dp[n]` is not equal to `-1`. If it is not, this means that a value has already been computed for this subproblem and is stored in the `dp` array. In this case, the method simply returns the value stored in `dp[n]`.
6. If `dp[n]` is equal to `-1`, this means that a value has not yet been computed for this subproblem. In this case, the method computes the value by making two recursive calls to itself with arguments `n-1` and `n-2`. It then adds these two values together and stores the result in `dp[n]`.
7. Finally, the method returns the value stored in `dp[n]`, which is the n-th number in the Fibonacci sequence.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(n), since it uses dynamic programming to avoid recomputing subproblems. Each subproblem is solved only once and its result is stored in the `dp` array for future use.

### `Space Complexity`:
The space complexity of this code is also O(n), since it uses an array of length `n+1` to store intermediate results.

## Code:
```java
class Solution {
    // Recursive function for calculating the Fibonacci number
    // using Dynamic Programming with memoization.
    int dynProg(int n, int[] dp) {
        // Base cases: The first two Fibonacci numbers are 0 and 1.
        if (n == 0 || n == 1) {
            return n;
        }
        
        // If the result for the current 'n' has already been calculated,
        // then return it directly from the memoized array.
        if (dp[n] != -1) {
            return dp[n];
        }
        
        // Calculate the Fibonacci number for 'n' by recursively calling
        // the function for 'n-1' and 'n-2', and then storing the result in dp[n].
        dp[n] = dynProg(n - 1, dp) + dynProg(n - 2, dp);
        
        // Return the result for 'n'.
        return dp[n];
    }
    
    // Wrapper function to initialize the memoization array and call the
    // dynamic programming function for calculating the nth Fibonacci number.
    public int fib(int n) {
        // Initialize the memoization array 'dp' with -1, indicating that no
        // Fibonacci number has been calculated yet.
        int[] dp = new int[n + 1];
        Arrays.fill(dp, -1);
        
        // Call the dynProg function to calculate the nth Fibonacci number
        // using dynamic programming with memoization.
        return dynProg(n, dp);
    }
}
```
