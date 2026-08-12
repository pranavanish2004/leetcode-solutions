class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        best_ending=nums[0]
        A1=nums[0]
        best_ending2=nums[0]
        A2=nums[0]
        for i in range(1,len(nums)):
            v1=nums[i]+best_ending
            v2=nums[i]
            best_ending=min(v1,v2)
            A1=min(A1,best_ending)
            v3=nums[i]+best_ending2
            v4=nums[i]
            best_ending2=max(v3,v4)
            A2=max(A2,best_ending2)
        if A2<0:
            return A2
        return max(A2,sum(nums)-A1)

    