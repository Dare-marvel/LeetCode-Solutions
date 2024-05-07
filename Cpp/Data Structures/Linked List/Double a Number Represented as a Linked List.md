### [Double a Number Represented as a Linked List](https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/description/)

## **Approach and Intuition:**:

1. **Initialization:**
   - Initialize variables `carry` and `listLen` to handle potential carryovers and track the length of the linked list, respectively.
   - Check if the input linked list is empty or has only one node.

2. **Handle Carry for the First Node:**
   - If the linked list has only one node, set `listLen` to 0.
   - Check if the next node exists and if its value is greater than 4 (a threshold for potential carry).
   - Calculate the new value for the first node after doubling and incorporate any carry.

3. **Update Head and Pointer:**
   - Create a pointer `ptr` to traverse the list.
   - If the new value of the first node is greater than 9, insert a new node with value 1 at the beginning of the list to handle carry.
   - Update the head to the new node and move the pointer accordingly.

4. **Traverse and Double Remaining Nodes:**
   - Traverse the rest of the list starting from `ptr`.
   - At each node, check if the next node exists and if its value is greater than 4.
   - Update the current node's value after doubling and handle any carry.
   - Move the pointer to the next node.

5. **Return Modified Head:**
   - Return the modified head of the list.

## Time and Space Complexity:
### `Time Complexity`:
- Traversing the linked list once takes O(n), where n is the number of nodes in the list.
- Doubling each node's value and handling carries are constant time operations within the loop.
- Overall, the time complexity is O(n).

### `Space Complexity`:
- The additional space used is minimal and constant.
- The space complexity is O(1).

## Code:
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val; // Value of the node
 *     ListNode *next; // Pointer to the next node
 *     ListNode() : val(0), next(nullptr) {} // Default constructor
 *     ListNode(int x) : val(x), next(nullptr) {} // Constructor with value
 *     ListNode(int x, ListNode *next) : val(x), next(next) {} // Constructor with value and next node
 * };
 */
class Solution {
public:
    // Function to double the value of each node in the linked list
    ListNode* doubleIt(ListNode* head) {
        int carry = 0; // Carry for the multiplication
        int listLen = 1; // Length of the list
        // Check if the list has only one node
        if(head->next == NULL){
            listLen = 0;
        }
        // Check if the next node's value is greater than 4
        if(head->next != NULL){
                if(head->next->val > 4){
                carry = 1;
                }
            }

        // Double the value of the head node and add the carry
        int firstVal = (head->val * 2) + carry;
        // Update the value of the head node
        head->val = firstVal % 10;
        
        ListNode * ptr;

        // Check if the doubled value is greater than 9
        if(firstVal > 9){
            // Create a new node with value 1
            ListNode * newAdd = new ListNode(1);
            // Make the new node as the head of the list
            newAdd -> next = head;
            head = newAdd;
            // Move the pointer to the next node
            ptr = (head->next)->next;
        }
        else{
            // Move the pointer to the next node
            if(head->next != NULL){
                ptr = head->next;
            }
        }

        // Traverse the list
        while(ptr != NULL && listLen == 1){
            // Check if the next node's value is greater than 4
            if(ptr->next != NULL){
                if(ptr->next->val > 4){
                carry = 1;
                }
                else{
                    carry = 0;
                }
            }
            else{
                carry = 0;
            }
            // Double the value of the current node and add the carry
            ptr->val = (2 * ptr->val) % 10 + carry;
            // Move the pointer to the next node
            ptr = ptr->next;
        }

        // Return the head of the list
        return head;
    }
};
```
