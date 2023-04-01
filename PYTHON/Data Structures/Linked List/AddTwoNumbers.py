# Link : https://leetcode.com/problems/add-two-numbers/description/

# Key Insight : We add numbers digit by digit with the carry and update it after the addition.
# Then we check whether one of the lists is exhausted and add the remaining digits of the list to the end of the result list
# At the end we check that whether a carry is generated and append it to the result list and return the resultant list's head

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
