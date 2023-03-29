// Link : https://leetcode.com/problems/multiply-strings/description/

// Key Insights :
// We initialize k at every iteration of i as k = res_size - (n2 - i) because we want to move backwards as per the place value of the 
// multiplier 

// This function multiplies two numbers represented as strings
// and returns the result as a string
char *multiply(char *num1, char *num2)
{
    // Find the lengths of the two input strings
    int n1 = strlen(num1), n2 = strlen(num2);
    // The size of the result string will be at most the sum of the
    // lengths of the input strings
    int res_size = n1 + n2;

    // Allocate memory for the result string and initialize it to '0'
    char *res = (char *)malloc(res_size + 1);
    memset(res, '0', res_size);

    // Add a null terminator to the end of the result string
    res[res_size] = '\0';

    // Perform long multiplication starting from the rightmost digit of num2
    for (int i = n2 - 1; i >= 0; i--)
    {
        // Initialize the carry to 0 and the index k to the current position
        // in the result string where the digits from the current multiplication
        // will be added
        int carry = 0, k = res_size - (n2 - i), mul = 1;

        // Multiply the current digit of num2 with all the digits of num1
        for (int j = n1 - 1; j >= 0; j--)
        {
            // Extract the digits from the two input strings
            int digit1 = num1[j] - '0', digit2 = num2[i] - '0';

            // Compute the product of the two digits and add the carry from the
            // previous multiplication and the digit in the result string at
            // position k
            int sum = digit1 * digit2 + carry + (res[k] - '0');

            // Update the carry and the digit in the result string
            carry = sum / 10;
            // Store the last digit of sum in the result
            res[k] = (sum % 10) + '0';
            k--;
        }
        if (carry > 0)
        {
            res[k] += carry;
        }
    }

    int i = 0;
    // Find first non-zero character in result
    while (res[i] == '0' && i < res_size - 1)
    {
        i++;
    }

    //Return from the first non-zero digit
    return &res[i];
}


  
