### [Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

## [Explanation](https://takeuforward.org/data-structure/construct-binary-tree-from-inorder-and-postorder-traversal/):

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

class Solution {
public:
    // Method to build the binary tree using inorder and postorder traversals.
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        // Check if the sizes of both traversals are not equal.
        if(inorder.size() != postorder.size()){
            return NULL;
        }

        // Create a hashmap to store the indices of elements in the inorder traversal.
        map<int, int> hm;

        // Populate the hashmap with the indices of elements in the inorder traversal.
        for(int i=0; i < inorder.size(); i++){
            hm[inorder[i]] = i;
        }

        // Call the recursive helper function to build the tree.
        return buildTree(inorder, 0, inorder.size()-1, postorder, 0, postorder.size()-1, hm);
    }

    // Recursive helper function to construct the binary tree.
    TreeNode* buildTree(vector<int>& inorder, int is, int ie, vector<int>& postorder, int ps, int pe, map<int, int> &hm) {
        // Base case: If the subtree is empty, return NULL.
        if(is > ie || ps > pe) return NULL;

        // Create a new node with the value of the last element in postorder.
        TreeNode* root = new TreeNode(postorder[pe]);

        // Find the index of the root node in the inorder traversal.
        int inRoot = hm[postorder[pe]];

        // Calculate the number of nodes in the left subtree.
        int numsLeft = inRoot - is;

        // Recursively build the left and right subtrees.
        root->left = buildTree(inorder, is, inRoot-1, postorder, ps, ps+numsLeft-1, hm);
        root->right = buildTree(inorder, inRoot+1, ie, postorder, ps+numsLeft, pe-1, hm);

        // Return the root of the constructed subtree.
        return root;
    }
};

// The code uses a hashmap to efficiently find the indices of elements in the inorder traversal.
// The recursive buildTree function constructs the binary tree using the given traversals.
// Proper base cases are included to handle empty subtrees.

```
