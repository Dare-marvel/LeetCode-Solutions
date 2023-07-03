### [Execute Asynchronous Functions in Parallel](https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/description/)

## Explanation:
1. The `promiseAll` function is defined as an asynchronous function that takes an array of functions as an argument.
2. Inside the function, a `try` block is used to catch any errors that might occur.
3. Within the `try` block, the `map` method is used to call each function in the input array and create a new array of promises.
4. The `Promise.all` method is then used to wait for all promises in the array to resolve and their resolved values are stored in a variable called `results`.
5. The function then returns a new promise that resolves to the value of `results`, which is an array containing the resolved values of all input promises.
6. If any of the promises is rejected, an error is thrown within the `catch` block.

## Time and Space Complexity:
### `Time Complexity`:
In terms of time complexity, this code has a time complexity of O(n), where n is the number of functions in the input array. This is because it needs to call each function in the input array once and wait for all promises to resolve.

### `Space Complexity`:
In terms of space complexity, this code has a space complexity of O(n), where n is the number of functions in the input array. This is because it needs to create an array of promises and an array of resolved values, both of which have a length equal to the number of functions in the input array.

## Code:
```js
/**
 * This function takes an array of functions as an argument and returns a new promise that resolves to an array of the resolved values of the promises returned by the input functions.
 * @param {Array<Function>} functions - An array of functions that return promises
 * @return {Promise<any>} - A new promise that resolves to an array of the resolved values of the promises returned by the input functions
 */

var promiseAll = async function(functions) {
    try {
        // Use the map method to call each function in the input array and create a new array of promises
        // Use the Promise.all method to wait for all promises in the array to resolve and store their resolved values in a variable called results
        const results = await Promise.all(functions.map(fn => fn()));
        // Return the array of resolved values
        return results;
    } catch (error) {
        // If any of the promises is rejected, throw an error
        throw error;
    }
};

/**
 * This code calls the promiseAll function with an array containing one function that returns a promise that resolves to 42.
 * The resulting promise resolves to an array containing 42, which is printed to the console using the then method.
const promise = promiseAll([() => new Promise(res => res(42))])
promise.then(console.log); // [42]
 */
```
