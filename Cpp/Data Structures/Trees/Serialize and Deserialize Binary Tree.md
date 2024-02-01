### [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/)

## Explanation(https://takeuforward.org/data-structure/serialize-and-deserialize-a-binary-tree/)

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

class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        // If the tree is empty, return an empty string.
        if(!root) return "";
        
        // Initialize an empty string to store the serialized tree.
        string s = "";

        // Initialize a queue for level order traversal.
        queue<TreeNode*> q;
        q.push(root);

        // Perform level order traversal and construct the serialized string.
        while(!q.empty()){
            TreeNode* curNode = q.front();
            q.pop();

            // Append the value of the current node to the string, followed by a comma.
            if(curNode == NULL){
                s.append("#,");
            }
            else{
                s.append(to_string(curNode->val) + ',');
            }

            // Enqueue the left and right children of the current node if they exist.
            if(curNode != NULL){
                q.push(curNode->left);
                q.push(curNode->right);
            }
        }

        return s;
    }

    // Decodes your encoded data to a tree.
    TreeNode* deserialize(string data) {
        // If the input string is empty, return NULL.
        if(data.size() == 0) return NULL;

        // Use a stringstream to tokenize the input string.
        stringstream s(data);
        string str;

        // Get the value of the root node from the tokenized string.
        getline(s, str, ',');
        TreeNode* root = new TreeNode(stoi(str));

        // Initialize a queue for level order traversal.
        queue<TreeNode*> q;
        q.push(root);

        // Reconstruct the tree by processing each level of the serialized string.
        while(!q.empty()){
            TreeNode* node = q.front();
            q.pop();

            // Process the left child.
            getline(s, str, ',');
            if(str == "#"){
                node->left = NULL;
            }
            else{
                Create a new left node with the corresponding value and enqueue it.
                TreeNode* leftNode = new TreeNode(stoi(str));
                node->left = leftNode;
                q.push(leftNode);
            }

            // Process the right child.
            getline(s, str, ',');
            if(str == "#"){
                node->right = NULL;
            }
            else{
                Create a new right node with the corresponding value and enqueue it.
                TreeNode* rightNode = new TreeNode(stoi(str));
                node->right = rightNode;
                q.push(rightNode);
            }
        }

        return root;
    }
};

// Comments provide a high-level explanation of the purpose of each section of code.
// The serialize method performs level order traversal and constructs a string representation of the tree.
// The deserialize method tokenizes the input string and reconstructs the tree using a queue for level order processing.
// Proper checks are included for handling empty trees and leaf nodes.

```
