### [Nested Array Generator](https://leetcode.com/problems/nested-array-generator/description/)

## Explanation:
1. The `inorderTraversal` function is defined as a generator function that takes an array as an argument.
2. Inside the function, the `flat` method is used to flatten the input array to any depth.
3. A `for...of` loop is entered to iterate over the elements of the flattened array.
4. Inside this loop, the `yield` keyword is used to yield each element of the array.
5. When this function is called, it returns a generator object that can be used to iterate over the elements of the input array in order.

## Time and Space Complexity:
### `Time Complexity`:
In terms of time complexity, this code has a time complexity of O(n), where n is the total number of elements in the input array (including elements in nested arrays). This is because it needs to flatten the input array (which takes O(n) time) and then iterate over all its elements once (which also takes O(n) time).

### `Space Complexity`:
In terms of space complexity, this code has a space complexity of O(n), where n is the total number of elements in the input array (including elements in nested arrays). This is because it needs to create a new flattened array that contains all elements of the input array.

## Code:
```js
/**
 * This function takes an array as an argument and returns a generator object that yields the elements of the input array in order.
 * @param {Array} arr - The input array
 * @return {Generator} - A generator object that yields the elements of the input array in order
 */

var inorderTraversal = function*(arr) {
    // Flatten the input array to any depth using the flat method
    arr = arr.flat(Infinity);

    // Use a for...of loop to iterate over the elements of the flattened array
    for (num of arr) {
        // Yield each element of the array using the yield keyword
        yield num;
    }
};
```
