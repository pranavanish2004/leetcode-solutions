class Solution:
    def countPrimes(self, n: int) -> int:
        prime=[True]*n
        if n<=2:
            return 0
        prime[0]=False
        prime[1]=False
        
        for i in range(2,int(n**0.5)+1):
            if(prime[i]==True):
                for j in range(i*i,n,i):
                    prime[j]=False
        return sum(prime)
        