class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dici={}
        dici2={}
        if len(s)!=len(t):
            return False
        for val in s:
            if(val in dici):
                dici[val]+=1
            else:
                dici[val]=1
        for val in t:
            if val in dici2:
                dici2[val]+=1
            else:
                dici2[val]=1
        return dici==dici2
        