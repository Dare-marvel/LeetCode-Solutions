### [Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)

## Key Insight : 
Recognize that anagrams have the same set of characters, even though the order of those characters is different.<br> 
So, if we can somehow identify a unique key for each set of characters, we can group all the anagrams together.<br>

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
