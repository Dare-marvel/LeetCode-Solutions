### [Integer To Roman](https://leetcode.com/problems/integer-to-roman/)

## Code :
```python
class Solution:
    def intToRoman(self, num: int) -> str:
        # Define a dictionary that maps integers to Roman numerals
        roman_dict = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 
            40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 
            400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
        }
        
        # Create an empty string to hold the Roman numeral equivalent of the input
        roman_str = ''
        
        # Iterate over the items in the roman_dict dictionary in descending order of integer value
        for value, numeral in sorted(roman_dict.items(), reverse=True):
            # While the input is greater than or equal to the integer value of the current item
            while num >= value:
                # Add the corresponding Roman numeral to the roman_str string
                roman_str += numeral
                # Subtract the integer value from the input
                num -= value
                
        # Return the Roman numeral equivalent of the input
        return roman_str
```
