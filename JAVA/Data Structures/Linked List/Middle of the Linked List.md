### [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/description/)

## Explanation:
This code finds and returns the middle node of a singly-linked list. Here is the main logic of the code explained in detail:

1. The code initializes a variable `length` to store the length of the linked list.
2. The code creates a pointer `ptr` to iterate through the linked list.
3. The code uses a `while` loop to iterate through the linked list and count the number of nodes. The loop continues until the `ptr` pointer reaches the end of the list.
4. After counting the number of nodes, the code calculates the index of the middle node by dividing the length of the list by 2.
5. The code creates another pointer `midNode` to iterate through the linked list again.
6. The code uses another `while` loop to iterate through the linked list until it reaches the middle node. The loop continues until the `mid` variable is 0.
7. After reaching the middle node, the code returns it.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(`n`) because it iterates through the entire linked list twice to find the middle node.

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
    public ListNode middleNode(ListNode head) {
        // Initialize a variable to store the length of the linked list
        int length = 0;
        
        // Create a pointer to iterate through the linked list
        ListNode ptr = head;
        
        // Iterate through the linked list and count the number of nodes
        while(ptr != null) {
            ptr = ptr.next;
            length++;
        }

        // Calculate the index of the middle node
        int mid = length / 2;

        // Create a pointer to iterate through the linked list again
        ListNode midNode = head;
        
        // Iterate through the linked list until the middle node is reached
        while(mid > 0) {
            midNode = midNode.next;
            mid--;
        }

        // Return the middle node
        return midNode;
    }
}
```
