### [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/description/?envType=study-plan-v2&envId=dynamic-programming)

## Dynamic Programming:
## Explanation:
This code is an implementation of a dynamic programming solution to the "Min Cost Climbing Stairs" problem. The goal of the problem is to find the minimum cost to reach the top of a staircase, where each step has an associated cost and you can advance one or two steps at a time.

Here's a detailed explanation of the main logic of the code, broken down into points:

1. The code defines a `Solution` class that contains two methods: `dynProg` and `minCostClimbingStairs`. The class also has an instance variable `dp`, which is used to store intermediate results for dynamic programming.
2. The `minCostClimbingStairs` method takes as input an array of integers `cost` and returns the minimum cost to reach the top of the staircase. This method initializes the `dp` array to have length `cost.length + 1` and then calls the `dynProg` method twice with arguments `n-1` and `n-2`, where `n` is the length of the `cost` array. It returns the minimum of these two values as the final result.
3. The `dynProg` method takes as input two arguments: an integer `i` and an array `cost`. This method implements a dynamic programming solution to find the minimum cost to reach step `i` in the staircase.
4. The `dynProg` method first checks if `i` is less than 0. If it is, it returns 0, since there is no cost to reach a step before the start of the staircase.
5. The method then checks if `i` is 0 or 1. If it is, it returns the corresponding value from the `cost` array, since these are the base cases for the problem.
6. The method then checks if `dp[i]` is not equal to 0. If it is not, this means that a value has already been computed for this subproblem and is stored in the `dp` array. In this case, the method simply returns the value stored in `dp[i]`.
7. If `dp[i]` is equal to 0, this means that a value has not yet been computed for this subproblem. In this case, the method computes the value by making two recursive calls to itself with arguments `i-1` and `i-2`. It then adds the minimum of these two values to `cost[i]` and stores the result in `dp[i]`.
8. Finally, the method returns the value stored in `dp[i]`, which is the minimum cost to reach step `i`.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(n), since it uses dynamic programming to avoid recomputing subproblems. Each subproblem is solved only once and its result is stored in the `dp` array for future use.

### `Space Complexity`:
The space complexity of this code is O(n), since it uses an array of length n+1 to store intermediate results.

## Code:
```java
class Solution {
    int[] dp;

    int dynProg(int i, int[] cost) {
        if (i < 0) {
            return 0;
        }
        if (i == 0 || i == 1) {
            return cost[i];
        }
        if (dp[i] != 0) {
            return dp[i];
        }
        dp[i] = cost[i] + Math.min(dynProg(i - 1, cost), dynProg(i - 2, cost));
        return dp[i];
    }

    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        dp = new int[cost.length + 1];
        return Math.min(dynProg(n - 1, cost), dynProg(n - 2, cost));
    }
}
```

## Iterative:
## Explanation:
This code is an optimized implementation of an iterative solution to the "Min Cost Climbing Stairs" problem. The goal of the problem is to find the minimum cost to reach the top of a staircase, where each step has an associated cost and you can advance one or two steps at a time.

Here's a detailed explanation of the main logic of the code, broken down into points:

1. The code defines a `Solution` class that contains a single method: `minCostClimbingStairs`.
2. The `minCostClimbingStairs` method takes as input an array of integers `cost` and returns the minimum cost to reach the top of the staircase.
3. The method first checks if the length of the `cost` array is less than or equal to 1. If it is, it returns 0, since there are no steps to climb.
4. The method then initializes two variables: `prevPrevCost` and `prevCost`. These variables are used to keep track of the minimum cost to reach the two most recent steps in the staircase.
5. The method enters a for loop that iterates from `i = 2` to `i = n - 1`. In each iteration of the loop, it calculates the minimum cost to reach step `i` by adding the value of `cost[i]` to the minimum of `prevPrevCost` and `prevCost`. It then updates these two variables to move them one step forward in the staircase.
6. After all iterations of the for loop are complete, the variables `prevPrevCost` and `prevCost` contain the minimum cost to reach the last step and second-to-last step in the staircase, respectively.
7. The method then returns the minimum of these two values as the final result.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(n), since it uses a for loop to iteratively calculate the minimum cost for each step in the staircase.

### `Space Complexity`:
The space complexity of this code is O(1), since it uses a constant amount of memory to store intermediate results.

## Code:
```java
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        if (n <= 1) return 0;
        
        int prevPrevCost = cost[0]; // Minimum cost to reach the 0-th step
        int prevCost = cost[1]; // Minimum cost to reach the 1st step
        
        // Iterate from the 2nd step to the last step
        for (int i = 2; i < n; i++) {
            int currentCost = cost[i] + Math.min(prevPrevCost, prevCost);
            prevPrevCost = prevCost;
            prevCost = currentCost;
        }
        
        // The minimum cost to reach the top can be either from the last step or the second-to-last step.
        return Math.min(prevPrevCost, prevCost);
    }
}
```
