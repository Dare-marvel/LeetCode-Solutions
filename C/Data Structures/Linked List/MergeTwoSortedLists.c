// Link to the problem : https://leetcode.com/problems/merge-two-sorted-lists/

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
