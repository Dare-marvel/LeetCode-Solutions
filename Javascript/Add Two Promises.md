### [Add Two Promises](https://leetcode.com/problems/add-two-promises/description/)

## Explanation
Sure! Here's a detailed explanation of the main logic of the code:

1. The `addTwoPromises` function is defined as an asynchronous function that takes two promises as arguments.
2. Inside the function, the `await` keyword is used to wait for both promises to resolve and their resolved values are stored in variables called `res1` and `res2`.
3. The function then returns a new promise that resolves to the sum of `res1` and `res2`.
4. After defining the `addTwoPromises` function, it is called with two promises that resolve to 2.
5. The resulting promise resolves to 4, which is printed to the console using the `then` method.

## Time and Space Complexity:
### `Time Complexity`:
In terms of time complexity, this code has a time complexity of O(1) because it performs a constant number of operations regardless of the size of the input. The time it takes for the promises to resolve is not considered in the time complexity analysis because it depends on external factors.

### `Space Complexity`:
In terms of space complexity, this code has a space complexity of O(1) because it uses a constant amount of memory regardless of the size of the input.

## Code:
```js
/**
 * This function takes two promises as arguments and returns a new promise that resolves to the sum of the values resolved by the input promises.
 * @param {Promise} promise1 - The first promise
 * @param {Promise} promise2 - The second promise
 * @return {Promise} - A new promise that resolves to the sum of the values resolved by the input promises
 */
var addTwoPromises = async function(promise1, promise2) {
    // Use the await keyword to wait for both promises to resolve and store their resolved values in variables
    let res1 = await promise1;
    let res2 = await promise2;

    // Return the sum of the resolved values
    return res1 + res2;
};

/**
 * This code calls the addTwoPromises function with two promises that resolve to 2.
 * The resulting promise resolves to 4, which is printed to the console using the then method.
 */
addTwoPromises(Promise.resolve(2), Promise.resolve(2))
   .then(console.log); // 4

```
