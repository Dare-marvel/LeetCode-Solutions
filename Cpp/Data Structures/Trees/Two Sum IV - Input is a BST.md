### [Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/)

## Explanation:
1. **Struct TreeNode**: This is a definition for a binary tree node. Each node contains an integer value, and pointers to left and right child nodes.

2. **Class BSTIterator**: This class is designed to iterate over a binary search tree (BST). It uses a stack to keep track of nodes, and a boolean variable `reverse` to control the iteration direction.

3. **BSTIterator Constructor**: The constructor takes a root node and a boolean indicating whether to iterate in reverse. It initializes the `reverse` variable and calls the `pushAll` method to push nodes into the stack.

4. **hasNext Method**: This method checks if there are more nodes to iterate over by checking if the stack is empty.

5. **next Method**: This method pops the top node from the stack, pushes its child nodes (right child if not reversed, left child if reversed), and returns the value of the popped node.

6. **pushAll Method**: This method pushes all nodes from the given node to the farthest node on the side determined by the `reverse` variable into the stack.

7. **Class Solution**: This class contains the method `findTarget` which is used to find if there exist two elements in the BST that add up to a given integer `k`.

8. **findTarget Method**: This method initializes two BSTIterators, one regular and one reversed. It then enters a loop where it continuously gets the next values from both iterators. If the sum of these values equals `k`, it returns true. If the sum is less than `k`, it gets the next value from the regular iterator. If the sum is greater than `k`, it gets the next value from the reversed iterator. If no pair of values sum to `k`, it returns false.

## Time and Space Complexity:
### `Time Complexity`:
In terms of time complexity, the `findTarget` method has a time complexity of O(N), where N is the number of nodes in the tree. This is because each node is visited once by the BSTIterators.

### `Space Complexity`:
The space complexity is O(H), where H is the height of the tree. This is due to the usage of a stack in the BSTIterator, which in the worst case needs to store all nodes from the root to the leaf of the longest branch, i.e., the height of the tree. 

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

// Iterator for a Binary Search Tree
class BSTIterator {
    stack<TreeNode*> myStack;  // Stack to store nodes during traversal
    bool reverse;  // Indicates the direction of traversal

public:
    // Constructor: Initializes the iterator with a root and traversal direction
    BSTIterator(TreeNode* root, bool isReverse) {
        reverse = isReverse;
        pushAll(root);  // Pushes nodes onto the stack based on the traversal direction
    }

    // Checks if there are more elements in the iterator
    bool hasNext() {
        return !myStack.empty();
    }

    // Returns the next element in the iterator
    int next() {
        TreeNode* tmpNode = myStack.top();
        myStack.pop();
        if (!reverse) pushAll(tmpNode->right);  // If forward, push right subtree
        else pushAll(tmpNode->left);  // If reverse, push left subtree
        return tmpNode->val;
    }

private:
    // Helper function to push all nodes in a given direction onto the stack
    void pushAll(TreeNode* node) {
        for (; node != NULL;) {
            myStack.push(node);
            if (reverse) {
                node = node->right;
            } else {
                node = node->left;
            }
        }
    }
};

// Solution class for finding a pair of elements in BST that sums up to a given value
class Solution {
public:
    // Finds if there exists a pair of elements in the BST that sums up to 'k'
    bool findTarget(TreeNode* root, int k) {
        if (!root) return false;  // Empty tree case

        // Create two iterators, one for forward traversal and one for reverse traversal
        BSTIterator l(root, false);
        BSTIterator r(root, true);

        // Initialize two values, one from forward traversal and one from reverse traversal
        int i = l.next();
        int j = r.next();

        // Iterate until the pointers meet or cross
        while (i < j) {
            if (i + j == k) return true;  // Found a pair with the required sum
            else if (i + j < k) i = l.next();  // Move the forward iterator
            else j = r.next();  // Move the reverse iterator
        }
        return false;  // No pair found with the required sum
    }
};
```
