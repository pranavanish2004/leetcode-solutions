class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        res=[]
        for i in range(len(nums)):
            res.insert(index[i],nums[i])
        return res