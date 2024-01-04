### [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

# Part 1 - Using Recursion
## Explanation:
This C++ code is a solution for finding the maximum depth of a binary tree. Here's an explanation of the main logic:

1. **Struct TreeNode**: This is a definition for a binary tree node. Each node has an integer value (`val`), and two pointers (`left` and `right`) pointing to its left child and right child respectively.

2. **Class Solution**: This class contains the method `maxDepth` which calculates the maximum depth of the binary tree.

3. **Method maxDepth**: This method takes a pointer to the root of the binary tree (`TreeNode* root`) as input and returns an integer representing the maximum depth of the tree.

4. **Base Case**: If the root is `NULL`, it means the tree is empty, so the depth is `0`.

5. **Recursive Case**: If the root is not `NULL`, the method calculates the maximum depth of the left subtree (`lh`) and the right subtree (`rh`) by recursively calling `maxDepth` on `root->left` and `root->right` respectively.

6. **Return Value**: The method returns `1 + max(lh,rh)`. The `1` accounts for the root itself, and `max(lh,rh)` ensures that the larger depth between the left and right subtrees is chosen.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is **O(n)**, where **n** is the number of nodes in the tree. This is because each node is visited once during the traversal.

### `Space Complexity`:
The space complexity is **O(h)**, where **h** is the height of the tree. This is because, in the worst case, if the tree is skewed, the maximum depth of the recursion stack would be equal to the height of the tree.

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
 
// This class defines a solution for finding the maximum depth of a binary tree.
class Solution {
public:
    // Function to calculate the maximum depth of the binary tree.
    int maxDepth(TreeNode* root) {
        // Check if the tree is empty.
        if(root == NULL) return 0;

        // Recursively calculate the maximum depth of the left and right subtrees.
        int leftHeight = maxDepth(root->left);
        int rightHeight = maxDepth(root->right);

        // Return the maximum depth of the current subtree.
        return 1 + max(leftHeight, rightHeight);
    }
};

```

# Part 2 - Using Level Order

## Explanation:
This C++ code is a solution for finding the maximum depth (or height) of a binary tree. Here's an explanation of the main logic:

1. **Struct TreeNode**: This is a definition for a binary tree node. Each node has an integer value (`val`), and two pointers (`left` and `right`) pointing to its left child and right child respectively.

2. **Class Solution**: This class contains the method `maxDepth` which calculates the maximum depth of the binary tree.

3. **Method maxDepth**: This method takes a pointer to the root of the binary tree (`TreeNode* root`) as input and returns an integer representing the maximum depth of the tree.

4. **Base Case**: If the root is `NULL`, it means the tree is empty, so the depth is `0`.

5. **Queue q**: This queue is used to perform a level order traversal (or breadth-first traversal) of the tree. The root node is initially pushed into the queue.

6. **Integer ht**: This variable keeps track of the maximum depth of the tree.

7. **While loop**: This loop continues until the queue is empty, which means all nodes have been visited. Inside the loop, all nodes at the current level are processed, and their children are added to the queue.

8. **For loop**: This loop processes all nodes at the current level. For each node, it is removed from the queue, and if it has a left or right child, the child is added to the queue.

9. **Incrementing ht**: After all nodes at the current level have been processed, `ht` is incremented by 1.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is **O(n)**, where **n** is the number of nodes in the tree. This is because each node is visited once during the traversal.

### `Space Complexity`:
The space complexity is **O(w)**, where **w** is the maximum width of the tree (i.e., the maximum number of nodes at any depth). The width of the tree is used instead of the height because in the worst-case scenario (a complete binary tree), the most nodes the queue will hold at once is the number of nodes at the widest level of the tree.

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
 
// This class defines a solution for finding the maximum depth of a binary tree.
class Solution {
public:
    // Function to calculate the maximum depth of the binary tree using level order traversal.
    int maxDepth(TreeNode* root) {
        // Check if the tree is empty.
        if(root == NULL) return 0;

        // Queue to perform level order traversal.
        queue<TreeNode*> q;
        
        // Enqueue the root node to start level order traversal.
        q.push(root);
        
        // Variable to store the height of the tree.
        int height = 0;

        // Loop until the queue is empty.
        while(!q.empty()){
            // Get the current level size to process nodes at the same level.
            int size = q.size();
            
            // Process nodes at the current level.
            for(int i = 0; i < size; i++){
                root = q.front();
                q.pop();
                
                // Enqueue the left child if it exists.
                if(root->left != NULL) q.push(root->left);
                
                // Enqueue the right child if it exists.
                if(root->right != NULL) q.push(root->right);
            }
            
            // Increment the height for each level processed.
            height++;
        }

        // Return the final height of the tree.
        return height;
    }
};

```
