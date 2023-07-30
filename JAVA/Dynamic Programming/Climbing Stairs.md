### [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/description/?envType=study-plan-v2&envId=dynamic-programming)

## Explanation:
This code is an implementation of an iterative solution to the "Climbing Stairs" problem. The goal of the problem is to find the number of distinct ways to climb to the top of a staircase with n steps, where you can advance one or two steps at a time.

Here's a detailed explanation of the main logic of the code, broken down into points:

1. The code defines a `Solution` class that contains a single method: `climbStairs`.
2. The `climbStairs` method takes as input an integer `n` and returns the number of distinct ways to climb to the top of a staircase with n steps.
3. The method first checks if `n` is 0 or 1. If it is, it returns 1, since there is only one way to climb a staircase with 0 or 1 steps.
4. The method then initializes two variables: `prev` and `curr`. These variables are used to keep track of the number of distinct ways to climb to the two most recent steps in the staircase.
5. The method enters a for loop that iterates from `i = 2` to `i = n`. In each iteration of the loop, it calculates the number of distinct ways to climb to step `i` by adding together the values of `prev` and `curr`. It then updates these two variables to move them one step forward in the staircase.
6. After all iterations of the for loop are complete, the variable `curr` contains the number of distinct ways to climb to the top of the staircase.
7. The method then returns the value of `curr`, which is the final result.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(n), since it uses a for loop to iteratively calculate the number of distinct ways to climb each step in the staircase.

### `Space Complexity`:
The space complexity of this code is O(1), since it uses a constant amount of memory to store intermediate results.

## Code:
```java
class Solution {
    public int climbStairs(int n) {
        // Base cases: There is only one way to climb 0 or 1 stair.
        if (n == 0 || n == 1) {
            return 1;
        }
        
        // Initialize variables to keep track of the previous and current ways to climb stairs.
        int prev = 1, curr = 1;
        
        // Iterate from the 2nd stair to the nth stair, calculating the number of ways to reach each stair.
        for (int i = 2; i <= n; i++) {
            int temp = curr;
            curr = prev + curr; // Calculate the current number of ways to climb the current stair.
            prev = temp; // Update the 'prev' variable for the next iteration.
        }
        
        // The 'curr' variable holds the number of ways to reach the nth stair, so return it.
        return curr;
    }
}
```
