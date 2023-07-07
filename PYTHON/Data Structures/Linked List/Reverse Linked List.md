### [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)

## Key Insight : 
We use three pointer approach to keep track of the previous node , current node and the next node<br> 
For e.g. consider Linked list : 1 -> 2 -> 3 -> 4 -> 5 -> None<br>

##### Step 1:
     1 -> None | 2 -> 3 -> 4 -> 5 -> None
     ^           ^    ^
     |           |    |
    prev       curr  next

##### Step 2:
     2 -> 1 -> None |   3 -> 4 -> 5 -> None
     ^                  ^    ^
     |                  |    |
    prev              curr  next

##### Step 3:
     3 -> 2 -> 1 -> None | 4 -> 5 -> None
     ^                     ^    ^
     |                     |    |
    prev                 curr  next

##### Step 4:
     4 -> 3 -> 2 -> 1 -> None |  5 -> None
     ^                           ^    ^
     |                           |    |
    prev                       curr  next

##### Step 5: (As current is None we break out of loop)
     5 -> 4 -> 3 -> 2 -> 1 -> None |  None
     ^                                 ^   
     |                                 |   
    prev                              curr

## Code : 
#### Optimized Solution
```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check if head is None or the linked list has only one node
        if head is None or head.next is None:
            return head
        
        # Reverse the linked list using three pointers: prev, curr, and nextNode
        prev = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        # Return the new head of the reversed linked list
        return prev

```
------------------------------------------------------------------------------------------------------------------------------------------
#### You can use another approach of inserting all the elements after the last node one by one and in the end return the last node

#### Not Optimal but working solution
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAfter(self, prevNode, nodeToInsert):
        # Check if prevNode is None
        if prevNode is None:
            print("The previous node must be in linked list")
            return
        
        # Insert nodeToInsert after prevNode
        nodeToInsert.next = prevNode.next
        prevNode.next = nodeToInsert
        
    def printList(self):
        # Traverse the linked list and print each value
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Try out the solution on your own
```
