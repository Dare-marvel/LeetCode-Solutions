### [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/description/)

## Explanation:
Sure, let's break down the code:

1. **TreeNode Structure**: The `TreeNode` structure is a common way to represent a binary tree in C++. Each node has a value (`val`), and two pointers (`left` and `right`) pointing to its left child and right child respectively. If a node does not have a left or right child, the corresponding pointer is `nullptr`.

2. **isValidBST Function**: The main function `isValidBST(TreeNode* root)` is a public member of the `Solution` class. It takes the root of a binary tree as input and returns a boolean value indicating whether the tree is a valid binary search tree (BST) or not.

3. **Helper Function**: The main function calls a helper function `isValidBST(TreeNode* root, long long minVal, long long maxVal)`. This function also takes the root of a subtree as input, along with two long long integers `minVal` and `maxVal` representing the valid range for the value of the root node.

4. **Base Case**: The base case of the recursion is when the root is `nullptr`, which means we've reached a leaf node. In this case, the function returns `true`, because a leaf node (or an empty tree) is a valid BST.

5. **Value Check**: If the root is not `nullptr`, the function checks whether its value is within the valid range. If `root->val` is not strictly between `minVal` and `maxVal`, the function returns `false`.

6. **Recursive Calls**: If the value of the root node is valid, the function makes two recursive calls for the left and right subtrees. The valid range for the left subtree is between `minVal` and `root->val`, and the valid range for the right subtree is between `root->val` and `maxVal`.

7. **Final Result**: The function returns `true` if and only if both the left and right subtrees are valid BSTs.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of the code is **O(n)**, where **n** is the number of nodes in the tree. This is because each node in the tree is visited exactly once.
Please note that in the worst case scenario (when the tree is a skewed tree), the height of the tree is equal to the number of nodes in the tree, so the space complexity could also be considered **O(n)** in the worst case..

### `Space Complexity`:
The space complexity of the code is **O(h)**, where **h** is the height of the tree. This is due to the recursive nature of the algorithm, which requires a stack depth equal to the height of the tree.

## Code:
```cpp
/*
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

// Define a Solution class to check if a binary tree is a valid binary search tree (BST)
class Solution {
public:
    // Function to check if the given binary tree is a valid BST
    bool isValidBST(TreeNode* root) {
        // Call the helper function with initial minimum and maximum values
        return isValidBST(root, LLONG_MIN, LLONG_MAX);
    }

private:
    // Helper function to recursively check if the subtree is a valid BST
    bool isValidBST(TreeNode* root, long long minVal, long long maxVal) {
        // Base case: if the current node is NULL, it's a valid BST
        if (root == NULL) return true;

        // Check if the current node's value is within the valid range
        if (root->val >= maxVal || root->val <= minVal) return false;

        // Recursively check the left and right subtrees with updated valid ranges
        // For the left subtree, the maximum value is updated to the current node's value
        // For the right subtree, the minimum value is updated to the current node's value
        return isValidBST(root->left, minVal, root->val) && isValidBST(root->right, root->val, maxVal);
    }
};
```
