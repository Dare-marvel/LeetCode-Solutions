### [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

## Explanation:
This Python code checks if a singly-linked list is a palindrome. Here's how it works:

1. The `isPalindrome` method is called with the head of the linked list as an argument.
2. Two pointers, `slow` and `fast`, are initialized to the head of the list.
3. The `fast` pointer moves twice as fast as the `slow` pointer, so when the `fast` pointer reaches the end of the list, the `slow` pointer will be pointing to the middle node.
4. The second half of the list is reversed in place using a while loop and three pointers: `prev`, `slow`, and `slow.next`.
5. Two pointers, `fast` and `slow`, are initialized to the head of the list and the head of the reversed second half of the list, respectively.
6. The values of nodes pointed to by `fast` and `slow` are compared in a while loop.
7. If all values match, the method returns true, otherwise false.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this solution is O(n), where n is the number of nodes in the linked list. This is because each node is visited once when finding the middle node, reversing the second half of the list, and comparing values.

### `Space Complexity`:
The space complexity is O(1), as no additional data structures are used and only a constant number of pointers are needed.

## Code:
```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Initialize two pointers: slow and fast
        # slow moves one step at a time, fast moves two steps at a time
        slow, fast, prev = head, head, None
        
        # Find the middle of the linked list using the slow and fast pointers
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        # Reverse the second half of the linked list
        # by manipulating the next pointers
        prev, slow, prev.next = slow, slow.next, None
        
        # Compare the reversed second half with the first half
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        
        # Traverse both halves and check if the values are equal
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val:
                return False
            fast, slow = fast.next, slow.next
        
        # If all values match, the linked list is a palindrome
        return True
```

<hr>

## Explanation:
This Python code checks if a singly-linked list is a palindrome using a recursive approach. Here's how it works:

1. The `isPalindrome` method is called with the head of the linked list as an argument.
2. A `front` pointer is initialized to the head of the list.
3. The `palindromeCheck` method is called with the head of the list as an argument.
4. If the current node is `None`, the method returns true.
5. The `palindromeCheck` method is called recursively with the next node as an argument.
6. If the recursive call returns false, the method returns false.
7. If the value of the current node is not equal to the value of the node pointed to by the `front` pointer, the method returns false.
8. The `front` pointer is moved to the next node.
9. The method returns true.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this solution is O(n), where n is the number of nodes in the linked list. This is because each node is visited once when checking if values match.

### `Space Complexity`:
The space complexity is O(n), as there are n recursive calls on the call stack.

## Code:
```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Create a member variable 'front' to keep track of the front of the list
        self.front = head
        # Call the palindromeCheck function to check if the list is a palindrome
        return self.palindromeCheck(head)
    
    def palindromeCheck(self, head: Optional[ListNode]) -> bool:
        # Base case: if the head is None, we have reached the end of the list
        # and it is a palindrome
        if not head:
            return True
        # Recursively call palindromeCheck on the next node
        # If it returns False, it means the remaining list is not a palindrome
        if not self.palindromeCheck(head.next):
            return False
        # Compare the value of the front node with the current node
        # If they are not equal, it is not a palindrome
        if self.front.val != head.val:
            return False
        # Move the front pointer to the next node
        self.front = self.front.next
        # Return True if all values checked so far are equal
        return True        
```

<hr>
