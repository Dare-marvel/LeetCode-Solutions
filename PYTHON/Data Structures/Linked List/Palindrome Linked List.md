### [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

## Explanation:

## Time and Space Complexity:
### `Time Complexity`:

### `Space Complexity`:

## Code:
```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
    private:
            ListNode* middle(ListNode* &head){
        ListNode* fast=head->next;
        ListNode* slow=head;
        while(fast!=NULL){
            fast=fast->next;
            if(fast!=NULL){
                slow=slow->next;
                fast=fast->next;
            }
        }
        return slow;
    }
    ListNode* reverse(ListNode* &head){
        ListNode* prev=NULL;
        ListNode* curr=head;
        ListNode* next=curr->next;
        while(curr!=NULL){
            next=curr->next;
            curr->next=prev;
            prev=curr;
            curr=next;
        }
        return prev;
    }
    
    public:
    bool isPalindrome(ListNode* head) {
        ListNode* temp=head;
        if(temp==NULL)
            return true;
        if(head->next==NULL)
            return true;
        
        //slowis pointing to the middle 
        ListNode* mid=middle(head);
        ListNode* temp1=head;
        ListNode* temp2=reverse(mid->next);
        while(temp2!=NULL){
            if(temp1->val!=temp2->val)
                return false;
            temp1=temp1->next;
            temp2=temp2->next;
        }
        return true;
    }

};
```

<hr>

## Explanation:

## Time and Space Complexity:
### `Time Complexity`:

### `Space Complexity`:

## Code:
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True

        
```

<hr>

## Explanation:

## Time and Space Complexity:
### `Time Complexity`:

### `Space Complexity`:

## Code:
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.front = head
        return self.palindromeCheck(head)
    
    def palindromeCheck(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        if not self.palindromeCheck(head.next):
            return False
        if self.front.val != head.val:
            return False
        self.front = self.front.next
        return True


        
```

<hr>
