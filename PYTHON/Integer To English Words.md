### [Integer to English Words](https://leetcode.com/problems/integer-to-english-words/description/)

## Key Insights :
1) Create chunks of 3 numbers each starting from the unit's place of the number<br>
2) Convert each of these chunks to the english words in the form of hundreds<br>
3) In the main function , start from place of 0 and then increase the place value by one<br> 
4) The place value helps us in putting the strings Thousands , Millions and Billions to their right place<br>

## Explanation:
This code defines a class `Solution` with two methods: `helper` and `numberToWords`. The `numberToWords` method takes in an integer `num` and returns a string representing its English words. Here's the main logic of the code in points:
1. The `__init__` method of the class defines three arrays to hold the string values of numbers below 20, the tens places in numbers, and the thousands, millions, and billions places in numbers.
2. The `helper` method takes in an integer `num` less than 1000 and returns its string value. It checks if `num` is greater than or equal to 100 and adds its hundreds place to the string value if it is. It then checks if `num`'s tens place is greater than or equal to 20 and adds its tens place to the string value if it is. If `num` is less than 20, its string value is added directly to the string value being built.
3. The `numberToWords` method checks if `num` is 0 and returns "Zero" if it is. It then initializes variables to hold the remaining number to convert and the place value of the current number being converted. It enters a loop that continues until there are no more numbers to convert. In each iteration, it checks if the last three digits of the current number are not 0 and adds their string value and their place value to the final string value if they are not. It then divides the remaining number by 1000 and increases the place value by 1. After all numbers have been converted, it returns the final string value.

## Time and Space Compexity:
### `Time Complexity`:
The time complexity of this code is O(log(num)), where num is the input to the `numberToWords` method. This is because each group of three digits in `num` is processed once.

### `Space Complexity`:
The space complexity of this code is O(log(num)), where num is the input to the `numberToWords` method. This is because memory is allocated for strings representing groups of three digits that can have at most log(num) characters.

## Code :
```python
class Solution:
    def __init__(self):
        # Define three arrays to hold the string values of numbers.
        # The first array holds the string values of numbers below 20.
        self.below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        # The second array holds the string values of the tens places in numbers.
        self.tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        # The third array holds the string values of the thousands, millions, and billions places in numbers.
        self.thousands = ["", "Thousand", "Million", "Billion"]
        
    # Define a helper function to convert a number less than 1000 to its string value.
    def helper(self, num: int ) -> str:
        # Initialize an empty string to hold the string value of the number.
        res=''
        # If the number is greater than or equal to 100, add its hundreds place to the string value.
        if num >= 100:
            # If the number is a multiple of 100, add only the hundreds place to the string value.
            if num % 100 == 0:
                res += self.below_20[num // 100] +' '+ 'Hundred'
            # If the number is not a multiple of 100, add both the hundreds and tens places to the string value.
            else:
                res += self.below_20[num // 100] +' '+ 'Hundred '
        # If the number's tens place is greater than or equal to 20, add its tens place to the string value.
        if num % 100 >= 20:
            # If the number's ones place is 0, add only the tens place to the string value.
            if num % 10 == 0:
                res += self.tens[(num % 100) // 10]
            # If the number's ones place is not 0, add both the tens and ones places to the string value.
            else:
                res += self.tens[(num % 100) // 10] +' '+ self.below_20[num % 10]
        # If the number is less than 20, add its string value directly to the string value being built.
        else:
            res += self.below_20[num % 100]
        # Return the final string value.
        return res
    
    # Define the main function to convert a number to its string value.
    def numberToWords(self, num: int) -> str:
        # If the number is 0, return "Zero".
        if num == 0:
            return 'Zero'
        # Initialize variables to hold the remaining number to convert and the place value of the current number being converted.
        newNum , place = num , 0
        # Initialize an empty string to hold the final string value of the number.
        result = ''
        # While there are still numbers to convert,
        while newNum > 0:
            # If the current number's last three digits is not 0, add its string value and its place value to the final string value.
            if newNum % 1000 != 0:
                result = self.helper(newNum % 1000) +' '+ self.thousands[place] +' '+ result 
            # Divide the remaining number by 1000 and increase the place value by 1.
            newNum //= 1000
            place += 1
        # Return the final string value, removing any trailing whitespace characters.
        return result.rstrip()
```
