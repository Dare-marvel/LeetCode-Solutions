class Solution:
    def longestPalindrome(self, s: str) -> str:
        LongSub=""
        n = len(s)
        length = 0
        for i in range(n):
          #Check for even length palindromic sequence
            l , r = i , i+1
            while (l>=0 and r<n) and s[l]==s[r]:
                if r-l+1>length:
                    length=r-l+1
                    LongSub = s[l:r+1]
                l , r = l-1,r+1
          #Check for odd length palindromic sequence      
            l,r=i,i
            while (l>=0 and r<n) and s[l]==s[r]:
                if r-l+1>length:
                    length=r-l+1
                    LongSub = s[l:r+1]
                l , r = l-1,r+1
             
        return LongSub
