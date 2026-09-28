class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        dici={}
        for i in range(len(nums)):
            val=nums[i]
            if val in dici:
                dici[val]=dici[val]+1
            else:
                dici[val]=1
        i=0
        for num in dici:
            nums[i]=num
            i+=1
        return len(dici)
        