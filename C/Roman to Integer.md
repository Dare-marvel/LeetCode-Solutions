## [Roman To Integer](https://leetcode.com/problems/roman-to-integer/)

## Explanation:
This code defines a function `romanToInt` that takes in a string `s` representing a Roman numeral and returns an integer representing its value. Here's the main logic of the code in points:
1. The code creates an array `dec` of integer values corresponding to each Roman numeral. The value at index `i` corresponds to the Roman numeral represented by the character `i + 'A'`.
2. The code initializes variables `result`, `prev`, and `curr` to represent the final result, the value of the previous Roman numeral, and the value of the current Roman numeral, respectively.
3. The code iterates over the input string backwards. For each character in the string, it gets its integer value from the `dec` array.
4. If the current value is greater than or equal to the previous value, it is added to the result. Otherwise, it is subtracted from the result.
5. The current value is set as the previous value for the next iteration.
6. After all characters have been processed, the final result is returned.


## Time and Space Compexity:
### `Time Complexity`:
The time complexity of this code is O(n), where n is the length of `s`. This is because each character in `s` is processed once.

### `Space Complexity`:
The space complexity of this code is O(1), because only a constant amount of additional memory is used.

## Code :
#### Method - 1 (Accepted by Leetcode)
```c
int romanToInt(char *s) {
    // Create an array of integer values corresponding to each Roman numeral.
    // The value at index i corresponds to the Roman numeral (char) i+'A'.
    int dec[26];
    dec['I'-'A'] = 1;
    dec['V'-'A'] = 5;
    dec['X'-'A'] = 10;
    dec['L'-'A'] = 50;
    dec['C'-'A'] = 100;
    dec['D'-'A'] = 500;
    dec['M'-'A'] = 1000;
    
    // Initialize the result variable to zero and the previous value to zero.
    int result = 0;
    int prev = 0;
    int curr = 0;
    
    // Iterate over the string backwards.
    for (int i = strlen(s) - 1; i >= 0; i--) {
        // Get the integer value corresponding to the current Roman numeral.
        curr = dec[s[i]-'A'];
        // If the current value is greater than or equal to the previous value,
        // add it to the result. Otherwise, subtract it from the result.
        if (curr >= prev) {
            result += curr;
        } 
        else {
            result -= curr;
        }
        // Set the current value as the previous value for the next iteration.
        prev = curr;
    }
    
    // Return the final result.
    return result;
}
```
