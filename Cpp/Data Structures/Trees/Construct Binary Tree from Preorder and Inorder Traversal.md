### [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

## Explanation:
1. **Class Definition**: The code defines a class named `Solution`. In C++, a **class** is a user-defined data type that we can use to create objects of this type. It acts as a blueprint for the object we will create.

2. **TreeNode Structure**: Before the `Solution` class, there's a structure defined for a binary tree node, `TreeNode`. Each `TreeNode` contains an integer value (`val`), and two pointers to its left and right child nodes (`left` and `right`). There are three constructors for `TreeNode` to initialize these members.

3. **Function Declaration**: Inside the `Solution` class, two public functions named `buildTree` are declared. The **public** keyword means these functions can be accessed from outside the class. The first `buildTree` function takes eight parameters, including two vectors `preorder` and `inorder`, four integers `preStart`, `preEnd`, `inStart`, `inEnd`, and a map `inMap`. The second `buildTree` function takes two vectors `preorder` and `inorder`.

4. **Function Logic**: The main logic of the code is to construct a binary tree from its preorder and inorder traversal arrays.

    - **Preorder Traversal**: In a preorder traversal of a binary tree, the root node is visited first, then the left subtree, and finally the right subtree.
    - **Inorder Traversal**: In an inorder traversal, the left subtree is visited first, then the root node, and finally the right subtree.

    The first element of the preorder array is always the root of the tree. In the inorder array, all elements before the root element are in the left subtree, and all elements after it are in the right subtree. This property is used to recursively construct the binary tree.

5. **Map Creation**: In the second `buildTree` function, a map `inMap` is created to store the indices of elements in the inorder array for quick lookup. This map is then passed to the first `buildTree` function to construct the binary tree.

6. **Tree Construction**: In the first `buildTree` function, a new `TreeNode` is created with the first element of the preorder array as the root. The index of the root in the inorder array is found using `inMap`. All elements before this index in the inorder array make up the left subtree, and all elements after it make up the right subtree. The `buildTree` function is then recursively called to construct the left and right subtrees.

7. **Base Case**: If there are no elements in the current range of the preorder or inorder array (i.e., `preStart > preEnd` or `inStart > inEnd`), a `NULL` pointer is returned. This represents an empty subtree.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of the code is **O(n)**, where **n** is the number of nodes in the tree. This is because each node is created exactly once.

### `Space Complexity`:
The space complexity is also **O(n)**. This is because a map of size **n** is created for the inorder array, and the maximum depth of the recursive call stack will be **n** in the worst case (when the tree is skewed).

## Code:
```cpp
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    // Recursive function to build the binary tree using preorder and inorder traversals
    TreeNode* buildTree(vector<int>& preorder, int preStart, int preEnd, vector<int>& inorder, int inStart, int inEnd, map<int, int>& inMap) {
        // Base case: if the current subtree is empty, return NULL
        if (preStart > preEnd || inStart > inEnd) return NULL;

        // Create a new TreeNode with the value from the current preorder index
        TreeNode* root = new TreeNode(preorder[preStart]);

        // Find the index of the root value in the inorder traversal
        int inRoot = inMap[root->val];

        // Calculate the number of elements in the left subtree
        int numsLeft = inRoot - inStart;

        // Recursively build the left subtree
        root->left = buildTree(preorder, preStart + 1, preStart + numsLeft, inorder, inStart, inRoot - 1, inMap);

        // Recursively build the right subtree
        root->right = buildTree(preorder, preStart + numsLeft + 1, preEnd, inorder, inRoot + 1, inEnd, inMap);

        // Return the root of the current subtree
        return root;
    }

    // Main function to build the binary tree using preorder and inorder traversals
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        // Create a map to store the indices of values in the inorder traversal
        map<int, int> inMap;

        // Populate the map with indices of values in the inorder traversal
        for (int i = 0; i < inorder.size(); i++) {
            inMap[inorder[i]] = i;
        }

        // Call the recursive function to build the binary tree
        return buildTree(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1, inMap);
    }
};
```
