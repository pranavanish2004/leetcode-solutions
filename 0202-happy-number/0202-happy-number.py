class Solution:
    def isHappy(self, n: int) -> bool:
        
        while n!=1 and n!=4:
            ans=0
            while(n>0):
                num=n%10
                ans+=num**2
                n=n//10
            n=ans
        return n==1