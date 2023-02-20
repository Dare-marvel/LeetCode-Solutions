class Solution:
    def reverse(self, x: int) -> int:
        num,rev_num = abs(x),0
        while num!=0:
            rev_num = rev_num*10 + num%10
            num=num//10
        if rev_num<-2**31 or rev_num>2**31 - 1:
            return 0
        elif x>0:
            return rev_num
        else :
            return rev_num*(-1)
