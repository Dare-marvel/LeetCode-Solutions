### [Maximum Width of Binary Tree](https://leetcode.com/problems/maximum-width-of-binary-tree/description/)

## Explanation:
Sure, let's break down the code:

1. **Struct TreeNode**: This is a definition for a binary tree node. Each node has an integer value (`val`), and two pointers (`left` and `right`) pointing to its left child and right child respectively. There are three constructors for creating a new node.

2. **Class Solution**: This class contains the main logic of the program. It has one public method: `widthOfBinaryTree`.

3. **Method widthOfBinaryTree**: This function calculates the maximum width of a binary tree. It takes a pointer to the root of the tree as an argument. The function works as follows:
    - If the root is `NULL`, it returns 0 because a `NULL` tree has a width of 0.
    - It initializes `ans` to 0 to store the maximum width of the tree.
    - It creates a queue `q` to perform a level order traversal of the tree. Each element of `q` is a pair consisting of a pointer to a node and the position of the node. The position of the root is 0.
    - It performs a level order traversal of the tree using a while loop. For each level, it calculates the width of the level and updates `ans` if the width of the level is greater than `ans`.
    - For each node, it calculates the position of the node relative to the first node in the level (`cur_id`). It pushes the left and right children of the node into `q` with their positions.
    - After visiting all nodes in a level, it calculates the width of the level as `last - first + 1` and updates `ans` if necessary.
    - After visiting all levels, it returns `ans`.

## Time and Space Complexity:
### `Time Complexity`:
The **time complexity** of the code is **O(n)**, where **n** is the number of nodes in the tree. This is because each node in the tree is visited once by the function `widthOfBinaryTree`.

### `Space Complexity`:
The **space complexity** of the code is **O(n)**, where **n** is the number of nodes in the tree. This is due to the queue `q` used by the function `widthOfBinaryTree`. In the worst case, all nodes in a level need to be stored in `q`, and this happens when the tree is a complete binary tree.

## Code:
```cpp
// Definition of a class named Solution
class Solution {
public:
    // Function to calculate the width of a binary tree
    int widthOfBinaryTree(TreeNode* root) {
        // Base case: If the root is NULL, the width is 0
        if (!root) return 0;

        // Initialize variables for maximum width and a queue for level-order traversal
        int ans = 0;
        queue<pair<TreeNode*, long long int>> q;
        q.push({root, 0});

        // Level-order traversal using a queue
        while (!q.empty()) {
            int size = q.size();
            long long int mmin = q.front().second;
            long long int first, last;

            // Traverse each level of the tree
            for (int i = 0; i < size; i++) {
                long long int cur_id = q.front().second - mmin;
                TreeNode* node = q.front().first;
                q.pop();

                // Record the first and last indices of the current level
                if (i == 0) first = cur_id;
                if (i == size - 1) last = cur_id;

                // Enqueue the left and right children with updated indices
                if (node->left) q.push({node->left, cur_id * 2 + 1});
                if (node->right) q.push({node->right, cur_id * 2 + 2});
            }

            // Update the maximum width for the current level
            ans = max(ans, static_cast<int>(last - first + 1));
        }

        // Return the maximum width of the binary tree
        return ans;
    }
};
```
