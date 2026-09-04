class Solution:
    def firstUniqChar(self, s: str) -> int:
        dici={}
        for val in s:
            if val in dici:
                dici[val]=dici[val]+1
            else:
                dici[val]=1
        for i in range(len(s)):
            if dici[s[i]]==1:
                return i
        return -1
        
        