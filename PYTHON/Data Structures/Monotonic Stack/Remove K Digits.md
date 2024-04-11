### [Remove K Digits](https://leetcode.com/problems/remove-k-digits/description/)

## Approach and Intuition of Main Logic:
1. **Initialize an Empty Stack**: We start by initializing an empty stack to store digits. This stack will help us construct the smallest number possible by removing digits strategically.

2. **Iterate Through Each Digit of the Input Number**: We iterate through each digit of the input number (`num`). For each digit `c`:
   - **Compare and Remove Digits**: We compare the current digit with the digits already in the stack. If the current digit is smaller than the top of the stack, we pop the stack and decrement `k`. We repeat this process until `k` becomes 0 or the stack is empty or the current digit is not smaller than the top of the stack.
   - **Push Current Digit to Stack**: After handling the removal of digits, we push the current digit onto the stack.

3. **Remove Remaining Digits if Necessary**: After processing all digits in the input number, if there are still digits left to remove (`k > 0`), we pop digits from the end of the stack until `k` becomes 0.

4. **Convert Stack to String and Remove Leading Zeros**: We convert the stack back to a string and remove any leading zeros. This step ensures that we get the smallest possible number.

5. **Handle Edge Case of Empty Result**: Finally, if the resulting string is empty, we return "0" to indicate that no digits remain after removal; otherwise, we return the resulting string.

## Time and Space Complexity:
### `Time Complexity`:
- The algorithm iterates through each digit of the input number once in a single pass, resulting in a time complexity of O(n), where n is the length of the input number `num`.
- Within each iteration, the operations performed on the stack are constant time (O(1)) since they involve appending, popping, and accessing elements from the end of the stack.

### `Space Complexity`:
- The space complexity is O(n) since the stack can potentially contain all the digits of the input number `num` in the worst case, where n is the length of `num`.
- Additionally, the space used for the resulting string (`res`) is also O(n) in the worst case.
- Overall, the space complexity is dominated by the space used by the stack and the resulting string.

## Code:
```py
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Initialize an empty stack to store digits
        stack = []

        # Iterate through each digit in the input number
        for c in num:
            # While there are still digits to be removed (k > 0) and the stack is not empty and the current digit is smaller than the top of the stack
            while k > 0 and stack and stack[-1] > c:
                # Remove the top of the stack
                k -= 1
                stack.pop()
            # Add the current digit to the stack
            stack.append(c)

        # After processing all digits, if there are still digits to be removed (k > 0), remove them from the end of the stack
        while k > 0:
            stack.pop()
            k -= 1

        # Convert the stack back to a string and remove leading zeros
        res = "".join(stack).lstrip('0')

        # If the resulting string is empty, return "0", otherwise return the resulting string
        return res if res else "0"

```
