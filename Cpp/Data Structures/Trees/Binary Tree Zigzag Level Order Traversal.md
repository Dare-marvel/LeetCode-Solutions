### [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/)

## Explanation:
Sure, I'd be happy to explain this code. This is a C++ program that performs a zigzag level order traversal of a binary tree. Here's a step-by-step explanation:

1. **Struct TreeNode**: This is the definition of a binary tree node. Each node has an integer value (`val`), and two pointers (`left` and `right`) pointing to its left child and right child respectively.

2. **Class Solution**: This class contains the main logic of the program. It has a public method: `zigzagLevelOrder`.

3. **zigzagLevelOrder**: This function performs a zigzag level order traversal of the binary tree. It takes a pointer to the root of the tree as a parameter.

    - It initializes an empty vector of vectors, `result`, to store the traversal.
    - If the root is `NULL`, it returns `result`.
    - It creates a queue, `nodesQueue`, and pushes the root into it.
    - It initializes a boolean variable, `leftToRight`, to `true`. This variable is used to alternate between left-to-right and right-to-left traversal at each level.
    - It enters a loop that continues until `nodesQueue` is empty. In each iteration of the loop:
        - It gets the size of `nodesQueue`, which represents the number of nodes at the current level.
        - It creates a vector, `row`, to store the values of the nodes at the current level.
        - It enters a loop that continues for `size` iterations. In each iteration of the loop:
            - It removes the front node from `nodesQueue` and assigns it to `root`.
            - It calculates the index in `row` where the value of the current node should be placed. If `leftToRight` is `true`, the index is `i`; otherwise, the index is `size-1-i`.
            - It assigns the value of the current node to the calculated index in `row`.
            - If the current node has a left child, it pushes the left child into `nodesQueue`.
            - If the current node has a right child, it pushes the right child into `nodesQueue`.
        - It toggles the value of `leftToRight`.
        - It pushes `row` into `result`.
    - It returns `result`.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is **O(n)**, where **n** is the number of nodes in the tree. This is because each node in the tree is visited exactly once.

### `Space Complexity`:
The space complexity of this code is **O(n)**, where **n** is the number of nodes in the tree. This is due to the use of the queue data structure, which could potentially store all the nodes of the tree in the worst case.

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

// Define a class named Solution for handling the problem
class Solution {
public:
    // Function to perform zigzag level order traversal and return the result as a 2D vector
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        // Initialize the result vector to store the zigzag level order traversal
        vector<vector<int>> result;
        
        // Base case: If the root is NULL, return an empty result
        if(root == NULL) return result;

        // Create a queue for level order traversal
        queue<TreeNode* > nodesQueue;
        // Push the root node to the queue to start the traversal
        nodesQueue.push(root);

        // Variable to control the direction of traversal (left to right or right to left)
        bool leftToRight = true;

        // Loop until all levels are traversed
        while(!nodesQueue.empty()){
            // Get the size of the current level
            int size = nodesQueue.size();
            
            // Vector to store the current level's values in the correct order
            vector<int> row(size);
            
            // Process each node in the current level
            for(int i=0; i<size; i++){
                // Pop the front node from the queue
                root = nodesQueue.front();
                nodesQueue.pop();

                // Calculate the index based on the traversal direction
                int index = leftToRight ? i : (size-1-i);

                // Store the node's value in the corresponding position in the row vector
                row[index] = root->val;
                
                // Enqueue the left and right children if they exist
                if(root->left) nodesQueue.push(root->left);
                if(root->right) nodesQueue.push(root->right);
            }
            
            // Toggle the direction for the next level
            leftToRight = !leftToRight;
            
            // Add the row vector to the result vector
            result.push_back(row);
        }
        
        // Return the final result after zigzag level order traversal
        return result;
    }
};
```
