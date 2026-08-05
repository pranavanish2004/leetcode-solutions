class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l=0
        vowels={'a','e','i','o','u'}
        count=0
        ans=0
        for r in range(len(s)):
            if(s[r] in vowels):
                count+=1
            if(r-l==k):
                if s[l] in vowels:
                    count-=1
                l+=1
            if(r-l+1==k):
                ans=max(ans,count)
        return ans
        