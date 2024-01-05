### [Same Tree](https://leetcode.com/problems/same-tree/description/)

## Explanation:
Here's a step-by-step explanation:

1. **Struct TreeNode**: This is the definition of a binary tree node. Each node has an integer value (`val`), and two pointers (`left` and `right`) pointing to its left child and right child respectively.

2. **Class Solution**: This class contains the main logic of the program. It has a public method: `isSameTree`.

3. **isSameTree**: This function checks if two binary trees are the same. It takes two parameters: pointers to the roots of the two trees (`p` and `q`).

    - If either `p` or `q` is `NULL`, it returns `true` only if both are `NULL`. This is because a `NULL` tree is considered to be the same as another `NULL` tree.
    
    - If both `p` and `q` are not `NULL`, it checks if the values of the current nodes are the same, and recursively checks if the left and right subtrees are the same. If all these conditions are true, it returns `true`; otherwise, it returns `false`.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is **O(n)**, where **n** is the number of nodes in the tree. This is because each node in the tree is visited exactly once.

### `Space Complexity`:
The space complexity of this code is **O(h)**, where **h** is the height of the tree. This is due to the recursive nature of the `isSameTree` function, which could potentially have up to **h** recursive calls on the stack in the worst case.

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
    // Function to check if two binary trees are the same
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // Base case: If either tree is NULL, return true only if both are NULL
        if (p == NULL || q == NULL) {
            return (p == q);
        }

        // Check if the current nodes have the same value and recursively check the left and right subtrees
        return (p->val == q->val) && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};

```
