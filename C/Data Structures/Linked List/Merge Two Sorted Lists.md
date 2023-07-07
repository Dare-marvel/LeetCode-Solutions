### [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

## Explanation :
This is a C function that merges two sorted linked lists into one sorted linked list. Here's the main logic of the code in detail:

1. A dummy node is created to serve as the head of the merged list.
2. A tail pointer is created that initially points to the dummy node.
3. The two lists are merged by appending each node to the tail of the merged list.
4. If the current node in `l1` has a value less than or equal to the current node in `l2`, it is appended to the merged list and `l1` is advanced to the next node.
5. Otherwise, the current node in `l2` is appended to the merged list and `l2` is advanced to the next node.
6. The tail pointer is advanced to the next node in the merged list.
7. Any remaining nodes in either `l1` or `l2` are appended to the tail of the merged list.
8. The head of the merged list (i.e., the next node after the dummy node) is returned.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this function is O(n), where n is the total number of nodes in both lists, since each node is visited once.

### `Space Complexity`:
The space complexity is O(1), since only a constant amount of extra space is used (i.e., for the dummy node and tail pointer).

## Code :
```c
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
    // Create a dummy node as the head of the merged list.
    struct ListNode dummy = {0, NULL};
    // Create a tail pointer that initially points to the dummy node.
    struct ListNode* tail = &dummy;

    // Merge the two lists, appending each node to the tail of the merged list.
    while (l1 && l2) {
        if (l1->val <= l2->val) {
            // Append the current node in l1 to the merged list.
            tail->next = l1;
            // Advance l1 to the next node.
            l1 = l1->next;
        } else {
            // Append the current node in l2 to the merged list.
            tail->next = l2;
            // Advance l2 to the next node.
            l2 = l2->next;
        }
        // Advance tail to the next node in the merged list.
        tail = tail->next;
    }

    // Append any remaining nodes to the tail of the merged list.
    tail->next = l1 ? l1 : l2;

    // Return the head of the merged list (i.e., the next node after the dummy node).
    return dummy.next;
}
```
