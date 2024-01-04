### [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)

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
 
// This class defines a solution for performing inorder traversal on a binary tree.
class Solution {
public:
    // Function to perform inorder traversal and return a vector of integers.
    vector<int> inorderTraversal(TreeNode* root) {
        // Stack to keep track of nodes during traversal.
        stack<TreeNode *> st;
        
        // Pointer to the current node during traversal.
        TreeNode * node = root;
        
        // Vector to store the inorder traversal result.
        vector<int > inorder;
        
        // Loop until all nodes are processed.
        while(true){
            // Traverse left subtree and push nodes onto the stack.
            if(node != NULL){
                st.push(node);
                node = node->left;
            }
            else{
                // If the stack is empty, traversal is complete.
                if(st.empty()) return inorder;
                
                // Pop a node from the stack.
                node = st.top();
                st.pop();
                
                // Add the value of the current node to the inorder vector.
                inorder.push_back(node->val);
                
                // Move to the right subtree.
                node = node->right;
            }
        }
        
        // This line is not reachable, as the loop has a return statement.
        return inorder;
    }
};

```
