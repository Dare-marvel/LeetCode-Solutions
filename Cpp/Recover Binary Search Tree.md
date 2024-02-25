### [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/description/)

## [Explanation](https://www.geeksforgeeks.org/fix-two-swapped-nodes-of-bst/)

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
private:
    // Pointers to track the incorrectly placed nodes
    TreeNode * first;
    TreeNode * prev;
    TreeNode * middle;
    TreeNode * last;

private:
    // In-order traversal to identify incorrectly placed nodes
    void inorder(TreeNode* root){
        if(root == NULL) return;

        inorder(root->left);

        // Check for misplaced nodes
        if(prev != NULL && (root->val < prev->val)){
            if(first == NULL){
                first = prev;
                middle = root;
            }
            else{
                last = root;
            }
        }

        prev = root;
        inorder(root->right);
    }

public:
    // Main function to recover the binary search tree
    void recoverTree(TreeNode* root) {
        // Initialization of pointers
        first = middle = last = NULL;
        prev = new TreeNode(INT_MIN);  // Dummy node to handle the case when the misplaced node is the root

        // Perform in-order traversal to identify misplaced nodes
        inorder(root);

        // Swap values of incorrectly placed nodes
        if(first && last)
            swap(first->val, last->val);
        else if(first && middle)
            swap(first->val, middle->val); 
    }
};

```
