### [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/description/)

## Explanation:
Sure, let's break down the code:

1. **Struct Definition**: The code begins with the definition of a `struct` named `TreeNode`. This struct represents a node in a binary tree and contains an integer value (`val`), and two pointers (`left` and `right`) to the left and right child nodes respectively. It also has three constructors for creating a new `TreeNode`.

2. **Class Definition**: The code then defines a class named `Solution` which contains two public methods: `rightSideUtil` and `rightSideView`.

3. **Utility Function**: The `rightSideUtil` function is a utility function used to perform a depth-first traversal of the binary tree. It takes three arguments: a pointer to a `TreeNode` (`root`), an integer (`level`), and a reference to a vector of integers (`ds`).

4. **Base Case**: If the `root` is `NULL`, the function returns immediately as there is nothing to process.

5. **Level Check**: If the current `level` is equal to the size of the `ds` vector, the value of the `root` node is added to the `ds` vector. This is because the rightmost node at each level is the one that is visible from the right side.

6. **Recursive Calls**: The function then makes recursive calls to `rightSideUtil` for the right and left child nodes of the `root`, with the `level` incremented by 1. The right subtree is traversed before the left subtree to ensure that the rightmost node at each level is processed first.

7. **Main Function**: The `rightSideView` function is the main function that gets the right side view of a binary tree. It creates an empty vector `ds`, calls `rightSideUtil` with the `root` of the tree and `ds`, and then returns `ds`.

## Time and Space Complexity:
### `Time Complexity`:
The **time complexity** of the code is **O(n)**, where **n** is the number of nodes in the binary tree. This is because each node is visited once during the depth-first traversal.

### `Space Complexity`:
The **space complexity** is **O(h)**, where **h** is the height of the binary tree. This is due to the extra space required for the recursive call stack during the depth-first traversal.

## Code:
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

// Definition of a class named Solution
class Solution {
public:
    // Utility function for the right side view traversal
    void rightSideUtil(TreeNode* root, int level, vector<int> &ds) {
        // Base case: if the node is NULL, return
        if(root == NULL ) return;

        // If the current level matches the size of the result vector, add the value to the result
        if(level == ds.size()) ds.push_back(root->val);

        // Recursively traverse the right subtree first
        rightSideUtil(root->right, level + 1, ds);

        // Then, recursively traverse the left subtree
        rightSideUtil(root->left, level + 1, ds);
    }

    // Main function to get the right side view of a binary tree
    vector<int> rightSideView(TreeNode* root) {
        // Vector to store the right side view elements
        vector<int> ds;

        // Call the utility function to perform the traversal
        rightSideUtil(root, 0, ds);

        // Return the right side view result
        return ds;
    }
};
```
