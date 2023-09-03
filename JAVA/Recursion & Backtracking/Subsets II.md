### [Subsets II](https://leetcode.com/problems/subsets-ii/description/)

## Explanation:
This code is a solution to the problem of finding all possible subsets of an array that may contain duplicates. Here is the main logic of the code in detail:

1. The `findSubsets` function is a recursive function that takes four arguments: `ind`, `nums`, `ds`, and `ans`. `ind` is the current index in the array `nums`, `ds` is the current subset, and `ans` is the list of all subsets.
2. The function first adds the current subset `ds` to the list of all subsets `ans`.
3. Then, it iterates from the current index `ind` to the end of the array `nums`. If the current element is equal to the previous element, it skips this iteration to avoid adding duplicate subsets.
4. Otherwise, it adds the current element to the current subset `ds`, calls the function recursively with the next index, and then removes the current element from `ds`.
5. The `subsetsWithDup` function first sorts the input array `nums` and then calls the `findSubsets` function with initial arguments.

## Time and Space Complexity:

### `Time Complexity`:
The time complexity of this code is **O(n * 2^n)**, where **n** is the length of the input array. This is because in the worst case, there are **2^n** possible subsets and each subset takes **O(n)** time to be added to the list of all subsets.

### `Space Complexity`:
The space complexity of this code is **O(n * 2^n)**, where **n** is the length of the input array. This is because in the worst case, there are **2^n** possible subsets and each subset takes **O(n)** space.

## Code:
```java
class Solution {
    // This function recursively generates subsets of the input array 'nums' while avoiding duplicates.
    // Parameters:
    // - ind: The current index to start generating subsets from.
    // - nums: The input array of integers.
    // - ds: The current subset being generated.
    // - ans: The list to store the final list of subsets.
    public void findSubsets(int ind, int[] nums, List<Integer> ds, List<List<Integer>> ans) {
        // Add the current subset 'ds' to the answer list 'ans'.
        ans.add(new ArrayList<>(ds));
        
        // Iterate through the array 'nums' starting from the given index 'ind'.
        for (int i = ind; i < nums.length; i++) {
            // Check if the current element is a duplicate of the previous element.
            // If it is, skip this iteration to avoid duplicate subsets.
            if (i != ind && nums[i] == nums[i - 1]) continue;
            
            // Include the current element in the current subset 'ds'.
            ds.add(nums[i]);
            
            // Recursively generate subsets starting from the next index 'i+1'.
            findSubsets(i + 1, nums, ds, ans);
            
            // Backtrack: Remove the last added element to explore other possibilities.
            ds.remove(ds.size() - 1);
        }
    }
    
    // This function finds all subsets of the input array 'nums' while avoiding duplicates.
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        // Sort the input array to group duplicate elements together.
        Arrays.sort(nums);
        
        // Initialize a list to store the final list of subsets.
        List<List<Integer>> ansList = new ArrayList<>();
        
        // Start generating subsets from the beginning of the array (index 0).
        findSubsets(0, nums, new ArrayList<>(), ansList);
        
        // Return the list of subsets with duplicates removed.
        return ansList;
    }
}
```
