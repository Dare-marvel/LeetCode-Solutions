### [Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/description/)

## Approach and Intuition

The solution utilizes a recursive approach to traverse the binary tree and accumulate the values of the left leaves. Here is a breakdown of the main logic and intuition behind the code:

1. **Structural Overview**:
   - A `TreeNode` struct is defined with three attributes: `val`, `left`, and `right`. Additionally, it has constructors for different initialization scenarios.
   - A `Solution` class contains the public function `sumOfLeftLeaves` and a private helper function `helper`.

2. **Problem Understanding**:
   - A leaf node is defined as a node with no children.
   - The goal is to sum the values of all nodes that are "left leaves." A node is considered a left leaf if it is a leaf node and is the left child of its parent.

3. **Recursive Solution**:
   - The solution involves a recursive function `helper` which is called initially from `sumOfLeftLeaves`.
   - The recursion is initiated on the root node, with a boolean flag `isLeft` indicating whether the node is a left child. The flag is `false` for the root since it has no parent.

4. **Function `helper`**:
   - **Base Case**: If the current node (`node`) is `nullptr`, return 0. This handles the cases where the tree is empty or we reach beyond the leaf nodes (end of a branch).
   - **Leaf Check**: If the current node is a leaf (`!node->left && !node->right`) and it's a left child (`isLeft`), its value is added to the sum.
   - **Recursive Traversal**: The function recursively calls itself for the left and right children:
     - For the left child, `helper(node->left, true)` is called, setting `isLeft` to `true`.
     - For the right child, `helper(node->right, false)` is called, setting `isLeft` to `false`.
   - **Sum Accumulation**: The results from both the left and right recursive calls are summed up and returned.

5. **Handling Different Tree Configurations**:
   - The recursive structure ensures that each node in the tree is visited exactly once, and its role (whether it's a left leaf or not) is assessed based on the `isLeft` flag passed down by its parent node.
   - The approach is exhaustive and ensures no node is missed or double-counted.

6. **Simplicity and Elegance**:
   - The recursion inherently handles varying tree sizes and structures, from a single node to a full or skewed tree.
   - The use of a helper function keeps the primary function (`sumOfLeftLeaves`) clean and focused solely on initiating the recursive process.

## Time and Space Complexity
### `Time Complexity:`
- **O(N)**, where N is the number of nodes in the binary tree. Each node is visited exactly once during the traversal, making the time complexity linear relative to the number of nodes.

### `Space Complexity:`
- **O(H)**, where H is the height of the binary tree. The space complexity is determined by the maximum height of the stack used due to recursive calls. In the worst case (a skewed tree), this would be O(N), but for a balanced tree, it would be `O(log N)`.

## Code
```cpp
/*
// Definition for a binary tree node structure.
struct TreeNode {
    int val;                 // Value of the node
    TreeNode *left;          // Pointer to the left child
    TreeNode *right;         // Pointer to the right child
    TreeNode() : val(0), left(nullptr), right(nullptr) {} // Default constructor
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {} // Constructor initializing node value
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {} // Constructor initializing node and its children
};

*/

class Solution {
public:
    // Public function to calculate sum of left leaves
    int sumOfLeftLeaves(TreeNode* root) {
        // Start recursion from the root, initially it's not a left child
        return helper(root, false);
    }

private:
    // Helper recursive function to compute sum of left leaves
    // 'node' points to current node, 'isLeft' indicates if it is a left child
    int helper(TreeNode* node, bool isLeft) {
        // Base case: if the current node is null, return 0
        if (!node) return 0;
        
        // Check if current node is a leaf and a left child
        if (isLeft && !node->left && !node->right) 
            return node->val; // If so, return its value as it contributes to the sum
        
        // Recursive call for the left child (true as it's a left child)
        // and for the right child (false as it's not a left child)
        // Sum the results from left and right subtrees
        return helper(node->left, true) + helper(node->right, false);
    }
};


```

