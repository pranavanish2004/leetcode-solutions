class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        dici={}
        for val in nums:
            if val in dici:
                dici[val]+=1
            else:
                dici[val]=1
        for k in dici:
            if dici[k]>1:
                return k
        