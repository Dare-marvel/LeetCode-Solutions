### [Combination Sum](https://leetcode.com/problems/combination-sum/description/)

## Explanation:
This code is a solution to the problem of finding all unique combinations of candidates where the chosen numbers sum to the target. The main logic of the code is as follows:
1. The `findCombinations` method is a recursive function that takes as input the current index `ind`, the input array `arr`, the current target value `target`, a list `ans` to store the final result, and a list `ds` to store the current combination of numbers.
2. The base case of the recursion is when `ind` is equal to the length of the input array. In this case, if `target` is equal to 0, then a valid combination has been found and it is added to the list `ans`. The function then returns.
3. If `ind` is not equal to the length of the input array, then the code checks if the value of `arr[ind]` is less than or equal to `target`. If it is, then this value is added to the list `ds`, and the function is called recursively with `ind` unchanged, `target` decreased by `arr[ind]`, and `ds` updated.
4. After this recursive call returns, the last element is removed from `ds`.
5. The function is then called again recursively with `ind` incremented by 1 and all other parameters unchanged.
6. The `combinationSum` method simply initializes an empty list `ans`, calls the `findCombinations` method with appropriate initial values, and returns the final result stored in `ans`.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is **O(2^n * n)**, where **n** is the length of the input array, since in the worst case, each element can be included or excluded from a combination, leading to 2^n possible combinations, and each combination takes O(n) time to be copied into the final result.

### `Space Complexity`:
The space complexity is **O(n)**, since at most n elements can be stored in the list `ds`.

## Code:
```java
class Solution {
    // A private recursive function to find combinations that sum up to the target.
    private void findCombinations(int ind, int[] arr, int target, List<List<Integer>> ans, List<Integer> ds) {
        // Base case: If we've reached the end of the array.
        if (ind == arr.length) {
            // If the current combination sums up to the target, add it to the 'ans' list.
            if (target == 0) {
                ans.add(new ArrayList<>(ds));
            }
            return; // Return to backtrack.
        }

        // Check if the current element 'arr[ind]' can be included in the combination.
        if (arr[ind] <= target) {
            ds.add(arr[ind]); // Add the current element to the combination.
            findCombinations(ind, arr, target - arr[ind], ans, ds); // Recursively explore combinations with the current element.
            ds.remove(ds.size() - 1); // Backtrack: Remove the current element from the combination.
        }

        // Move to the next element in the array without including the current one.
        findCombinations(ind + 1, arr, target, ans, ds);
    }

    // Public function to find all combinations that sum up to the target.
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList<>(); // Initialize a list to store the result.

        // Start the recursive combination search from index 0 of 'candidates' array.
        findCombinations(0, candidates, target, ans, new ArrayList<>());

        return ans; // Return the list of combinations that sum up to the target.
    }
}
```
