### [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

## Explanation:

This code defines a `maxProfit` function that takes in an array of stock prices and returns the maximum profit that can be achieved by buying and selling one share of stock, where the buy and sell transactions must occur in order.
1. The function initializes two variables: `profit`, which keeps track of the maximum profit that can be achieved, and `minPrice`, which keeps track of the minimum price seen so far.
2. The function enters a loop that iterates through each price in the input array.
3. For each price, the function updates the `minPrice` variable to be the minimum of its current value and the current price.
4. The function then updates the `profit` variable to be the maximum of its current value and the difference between the current price and the `minPrice`.
5. After all prices have been processed, the function returns the final value of the `profit` variable, which represents the maximum profit that can be achieved.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(n), where n is the length of the input array, because it needs to iterate through each element of the array once.

### `Space Complexity`:
The space complexity is O(1), because it uses a constant amount of additional memory to store the `profit` and `minPrice` variables.

## Code:
```javascript
/**
 * This function takes in an array of prices and returns the maximum profit that can be achieved
 * by buying and selling one share of stock, where the buy and sell transactions must occur in order.
 *
 * @param {number[]} prices - An array of stock prices, where prices[i] is the price of the stock on the ith day
 * @return {number} - The maximum profit that can be achieved
 */

var maxProfit = function(prices) {
    // Initialize a variable to keep track of the maximum profit
    let profit = 0;
    // Initialize a variable to keep track of the minimum price seen so far
    let minPrice = Number.MAX_VALUE;
    // Loop through each price in the array
    for (let i = 0; i < prices.length; i++) {
        // Update the minimum price seen so far
        minPrice = Math.min(minPrice, prices[i]);
        // Update the maximum profit by comparing it to the current price minus the minimum price seen so far
        profit = Math.max(profit, prices[i] - minPrice);
    }
    // Return the maximum profit
    return profit;  
};

```
