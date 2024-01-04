### [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)

## Explanation:
Sure, let's break down the code:

1. **Struct TreeNode**: This is a definition for a binary tree node. Each node has an integer value (`val`), and two pointers (`left` and `right`) pointing to its left child and right child respectively. There are three constructors for creating a new TreeNode.

2. **Class Solution**: This class contains the method `preorderTraversal` which performs a preorder traversal of a binary tree.

3. **Preorder Traversal**: In a preorder traversal, the order of visiting nodes is Root, Left, Right. This is what the `preorderTraversal` method implements.

4. **Method - preorderTraversal**: This method takes the root of a binary tree as input and returns a vector of integers representing the preorder traversal of the tree.

5. **Vector 'preorder'**: This vector stores the nodes in their preorder traversal order.

6. **Stack 'st'**: This stack is used to temporarily store nodes of the tree during the traversal.

7. **While Loop**: The loop continues until there are no more nodes left to process (i.e., the stack is empty).

8. **Root Node Processing**: The top node of the stack is popped and its value is added to the 'preorder' vector.

9. **Right Child**: If the popped node has a right child, it is pushed onto the stack.

10. **Left Child**: If the popped node has a left child, it is pushed onto the stack. Since the stack is LIFO (Last In First Out), the left child will be processed before the right child, maintaining the preorder (Root, Left, Right) property.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is **O(n)**, where **n** is the number of nodes in the tree. This is because each node is 'visited' once during the traversal.

### `Space Complexity`:
The space complexity of this code is also **O(n)** in the worst case. This is because in the worst case (when the tree is a skewed tree), the stack will hold all the nodes of the tree. However, in the average case, the space complexity is **O(log n)**, where **log n** is the height of the binary tree.

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
