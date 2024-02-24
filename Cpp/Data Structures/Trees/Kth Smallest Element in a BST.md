### [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)

## Explanation:
Sure, let's break down the logic of this code:

1. **Struct TreeNode**: This is a basic structure for a node in a binary search tree (BST). Each node contains an integer value (`val`), and two pointers (`left` and `right`) pointing to its left child and right child respectively. If a node does not have a left or right child, the corresponding pointer is `nullptr`.

2. **Class Solution**: This class contains the method `kthSmallest` which is used to find the kth smallest element in the BST.

3. **Method kthSmallest**: This method takes two arguments - a pointer to the root node of the BST (`root`), and the rank of the element to be found (`k`). The method initializes a counter (`count`) to 0 and calls the `helper` function with `root`, `count`, and `k`. It returns the value returned by the `helper` function.

4. **Method helper**: This method is used to traverse the BST and find the kth smallest element. It takes three arguments - a pointer to the current node (`root`), a reference to the counter (`count`), and the rank of the element to be found (`k`). The counter is passed by reference, so it keeps its value across recursive calls.

5. **Traversal and Search**: The method uses an in-order traversal (left, root, right) to visit the nodes in ascending order. If the current node is not `nullptr`, it first recursively visits the left subtree. After the left subtree is visited, it checks if the counter is equal to `k`. If it is, it means the kth smallest element has been found in the left subtree, so it returns the value of that element. If the counter is not equal to `k`, it increments the counter and checks again. If the counter is now equal to `k`, it means the current node is the kth smallest element, so it returns the value of the current node. If the counter is still not equal to `k`, it recursively visits the right subtree. If the current node is `nullptr`, it means the end of a branch has been reached, so it returns -1.

Please note that this code assumes that the BST does not contain duplicate values. If your BST can contain duplicates, you might need to adjust the code accordingly. Also, the code returns -1 when the BST does not contain k elements. You can replace -1 with any value that is invalid in your context.
## Time and Space Complexity:
### `Time Complexity`:
The time complexity of the `kthSmallest` method is O(N) in the worst case, where N is the number of nodes in the BST. This is because in the worst case, the function might need to visit all nodes of the BST.

### `Space Complexity`:
The space complexity of the `kthSmallest` method is O(H), where H is the height of the BST. This is because in the worst case, the maximum depth of the recursive call stack is H. If the BST is balanced, H is log(N), so the space complexity is O(log(N)). However, in the worst case where the BST degenerates into a linked list, H is N, so the space complexity is O(N).

## Code:
```cpp
/*
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

// Define a Solution class to find the kth smallest element in a binary search tree
class Solution {
public:
    // Function to find the kth smallest element in the BST
    int kthSmallest(TreeNode* root, int k) {
        int count = 0;  // Initialize a counter to keep track of the number of nodes visited
        return helper(root, count, k);  // Call the helper function to find the kth smallest element
    }

private:
    // Helper function to recursively traverse the BST and find the kth smallest element
    int helper(TreeNode* root, int& count, int k) {
        // Check if the current node is not NULL
        if (root) {
            // Recursively traverse the left subtree and get the result
            int val = helper(root->left, count, k);
            
            // If the count equals k, return the result obtained from the left subtree
            if (count == k) return val;
            
            // If the current node is the kth smallest, return its value
            if (++count == k) return root->val;
            
            // Recursively traverse the right subtree and get the result
            return helper(root->right, count, k);
        }
        
        // Return -1 or any invalid value when root is NULL
        return -1;
    }
};
```
