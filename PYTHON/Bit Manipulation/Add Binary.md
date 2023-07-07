### [Add Binary](https://leetcode.com/problems/add-binary/description/)

## Key Insight : 
##### Bit-wise AND Truth Table :
      a   b   a & b
      0   0     0
      0   1     0
      1   0     0
      1   1     1


#### Bit-wise XOR Truth Table :
      a   b   a ^ b
      0   0     0
      0   1     1
      1   0     1
      1   1     0

#### From the repective truth table we can infer that Bit-wise `AND` can be used to calculate `SUM` and
#### Bit-wise `XOR` can be used to calculate `CARRY`

## Explanation
This is a Python program that defines a `Solution` class with a method `addBinary` that adds two binary strings and returns their sum as a binary string. Here's the main logic of the code in detail:

1. The `Solution` class defines a method `addBinary` that takes two arguments, `a` and `b`, which are the two binary strings to be added.
2. The binary strings are converted to decimal integers using base 2.
3. The two decimal integers are added bitwise using XOR and AND operators.
4. The sum of two bits is calculated using the XOR operator.
5. The carry is calculated using the AND operator and left-shifted by 1 bit.
6. The variables `x` and `y` are updated to the sum of two bits and the carry value, respectively.
7. This process is repeated until there is no carry (i.e., `y` becomes 0).
8. The final sum is converted to a binary string using the built-in `bin()` function and the leading "0b" is removed using string slicing.
9. The resulting binary string is returned.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this function is O(n), where n is the maximum length of the two binary strings, since each bit in both strings is visited once.

### `Space Complexity`:
The space complexity is O(1), since only a constant amount of extra space is used (i.e., for the variables `x`, `y`, `sum`, and `carry`).

## Code : 
```py
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert the binary strings to decimal integers using base 2
        x = int(a, 2)
        y = int(b, 2)
        
        # Add the two decimal integers bitwise using XOR and AND operators
        while y:
            # Calculate the sum of two bits using XOR operator
            sum = x ^ y
            # Calculate the carry using AND operator
            carry = (x & y) << 1
            x = sum  # Update x to the sum of two bits
            y = carry  # Update y to the carry value
        
        # Convert the final sum to a binary string using the built-in bin() function
        # and remove the leading "0b" using string slicing
        return bin(x)[2:]
```
