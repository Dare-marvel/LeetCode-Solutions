# Key Insight : 
#Repeatedly subtract the divisor from the dividend until the dividend becomes less than the divisor. At each iteration, 
# we double the divisor and quotient until the doubled divisor becomes greater than the dividend.
# Then, we subtract the temporary divisor and add the temporary quotient to the final quotient. 

# Brief Overview about the left shift operator:

# << Operator

# When used with integers, it shifts the bits of the left operand to the left by a number of positions specified by the right operand, 
# and fills the empty positions with zeroes. In other words, 
# it multiplies the left operand by 2 raised to the power of the right operand.

# <<= Operator 

# It's a combined bitwise left shift and assignment operator.
# It first performs a bitwise left shift operation on the left operand by the number of positions specified by the right operand
# and then assigns the result back to the left operand.

# Link : https://leetcode.com/problems/divide-two-integers/submissions/923158018/

# Code:

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle edge cases
        if divisor == 0:
            return 0
        if dividend == -2147483648 and divisor == -1:
            return 2147483647   # Handle overflow case
        
        # Convert dividend and divisor to positive
        positive = (dividend > 0) is (divisor > 0)  # Check if both numbers are of same sign
        dividend, divisor = abs(dividend), abs(divisor)  # Convert both numbers to positive

        quotient = 0  # Initialize quotient
        while dividend >= divisor:  # While dividend is greater than or equal to divisor
            temp_divisor , temp_quotient = divisor , 1  # Initialize temporary divisor and quotient
            while dividend >= (temp_divisor << 1):  # While shifting divisor left by 1 doesn't make it greater than dividend
                temp_divisor <<= 1  # Shift divisor left by 1
                temp_quotient <<= 1  # Multiply quotient by 2

            dividend -= temp_divisor  # Subtract the temporary divisor from the dividend
            quotient += temp_quotient  # Add the temporary quotient to the quotient

        return quotient if positive else -quotient  # Return the quotient with the sign

  
