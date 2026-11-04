class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        ans=1
        count=1
        if len(nums)==0:
            return 0
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                continue
            elif((nums[i+1]-nums[i]==1)):
                count+=1
            else:
                count=1

            ans=max(ans,count)
        return ans

            
        