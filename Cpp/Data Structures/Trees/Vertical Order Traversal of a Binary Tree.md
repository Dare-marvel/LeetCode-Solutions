### [Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/)

## Explanation:
Sure, here's an explanation of the code:

1. **Struct TreeNode**: This is a definition for a binary tree node. Each node contains an integer value, and pointers to its left and right children.

2. **Class Solution**: This class contains the method `verticalTraversal` which performs the vertical traversal of a binary tree.

3. **Function verticalTraversal**: This function takes the root of a binary tree as input and returns a 2D vector containing the vertical order traversal of the tree.

4. **Map nodes**: This map stores nodes at each vertical and horizontal position. The structure of the map is: level -> vertical -> set of node values.

5. **Queue todo**: This queue is used to perform level-order traversal. The structure of the queue is: TreeNode* -> pair(vertical position, level).

6. **While loop**: This loop traverses the tree using level-order traversal. For each node, it inserts the node value into the map based on its vertical and horizontal positions. It then enqueues the left and right children with adjusted vertical and increased level.

7. **Inserting node value into map**: The node value is inserted into the map based on its vertical and horizontal positions.

8. **Enqueue left and right children**: The left child is enqueued with a decreased vertical position and increased level. The right child is enqueued with an increased vertical position and level.

9. **Prepare the final result**: The final result is prepared by extracting values from the map. For each vertical position, it creates a vector of node values in their appearing order and adds it to the result.

10. **Return the result**: The function returns the result, which is a 2D vector containing the vertical order traversal of the tree.


## Time and Space Complexity:
### `Time Complexity`:
The **time complexity** of the code is **O(N log N)**, where N is the number of nodes in the tree. This is because for each node, we insert the node value into a multiset (which is implemented as a self-balancing binary search tree) and insertion into a multiset has a time complexity of O(log N). Since we do this for all N nodes, the total time complexity is O(N log N).

### `Space Complexity`:
The **space complexity** is **O(N)**, as in the worst case, we might end up storing all the nodes in the queue (when the binary tree is a complete binary tree). Additionally, we also store all nodes in the map. Therefore, the space complexity is linear in the number of nodes.

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

// Class Solution to find the vertical traversal of a binary tree
class Solution {
public:
    // Function to perform vertical traversal
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        // Map to store nodes at each vertical and horizontal position
        // Map structure: level -> vertical -> set of node values
        map<int, map<int, multiset<int>>> nodes;
        
        // Queue to perform level-order traversal
        // Pair structure: TreeNode* -> pair(vertical position, level)
        queue<pair<TreeNode*, pair<int, int>>> todo;
        todo.push({root, {0, 0}});

        // Traverse the tree using level-order traversal
        while (!todo.empty()) {
            auto p = todo.front();
            todo.pop();
            TreeNode *node = p.first;
            int x = p.second.first, y = p.second.second;

            // Insert the node value into the map based on its vertical and horizontal positions
            nodes[x][y].insert(node->val);

            // Enqueue left child with adjusted vertical and increased level
            if (node->left) 
                todo.push({node->left, {x - 1, y + 1}});

            // Enqueue right child with adjusted vertical and increased level
            if (node->right) 
                todo.push({node->right, {x + 1, y + 1}});
        }

        // Prepare the final result by extracting values from the map
        vector<vector<int>> ans;
        for (auto p : nodes) {
            vector<int> col;
            for (auto q : p.second) {
                col.insert(col.end(), q.second.begin(), q.second.end());
            }
            ans.push_back(col);
        }

        // Return the result
        return ans;
    }
};
```
