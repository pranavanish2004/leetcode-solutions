class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        min_ending=nums[0]
        max_ending=nums[0]
        ans=nums[0]
        for i in range(1,n):
            v1=nums[i]
            v2=max_ending*nums[i]
            v3=min_ending*nums[i]
            max_ending=max(v1,max(v2,v3))
            min_ending=min(v1,min(v2,v3))
            ans=max(ans,max(max_ending,min_ending))
        return ans
        