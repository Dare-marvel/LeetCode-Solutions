// Link : https://leetcode.com/problems/add-strings/description/

// Key Insight : We add numbers digit by digit with the carry and update it after the addition.
// Then we check whether one of the strings is exhausted and add the remaining digits of the string
// At the end we check that whether a carry is generated and then put it at it's appropriate position


// Code : 
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
