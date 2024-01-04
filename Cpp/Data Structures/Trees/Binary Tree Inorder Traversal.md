### [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)

## Explanation:
Sure, let's break down the code:

1. **Struct TreeNode**: This is a definition for a binary tree node. Each node has an integer value (`val`), and two pointers (`left` and `right`) pointing to its left child and right child respectively. There are three constructors for creating a new TreeNode.

2. **Class Solution**: This class contains the method `inorderTraversal` which performs an inorder traversal of a binary tree.

3. **Inorder Traversal**: In an inorder traversal, the order of visiting nodes is Left, Root, Right. This is what the `inorderTraversal` method implements.

4. **Method - inorderTraversal**: This method takes the root of a binary tree as input and returns a vector of integers representing the inorder traversal of the tree.

5. **Stack 'st'**: This stack is used to temporarily store nodes of the tree during the traversal.

6. **While Loop**: The loop continues until all nodes have been processed.

7. **Node Processing**: If the current node is not null, it is pushed onto the stack and the left child becomes the current node. If the current node is null, the top node from the stack is popped, its value is added to the 'inorder' vector, and the right child becomes the current node.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is **O(n)**, where **n** is the number of nodes in the tree. This is because each node is 'visited' once during the traversal.

### `Space Complexity`:
The space complexity of this code is **O(n)** in the worst case. This is because in the worst case (when the tree is skewed), the stack will hold all the nodes of the tree.

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
