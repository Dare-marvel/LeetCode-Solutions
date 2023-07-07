### [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/)

## Key Insight : 
* We add numbers digit by digit with the carry and update it after the addition.
* Then we check whether one of the lists is exhausted and add the remaining digits of the list to the end of the result list
* At the end we check that whether a carry is generated and append it to the result list and return the resultant list's head

## Explanation:
This is a Python program that defines a `Solution` class with a method `addTwoNumbers` that adds two linked lists that represent non-negative integers. Here's the main logic of the code in detail:

1. The `Solution` class defines a method `addTwoNumbers` that takes two arguments, `l1` and `l2`, which are the heads of the two linked lists to be added.
2. A variable `carry` is initialized to 0 to keep track of the carry from adding the digits.
3. A new linked list `res` is created to store the result of adding the two linked lists.
4. The two linked lists are traversed until one of them is empty.
5. The current digits in both linked lists, along with the carry, are added and the units digit of the sum is appended to the result linked list.
6. The carry for the next digit is calculated by dividing the sum by 10.
7. The pointers to the next digits in both linked lists are advanced.
8. If one of the linked lists is not empty, its remaining digits are added to the result along with any carry.
9. If there is still a carry after adding all the digits, it is appended to the end of the result linked list.
10. The head of the result linked list is returned.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this function is O(max(n, m)), where n and m are the lengths of the two linked lists, since each node in both lists is visited once.

### `Space Complexity`:
The space complexity is O(max(n, m)), since a new linked list is created to store the result, which can have at most max(n, m) + 1 nodes.

## Code:
```py
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for linked list
class LinkedList:
    def __init__(self):
        self.head = None
    
    # function to add a new node to the end of the linked list
    def append(self, data):
        new_node = ListNode(data)
        
        # if the linked list is empty, set the new node as the head node
        if self.head == None:
            self.head = new_node
            return
        
        # traverse the linked list to find the last node
        last = self.head
        while(last.next):
            last = last.next
        
        # add the new node to the end of the linked list
        last.next = new_node

class Solution:
    # function to add two linked lists that represent non-negative integers
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0 
        res = LinkedList()  # create a new linked list to store the result
        # traverse both linked lists until one of them is empty
        while (l1 != None and l2 != None):
            summ = l1.val + l2.val + carry  # add the current digits and the carry
            res.append(summ % 10)  # add the units digit of the sum to the result linked list
            carry = summ // 10  # calculate the carry for the next digit
            l1 = l1.next  # move to the next digit in l1
            l2 = l2.next  # move to the next digit in l2
        
        # if l1 is not empty, add the remaining digits to the result
        while l1 != None:
            summ = l1.val + carry
            res.append(summ % 10)
            carry = summ // 10
            l1 = l1.next
        
        # if l2 is not empty, add the remaining digits to the result
        while l2 != None:
            summ = l2.val + carry
            res.append(summ % 10)
            carry = summ // 10
            l2 = l2.next
        
        # if there is still a carry, add it to the end of the result
        if carry > 0:
            res.append(carry)
        
        return res.head  # return the head of the result linked list
```
