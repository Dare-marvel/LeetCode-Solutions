### [Join Two Arrays by ID](https://leetcode.com/problems/join-two-arrays-by-id/description/)

##### [Object.assign() method](https://www.geeksforgeeks.org/javascript-object-assign-method/)

## Explanation:
1. The `join` function is defined as a function that takes two arrays of objects as arguments.
2. Inside the function, both input arrays are sorted by the `id` property of their objects using the `sort` method.
3. An empty array called `res` is created to store the result.
4. Two pointers (`i` and `j`) are initialized to keep track of the current position in each input array.
5. A `while` loop is entered that continues until one of the pointers reaches the end of its respective array.
6. Inside this loop, the `id` property of the current object in each input array is compared and either one or both objects (merged into a single object) are added to the `res` array. One or both pointers are also moved to their next position.
7. After this loop is done, there may be some remaining objects in one or both input arrays. Two additional loops are used to add these remaining objects to the `res` array.
8. The function then returns the `res` array as its result.

## Time and Space Complexity:
### `Time Complexity`:
In terms of time complexity, this code has a time complexity of O(n log n + m log m), where n is the length of the first input array and m is the length of the second input array. This is because it needs to sort both input arrays (which takes O(n log n) and O(m log m) time, respectively) and then process all objects in both arrays once (which takes O(n + m) time).

### `Space Complexity`:
In terms of space complexity, this code has a space complexity of O(n + m), where n is the length of the first input array and m is the length of the second input array. This is because it needs to create an array called `res` that can contain up to n + m objects.

## Code:
```js
/**
 * This function takes two arrays of objects as arguments and returns a new array that contains all objects from both input arrays, merged by their id property.
 * @param {Array<Object>} arr1 - The first array of objects
 * @param {Array<Object>} arr2 - The second array of objects
 * @return {Array<Object>} - A new array that contains all objects from both input arrays, merged by their id property
 */
var join = function(arr1, arr2) {
    // Sort both input arrays by the id property of their objects
    arr1.sort((a,b) => a.id - b.id);
    arr2.sort((a,b) => a.id - b.id);

    // Create an empty array to store the result
    const res = [];

    // Initialize two pointers to keep track of the current position in each input array
    let i = 0, j = 0;

    // Loop through both input arrays until one of them is fully processed
    while(i < arr1.length && j < arr2.length) {
        // If the current object in the first array has a smaller id than the current object in the second array
        if (arr1[i].id < arr2[j].id) {
            // Add the current object from the first array to the result and move its pointer to the next object
            res.push(arr1[i++]);
        } else if (arr1[i].id === arr2[j].id){
            // If the current objects in both arrays have the same id, merge them into a single object and add it to the result
            // Move both pointers to the next object in their respective arrays
            res.push(Object.assign(arr1[i++], arr2[j++]));
        } else {
            // If the current object in the second array has a smaller id than the current object in the first array
            // Add the current object from the second array to the result and move its pointer to the next object
            res.push(arr2[j++]);
        }
    }

    // If there are any remaining objects in the first array, add them to the result
    while(i < arr1.length) {
        res.push(arr1[i++]);
    }

    // If there are any remaining objects in the second array, add them to the result
    while(j < arr2.length) {
        res.push(arr2[j++]);
    }

    // Return the resulting array
    return res;
};

```
