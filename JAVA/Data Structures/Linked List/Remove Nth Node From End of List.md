### [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)

## Approach 1:
## Explanation:
This code removes the `n-th` node from the end of a singly-linked list. Here is the main logic of the code explained in detail:

1. The code creates a dummy node and sets its `next` pointer to point to the head of the list. This simplifies handling edge cases where the first node of the list needs to be removed.
2. The code creates two pointers: `first` and `second`, and initializes them to point to the dummy node.
3. The code uses a `for` loop to move the `first` pointer `n+1` steps ahead of the `second` pointer.
4. The code uses a `while` loop to move both pointers forward until the `first` pointer reaches the end of the list. At this point, the `second` pointer points to the node before the `n-th` node from the end.
5. The code removes the `n-th` node from the end by updating the `next` pointer of its previous node (pointed to by the `second` pointer) to point to its next node.
6. Finally, the code returns the head of the modified list by returning the `next` pointer of the dummy node.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(`L`) where `L` is the length of the linked list because it iterates through the entire linked list once to find and remove the `n-th` node from the end.

### `Space Complexity`:
The space complexity of this code is O(1) because it uses a constant amount of extra memory to store temporary variables.

## Code:
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // Create a dummy node to simplify handling edge cases
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        // Create two pointers: first and second
        ListNode first = dummy;
        ListNode second = dummy;
        
        // Move the first pointer n+1 steps ahead
        for (int i = 1; i <= n + 1; i++) {
            first = first.next;
        }
        
        // Move both pointers until the first pointer reaches the end of the list
        while (first != null) {
            first = first.next;
            second = second.next;
        }
        
        // Remove the n-th node from the end of the list
        second.next = second.next.next;
        
        // Return the head of the modified list
        return dummy.next;
    }
}
```

## Approach 2:
## Explanation:
This code removes the `n-th` node from the end of a singly-linked list. Here is the main logic of the code explained in detail:

1. The code initializes several pointers and variables: `nthFromEnd`, `prev`, `length`, and `ptr`. The `nthFromEnd` and `prev` pointers are used to keep track of the `n-th` node from the end and its previous node, respectively. The `length` variable is used to store the length of the linked list. The `ptr` pointer is used to iterate through the linked list.
2. The code uses a `while` loop to iterate through the linked list using the `ptr` pointer and count the number of nodes in the list.
3. After counting the number of nodes, the code calculates the index of the `n-th` node from the end by subtracting `n` from the length of the list.
4. If `n` is equal to the length of the linked list, the code removes the first node of the list by returning `head.next`.
5. The code initializes the `nthFromEnd` pointer to point to the second node of the list and moves it one step ahead of the `prev` pointer.
6. The code uses another `while` loop to iterate through the linked list until it reaches the `n-th` node from the end. In each iteration, it moves both the `nthFromEnd` and `prev` pointers forward by one position.
7. After reaching the `n-th` node from the end, the code removes it by updating the `next` pointer of its previous node to point to its next node.
8. Finally, the code returns the head of the modified list.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(`L`) where `L` is the length of the linked list because it iterates through the entire linked list twice: once to count the number of nodes and once to find and remove the `n-th` node from the end.

### `Space Complexity`:
The space complexity of this code is O(1) because it uses a constant amount of extra memory to store temporary variables.

## Code:
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // Initialize pointers and variables
        ListNode nthFromEnd = null;
        ListNode prev = head;
        int length = 0;
        ListNode ptr = head;

        // Iterate through the linked list and count the number of nodes
        while (ptr != null) {
            ptr = ptr.next;
            length++;
        }

        // Calculate the index of the n-th node from the end
        int nIdx = length - n;
        
        // If n is equal to the length of the linked list, remove the first node
        if (nIdx == 0) {
            return head.next;
        }

        // Initialize the nthFromEnd pointer to the second node of the list
        nthFromEnd = head.next;
        
        // Move the nthFromEnd pointer one step ahead of prev
        nIdx--;

        // Iterate through the linked list until the n-th node from the end is reached
        while (nIdx > 0) {
            nthFromEnd = nthFromEnd.next;
            prev = prev.next;
            nIdx--;
        }

        // Remove the n-th node from the end of the list
        if (nthFromEnd != null) {
            prev.next = nthFromEnd.next;
        } else {
            prev.next = null;
        }

        // Return the head of the modified list
        return head;
    }
}
```
