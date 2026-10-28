class Solution:
    def addDigits(self, num: int) -> int:
        ans=0
        while(len(str(num))!=1):
            ans=0
            while(num!=0):
                n=num%10
                ans=ans+n
                num=num//10
            num=ans
        if len(str(num))==1:
            return num
        return ans
            
        