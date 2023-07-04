### [Chunk Array](https://leetcode.com/problems/chunk-array/description/)

## Explanation:
1. The function takes an input array `arr` and a `size` as arguments.
2. It initializes an empty array `chunkedArr` to store the chunked arrays.
3. The function then enters a for loop, where it iterates through the input array from index 0 to `arr.length-size+1`, incrementing by `size` in each iteration.
4. In each iteration, the function uses the `slice` method to extract a subarray from the input array, starting from the current index `i` and ending at index `i+size`. This subarray is then pushed to the `chunkedArr`.
5. After the for loop, the function checks if the length of the input array is divisible by `size`. If it is not, it means that there are some remaining elements in the input array that have not been included in any chunk. The function then uses the `slice` method again to extract these remaining elements and push them as a separate chunk to the `chunkedArr`.
6. Finally, the function returns the `chunkedArr`.

I hope that helps!

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(n), where n is the length of the input array. This is because the for loop iterates through the entire input array once.

### `Space Complexity`:
The space complexity of this code is also O(n), where n is the length of the input array. This is because the function creates a new array `chunkedArr` to store the chunked arrays, and in the worst case, this array can have a length equal to the length of the input array.

## Code:
```js
/**
 * This function takes an array and a size as input and returns an array of arrays, where each subarray has the specified size.
 * @param {Array} arr - The input array to be chunked
 * @param {number} size - The size of each chunk
 * @return {Array[]} - An array of arrays, where each subarray has the specified size
 */
var chunk = function(arr, size) {
    // Initialize an empty array to store the chunked arrays
    let chunkedArr = []

    // Loop through the input array, incrementing by the size of each chunk
    for(let i=0;i<arr.length-size+1;i=i+size){
        // Slice the input array from the current index to the current index + size and push it to the chunked array
        chunkedArr.push(arr.slice(i,i+size))
    }

    // If the length of the input array is not divisible by the size, add the remaining elements as a separate chunk
    if(arr.length % size != 0){
        chunkedArr.push(arr.slice(arr.length-(arr.length % size),arr.length))
    }

    // Return the chunked array
    return chunkedArr;
};

```
