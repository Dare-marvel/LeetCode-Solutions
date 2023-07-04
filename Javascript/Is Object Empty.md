### [Is Object Empty](https://leetcode.com/problems/is-object-empty/description/)

## Explanation:
The main logic of the code can be explained in the following points:

1. The `isEmpty` function takes an input object or array `obj` as an argument.
2. The function uses the `Object.keys` method to get an array of the keys of the input object or array.
3. It then checks if the length of this array is equal to 0. If it is, it means that the input object or array is empty, so the function returns `true`. Otherwise, it returns `false`.

I hope that helps!

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(n), where n is the number of keys in the input object or array. This is because the `Object.keys` method has a time complexity of O(n).

### `Space Complexity`:
The space complexity of this code is also O(n), where n is the number of keys in the input object or array. This is because the `Object.keys` method returns a new array with a length equal to the number of keys in the input object or array.

## Code:
```js
/**
 * @param {Object | Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    return Object.keys(obj).length === 0;
};
```
