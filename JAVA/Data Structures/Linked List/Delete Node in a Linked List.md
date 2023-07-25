### [Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/description/)

## Explanation:
This code deletes a node from a singly-linked list, given only access to that node. Here is the main logic of the code explained in detail:

1. The code copies the value of the next node to the current node by updating the `val` field of the current node to be equal to the `val` field of the next node.
2. The code updates the `next` pointer of the current node to skip the next node by setting it to be equal to the `next` pointer of the next node.
3. After these two steps, the current node effectively takes on the value and `next` pointer of the next node, and the next node is removed from the list.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(1) because it performs a constant number of operations to delete the node.

### `Space Complexity`:
The space complexity of this code is also O(1) because it uses a constant amount of extra memory to store temporary variables.

## Code:
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        // Copy the value of the next node to the current node
        node.val = node.next.val;
        
        // Update the next pointer of the current node to skip the next node
        node.next = node.next.next;
    }
}
```
