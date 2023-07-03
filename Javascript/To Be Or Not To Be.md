### [To Be Or Not To Be](https://leetcode.com/problems/to-be-or-not-to-be/description/)

## Explanation:
1. The `expect` function is defined as a function that takes a value as an argument.
2. Inside the function, an object is returned with two methods: `toBe` and `notToBe`.
3. The `toBe` method takes a second value as an argument and compares it to the first value using the strict equality operator (`!==`). If the two values are not equal, it throws an error with the message "Not Equal". Otherwise, it returns `true`.
4. The `notToBe` method takes a second value as an argument and compares it to the first value using the strict equality operator (`===`). If the two values are equal, it throws an error with the message "Equal". Otherwise, it returns `true`.

## Time and Space Complexity:
### `Time Complexity`:
In terms of time complexity, this code has a time complexity of O(1) because it performs a constant number of operations regardless of the size of the input.

### `Space Complexity`:
In terms of space complexity, this code has a space complexity of O(1) because it uses a constant amount of memory regardless of the size of the input.

## Code:
```js
/**
 * This function takes a value as an argument and returns an object with two methods: toBe and notToBe.
 * The toBe method takes a second value as an argument and throws an error if the two values are not equal.
 * The notToBe method takes a second value as an argument and throws an error if the two values are equal.
 * @param {any} val - The first value to compare
 * @return {Object} - An object with two methods: toBe and notToBe
 */
var expect = function(val) {
    return {
        // Define the toBe method
        toBe: (val2) => {
            // If the two values are not equal, throw an error
            if (val !== val2) throw new Error("Not Equal");
            // Otherwise, return true
            else return true;
        },
        // Define the notToBe method
        notToBe: (val2) => {
            // If the two values are equal, throw an error
            if (val === val2) throw new Error("Equal");
            // Otherwise, return true
            else return true;
        }
    }
};

```
