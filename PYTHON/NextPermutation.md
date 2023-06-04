### [Next Permutation](https://leetcode.com/problems/next-permutation/description/)
### [Articles to refer](https://www.geeksforgeeks.org/next-permutation/)


## Explanation
### Steps of the Algorithm:
Follow the steps below to implement the above observation:

* Iterate over the given array from end and find the first index (pivot) which doesn’t follow property of non-increasing suffix, (i.e,  arr[i] < arr[i + 1]).
* Check if pivot index does not exist 
* This means that the given sequence in the array is the largest as possible. So, swap the complete array.
* Otherwise, Iterate the array from the end and find for the successor of pivot in suffix.
* Swap the pivot and successor
* Minimize the suffix part by reversing the array from pivot + 1 till N.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20220908060940/Nextpermutation.png" >


## Time and Space Complexity:
### `Time Complexity`:
The time complexity of the `nextPermutation` function is `O(n)`, where `n` is the size of the input array. 
This is because the function consists of three loops that each take `O(n)` time to complete. The first loop finds the rightmost element that is smaller than its next element, the second loop finds the rightmost element that is greater than the pivot, and the third loop reverses a portion of the array. Each of these operations takes linear time.

### `Space Complexity`:
The space complexity of the `nextPermutation` function is `O(1)`, because it uses a constant amount of extra space to store variables such as `pivot` and `piIdx`.
## Code:
```c
// Function to swap two integers
void swap(int *a, int *b)
{
    int t;
    t = *a;
    *a = *b;
    *b = t;
}

// Function to reverse an array from a given index to the end
void arrRev(int n, int *arr, int left)
{
    while (left < n)
    {
        swap(&arr[left], &arr[n]);
        left++;
        n--;
    }
}

// Function to find the next lexicographic permutation of a given array of integers
void nextPermutation(int *nums, int numsSize)
{
    int pivot, piIdx;

    // Find the rightmost element that is smaller than its next element
    for (int i = numsSize - 2; i >= 0; i--)
    {
        if (nums[i] < nums[i + 1])
        {
            pivot = nums[i];
            piIdx = i;
            break;
        }
    }

    // Find the rightmost element that is greater than the pivot
    for (int i = numsSize - 1; i > piIdx; i--)
    {
        if (nums[i] > pivot)
        {
            // Swap the pivot with the found element
            swap(&nums[i], &nums[piIdx]);
            break;
        }
    }

    // Reverse the elements from piIdx + 1 to the end of the array
    arrRev(numsSize - 1, nums, piIdx + 1);
}

```
