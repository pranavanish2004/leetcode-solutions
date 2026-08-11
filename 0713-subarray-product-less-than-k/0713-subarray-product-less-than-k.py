class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l=0
        temp=1
        ans=0
        if k<=1:
            return 0
        for r in range(len(nums)):
            temp=temp*nums[r]
            while(temp>=k):
                temp=temp//nums[l]
                l+=1
            ans+=r-l+1
        return ans
        