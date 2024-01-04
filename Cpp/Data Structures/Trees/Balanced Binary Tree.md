### [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/)

## Explanation:
This C++ code is a solution for checking if a binary tree is balanced. Here's an explanation of the main logic:

1. **Struct TreeNode**: This is a definition for a binary tree node. Each node has an integer value (`val`), and two pointers (`left` and `right`) pointing to its left child and right child respectively.

2. **Class Solution**: This class contains two methods, `dfsHeight` and `isBalanced`. `dfsHeight` calculates the height of the tree using Depth-First Search (DFS), and `isBalanced` checks if the tree is balanced.

3. **Method dfsHeight**: This method takes a pointer to the root of the binary tree (`TreeNode* root`) as input and returns an integer representing the height of the tree. If the tree is not balanced, it returns `-1`.

4. **Base Case**: If the root is `NULL`, it means the tree is empty, so the height is `0`.

5. **Recursive Case**: If the root is not `NULL`, the method calculates the height of the left subtree (`lh`) and the right subtree (`rh`) by recursively calling `dfsHeight` on `root->left` and `root->right` respectively. If either `lh` or `rh` is `-1`, it means the left or right subtree is not balanced, so it returns `-1`. If the absolute difference between `lh` and `rh` is greater than `1`, it means the tree is not balanced, so it returns `-1`. Otherwise, it returns the maximum of `lh` and `rh` plus `1`.

6. **Method isBalanced**: This method takes a pointer to the root of the binary tree (`TreeNode* root`) as input and returns a boolean indicating whether the tree is balanced. It calls `dfsHeight` on the root and checks if the returned value is `-1`. If it is, it means the tree is not balanced, so it returns `false`. Otherwise, it returns `true`.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is **O(n)**, where **n** is the number of nodes in the tree. This is because each node is visited once during the DFS traversal.

### `Space Complexity`:
The space complexity is **O(h)**, where **h** is the height of the tree. This is because, in the worst case, if the tree is skewed, the maximum depth of the recursion stack would be equal to the height of the tree.

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

// This class defines a solution for checking if a binary tree is balanced.
class Solution {
public:
    // Helper function to calculate the height of the tree in a depth-first manner.
    int dfsHeight(TreeNode* root) {
        // Check if the current node is NULL (base case).
        if(root == NULL) return 0;

        // Recursively calculate the height of the left subtree.
        int leftHeight = dfsHeight(root->left);
        // If the left subtree is unbalanced, propagate -1 to indicate an unbalanced tree.
        if(leftHeight == -1) return -1;

        // Recursively calculate the height of the right subtree.
        int rightHeight = dfsHeight(root->right);
        // If the right subtree is unbalanced, propagate -1 to indicate an unbalanced tree.
        if(rightHeight == -1) return -1;

        // Check if the current subtree is balanced by comparing the heights of left and right subtrees.
        if(abs(leftHeight - rightHeight) > 1) return -1;

        // Return the height of the current subtree.
        return max(leftHeight, rightHeight) + 1;
    }

    // Function to check if the entire binary tree is balanced.
    bool isBalanced(TreeNode* root) {
        // Call the helper function to get the height of the tree.
        // If the height is -1, the tree is unbalanced; otherwise, it is balanced.
        return dfsHeight(root) != -1;
    }
};

```
