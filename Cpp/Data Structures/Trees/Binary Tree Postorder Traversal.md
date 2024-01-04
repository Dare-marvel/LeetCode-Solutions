### [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/description/)

# Part-1 ----> Using 2 Stacks

## Explanation:
This C++ code is a solution for the problem of performing a post-order traversal on a binary tree. Here's an explanation of the main logic:

1. **Struct TreeNode**: This is a definition for a binary tree node. Each node has an integer value (`val`), and two pointers (`left` and `right`) pointing to its left child and right child respectively.

2. **Class Solution**: This class contains the method `postorderTraversal` which performs the post-order traversal on the binary tree.

3. **Method postorderTraversal**: This method takes a pointer to the root of the binary tree (`TreeNode* root`) as input and returns a vector of integers (`vector<int>`) representing the post-order traversal of the tree.

4. **Vector postorder**: This vector stores the nodes' values in the order they are visited during the post-order traversal.

5. **Stacks st1 and st2**: These are used to temporarily store the nodes of the tree during the traversal. `st1` is used to hold nodes as they are encountered, while `st2` is used to hold nodes in the order they should be output.

6. **While loop (st1)**: This loop continues until all nodes have been visited. Inside the loop, the top node of `st1` is popped and pushed onto `st2`. If the popped node has a left or right child, they are pushed onto `st1`.

7. **While loop (st2)**: This loop continues until `st2` is empty. Inside the loop, the top node of `st2` is popped and its value is added to the `postorder` vector.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is **O(n)**, where **n** is the number of nodes in the tree. This is because each node is visited once.

### `Space Complexity`:
The space complexity is also **O(n)**. In the worst case, if the tree is skewed, the stack can hold all the nodes of the tree. Hence, the space complexity is linear.

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
 
// This class defines a solution for performing postorder traversal on a binary tree.
class Solution {
public:
    // Function to perform postorder traversal and return a vector of integers.
    vector<int> postorderTraversal(TreeNode* root) {
        // Vector to store the postorder traversal result.
        vector<int> postorder;
        
        // Check if the tree is empty.
        if(root == NULL) return postorder;
        
        // Two stacks to help in the postorder traversal.
        stack<TreeNode* > st1, st2;
        
        // Push the root node onto the first stack to start traversal.
        st1.push(root);
        
        // Loop until the first stack is empty.
        while(!st1.empty()){
            // Get the top node from the first stack.
            root = st1.top();
            st1.pop();
            
            // Push the node onto the second stack.
            st2.push(root);
            
            // Push the left child onto the first stack if it exists.
            if(root-> left != NULL) st1.push(root->left);
            
            // Push the right child onto the first stack if it exists.
            if(root-> right != NULL) st1.push(root->right);
        }
        
        // Pop nodes from the second stack and add their values to the result vector.
        while(!st2.empty()){
            postorder.push_back(st2.top()->val);
            st2.pop();
        }
        
        // Return the final postorder traversal result.
        return postorder;
    }
};
```

# Part-2 ----> Using 1 Stacks

## Explanation:
This C++ code is a solution for the problem of performing a post-order traversal on a binary tree. Here's an explanation of the main logic:

1. **Struct TreeNode**: This is a definition for a binary tree node. Each node has an integer value (`val`), and two pointers (`left` and `right`) pointing to its left child and right child respectively.

2. **Class Solution**: This class contains the method `postorderTraversal` which performs the post-order traversal on the binary tree.

3. **Method postorderTraversal**: This method takes a pointer to the root of the binary tree (`TreeNode* root`) as input and returns a vector of integers (`vector<int>`) representing the post-order traversal of the tree.

4. **Vector postorder**: This vector stores the nodes' values in the order they are visited during the post-order traversal.

5. **Stack st**: This is used to temporarily store the nodes of the tree during the traversal.

6. **TreeNode* curr**: This is a pointer to the current node being processed.

7. **While loop**: This loop continues until all nodes have been visited. Inside the loop, if the current node is not null, it is pushed onto the stack and the left child is visited. If the current node is null, the right child of the top node of the stack is checked. If the right child is null, the node is popped from the stack and its value is added to the `postorder` vector. If the right child is not null, it is visited next.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is **O(n)**, where **n** is the number of nodes in the tree. This is because each node is visited once.

### `Space Complexity`:
The space complexity is also **O(n)**. In the worst case, if the tree is skewed, the stack can hold all the nodes of the tree. Hence, the space complexity is linear.

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
 
// This class defines a solution for performing postorder traversal on a binary tree.
class Solution {
public:
    // Function to perform postorder traversal and return a vector of integers.
    vector<int> postorderTraversal(TreeNode* root) {
        // Vector to store the postorder traversal result.
        vector<int> postorder;
        
        // Check if the tree is empty.
        if(root == NULL) return postorder;
        
        // Stack to keep track of nodes during traversal.
        stack<TreeNode* > st;
        
        // Pointer to the current node during traversal.
        TreeNode* curr = root;

        // Loop until all nodes are processed.
        while(curr != NULL || !st.empty()){
            // Traverse left subtree and push nodes onto the stack.
            if(curr != NULL){
                st.push(curr);
                curr = curr->left;
            }
            else{
                // Get the right child of the top node on the stack.
                TreeNode* temp = st.top()->right;
                
                // If the right child is NULL, pop nodes and add their values to the result vector.
                if(temp == NULL){
                    temp = st.top();
                    st.pop();
                    postorder.push_back(temp->val);
                    
                    // Continue popping nodes with a right child until no more such nodes exist.
                    while(!st.empty() && temp == st.top()->right){
                        temp = st.top();
                        st.pop();
                        postorder.push_back(temp->val);
                    }
                }
                else{
                    // Move to the right subtree.
                    curr = temp;
                }
            }
        }
        
        // Return the final postorder traversal result.
        return postorder;
    }
};

```
