## **Approach and Intuition:**

1. **Problem Understanding:**
   - We're given a binary tree where each node contains a single digit (0-9).
   - We need to find the sum of all root-to-leaf numbers represented by the paths in the tree.

2. **Recursive Approach:**
   - We'll traverse the tree in a depth-first manner, keeping track of the current number formed from root to the current node.
   - At each node, we'll update the current number by appending the current node's value.
   - If the current node is a leaf node, we'll add the formed number to the total sum.

3. **Helper Function `calculatePaths()`:**
   - Takes three parameters: the current node, the current number formed, and the total sum.
   - Updates the current number by appending the value of the current node.
   - If the current node is a leaf node (both children are NULL), it adds the formed number to the total sum and returns.
   - Recursively calls itself for the left and right children if they exist.

4. **Main Function `sumNumbers()`:**
   - Initializes the total sum to 0.
   - Calls the `calculatePaths()` function with the root node, starting with a current number of 0.
   - Returns the total sum after the function call.


## Time and Space Complexity
### 1. **Time Complexity:**
   - In the worst case, we visit each node of the binary tree once.
   - Hence, the time complexity is O(n), where n is the number of nodes in the tree.

### 2. **Space Complexity:**
   - The space complexity is determined by the recursive call stack.
   - In the worst case, the depth of the recursion can be equal to the height of the tree.
   - Hence, the space complexity is O(h), where h is the height of the tree. However, for a balanced binary tree, the height is O(log n), where n is the number of nodes.
  


## Code
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

class Solution {
private:
    // This function calculates the sum of numbers formed by root-to-leaf paths
    void calculatePaths(TreeNode* currentNode, int currentNumber, int &totalSum) {
        // Update the currentNumber by appending the value of the currentNode
        currentNumber = currentNumber * 10 + currentNode->val;
        // If the currentNode is a leaf node, add the formed number to the totalSum
        if(currentNode->left == NULL && currentNode->right == NULL) {
            totalSum += currentNumber;
            return;
        }
        // If the currentNode has a left child, recursively calculate path sums for the left subtree
        if(currentNode->left != NULL) {
            calculatePaths(currentNode->left, currentNumber, totalSum);
        }
        // If the currentNode has a right child, recursively calculate path sums for the right subtree
        if(currentNode->right != NULL) {
            calculatePaths(currentNode->right, currentNumber, totalSum);
        }
    }
public:
    // This function calculates the total sum of numbers formed by root-to-leaf paths in the binary tree
    int sumNumbers(TreeNode* root) {
        // Initialize totalSum to 0
        int totalSum = 0;
        // Call the helper function to calculate path sums starting from the root
        calculatePaths(root, 0, totalSum);
        // Return the total sum of numbers formed by root-to-leaf paths
        return totalSum;
    }
};

```
