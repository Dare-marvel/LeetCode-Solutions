### [Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/description/)

## Explanation:
Sure, here's an explanation of the code:

1. **Struct TreeNode**: This is a structure for a binary tree node. It contains an integer `val`, and two pointers `left` and `right` to point to the left and right child of the node respectively. It also has three constructors to initialize a TreeNode.

2. **Class Solution**: This class contains the main logic of the program. It has three public methods: `findHeightLeft`, `findHeightRight`, and `countNodes`.

3. **Method findHeightLeft**: This method calculates the height of the left subtree of a given node. It starts from the given node and traverses down the left subtree, incrementing a height counter `ht` until it reaches a null node. It then returns the height.

4. **Method findHeightRight**: This method is similar to `findHeightLeft`, but it calculates the height of the right subtree of a given node.

5. **Method countNodes**: This is the main method that is called with the root of the binary tree. It first checks if the root is null, in which case it returns 0. Then it calculates the height of the left and right subtrees of the root. If the heights are equal, it means the tree is a perfect binary tree, so it calculates the number of nodes using the formula `(1<<lh) - 1` and returns it. If the heights are not equal, it recursively calls `countNodes` for the left and right subtrees, adds the results, adds 1 for the root node, and returns the total.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of the code is **O(log^2 n)**, where **n** is the number of nodes in the binary tree. This is because in the worst case, `countNodes` is called recursively for the left or right subtree, and each call involves calculating the height of the subtree which takes **O(log n)** time. So the total time complexity is **O(log^2 n)**.

### `Space Complexity`:
The space complexity of the code is **O(log n)**. This is the maximum height of the binary tree, which is the maximum depth of the recursive call stack in the `countNodes` method.

## Code:
```cpp
/*
   The given C++ code defines a class Solution that contains functions to find the number of nodes in a 
   complete binary tree using a recursive approach. The binary tree is represented using the TreeNode structure.
*/

#include <iostream>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    // Function to find the height of the left subtree
    int findHeightLeft(TreeNode* root) {
        int ht = 0;
        TreeNode * node = root;
        while (node) {
            ht++;
            node = node->left;
        }
        return ht;
    }

    // Function to find the height of the right subtree
    int findHeightRight(TreeNode* root) {
        int ht = 0;
        TreeNode * node = root;
        while (node) {
            ht++;
            node = node->right;
        }
        return ht;
    }

    // Function to count the number of nodes in the binary tree
    int countNodes(TreeNode* root) {
        // Base case: if the root is NULL, the tree is empty
        if (root == nullptr) 
            return 0;

        // Find the height of the left and right subtrees
        int lh = findHeightLeft(root);
        int rh = findHeightRight(root);

        // If the left and right subtrees have the same height, the tree is a complete binary tree
        if (lh == rh) 
            return (1 << lh) - 1;  // Formula to calculate the total nodes in a complete binary tree

        // If the left and right subtrees have different heights, recursively count nodes in left and right subtrees
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
};

```
