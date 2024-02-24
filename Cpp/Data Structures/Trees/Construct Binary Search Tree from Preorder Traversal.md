### [Construct Binary Search Tree from Preorder Traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)

## Explanation:
1. **Struct TreeNode**: This is a definition of a binary tree node. Each node has an integer value, a left child, and a right child.

2. **Class Solution**: This class contains the main logic of the program. It has two public methods: `bstFromPreorder` and `build`.

3. **bstFromPreorder Method**: This method is the entry point of the program. It takes a vector of integers (the preorder traversal of a binary search tree) as input and returns the root of the constructed binary search tree. It initializes an index `i` to 0 and calls the `build` method with the preorder vector, `i`, and `INT_MAX` as the bound.

4. **Build Method**: This method is a helper function that constructs the binary search tree. It takes the preorder vector, the index `i` (passed by reference), and a bound as input. The bound is used to ensure the binary search tree property (all left descendants <= n < all right descendants) is maintained.

5. **Base Case**: If `i` equals the size of the preorder vector or if the current element in the preorder vector is greater than the bound, it returns `NULL`. This means we've either processed all elements in the preorder vector or we've encountered an element that cannot be placed in the current position of the binary search tree due to the binary search tree property.

6. **Recursive Case**: If the base case is not met, it creates a new tree node with the current element, increments `i`, and recursively builds the left and right subtrees. The left subtree is built with the current node's value as the new bound, while the right subtree is built with the original bound. This is because all elements in the left subtree must be less than the node's value and all elements in the right subtree must be less than the original bound.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of the code is O(n), where n is the number of nodes in the tree. This is because each node is visited once during the construction of the tree.

### `Space Complexity`:
The space complexity of the code is O(n), where n is the number of nodes in the tree. This is due to the space required for the call stack in the case of a skewed binary tree (worst case). In the average case, the space complexity can be considered as O(log n), where n is the number of nodes in the tree, due to the height of a balanced binary tree.

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

// The Solution class contains the logic for constructing a Binary Search Tree (BST) from a preorder traversal.
class Solution {
public:
    // Function to initiate the construction of a BST from a given preorder traversal.
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        int i = 0;  // Starting index for the preorder traversal.
        return build(preorder, i, INT_MAX);  // Initial call to the build function.
    }

    // Recursive function to construct the BST from the preorder traversal.
    TreeNode* build(vector<int> &preorder, int &i, int bound) {
        // If the index reaches the end of the traversal or the current value is greater than the upper bound, return NULL.
        if (i == preorder.size() || preorder[i] > bound) {
            return NULL;
        }

        // Create a new TreeNode with the current value from the preorder traversal.
        TreeNode *root = new TreeNode(preorder[i++]);

        // Recursively build the left subtree with values less than the current root value.
        root->left = build(preorder, i, root->val);

        // Recursively build the right subtree with values greater than the current root value and within the specified bound.
        root->right = build(preorder, i, bound);

        // Return the constructed root of the subtree.
        return root;
    }
};

```
