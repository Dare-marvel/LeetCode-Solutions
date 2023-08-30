### [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)

## Explanation:
This code is a solution to the problem of detecting if a singly-linked list has a cycle. The main logic of the code is as follows:
1. First, it checks if the linked list is null or if it has only one node. If either of these conditions is true, it returns false as there can be no cycle.
2. Then, it initializes two pointers, `fast` and `slow`, to the head of the linked list.
3. The code enters a while loop that continues until `fast.next` and `fast.next.next` are not null.
4. Inside the loop, `fast` is moved two nodes ahead and `slow` is moved one node ahead.
5. If `fast` and `slow` are equal, it means that there is a cycle in the linked list and the function returns true.
6. If the loop exits, it means that there is no cycle in the linked list and the function returns false.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this solution is O(n), where n is the number of nodes in the linked list. This is because in the worst case, the while loop will run for n/2 iterations before determining that there isn't a cycle.

### `Space Complexity`:
The space complexity of this solution is O(1), as it only uses a constant amount of extra space to store the two pointers `fast` and `slow`. It does not use any additional data structures or allocate any additional memory dynamically.

## Code:
```java
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

// This class is a solution to detect cycles in a singly-linked list.
public class Solution {
    
    // This method checks whether a given linked list has a cycle or not.
    public boolean hasCycle(ListNode head) {
        // If the list is empty or has only one node, there can't be a cycle.
        if (head == null || head.next == null) {
            return false;
        }

        // Initialize two pointers, fast and slow, both starting from the head.
        ListNode fast = head;
        ListNode slow = head;

        // Traverse the linked list using two pointers:
        // Fast pointer moves 2 steps at a time, while slow pointer moves 1 step.
        // If there's a cycle, fast pointer will eventually catch up to slow pointer.
        while (fast.next != null && fast.next.next != null) {
            fast = fast.next.next; // Move fast pointer by 2 steps.
            slow = slow.next;      // Move slow pointer by 1 step.
            
            // If the fast and slow pointers meet, it indicates a cycle.
            if (fast == slow) {
                return true;
            }
        }

        // If fast pointer reaches the end of the list, there's no cycle.
        return false;
    }
}
```
