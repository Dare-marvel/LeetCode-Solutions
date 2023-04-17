### [Median Of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)

## Key Insights:
The code uses two iterators to keep track of the current position in each input list. This approach allows the code to efficiently merge the two lists into a single sorted list without using extra memory.

The merged list is built up one element at a time by comparing the current elements at the current positions of the iterators, and adding the smaller one to the merged list. This approach ensures that the merged list is sorted in ascending order.

The code computes the median value of the merged list by checking whether the length of the list is even or odd, and then computing the appropriate value. This approach is straightforward and works well for small to medium-sized input lists.

## Time and Space Complexity:
* `Time Complexity`
The time complexity of the findMedianSortedArrays function is O(m+n), where m and n are the lengths of the input lists nums1 and nums2. This is because the function loops through both input lists once to merge them into a single list, which takes O(m+n) time. 

* `Space Complexity`
The space complexity of the function is also O(m+n), because it creates a new list to store the merged list. The size of the merged list is equal to the sum of the sizes of the input lists, which is O(m+n). Therefore, the space complexity of the function is O(m+n) as well.

## Code:
```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Initialize two iterators for the two arrays
        leftIt, rightIt = 0, 0
        
        # Initialize an empty list to store the merged array
        mergedList = []
        
        # Loop through both arrays until at least one of the iterators reaches the end of its array
        while leftIt < len(nums1) and rightIt < len(nums2):
            # Compare the elements at the current positions of the iterators and add the smaller one to the merged array
            if nums1[leftIt] >= nums2[rightIt]:
                mergedList.append(nums2[rightIt])
                rightIt += 1
            else:
                mergedList.append(nums1[leftIt])
                leftIt += 1
        
        # If there are any remaining elements in the first array, add them to the merged array
        while leftIt < len(nums1):
            mergedList.append(nums1[leftIt])
            leftIt += 1
        
        # If there are any remaining elements in the second array, add them to the merged array
        while rightIt < len(nums2):
            mergedList.append(nums2[rightIt])
            rightIt += 1
        
        # Check if the length of the merged array is even or odd
        if len(mergedList) % 2 == 0:
            # If it's even, calculate the average of the middle two elements
            return (mergedList[len(mergedList) // 2] + mergedList[(len(mergedList) // 2) - 1]) / 2 
        else:
            # If it's odd, return the middle element
            return mergedList[len(mergedList) // 2]

```
