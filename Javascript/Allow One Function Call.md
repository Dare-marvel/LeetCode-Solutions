### [Allow One Function Call](https://leetcode.com/problems/allow-one-function-call/description/)

## Explanation:
This code defines a function `once` that takes a function `fn` as an argument and returns a new function. The returned function, when invoked, will call the function `fn` with the provided arguments only once. Subsequent calls to the returned function will return `undefined`.

Here's a detailed explanation of the code:
1. The `once` function takes a single argument, `fn`, which is expected to be a function.
2. The `once` function declares a variable `freq` and initializes it to 0. This variable is used to keep track of how many times the returned function has been called.
3. The `once` function returns an anonymous function that takes any number of arguments (represented by the `...args` syntax).
4. When the returned function is invoked, it increments the value of `freq` by 1.
5. If the value of `freq` is equal to 1, the returned function calls `fn` with the provided arguments (using the spread syntax `...args`) and returns its result.
6. If the value of `freq` is not equal to 1, the returned function returns `undefined`.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(1) because all operations inside the returned function take constant time.

### `Space Complexity`:
The space complexity is also O(1) because only a constant amount of additional memory is used (for the `freq` variable).


## Code:
```js
/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    // Declare a variable to keep track of how many times the returned function has been called
    let freq = 0;
    // Return a new function
    return function(...args){
        // Increment the call count
        freq += 1;
        // If this is the first time the function is being called
        if(freq === 1){
            // Call the original function with the provided arguments and return its result
            return fn(...args);
        }
        // If the function has already been called once, return undefined
        return undefined;
    }
};

```
