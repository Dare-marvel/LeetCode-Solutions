### [Delete and Earn](https://leetcode.com/problems/delete-and-earn/description/)

## Explanation:
1. **Problem Statement**: The problem this code is trying to solve is a variant of the classic **dynamic programming** problem, where you're given an array of integers and you need to delete elements from the array to maximize your total score. The score is calculated as the product of the number and its frequency. However, if you delete a number, you must also delete all occurrences of the number plus one and the number minus one.

2. **Data Structures Used**: The code uses a `vector<int>` to store the input numbers, a `set<int>` to store the unique numbers, and an `unordered_map<int, int>` to store the frequency of each number.

3. **deleteAndEarn Function**: This is the main function that takes the input vector and prepares the data for processing. It populates the frequency map and the set of unique numbers. It then calls the `deleteEarnHelper` function with these data structures.

4. **deleteEarnHelper Function**: This function contains the main logic of the solution. It initializes four variables: `prev2`, `prev1`, `curEarn`, and `temp`. `prev2` and `prev1` are used to keep track of the maximum score that can be obtained by deleting numbers up to the current number, excluding and including the current number respectively. `curEarn` is used to store the current score, and `temp` is used as a temporary variable to swap values.

5. **Loop in deleteEarnHelper Function**: The function then enters a loop that iterates over each unique number in ascending order. For each number, it calculates the current score as the product of the number and its frequency.

6. **If-Else Condition in Loop**: If the current number is one more than the previous number (which means they are consecutive), it updates `prev1` to be the maximum of the current score plus `prev2` and the old `prev1`, and updates `prev2` to be the old `prev1`. If the current number is not one more than the previous number, it adds the current score to `prev1` and updates `prev2` to be the old `prev1`.

7. **Return Statement**: After the loop, the function returns `prev1`, which is the maximum score that can be obtained by deleting numbers from the array.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of the code is O(n log n), where n is the size of the input array. This is because it needs to sort the unique numbers, which takes O(n log n) time. The rest of the operations (calculating frequencies, iterating over unique numbers) take O(n) time.

### `Space Complexity`:
The space complexity of the code is O(n), where n is the size of the input array. This is because it needs to store the unique numbers and their frequencies, which takes O(n) space.

## Code:
```cpp
// Definition of the Solution class
class Solution {
public:
    // deleteEarnHelpersive helper function that calculates the maximum points earnable by deleting numbers
    // Params: vector nums - input vector, set unique - set of unique numbers, unordered_map freq - frequency of each number
    int deleteEarnHelper(vector<int>& nums, set<int> unique, unordered_map<int, int> freq) {
        // Variables to keep track of the points earned in the current and previous two steps
        int prev2 = 0, prev1 = 0, curEarn = 0, temp = 0;
        // Iterator to traverse the set of unique numbers
        auto it = unique.begin();

        // Loop through the unique numbers
        for(int i = 0; i < unique.size(); i++){
            // Calculate the points earned by multiplying the current number with its frequency
            curEarn = *it * freq[*it];

            // Check if the current number is consecutive to the previous one
            if(i > 0 && *it == *(prev(it)) + 1){
                // If consecutive, update the current and previous points earned considering deletion
                temp = prev1;
                prev1 = max(curEarn + prev2, prev1);
                prev2 = temp;
            }
            else{
                // If not consecutive, update the current and previous points earned without deletion
                temp = prev1;
                prev1 = curEarn + prev1;
                prev2 = temp;
            }
            it++;
        }

        // Return the maximum points earned
        return prev1;
    }

    // Main function to calculate the maximum points earnable by deleting some numbers
    int deleteAndEarn(vector<int>& nums) {
        // Frequency map to store the count of each number
        unordered_map<int , int> freq;
        // Set to store unique numbers
        set <int> unique;
        // Populate the frequency map and set with input numbers
        for(int i = 0; i < nums.size(); i++) {
            freq[nums[i]]++;
            unique.insert(nums[i]);
        }
        // Call the recursive function to get the result
        return deleteEarnHelper(nums, unique, freq);
    }
};
```
