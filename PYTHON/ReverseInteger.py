# Link to the problem : https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        # Extract the absolute value of the input number.
        num = abs(x)
        # Initialize the reversed number to zero.
        rev_num = 0
        
        # Reverse the digits of the input number.
        while num != 0:
            # Multiply the current reversed number by 10 and add the next digit of the input number.
            rev_num = rev_num * 10 + num % 10
            # Move to the next digit of the input number.
            num = num // 10
        
        # Check if the reversed number is outside the range of a 32-bit signed integer.
        if rev_num < -2**31 or rev_num > 2**31 - 1:
            return 0
        # If the input number was positive, return the reversed number.
        elif x > 0:
            return rev_num
        # Otherwise, return the negated reversed number.
        else:
            return rev_num * (-1)

