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

## Time and Space Complexity:
### `Time Complexity`:

### `Space Complexity`:

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
