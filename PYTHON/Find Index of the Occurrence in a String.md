### [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/)

## Brief Description:
If the substring is present return the first index<br>
Else return -1<br>

## Code:
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # If the substring is present return the first index
        if needle in haystack:
            return haystack.index(needle)
        # Else return -1
        else:
            return -1
```
