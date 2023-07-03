### [Array Prototype Last](https://leetcode.com/problems/array-prototype-last/description/)

## Explanation:
1. The `last` method is added to the `Array` prototype.
2. This method can be called on any array and returns its last element or `-1` if the array is empty.
3. Inside the method, an `if` statement is used to check if the array is empty by comparing its `length` property to `0`.
4. If the array is empty, the method returns `-1`.
5. Otherwise, the method returns the last element of the array using its `length` property and bracket notation.

## Time and Space Complexity:
### `Time Complexity`:
In terms of time complexity, this code has a time complexity of O(1) because it performs a constant number of operations regardless of the size of the input array.

### `Space Complexity`:
In terms of space complexity, this code has a space complexity of O(1) because it uses a constant amount of memory regardless of the size of the input array.

## Code:
```js
/**
 * This code adds a new method called last to the Array prototype.
 * This method returns the last element of the array or -1 if the array is empty.
 */
Array.prototype.last = function() {
    // Check if the array is empty
    if (this.length === 0) {
        // If the array is empty, return -1
        return -1;
    } else {
        // If the array is not empty, return its last element
        return this[this.length - 1];
    }
};

```
