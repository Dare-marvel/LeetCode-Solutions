### [Longest String Chain](https://leetcode.com/problems/longest-string-chain/description/)

## Explanation:
1. **Class Definition**: The code defines a class named `Solution`. This class contains three public methods: `checkPossible`, `comp`, and `longestStrChain`.

2. **Method `checkPossible`**: This method checks if it's possible to form string `s1` by adding one character to string `s2`. It does this by iterating through both strings simultaneously and comparing characters. If the characters are the same, it increments both pointers; if not, it only increments the pointer for `s1`. If it reaches the end of both strings, it returns `true`; otherwise, it returns `false`.

3. **Method `comp`**: This is a comparator function used for sorting. It compares two strings based on their sizes and returns `true` if the size of `s1` is less than the size of `s2`.

4. **Method `longestStrChain`**: This is the main function that implements the logic for finding the longest string chain. It takes a vector of strings as input.

5. **Sorting the Words**: The words are sorted in ascending order of their sizes using the `sort` function and the `comp` comparator.

6. **Dynamic Programming Array**: A dynamic programming (DP) array is initialized with all elements as 1, representing that each word is at least a chain of length 1.

7. **Nested Loop**: There are two nested loops that iterate over the words. The outer loop (`current`) goes from 0 to `size`, and the inner loop (`previous`) goes from 0 to `current`.

8. **Checking Possibility and Updating DP Array**: For each pair of words, it checks if it's possible to form the current word by adding one character to the previous word using the `checkPossible` function. If it's possible and the chain length through the current word is greater than its existing chain length, it updates the DP array.

9. **Finding the Maximum Chain Length**: It keeps track of the maximum chain length found so far. After iterating over all the words, it returns this maximum length as the longest string chain.

## Time and Space Complexity:
### `Time Complexity`:
The **time complexity** of this code is **O(N^2 * M)**, where **N** is the number of words and **M** is the maximum length of a word. This is because there are two nested loops iterating over the words, and for each pair of words, it checks the possibility in **O(M)** time.

### `Space Complexity`:
The **space complexity** is **O(N)**, which is used for the DP array. Here, **N** is the number of words.

## Code:
```cpp
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

class Solution {
public:
    // Function to check if it's possible to form a chain between two words
    bool checkPossible(string &s1, string &s2) {
        if (s1.size() != s2.size() + 1) return false;

        int first = 0, second = 0;

        while (first < s1.size()) {
            if (s1[first] == s2[second]) {
                first++, second++;
            } else {
                first++;
            }
        }

        // If both strings are completely traversed, it means a chain is possible
        if (first == s1.size() && second == s2.size()) return true;
        return false;
    }

    // Static comparison function to be used in sorting the words based on length
    static bool comp(string &s1, string &s2) {
        return s1.size() < s2.size();
    }

    // Main function to find the length of the longest string chain
    int longestStrChain(vector<string>& words) {

        // Sorting the words based on length using the comparison function
        sort(words.begin(), words.end(), comp);

        // Initializing dynamic programming array to store chain lengths
        int size = words.size();
        vector<int> dynamicProgramming(size, 1);

        // Initializing maximum chain length
        int maximum = 1;

        // Dynamic programming loop to find the longest chain
        for (int current = 0; current < size; current++) {

            for (int previous = 0; previous < current; previous++) {
                // Checking if it's possible to form a chain and updating the length
                if (checkPossible(words[current], words[previous]) && 1 + dynamicProgramming[previous] > dynamicProgramming[current]) {
                    dynamicProgramming[current] = 1 + dynamicProgramming[previous];
                }
            }

            // Updating the maximum chain length if needed
            if (dynamicProgramming[current] > maximum) {
                maximum = dynamicProgramming[current];
            }
        }

        // Returning the maximum chain length
        return maximum;
    }
};
```
