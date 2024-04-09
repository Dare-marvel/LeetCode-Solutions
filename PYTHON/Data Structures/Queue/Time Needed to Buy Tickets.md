### [Time Needed to Buy Tickets](https://leetcode.com/problems/time-needed-to-buy-tickets/description/)

## Naive Approach : Going as per the problem using Queue
## Explanation:
1. **Problem Statement**: The problem is about calculating the total time required for a person at a given index in a queue to buy all their tickets. Each person in the queue has a certain number of tickets, and it takes one unit of time to process one ticket. After each unit of time, the person at the front of the queue moves to the end.

2. **Initialization**: The code starts by initializing some variables. `n` is the total number of people in the queue. `queue` is a deque (a double-ended queue) that stores pairs of indices and ticket counts for each person in the queue. `time` is the total time required for the target person to buy all their tickets.

3. **Iteration**: The code then enters a while loop that continues until the queue is empty. In each iteration of the loop, it processes the tickets of the person at the front of the queue.

4. **Processing Tickets**: At the start of each iteration, the code removes the person at the front of the queue and gets their index and the number of tickets they have. It then increments `time` by 1, because each iteration represents one second of time. It also decrements the number of tickets for the current person, because one ticket is processed in each second.

5. **Checking Completion**: The code then checks if the current person is the target person and if they have finished buying all their tickets (i.e., their number of tickets is 0). If so, it breaks out of the loop, because the target person has finished buying all their tickets.

6. **Requeueing**: If the current person still wants to buy tickets (i.e., their number of tickets is greater than 0), the code puts them back in the queue. This simulates the behavior of the queue in the problem statement, where the person at the front of the queue moves to the end after each unit of time.

7. **Return Value**: After the loop ends, the code returns `time`, which is the total time required for the target person to buy all their tickets.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of the code is O(n), where n is the number of people in the queue. This is because the code potentially processes the tickets of each person in the queue once for each ticket they have.

### `Space Complexity`:
The space complexity of the code is O(n), where n is the number of people in the queue. This is because the code uses a deque to store the indices and ticket counts for each person in the queue.

## Code:
```py
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        queue = deque([(i, tickets[i]) for i in range(n)])  # Initialize the queue with indices and ticket counts
        time = 0

        while queue:
            index, num_tickets = queue.popleft()
            time += 1  # Each iteration represents one second
            
            # Decrement the number of tickets for the current person
            num_tickets -= 1
            
            # Check if the current person has finished buying tickets
            if index == k and num_tickets == 0:
                break
            
            # If the person still wants to buy tickets, put them back in the queue
            if num_tickets > 0:
                queue.append((index, num_tickets))

        return time
```

<hr/>

## Optimal Solution in One Pass
## Explanation:
1. **Problem Statement**: The problem is about calculating the total time required for a person at a given index in a queue to buy all their tickets. Each person in the queue has a certain number of tickets, and it takes one unit of time to process one ticket. After each unit of time, the person at the front of the queue moves to the end.

2. **Initialization**: The code starts by initializing some variables. `num_people` is the total number of people in the queue, `target_tickets` is the number of tickets the target person wants to buy, and `total_time` is the total time required for the target person to buy all their tickets.

3. **Iteration**: The code then iterates over each person in the queue. For each person, it checks their position relative to the target person and updates `total_time` accordingly.

4. **Before the Target Person**: If the current person is before the target person in the queue, the target person will have to wait for the current person's tickets to be processed. However, the target person only needs to wait for the minimum of the current person's tickets and their own tickets, because each person can only process their own tickets.

5. **The Target Person**: If the current person is the target person, the target person will process all their tickets, so the number of their tickets is added to `total_time`.

6. **After the Target Person**: If the current person is after the target person in the queue, the target person will have to wait for the current person's tickets to be processed. However, since the target person will have processed one of their tickets by the time the current person gets to the front of the queue, the target person only needs to wait for the minimum of the current person's tickets and their own tickets minus one.

7. **Return Value**: After iterating over all the people in the queue, the code returns `total_time`, which is the total time required for the target person to buy all their tickets.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of the code is O(n), where n is the number of people in the queue. This is because the code iterates over each person in the queue exactly once.

### `Space Complexity`:
The space complexity of the code is O(1), which means the space required by the algorithm is constant, regardless of the number of people in the queue. This is because the code only uses a fixed amount of space to store the variables `num_people`, `target_tickets`, `total_time`, and `current_person_index`, and does not use any data structures that grow with the size of the input.

## Code:
```py
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], target_person_index: int) -> int:
        # Get the number of people in the queue
        num_people = len(tickets)
        
        # Get the number of tickets the target person wants to buy
        target_tickets = tickets[target_person_index]
        
        # Initialize the total time
        total_time = 0
        
        # Iterate through each person in the queue
        for current_person_index in range(num_people):
            # If the current person is before the target person
            if current_person_index < target_person_index:
                # Add the minimum of the ticket value of the current person and the target person's tickets to the total time
                total_time += min(tickets[current_person_index], target_tickets)
            # If the current person is the target person
            elif current_person_index == target_person_index:
                # Add the ticket value of the target person to the total time
                total_time += target_tickets
            # If the current person is after the target person
            else:
                # If the ticket value of the current person is less than the target person's tickets
                if tickets[current_person_index] < target_tickets:
                    # Add the ticket value of the current person to the total time
                    total_time += tickets[current_person_index]
                # If the ticket value of the current person is greater than or equal to the target person's tickets
                else:
                    # Add the ticket value of the target person minus one to the total time
                    total_time += target_tickets - 1
        
        # Return the total time required for the target person to finish buying tickets
        return total_time

```
