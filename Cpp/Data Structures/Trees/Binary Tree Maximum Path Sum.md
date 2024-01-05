### [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/)

## Explanation:
Sure, I'd be happy to explain this code. This is a C++ program that finds the maximum path sum in a binary tree. The path may start and end at any node in the tree.

Here's a step-by-step explanation of the code:

1. **Struct TreeNode**: This is the definition of a binary tree node. Each node has an integer value (`val`), and two pointers (`left` and `right`) pointing to its left child and right child respectively.

2. **Class Solution**: This class contains the main logic of the program. It has two public methods: `maxPathDown` and `maxPathSum`.

3. **maxPathDown**: This is a helper function that computes the maximum path sum that can be obtained by starting from the current node and going down. It takes two parameters: a pointer to the current node (`node`), and a reference to an integer (`maxi`) that keeps track of the maximum path sum found so far.

    - If the current node is `NULL`, it returns `0`.
    - It recursively calls itself for the left and right children of the current node, and stores the results in `left` and `right` respectively. If the result is negative, it is replaced with `0` (since we can choose not to include that path).
    - It updates `maxi` with the maximum of `maxi` and the sum of the value of the current node, `left`, and `right`.
    - It returns the maximum of `left` and `right`, plus the value of the current node. This represents the maximum path sum that can be obtained by starting from the current node and going down.

4. **maxPathSum**: This is the main function that computes the maximum path sum in the binary tree. It takes a pointer to the root of the tree as a parameter.

    - It initializes `maxi` with `INT_MIN` (the smallest possible integer).
    - It calls `maxPathDown` with the root of the tree and `maxi`.
    - It returns `maxi`, which now contains the maximum path sum in the tree.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is **O(n)**, where **n** is the number of nodes in the tree. This is because each node in the tree is visited exactly once.

### `Space Complexity`:
The space complexity of this code is **O(h)**, where **h** is the height of the tree. This is due to the recursive nature of the `maxPathDown` function, which could potentially have up to **h** recursive calls on the stack in the worst case.

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
    // Function to calculate the maximum path sum starting from a given node and updating the global maximum
    int maxPathDown(TreeNode* node, int &maxi) {
        // Base case: If the node is NULL, return 0
        if (node == NULL) return 0;

        // Recursively calculate the maximum path sum for the left and right subtrees
        int left = max(0, maxPathDown(node->left, maxi));
        int right = max(0, maxPathDown(node->right, maxi));

        // Update the global maximum by considering the current node's value and paths from left and right subtrees
        maxi = max(maxi, node->val + left + right);

        // Return the maximum path sum starting from the current node, considering only one side
        return max(left, right) + node->val;
    }

    // Function to calculate the overall maximum path sum for the given binary tree
    int maxPathSum(TreeNode* root) {
        // Initialize the global maximum to the minimum possible integer value
        int maxi = INT_MIN;

        // Call the helper function to calculate the maximum path sum starting from the root
        maxPathDown(root, maxi);

        // Return the overall maximum path sum
        return maxi;
    }
};

```
