### [Execute Cancellable Function With Delay](https://leetcode.com/problems/execute-cancellable-function-with-delay/description/)

## Explanation:
1. The `cancellable` function is defined as a function that takes a function (`fn`), an array of arguments (`args`), and a time delay (`t`) as arguments.
2. Inside the function, the `setTimeout` function is used to schedule the execution of `fn` after `t` milliseconds. The ID of this timeout is stored in a variable called `id`.
3. The function then returns an asynchronous function that can be used to cancel the scheduled execution of `fn`.
4. This returned function uses the `clearTimeout` method and the `id` variable to cancel the scheduled execution of `fn`.

## Time and Space Complexity:
### `Time Complexity`:
In terms of time complexity, this code has a time complexity of O(1) because it performs a constant number of operations regardless of the size of the input.

### `Space Complexity`:
In terms of space complexity, this code has a space complexity of O(1) because it uses a constant amount of memory regardless of the size of the input.

## Code:
```js
/**
 * This function takes a function, an array of arguments, and a time delay as arguments and returns an asynchronous function that can be used to cancel the execution of the input function.
 * @param {Function} fn - The function to execute after the time delay
 * @param {Array} args - The arguments to pass to the input function when it is executed
 * @param {number} t - The time delay in milliseconds before executing the input function
 * @return {Function} - An asynchronous function that can be used to cancel the execution of the input function
 */

var cancellable = function(fn, args, t) {
    // Use the setTimeout function to schedule the execution of the input function after the specified time delay
    // Store the ID of the timeout in a variable called id
    let id = setTimeout(() => {
        fn(...args);
    }, t);

    // Return an asynchronous function that can be used to cancel the execution of the input function
    return async function() {
        // Use the clearTimeout function and the id variable to cancel the scheduled execution of the input function
        clearTimeout(id);
    }
};

```
