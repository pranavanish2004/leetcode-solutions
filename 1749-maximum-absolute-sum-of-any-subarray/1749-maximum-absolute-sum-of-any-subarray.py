class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum=nums[0]
        best_ending=nums[0]
        min_sum=nums[0]
        best_ending1=nums[0]
        for i in range(1,len(nums)):
            v1=nums[i]+best_ending
            v2=nums[i]
            best_ending=max(v1,v2)
            max_sum=max(max_sum,best_ending)
        for i in range(1,len(nums)):
            v1=nums[i]+best_ending1
            v2=nums[i]
            best_ending1=min(v1,v2)
            min_sum=min(min_sum,best_ending1)
        return max(abs(max_sum),abs(min_sum))
        