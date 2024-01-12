### [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/description/)

## Explanation:
Sure, let's break down the code:

1. **Struct TreeNode**: This is a definition for a binary tree node. Each node has an integer value (`val`), and two pointers (`left` and `right`) pointing to its left child and right child respectively. There are three constructors for creating a new node.

2. **Class Solution**: This class contains the main logic of the program. It has two public methods: `isSymmetricHelp` and `isSymmetric`.

3. **Method isSymmetricHelp**: This is a helper function that checks if two subtrees are mirror images of each other. It takes two pointers to TreeNode (`left` and `right`) as arguments.
    - If both `left` and `right` are `NULL`, it returns `true` because two `NULL` trees are mirror images of each other.
    - If `left` and `right` are not `NULL`, it checks if the values of `left` and `right` are equal. If they are not equal, it returns `false`.
    - If the values are equal, it recursively checks if the left subtree of `left` is a mirror image of the right subtree of `right` and if the right subtree of `left` is a mirror image of the left subtree of `right`.

4. **Method isSymmetric**: This is the main function that checks if a tree is symmetric. It takes a pointer to the root of the tree as an argument.
    - If the `root` is `NULL`, it returns `true` because a `NULL` tree is symmetric.
    - If the `root` is not `NULL`, it calls the helper function `isSymmetricHelp` with the left and right children of the root.

## Time and Space Complexity:
### `Time Complexity`:
The **time complexity** of the code is **O(n)**, where **n** is the number of nodes in the tree. This is because each node in the tree is visited once by the `isSymmetricHelp` function.

### `Space Complexity`:
The **space complexity** of the code is **O(h)**, where **h** is the height of the tree. This is due to the recursive stack used by the `isSymmetricHelp` function. In the worst case, the height of the tree is **n** (for a skewed tree), so the space complexity is **O(n)**.

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
    // Helper function to check if two subtrees are symmetric
    bool isSymmetricHelp(TreeNode* left, TreeNode* right) {
        // Base case: If either subtree is NULL, they are symmetric if both are NULL
        if (left == NULL || right == NULL) {
            return left == right;
        }

        // Check if values of the current nodes are equal
        if (left->val != right->val) {
            return false;
        }

        // Recursively check the symmetry of the left and right subtrees
        return isSymmetricHelp(left->left, right->right) && isSymmetricHelp(left->right, right->left);
    }

    // Main function to check if a binary tree is symmetric
    bool isSymmetric(TreeNode* root) {
        // The tree is considered symmetric if it is empty or if its left and right subtrees are symmetric
        return root == NULL || isSymmetricHelp(root->left, root->right);
    }
};

```
