### [Add One Row to Tree](https://leetcode.com/problems/add-one-row-to-tree/description/)

## Explanation:
**Approach:**

1. **Problem Understanding:** The problem asks us to add a row of nodes with a given value at a specific depth in a binary tree.

2. **Recursive Approach:** The code utilizes a recursive approach to traverse the binary tree and add nodes at the desired depth.

**Intuition:**

1. **Base Case:** The recursive function `add` starts by checking if the current node (`root`) is `nullptr`, indicating that we have reached the end of a branch. In such a case, it returns `nullptr` to terminate the recursion.

2. **Depth Check:** If the current depth (`curr`) is one less than the target depth, it implies that we have reached the level just above the desired depth.

3. **Insertion at Target Depth:** When the current depth matches the target depth minus one (`depth - 1`), it means we are at the level just above the intended row insertion point.

   - At this point, we need to:
     - Store the current left and right children (`lTemp` and `rTemp`) of the current node (`root`).
     - Create new nodes with the given value and attach them to the `root` as left and right children.
     - Attach the original left and right children to the newly added nodes.

4. **Recursive Call:** If the current depth is not at the target depth minus one, we continue recursively traversing the left and right subtrees.

5. **Handling Special Case:** The function `addOneRow` serves as an entry point to the recursive process. If the target depth is 1, it means we need to add a new root with the given value and set the original root as its left child.

6. **Recursion Termination:** The recursion continues until it reaches the target depth or a leaf node, where it stops and returns the modified tree.

## Time and Space Complexity:
### `Time Complexity`:
- In the worst-case scenario, the entire tree is traversed until the target depth is reached.
- Each node is visited once, so the time complexity is O(n), where n is the number of nodes in the tree.

### `Space Complexity`:
- The space complexity is O(h), where h is the height of the tree.
- This is due to the recursive calls on the call stack, which can go as deep as the height of the tree.

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

// Class Solution for adding a row of nodes to a binary tree
class Solution {
public:
    // Function to add nodes at a specific depth
    TreeNode* add(TreeNode* root, int val, int depth, int curr) {
        // Base case: if root is null, return nullptr
        if (!root)
            return nullptr;

        // If the current depth is one less than the target depth
        if (curr == depth - 1) {
            // Store the current left and right children
            TreeNode* lTemp = root->left;
            TreeNode* rTemp = root->right;

            // Create new nodes with the given value and attach them to the root
            root->left = new TreeNode(val);
            root->right = new TreeNode(val);

            // Attach the original left and right children to the newly added nodes
            root->left->left = lTemp;
            root->right->right = rTemp;

            // Return the modified root
            return root;
        }

        // Recursively traverse left and right subtrees
        root->left = add(root->left, val, depth, curr + 1);
        root->right = add(root->right, val, depth, curr + 1);

        // Return the modified root
        return root;
    }

    // Function to add a row of nodes at a specific depth
    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
        // If depth is 1, insert a new root with the given value and set the original root as its left child
        if (depth == 1) {
            TreeNode* newRoot = new TreeNode(val);
            newRoot->left = root;
            return newRoot;
        }

        // Otherwise, call the add function to add nodes at the specified depth
        return add(root, val, depth, 1);
    }
};

```
