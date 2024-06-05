### [Lemonade Change](https://leetcode.com/problems/lemonade-change/description/)

## Approach and Intuition

The `lemonadeChange` function is designed to determine if a lemonade vendor can provide correct change to every customer in line. The customers pay with 5, 10, or 20 dollar bills, and the vendor needs to provide change such that each transaction is valid. Here's a step-by-step explanation of the approach and intuition behind the main logic of the code:

1. **Initialization**:
   - Two counters, `count5` and `count10`, are initialized to zero. These will keep track of the number of 5 and 10 dollar bills the vendor has.

2. **Processing Each Bill**:
   - The function iterates through each bill in the input list `bills` using a range-based for loop.
   
3. **Handling $5 Bills**:
   - If the customer pays with a 5 dollar bill, no change is needed. The vendor simply increments the `count5` counter to reflect the receipt of an additional 5 dollar bill.
   
4. **Handling $10 Bills**:
   - If the customer pays with a 10 dollar bill, the vendor needs to provide 5 dollars in change.
   - The function first checks if there is at least one 5 dollar bill available (`count5 > 0`). If so, it decrements `count5` by one and increments `count10` by one to account for the received 10 dollar bill.
   - If there are no 5 dollar bills available (`count5 == 0`), it means the vendor cannot provide the required change, and the function returns `false`.

5. **Handling $20 Bills**:
   - If the customer pays with a 20 dollar bill, the vendor needs to provide 15 dollars in change.
   - The function first tries to provide change using one 10 dollar bill and one 5 dollar bill. This is preferred because it conserves the 5 dollar bills, which are more versatile for future transactions.
   - If there are no 10 dollar bills available or not enough 5 dollar bills to pair with a 10 dollar bill (`count10 == 0` or `count5 == 0`), the function then checks if there are at least three 5 dollar bills (`count5 >= 3`). If so, it provides the change using three 5 dollar bills.
   - If neither condition is met, the vendor cannot provide the required change, and the function returns `false`.

6. **Successful Completion**:
   - If the function processes all the bills in the list without encountering a situation where it cannot provide the correct change, it returns `true`, indicating that all transactions were successful.

## Time and Space Complexity:
### Time Complexity:
- The time complexity of this function is \(O(n)\), where \(n\) is the number of elements in the `bills` vector. This is because the function processes each bill exactly once in a single pass through the list.

### Space Complexity:
- The space complexity of the function is \(O(1)\). The function uses a fixed amount of extra space regardless of the size of the input list. The space is used for the `count5` and `count10` counters, which occupy a constant amount of memory.


## Code:
```cpp
class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        // Initialize counters for $5 and $10 bills
        int count5 = 0, count10 = 0;

        // Iterate through each bill
        for(int bill : bills) {
            // If the bill is $5, increment the count5 counter
            if(bill == 5) {
                count5++;
            }
            // If the bill is $10
            else if(bill == 10) {
                // If there are no $5 bills available, return false (cannot give change)
                if(count5 == 0) return false;
                // Decrement the count5 counter and increment the count10 counter
                count5--;
                count10++;
            }
            // If the bill is $20
            else { // bill == 20
                // If there is at least one $10 bill and one $5 bill, use them for change
                if(count10 > 0 && count5 > 0) {
                    count10--;
                    count5--;
                }
                // If there are no $10 bills but at least three $5 bills, use three $5 bills for change
                else if(count5 >= 3) {
                    count5 -= 3;
                }
                // If there are not enough bills to give change, return false
                else {
                    return false;
                }
            }
        }

        // If the loop completes without returning false, it means all bills were successfully processed
        return true;
    }
};
```
