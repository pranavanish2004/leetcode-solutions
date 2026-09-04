class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dici={}
        for val in nums:
            if val in dici:
                dici[val]=dici[val]+1
            else:
                dici[val]=1
        for i in dici:
            if dici[i]>1:
                return True
        return False



        
        