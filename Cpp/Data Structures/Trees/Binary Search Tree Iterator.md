### [Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/description/)

## Explanation:
Sure, here's a detailed explanation of the code:

1. **Struct TreeNode**: This is a definition of a binary tree node. Each node has an integer value (`val`), a left child (`left`), and a right child (`right`). The constructors initialize a new node with the given value and set the left and right children.

2. **Class BSTIterator**: This class implements an iterator for a binary search tree (BST). It has a private stack (`myStack`) that is used to store the nodes of the BST in a specific order.

3. **BSTIterator Constructor**: The constructor takes the root of a BST as input. It calls the `pushAll` method with the root as the argument. This method pushes all the left descendants of the root onto the stack.

4. **pushAll Method**: This private method takes a tree node as input. It pushes the node and all its left descendants onto the stack. This is done in a loop that continues as long as the node is not `NULL`. In each iteration, the current node is pushed onto the stack and the node is updated to its left child.

5. **next Method**: This method returns the next smallest number in the BST. It first saves the top node of the stack in a temporary variable (`tmpNode`). Then it pops the top node from the stack and calls `pushAll` with the right child of the `tmpNode`. This is because the next smallest number in the BST is the leftmost node in the right subtree of the current node. Finally, it returns the value of `tmpNode`.

6. **hasNext Method**: This method returns whether the next smallest number exists. It simply checks if the stack is not empty.

## Time and Space Complexity:
### `Time Complexity`:
The `next` and `hasNext` methods have an average time complexity of O(1). This is because the `next` method only pops a node from the stack and pushes at most h nodes onto the stack, where h is the height of the right subtree of the popped node. Since the `next` method is called n times for n nodes in the BST, the total time complexity is O(n). The `hasNext` method only checks if the stack is empty, so its time complexity is O(1).

### `Space Complexity`:
The space complexity of the code is O(h), where h is the height of the BST. This is because in the worst case, the stack will contain all the nodes along the path from the root to the leftmost leaf node, which is the height of the BST.

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

// The BSTIterator class is designed to iterate through a Binary Search Tree (BST) in ascending order.

class BSTIterator {
private:
    stack<TreeNode *> myStack;  // Stack to store nodes during iteration.

public:
    // Constructor that initializes the iterator with the leftmost node of the BST.
    BSTIterator(TreeNode* root) {
        pushAll(root);
    }
    
    // Function to retrieve the next smallest element in the BST.
    int next() {
        TreeNode *tmpNode = myStack.top();  // Get the top node from the stack.
        myStack.pop();  // Pop the top node.
        pushAll(tmpNode->right);  // Push all nodes in the right subtree of the popped node.
        return tmpNode->val;  // Return the value of the popped node.
    }
    
    // Function to check if there is a next smallest element in the BST.
    bool hasNext() {
        return !myStack.empty();  // Return true if the stack is not empty.
    }

private:
    // Helper function to push all nodes from the current node to the leftmost node onto the stack.
    void pushAll(TreeNode *node) {
        for (; node != NULL; myStack.push(node), node = node->left);
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */

```
