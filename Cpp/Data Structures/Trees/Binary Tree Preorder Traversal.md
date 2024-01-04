### [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)

## Explanation:

## Time and Space Complexity:
### `Time Complexity`:

### `Space Complexity`:

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
 
// This class defines a solution for performing preorder traversal on a binary tree.
class Solution {
public:
    // Function to perform preorder traversal and return a vector of integers.
    vector<int> preorderTraversal(TreeNode* root) {
        // Vector to store the preorder traversal result.
        vector<int> preorder;
        
        // Check if the tree is empty.
        if(root == NULL) return preorder;

        // Stack to keep track of nodes during traversal.
        stack<TreeNode* >st;
        
        // Push the root node onto the stack to start traversal.
        st.push(root);
        
        // Loop until the stack is empty.
        while(!st.empty()){
            // Get the top node from the stack.
            root = st.top();
            st.pop();
            
            // Add the value of the current node to the preorder vector.
            preorder.push_back(root->val);
            
            // Push the right child onto the stack if it exists.
            if(root->right != NULL) st.push(root->right);
            
            // Push the left child onto the stack if it exists.
            if(root->left != NULL) st.push(root->left);
        }
        
        // Return the final preorder traversal result.
        return preorder;
    }
};

```
