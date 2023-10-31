### [Permutations](https://leetcode.com/problems/permutations/description/)

## Explanation:
This C++ code is a solution for generating all permutations of a given array of integers. Here's a detailed explanation of the main logic:

1. **Class Definition**: The `Solution` class is defined with two methods: `permute` and `recurPermute`.

2. **Public Method - permute**: This is the public method that takes an input vector of integers (`nums`) and returns a vector of all permutations of `nums`. It initializes an empty vector (`ans`) to store the permutations, calls the helper method `recurPermute` to fill `ans`, and then returns `ans`.

3. **Private Method - recurPermute**: This is a private helper method that generates permutations recursively. It takes three parameters: an index (`index`), the current permutation (`nums`), and the vector to store all permutations (`ans`).

4. **Base Case**: In `recurPermute`, if `index` equals the size of `nums`, it means we have generated a complete permutation, so we add `nums` to `ans` and return.

5. **Recursive Case**: If `index` is less than the size of `nums`, we iterate over the elements in `nums` from `index` to the end. For each element, we swap it with the element at `index`, recursively call `recurPermute` with `index+1`, and then swap the elements back. This backtracking ensures that `nums` is reset to its original state before the next iteration.

## Dry Run:
This is a C++ implementation of generating all permutations of a given array of integers. Here's a dry run of the code with a recursion tree for the input array [1, 2]:

1. Initially, `index` is 0 and `nums` is [1, 2]. We enter the `for` loop with `i` equal to `index` (0). We swap `nums[index]` and `nums[i]`, so `nums` remains [1, 2]. We make a recursive call with `index+1` (1).

    - At this level, `index` is 1 and `nums` is [1, 2]. We enter the `for` loop with `i` equal to `index` (1). We swap `nums[index]` and `nums[i]`, so `nums` remains [1, 2]. We make a recursive call with `index+1` (2).
        * At this level, `index` is 2 which is equal to the size of `nums`, so we add `nums` to the answer and return.
    - Back at the previous level, we increment `i` to 2 which is equal to the size of `nums`, so we exit the loop and return.

2. Back at the initial level, we increment `i` to 1. We swap `nums[index]` (which is 1) and `nums[i]` (which is 2), so now `nums` becomes [2, 1]. We make a recursive call with `index+1`.

    - At this level, `index` is 1 and `nums` is [2, 1]. We enter the loop with `i` equal to index. We swap `nums[index]` and `nums[i]`, so nums remains [2, 1]. We make a recursive call with index+1.
        * At this level, index is 2 which is equal to the size of nums, so we add nums to the answer and return.
    - Back at the previous level, we increment i to 2 which is equal to the size of nums, so we exit the loop and return.

3. Back at the initial level, we increment i to 2 which is equal to the size of nums, so we exit the loop. The function ends and returns the answer: [[1, 2], [2, 1]].

Here's a visual representation of the recursion tree:

```
permute([1, 2], index=0)
├─ permute([1, 2], index=1)
│   └─ permute([1, 2], index=2) -> add [1, 2] to ans
└─ permute([2, 1], index=1)
    └─ permute([2, 1], index=2) -> add [2, 1] to ans
```

Each node represents a function call and shows the state of nums and index for that call. The leaf nodes represent base cases where a permutation has been found. The final result is obtained by gathering all permutations found at the leaf nodes.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity is O(n*n!) because there are n! permutations and it requires O(n) time to print a permutation.

### `Space Complexity`:
The space complexity is O(n) because in the worst case, if you consider the function call stack size, for generating all permutations, depth can go up to n.

## Code:
```cpp
// Definition of a class named Solution
class Solution {
private:
    // Private recursive function to generate permutations
    void recurPermute(int index, vector<int> &nums, vector<vector<int>> &ans) {
        // Base case: If index reaches the end of the input vector nums
        if (index == nums.size()) {
            // Add the current permutation to the answer vector
            ans.push_back(nums);
            return;
        }
        // Iterate through the remaining elements in the vector nums
        for (int i = index; i < nums.size(); i++) {
            // Swap the elements at indices index and i
            swap(nums[index], nums[i]);
            // Recursively generate permutations for the next index
            recurPermute(index + 1, nums, ans);
            // Undo the previous swap to backtrack and explore other permutations
            swap(nums[index], nums[i]);
        }
    }
public:
    // Public function to generate all permutations of the input vector nums
    vector<vector<int>> permute(vector<int>& nums) {
        // Vector to store the resulting permutations
        vector<vector<int>> ans;
        // Call the recursive permutation generation function starting from index 0
        recurPermute(0, nums, ans);
        // Return the vector containing all permutations
        return ans;
    }
};
```
