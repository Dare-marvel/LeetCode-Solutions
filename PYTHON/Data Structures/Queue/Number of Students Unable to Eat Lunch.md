### [Number of Students Unable to Eat Lunch](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/)

## Approach 1 : Basic approach 
## Explanation:
1. **Class and Function Definition**: The function `countStudents` is defined within the class `Solution`. It takes two arguments: `students` and `sandwiches`, both of which are lists of integers. The function returns an integer.

2. **Deque Initialization**: Two deques, `stuD` and `sanD`, are initialized with the `students` and `sandwiches` lists respectively. A deque (double-ended queue) is a data structure that allows you to append and pop elements from both ends efficiently.

3. **Main Loop**: The main loop of the function runs while both `stuD` and `sanD` are not empty. This represents the process of distributing sandwiches to students.

4. **Distributing Sandwiches**: If the first student in the queue (`stuD[0]`) likes the first sandwich in the stack (`sanD[0]`), the student takes the sandwich and leaves the queue, and the sandwich is removed from the stack.

5. **Handling Dislikes**: If the first student does not like the first sandwich, two scenarios can occur:
   - If no students in the queue like the first sandwich (`stuD.count(sanD[0]) == 0`), the function returns the number of students left in the queue (`len(stuD)`). These students will not be able to eat a sandwich of their preferred type and will remain in the queue.
   - If there are other students in the queue who like the first sandwich, the first student moves to the end of the queue (`stuD.append(stuD.popleft())`).

6. **Return Statement**: If all sandwiches are distributed and there are no students left who cannot eat a sandwich of their preferred type, the function returns 0.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is `O(n^2)`, where `n` is the number of students. This is because in the worst case, each student may be moved to the end of the queue once for each sandwich, resulting in `n * n` operations.

### `Space Complexity`:
The space complexity of this code is `O(n)`, which means the amount of memory used grows linearly with the size of the input. This is because two deques are used to store the students and sandwiches.

## Code:
```py
from collections import deque
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Convert the lists into deques for efficient popping from the left
        stuD, sanD = deque(students), deque(sandwiches)

        # Continue while there are students and sandwiches left
        while stuD and sanD:
            # If the preference of the first student matches the available sandwich
            if stuD[0] == sanD[0]:
                # The student takes the sandwich
                stuD.popleft()
                sanD.popleft()

            # If there are still students and sandwiches, and the preference doesn't match
            if stuD and sanD and stuD[0] != sanD[0]:
                # Check if there are no students left who prefer the current sandwich
                if stuD.count(sanD[0]) == 0:
                    # If there are no such students, return the number of remaining students
                    return len(stuD)
                else:
                    # If there are students who prefer the current sandwich,
                    # move the student who doesn't get their preferred sandwich to the end of the queue
                    stuD.append(stuD.popleft())

        # If all students have received their sandwiches, return 0
        return 0

```

## Approach 2 : Optimized approach 
## Explanation:
1. **Class and Function Definition**: The function `countStudents` is defined within the class `Solution`. It takes two arguments: `students` and `sandwiches`, both of which are lists of integers. The function returns an integer.

2. **Count Array**: An array named `count` is initialized with two elements: `[0, 0]`. This array is used to count the number of students who prefer each type of sandwich (0 or 1).

3. **Counting Students**: A `for` loop iterates over the `students` list. For each student, the count of their preferred sandwich type is incremented by 1 in the `count` array.

4. **Iterating Over Sandwiches**: Another `for` loop iterates over the `sandwiches` list. For each sandwich, the code checks if there are any students who prefer that type of sandwich.

5. **Checking Student Preferences**: If there are no students who prefer the current type of sandwich (`count[sandwich] == 0`), the function returns the count of the other type of students (`count[1 - sandwich]`). This is because these students will not be able to eat a sandwich of their preferred type and will remain in the queue.

6. **Updating Count**: If there are students who prefer the current type of sandwich, the count of that type of students is decremented by 1 (`count[sandwich] -= 1`). This is because one of these students will eat the sandwich and leave the queue.

7. **Return Statement**: If all sandwiches are distributed and there are no students left who cannot eat a sandwich of their preferred type, the function returns 0.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is `O(n)`, where `n` is the number of students. This is because the code iterates over the `students` and `sandwiches` lists once.

### `Space Complexity`:
The space complexity of this code is `O(1)`, which means the amount of memory used does not change with the size of the input. This is because the `count` array uses a constant amount of space and does not grow with the size of the input.

## Code:
```py
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Initialize a count list to keep track of the number of students who prefer each type of sandwich
        # count[0] represents the number of students who prefer sandwich type 0
        # count[1] represents the number of students who prefer sandwich type 1
        count = [0, 0]
        
        # Iterate through the list of students
        for student in students:
            # Increment the count of the corresponding sandwich preference for each student
            count[student] += 1

        # Iterate through the list of sandwiches
        for sandwich in sandwiches:
            # Check if there are no students left who prefer the current type of sandwich
            if count[sandwich] == 0:
                # If there are no students left who prefer the current type of sandwich, return the count of the opposite type of sandwich
                # This is because if there are no students left who prefer the current type of sandwich, they must all prefer the opposite type of sandwich
                return count[1 - sandwich]
            
            # Decrement the count of the current type of sandwich, as one student has taken that sandwich
            count[sandwich] -= 1

        # If all sandwiches are eaten by the students without any issue, return 0
        return 0

```
