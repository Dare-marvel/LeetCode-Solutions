### [Counter](https://leetcode.com/problems/counter/description/)
### [Reference to Closures](https://www.w3schools.com/js/js_function_closures.asp)

## Explanation:
1. The `createCounter` function is defined as a function that takes a number (`n`) as an argument.
2. Inside the function, a new function is returned that, when called, returns the current value of `n` and then increments it using the post-increment operator (`++`).

## Time and Space Complexity:
### `Time Complexity`:
In terms of time complexity, this code has a time complexity of O(1) because it performs a constant number of operations regardless of the size of the input.

### `Space Complexity`:
In terms of space complexity, this code has a space complexity of O(1) because it uses a constant amount of memory regardless of the size of the input.

## Code:
```js
/**
 * This function takes a number as an argument and returns a new function that, when called, returns the current value of the input number and then increments it.
 * @param {number} n - The initial value of the counter
 * @return {Function} - A new function that, when called, returns the current value of the counter and then increments it
 */

var createCounter = function(n) {
    // Return a new function that, when called, returns the current value of n and then increments it
    return function() {
        return n++;
    };
};
```
