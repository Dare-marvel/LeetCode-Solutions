### [Sort By](https://leetcode.com/problems/sort-by/description/)

## Explanation:
The main logic of the code can be explained in the following points:

1. The `sortBy` function takes an input array `arr` and a function `fn` as arguments.
2. If the length of the input array is less than or equal to 1, the function returns the input array as it is already sorted.
3. The function then calculates the middle index of the input array and uses the `slice` method to split it into two halves: `left` and `right`.
4. The function then recursively calls itself on each half to sort them.
5. Once the two halves are sorted, the function calls the `merge` function to merge them into a single sorted array.
6. The `merge` function takes two sorted arrays `left` and `right`, and a function `fn` as arguments.
7. It initializes an empty array `resultArray` and two indices `leftIndex` and `rightIndex` to keep track of the current position in each input array.
8. The function then enters a while loop, where it iterates until either `leftIndex` is equal to the length of the `left` array or `rightIndex` is equal to the length of the `right` array.
9. In each iteration, the function compares the values at the current indices of the two input arrays using the given function `fn`. If the value at the current index of the `left` array is less than the value at the current index of the `right` array, it pushes that value to the `resultArray` and increments `leftIndex`. Otherwise, it pushes the value at the current index of the `right` array to the `resultArray` and increments `rightIndex`.
10. After the while loop, if there are any remaining values in either input array, they are concatenated to the end of the `resultArray`.
11. Finally, the function returns the sorted `resultArray`.

I hope that helps!

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(n log n), where n is the length of the input array. This is because merge sort has a time complexity of O(n log n).

### `Space Complexity`:
The space complexity of this code is also O(n), where n is the length of the input array. This is because merge sort requires additional space to store the two halves of the input array and to merge them.

## Code:
```js
/**
 * This function takes an array and a function as input and returns a new array sorted according to the function.
 * @param {Array} arr - The input array to be sorted
 * @param {function} fn - The function to use for sorting
 * @return {Array} - A new array sorted according to the function
 */
var sortBy = function(arr, fn) {
    // Base case: if the input array has length less than or equal to 1, return it
    if (arr.length <= 1) {
        return arr;
    }

    // Split the input array into two halves
    const middle = Math.floor(arr.length / 2);
    const left = arr.slice(0, middle);
    const right = arr.slice(middle);

    // Recursively sort the two halves using the sortBy function
    const sortedLeft = sortBy(left, fn);
    const sortedRight = sortBy(right, fn);

    // Merge the two sorted halves using the merge function
    return merge(sortedLeft, sortedRight, fn);
};

/**
 * This function takes two sorted arrays and a function as input and returns a new array that is the result of merging the two input arrays in sorted order according to the function.
 * @param {Array} left - The first sorted input array
 * @param {Array} right - The second sorted input array
 * @param {function} fn - The function to use for sorting
 * @return {Array} - A new array that is the result of merging the two input arrays in sorted order according to the function
 */
function merge(left, right, fn) {
    // Initialize an empty array to store the result
    let resultArray = [], leftIndex = 0, rightIndex = 0;

    // Concatenate values into the resultArray in sorted order according to the function
    while (leftIndex < left.length && rightIndex < right.length) {
        if (fn(left[leftIndex]) < fn(right[rightIndex])) {
            resultArray.push(left[leftIndex]);
            leftIndex++;
        } else {
            resultArray.push(right[rightIndex]);
            rightIndex++;
        }
    }

    // Concatenate any remaining values from the left or right arrays
    return resultArray
        .concat(left.slice(leftIndex))
        .concat(right.slice(rightIndex));
}

```
