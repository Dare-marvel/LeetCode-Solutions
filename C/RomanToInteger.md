## [Roman To Integer](https://leetcode.com/problems/roman-to-integer/)

## Code :
#### Method - 1  (Not accepted by Leetcode but logically correct)
```c
//function to find index of a character in the roman numeral string
int indexOf(char s){
    char rom[7] = "IVXLCDM";  // roman numeral string
    for(int i=0;i<strlen(rom);i++){  // loop through the string
        if(s==rom[i]){  // if character matches, return index
            return i;
        }
    }
    return -1;  // if character not found, return -1
}

// function to convert roman numeral to integer
int romanToInt(char * s){
    char rom[7] = "IVXLCDM";  // roman numeral string
    int dec[7] = {1,5,10,50,100,500,1000};  // integer values of roman numerals
    int sum = 0;  // initialize sum to 0
    int prev=0,curr;  // initialize prev and curr to 0
    for(int i=strlen(s)-1;i>=0;i--){  // loop through the input string backwards
        curr = dec[indexOf(s[i])];  // get the integer value of the current roman numeral
        if(curr<prev){  // if the current value is less than the previous value
            sum-=curr;  // subtract the current value from the sum
        }
        else{  // if the current value is greater than or equal to the previous value
            sum+=curr;  // add the current value to the sum
        }
        prev=curr;  // set prev to curr for the next iteration
    }
    return sum;  // return the final sum
}
```
-------------------------------------------------------------------------------------------------------------------------------------------
#### Method - 2 (Accepted by Leetcode)
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
