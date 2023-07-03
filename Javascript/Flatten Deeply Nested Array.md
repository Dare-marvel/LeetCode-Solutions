### [Flatten Deeply Nested Array](https://leetcode.com/problems/flatten-deeply-nested-array/description/)

## Explanation:
Sure! Here's a detailed explanation of the main logic of the code:

1. The `flat` function is defined as a function that takes an array (`arr`) and a depth (`n`) as arguments.
2. Inside the function, an `if` statement is used to check if `n` is equal to `0`. If it is, the function returns `arr` unchanged.
3. An empty array called `ans` is created to store the result.
4. A `for` loop is entered to iterate over the elements of `arr`.
5. Inside this loop, an `if` statement is used to check if `n` is greater than `0` and if the current element of `arr` is an array.
6. If both conditions are true, the `flat` function is recursively called with this element and a decremented value of `n`. The spread operator (`...`) is then used to add all elements of the resulting array to `ans`.
7. If either condition is not true, the current element of `arr` is added to `ans`.
8. After this loop is done, the function returns `ans` as its result.

## Time and Space Complexity:
### `Time Complexity`:
In terms of time complexity, this code has a time complexity of O(n), where n is the total number of elements in the input array (including elements in nested arrays). This is because it needs to process all elements of the input array once for each level of depth.

### `Space Complexity`:
In terms of space complexity, this code has a space complexity of O(n), where n is the total number of elements in the input array (including elements in nested arrays). This is because it needs to create a new flattened array that contains all elements of the input array.

## Code:
```js
/**
 * This function takes an array and a depth as arguments and returns a new array that is the result of flattening the input array to the specified depth.
 * @param {any[]} arr - The input array to flatten
 * @param {number} depth - The depth to which the input array should be flattened
 * @return {any[]} - A new array that is the result of flattening the input array to the specified depth
 */

var flat = function (arr, n) {
    // If the depth is 0, return the input array unchanged
    if (n == 0) {
        return arr;
    }

    // Create an empty array to store the result
    let ans = [];

    // Use a for loop to iterate over the elements of the input array
    for (let i = 0; i < arr.length; i++) {
        // If the current depth is greater than 0 and the current element is an array
        if (n > 0 && Array.isArray(arr[i])) {
            // Recursively call the flat function with the current element and a decremented depth
            // Use the spread operator to add all elements of the resulting array to the ans array
            ans.push(...flat(arr[i], n - 1));
        } else {
            // If the current element is not an array, add it to the ans array
            ans.push(arr[i]);
        }
    }

    // Return the resulting array
    return ans;
};
```
