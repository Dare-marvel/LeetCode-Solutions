### [Add Strings](https://leetcode.com/problems/add-strings/description/)

## Key Insights : 
We add numbers digit by digit with the carry and update it after the addition.
Then we check whether one of the strings is exhausted and add the remaining digits of the string
At the end we check that whether a carry is generated and then put it at it's appropriate position

## Explanation:
This code defines a function `addStrings` that takes in two strings `num1` and `num2` representing non-negative integers and returns a string representing their sum. Here's the main logic of the code in points:
1. The code calculates the length of the input strings `num1` and `num2`.
2. The code calculates the maximum possible length of the result string as the sum of the lengths of the input strings and allocates memory for it.
3. The code initializes the result string with '0' characters and sets the last character as a null character.
4. The code initializes indices for the input strings and the result string, as well as variables to keep track of the current sum and any carry from previous additions.
5. The code adds corresponding digits from the input strings until one of the strings is exhausted. For each addition, it calculates the current digit and adds it to the result string, and also calculates any carry for the next addition.
6. If one of the input strings is exhausted, the code adds any remaining digits from the other string to the result string.
7. If there is any carry left after all digits have been added, it is added to the result string.
8. The code finds the index of the first non-zero character in the result string.
9. The code returns a pointer to the first non-zero character in the result string.

## Time and Space Compexity:
### `Time Complexity`:
The time complexity of this code is O(max(n1, n2)), where n1 is the length of `num1` and n2 is the length of `num2`. This is because each digit in both input strings is processed once.

### `Space Complexity`:
The space complexity of this code is O(n1 + n2), where n1 is the length of `num1` and n2 is the length of `num2`. This is because memory is allocated for a result string that can have at most n1 + n2 characters.

## Code :
```c
char *addStrings(char *num1, char *num2)
{
    // Calculate length of input strings
    int n1 = strlen(num1), n2 = strlen(num2);
    // Calculate length of result string and allocate memory for it
    int res_size = n1 + n2;
    char *res = (char *)malloc(res_size + 1);
    // Initialize the result string with '0'
    memset(res, '0', res_size);

    // Set the last character of result string as null character
    res[res_size] = '\0';

    // Initialize indices for input strings and result string
    int i = n2 - 1, j = n1 - 1, k = res_size - 1, carry = 0, sum;

    // Add digits from input strings until one of the strings exhausts
    while (i >= 0 && j >= 0)
    {
        // Add corresponding digits and any carry from previous sum
        sum = (num1[j] - '0') + (num2[i] - '0') + carry;
        // Calculate current digit and add it to result string
        res[k] = sum % 10 + '0';
        // Calculate the carry for the next addition
        carry = sum / 10;
        i--, j--, k--;
    }

    // If one input string is exhausted, add remaining digits from other string
    while (i >= 0)
    {
        sum = (num2[i] - '0') + carry;
        res[k] = sum % 10 + '0';
        carry = sum / 10;
        i--, k--;
    }
    while (j >= 0)
    {
        sum = (num1[j] - '0') + carry;
        res[k] = sum % 10 + '0';
        carry = sum / 10;
        j--, k--;
    }

    // If there is any carry left, add it to the result string
    if (carry > 0)
    {
        res[k] = carry + '0';
    }

    // Find the index of first non-zero character in the result string
    i = 0;
    while (res[i] == '0' && i < res_size - 1)
    {
        i++;
    }

    // Return a pointer to the first non-zero character in the result string
    return &res[i];
}
```
