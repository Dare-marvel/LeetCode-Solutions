### [Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)

## Key Insight : 
Recognize that anagrams have the same set of characters, even though the order of those characters is different.<br> 
So, if we can somehow identify a unique key for each set of characters, we can group all the anagrams together.<br>

## Explanation:
This code defines a class `Solution` with a method `groupAnagrams` that takes in a list of strings `strs` and returns a list of lists where each list contains all the strings from the input list that are anagrams of each other. Here's the main logic of the code in points:
1. The code creates an empty dictionary `groups` to store groups of anagrams.
2. The code iterates over each word in the input list. For each word, it sorts its characters to get a unique key representing its group of anagrams.
3. If the key is not already present in the dictionary, a new list is created for it.
4. The current word is added to the list for its key in the dictionary.
5. After all words have been processed, the values in the dictionary are returned as a list of lists.

## Time and Space Compexity:
### `Time Complexity`:
The time complexity of this code is O(n * k log(k)), where n is the number of elements in `strs` and k is the maximum length of any string in `strs`. This is because for each element in `strs`, its characters are sorted which takes O(k log(k)) time.

### `Space Complexity`:
The space complexity of this code is O(n * k), where n is the number of elements in `strs` and k is the maximum length of any string in `strs`. This is because memory is allocated for a dictionary that can have at most n entries and for lists that can have at most n * k characters.


## Code:
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create an empty dictionary to store groups of anagrams
        groups = {}
        
        # iterate over each word in the list of strings
        for word in strs:
            # sort the characters in the word to get a unique key
            key = ''.join(sorted(word))
            
            # if the key is not already in the dictionary, create a new list for it
            if key not in groups:
                groups[key] = []
            
            # add the current word to the list for the key
            groups[key].append(word)
        
        # return the values in the dictionary as a list of lists
        return list(groups.values())
  ```
