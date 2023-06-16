### [Integer To Roman](https://leetcode.com/problems/integer-to-roman/)

## Explanation:
This code defines a class `Solution` with a method `intToRoman` that takes in an integer `num` and returns a string representing its Roman numeral equivalent. Here's the main logic of the code in points:
1. The code defines a dictionary `roman_dict` that maps integers to their Roman numeral equivalents.
2. The code creates an empty string `roman_str` to hold the Roman numeral equivalent of the input.
3. The code iterates over the items in the `roman_dict` dictionary in descending order of integer value. For each item, it enters a loop that continues until `num` is less than the integer value of the current item. In each iteration of the loop, it adds the corresponding Roman numeral to `roman_str` and subtracts the integer value from `num`.
4. After all items in the dictionary have been processed, the final value of `roman_str` is returned.

## Time and Space Compexity:
### `Time Complexity`:
The time complexity of this code is O(num), where num is the input to the `intToRoman` method. This is because in the worst case, each iteration of the inner loop subtracts 1 from `num`, so there can be at most num iterations.

### `Space Complexity`:
The space complexity of this code is O(1), because only a constant amount of additional memory is used.

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
