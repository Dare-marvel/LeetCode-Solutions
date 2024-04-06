### [Dota2 Senate](https://leetcode.com/problems/dota2-senate/description/)

## Explanation:
This Python code is a solution to a problem where two parties, **Radiant** and **Dire**, are in a senate. The parties take turns banning each other's senators. The party that still has senators left when all the bans are exhausted wins. The code uses a **deque** data structure and follows these steps:

1. **Initialization**: The `senate` string is converted into a list for easier manipulation. Two deques, `D` and `R`, are created to store the positions of the Dire and Radiant senators, respectively.

2. **Filling the Deques**: The code iterates over the `senate` list. If a senator is from the Radiant party (`R`), their position is appended to the `R` deque. If they're from the Dire party (`D`), their position is appended to the `D` deque.

3. **Banning Process**: The banning process continues as long as both deques have elements. The code removes the first element from both deques using the `popleft()` method, which represents the current turn of each party.

4. **Determining the Next Turn**: If the Radiant's turn is earlier than the Dire's, the Radiant senator bans the Dire senator, and the Radiant senator gets to ban again after all the current senators have had their turns. This is represented by appending the current position plus the total number of senators to the `R` deque. If the Dire's turn is earlier, the same process happens but in favor of the Dire party.

5. **Result**: After all the bans are exhausted, if there are still senators in the `R` deque, the Radiant party wins, otherwise, the Dire party wins.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity is O(n), where n is the number of senators. This is because each senator is processed once.

### `Space Complexity`:
The space complexity is also O(n), as in the worst case, all senators could be in one of the deques at the same time.

## Code:
```py
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Convert the input string to a list for easier manipulation
        senate = list(senate)
        
        # Create two queues, one for each party
        D, R = deque(), deque()

        # Iterate through the list to categorize senators into their respective queues
        for i,c in enumerate(senate):
            if c == "R":
                R.append(i)  # If senator is from Radiant party, add its index to the Radiant queue
            else:
                D.append(i)  # If senator is from Dire party, add its index to the Dire queue

        # Continue the elimination process until one party's senators are exhausted
        while D and R:
            # Each party's senator will eliminate the next senator from the other party
            dTurn = D.popleft()  # Dire's senator's turn to eliminate
            rTurn = R.popleft()  # Radiant's senator's turn to eliminate

            # If Radiant's senator is ahead of Dire's senator, add Dire's senator's index to the end of Dire queue
            if rTurn < dTurn:
                R.append(rTurn + len(senate))
            else:
                # If Dire's senator is ahead of Radiant's senator, add Radiant's senator's index to the end of Radiant queue
                D.append(dTurn + len(senate))

        # If Dire's queue is empty, Dire wins; otherwise, Radiant wins
        return "Radiant" if R else "Dire"
```
