### [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/)

## Explanation:
Sure, let's break down the code:

1. **Struct TreeNode**: This is a definition for a binary tree node. Each node has an integer value (`val`), and two pointers (`left` and `right`) pointing to its left child and right child respectively. There is a constructor for creating a new node with a given value.

2. **Class Solution**: This class contains the main logic of the program. It has one public method: `lowestCommonAncestor`.

3. **Method lowestCommonAncestor**: This function finds the lowest common ancestor (LCA) of two nodes `p` and `q` in a binary tree. It takes three arguments: a pointer to the root of the tree, and pointers to the two nodes `p` and `q`. The function works as follows:
    - If the root is `NULL`, or the root is `p`, or the root is `q`, it returns the root. This is because if the root is `NULL`, there is no LCA, and if the root is `p` or `q`, the root itself is the LCA.
    - It recursively calls `lowestCommonAncestor` on the left and right children of the root, and stores the results in `left` and `right` respectively.
    - If `left` is `NULL`, it means that neither `p` nor `q` is found in the left subtree, so it returns `right`. This is because `p` and `q` must be in the right subtree if they are in the tree.
    - If `right` is `NULL`, it means that neither `p` nor `q` is found in the right subtree, so it returns `left`. This is because `p` and `q` must be in the left subtree if they are in the tree.
    - If neither `left` nor `right` is `NULL`, it means that `p` is in one subtree and `q` is in the other, so it returns the root. This is because the root is the LCA of `p` and `q`.

## Time and Space Complexity:
### `Time Complexity`:
The **time complexity** of the code is **O(n)**, where **n** is the number of nodes in the tree. This is because in the worst case, the function `lowestCommonAncestor` may need to visit all nodes in the tree.

### `Space Complexity`:
The **space complexity** of the code is **O(h)**, where **h** is the height of the tree. This is due to the recursive stack used by the `lowestCommonAncestor` function. In the worst case, the height of the tree is **n** (for a skewed tree), so the space complexity is **O(n)**.

## Code:
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// Definition of a class named Solution
class Solution {
public:
    // Function to find the lowest common ancestor of two nodes in a binary tree
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // Base case: If the current node is NULL or matches either of the given nodes, return the current node
        if(root == NULL || root == p || root == q) {
            return root;
        }

        // Recursively search for the lowest common ancestor in the left and right subtrees
        TreeNode *left = lowestCommonAncestor(root->left, p, q);
        TreeNode *right = lowestCommonAncestor(root->right, p, q);

        // If one of the subtrees returns NULL, return the other subtree's result
        if(left == NULL){
            return right;
        }
        // If the other subtree returns NULL, return the result of the first subtree
        else if(right == NULL){
            return left;
        }
        // If both subtrees return non-NULL values, the current node is the lowest common ancestor
        else{
            return root;
        }
    }
};
```
