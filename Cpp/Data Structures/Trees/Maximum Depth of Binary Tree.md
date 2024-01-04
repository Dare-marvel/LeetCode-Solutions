### [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

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

## Time and Space Complexity:
### `Time Complexity`:

### `Space Complexity`:

## Code:
```cpp

```
