### [Hand of Straights](https://leetcode.com/problems/hand-of-straights/description/)

### Approach and Intuition

1. **Initial Check for Feasibility**:
   - **Purpose**: To quickly rule out cases where it's impossible to divide the cards into groups of the required size.
   - **Action**: Check if the total number of cards (`n`) is divisible by the `groupSize`.
   - **Reasoning**: If `n % groupSize != 0`, it's immediately impossible to form groups of the required size, so the function returns `false`.

2. **Counting Card Frequencies**:
   - **Purpose**: To understand how many of each card we have.
   - **Action**: Use an unordered map (`count`) to tally the occurrences of each card in the `hand`.
   - **Reasoning**: This step helps in tracking how many cards of each type are available, which is crucial for forming consecutive groups.

3. **Sorting the Unique Card Values**:
   - **Purpose**: To process cards in ascending order, ensuring that we always try to form the smallest possible group first.
   - **Action**: Extract the keys (unique card values) from the map and sort them.
   - **Reasoning**: Sorting helps in ensuring that when forming groups, we start from the smallest card value and move upwards, maintaining order.

4. **Forming Consecutive Groups**:
   - **Purpose**: To attempt forming groups of consecutive cards starting from the smallest available card.
   - **Action**: Iterate through each unique card value in the sorted list and try to form groups starting from that card.
   - **Sub-Actions**:
     - **Check Availability**: If the count of the current card is greater than zero, it indicates that this card can be the start of a new group.
     - **Form Group**: For each card from the current card to `current card + groupSize - 1`, ensure there are enough cards to form a group. Reduce the count of each card in the group by the starting card's count.
   - **Reasoning**: This ensures that we are consistently forming valid groups without skipping any necessary cards.

5. **Final Validation**:
   - **Purpose**: To confirm that all cards have been used to form valid groups.
   - **Action**: After attempting to form all possible groups, if no step fails, the function returns `true`.
   - **Reasoning**: If the function hasn't returned `false` during group formation, it means all cards were successfully grouped.

## Time and Space Complexity

### **Time Complexity**:
- **Counting Frequencies**: This step involves iterating through the `hand` array once, giving us \(O(n)\) time complexity.
- **Sorting Keys**: Sorting the unique keys of the map has a time complexity of \(O(k \log k)\), where \(k\) is the number of unique card values.
- **Forming Groups**: Iterating through the sorted keys and attempting to form groups involves operations proportional to the number of unique card values and the group size, approximately \(O(k \cdot groupSize)\).
  
  Overall, the most significant factors are the counting and sorting steps, giving us a combined time complexity of:
  \[
  O(n + k \log k + k \cdot groupSize)
  \]
  Given that \(k \leq n\), this simplifies to:
  \[
  O(n \log n)
  \]

### **Space Complexity**:
- **Map for Counting Frequencies**: The unordered map `count` stores each unique card and its count, giving us a space complexity of \(O(k)\).
- **Vector for Sorted Keys**: The sortedKeys vector stores each unique card value, also contributing \(O(k)\) to space complexity.

  Hence, the total space complexity is:
  \[
  O(k)
  \]

In summary, the approach is systematic, ensuring feasibility with initial checks, leveraging frequency counting for accurate tracking, and employing sorting for ordered processing. The time complexity is primarily driven by the sorting operation, while space complexity remains linear with respect to the number of unique card values.

## Code:
```cpp
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        int n = hand.size();

        // Check if the number of cards is divisible by the group size
        if (n % groupSize != 0) {
            return false;
        }

        // Create a map to count the occurrences of each card
        unordered_map<int, int> cardCount;
        for (int card : hand) {
            cardCount[card]++;
        }

        // Sort the keys (cards) in ascending order
        vector<int> sortedCards;
        for (auto& pair : cardCount) {
            sortedCards.push_back(pair.first);
        }
        sort(sortedCards.begin(), sortedCards.end());

        // Check if the cards can form valid groups
        for (int card : sortedCards) {
            if (cardCount[card] > 0) {
                int startCount = cardCount[card];

                // Check the next 'groupSize' cards
                for (int i = card; i < card + groupSize; i++) {
                    if (cardCount[i] < startCount) {
                        return false;
                    }
                    cardCount[i] -= startCount;
                }
            }
        }

        return true;
    }
};
```
