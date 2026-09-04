class Solution:
    def longestPalindrome(self, s: str) -> int:
        dici={}
        for val in s:
            if val in dici:
                dici[val]=dici[val]+1
            else:
                dici[val]=1
        length=0
        has_odd=False
        for val in dici:
            count=dici[val]
            length=length+(count//2)*2
            if count%2==1:
                has_odd=True
        if has_odd:
            length+=1
        return length


        