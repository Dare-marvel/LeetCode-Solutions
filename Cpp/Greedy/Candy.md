### [Candy](https://leetcode.com/problems/candy/description/)

### Approach and Intuition

1. **Initialization**:
   - `sum` is initialized to 1 because we start by giving at least one candy to the first child.
   - `i` is initialized to 1 to begin checking the ratings from the second child onwards.
   - `n` is the number of children, which is the size of the `ratings` vector.

2. **Iterating Through Ratings**:
   - The main loop runs while `i` is less than `n`, ensuring that we cover all children.

3. **Equal Ratings**:
   - If the rating of the current child is equal to the previous child (`ratings[i] == ratings[i-1]`), simply increment the sum by 1 and move to the next child (`i++`).
   - This handles the scenario where children with the same rating get exactly one candy.

4. **Increasing Ratings Sequence**:
   - If the ratings are increasing (`ratings[i] > ratings[i-1]`), enter a nested loop to count the length of this increasing sequence.
   - `peak` keeps track of the number of candies distributed in this increasing sequence. Start with 1 candy and increment both `peak` and `sum` as you move through the sequence.
   - Continue until you encounter a non-increasing rating.

5. **Decreasing Ratings Sequence**:
   - If the ratings are decreasing (`ratings[i] < ratings[i-1]`), enter another nested loop to count the length of this decreasing sequence.
   - `down` keeps track of the number of candies distributed in this decreasing sequence. Start with 1 candy and increment `down` and `sum` as you move through the sequence.
   - Continue until you encounter a non-decreasing rating.

6. **Adjustment for Peak and Down Sequences**:
   - After exiting the decreasing sequence loop, check if the length of the decreasing sequence (`down`) is greater than the peak sequence length (`peak`).
   - If it is, add the difference (`down - peak`) to the sum. This adjustment ensures that the peak in the increasing sequence is appropriately rewarded.

7. **Final Sum**:
   - The outer loop continues until all children are processed, and the final `sum` of candies is returned.

### Example Walkthrough

Consider an example where `ratings = [1, 2, 2, 1, 2, 3, 2, 1]`:
- Start with `sum = 1` and `i = 1`.
- At `i = 1`, `ratings[1] > ratings[0]` (1 < 2): Enter the increasing sequence loop.
  - Peak sequence: `ratings = [1, 2]` => `peak = 2`, `sum = 3`.
- At `i = 3`, `ratings[3] < ratings[2]` (2 > 1): Enter the decreasing sequence loop.
  - Decreasing sequence: `ratings = [2, 1]` => `down = 2`, `sum = 5`.
- Continue processing similarly for the rest of the array.

## Time and Space Complexity:
### Time Complexity

The time complexity of the solution is **O(n)**, where `n` is the number of children (size of the `ratings` vector). This is because:
- Each element in the `ratings` array is processed at most once.
- The nested loops for increasing and decreasing sequences move the index `i` forward without reprocessing any element.

### Space Complexity

The space complexity of the solution is **O(1)**. The algorithm uses a constant amount of extra space:
- Variables `sum`, `i`, `peak`, and `down` are used irrespective of the input size.
- No additional data structures are used that scale with the input size.

## Code:
```cpp
class Solution {
public:
    // Function to calculate the minimum candies to distribute
    int candy(vector<int>& ratings) {
        // Initialize sum with 1 candy for the first child
        int sum = 1, i = 1;
        // Get the number of children from the ratings size
        int n = ratings.size();

        // Iterate over each child starting from the second one
        while(i < n){
            // If current child has same rating as previous, give 1 candy
            if(ratings[i] == ratings[i-1]){
                sum += 1;
                i++;
            }
            // Initialize peak variable to track increasing sequence of ratings
            int peak = 1;
            // Traverse up the peak (increasing ratings)
            while(i < n && ratings[i] > ratings[i-1]){
                peak++;
                sum += peak;
                i++;
            }
            // Initialize down variable to track decreasing sequence of ratings
            int down = 1;
            // Traverse down the peak (decreasing ratings)
            while(i < n && ratings[i] < ratings[i-1]){
                sum += down;
                down++;
                i++;
            }
            // If descending sequence is longer than ascending, adjust sum
            if(down > peak){
                sum += down - peak;
            }
        }

        // Return the total candies needed
        return sum;
    }
};
```
