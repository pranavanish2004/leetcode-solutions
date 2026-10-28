class Solution:
    def reverse(self, x: int) -> int:
        ans=0
        sign=1
        if x<0:
            sign=-1
            x=-x
        while(x!=0):
            n=x%10
            ans=ans*10+n
            x=x//10
        ans=ans*sign
        if ans<-2**31 or ans> 2**31 -1:
            return 0
        return ans

        