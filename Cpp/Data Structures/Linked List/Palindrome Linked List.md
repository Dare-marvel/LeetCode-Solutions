### [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

## Explanation:
This C++ code checks if a singly-linked list is a palindrome. Here's how it works:

1. The `isPalindrome` method is called with the head of the linked list as an argument.
2. If the list is empty or contains only one node, the method returns true.
3. The `middle` method is called to find the middle node of the list.
4. The second half of the list is reversed using the `reverse` method.
5. The values of nodes in both halves of the list are compared.
6. If all values match, the method returns true, otherwise false.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this solution is O(n), where n is the number of nodes in the linked list. This is because each node is visited once when finding the middle node, reversing the second half of the list, and comparing values.

### `Space Complexity`:
The space complexity is O(1), as no additional data structures are used and only a constant number of pointers are needed.

## Code:
```cpp
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
