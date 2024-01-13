### [All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/)

## Explanation:
Sure, here's an explanation of the code:

1. **Struct TreeNode**: This is a definition for a binary tree node. Each node has an integer value, a left child, and a right child.

2. **Class Solution**: This class contains the main logic of the program. It has two main methods: `markParents` and `distanceK`.

3. **markParents Method**: This method is used to track the parent of each node in the binary tree. It uses a breadth-first search (BFS) approach to traverse the tree. For each node, it checks if the node has a left or right child. If it does, it adds the child to the queue and maps the child to its parent in the `parent_track` map.

4. **distanceK Method**: This method is used to find all nodes that are `k` distance from the target node. It uses the `markParents` method to track the parents of each node. Then, it uses a BFS approach to traverse the tree from the target node. It keeps track of the visited nodes to avoid cycles. It also keeps track of the current level of the BFS. Once the current level reaches `k`, it stops the BFS. Finally, it returns all the nodes at the `k`th level.


## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(N), where N is the number of nodes in the tree. This is because each node is visited once by the BFS in the `markParents` method and once by the BFS in the `distanceK` method.
 
### `Space Complexity`:
The space complexity of this code is also O(N). This is because the `parent_track` map and the `visited` map can each potentially store N nodes. In addition, the queue used for the BFS can also potentially store N nodes.
 
## Code:
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    // Function to mark parents of each node in a binary tree
    void markParents(TreeNode* root, unordered_map<TreeNode*, TreeNode*> &parent_track) {
        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            TreeNode* current = q.front();
            q.pop();

            // Enqueue left child and mark parent
            if (current->left) {
                q.push(current->left);
                parent_track[current->left] = current;
            }

            // Enqueue right child and mark parent
            if (current->right) {
                q.push(current->right);
                parent_track[current->right] = current;
            }
        }
    }

    // Function to find nodes at distance K from the target node
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        // Map to track parents of each node
        unordered_map<TreeNode*, TreeNode*> parent_track;
        markParents(root, parent_track);

        // Queue for BFS traversal
        queue<TreeNode*> q;
        q.push(target);

        // Map to track visited nodes
        unordered_map<TreeNode*, bool> visited;
        visited[target] = true;

        int cur_level = 0;
        while (!q.empty()) {
            int size = q.size();
            if (cur_level++ == k) break;

            for (int i = 0; i < size; i++) {
                TreeNode* current = q.front();
                q.pop();

                // Enqueue left child if not visited
                if (current->left && !visited[current->left]) {
                    q.push(current->left);
                    visited[current->left] = true;
                }

                // Enqueue right child if not visited
                if (current->right && !visited[current->right]) {
                    q.push(current->right);
                    visited[current->right] = true;
                }

                // Enqueue parent if not visited
                if (parent_track[current] && !visited[parent_track[current]]) {
                    q.push(parent_track[current]);
                    visited[parent_track[current]] = true;
                }
            }
        }

        // Extract nodes at distance K
        vector<int> result;
        while (!q.empty()) {
            TreeNode* curr = q.front();
            q.pop();
            result.push_back(curr->val);
        }

        return result;
    }
};

```
