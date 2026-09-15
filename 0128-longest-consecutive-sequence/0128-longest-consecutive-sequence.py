class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        longest=1
        current=1
        for i in range(len(nums)-1):
            if(nums[i+1]==nums[i]):
                continue
            if(nums[i+1]-nums[i]==1):
                current+=1
            else:
                current=1
            longest=max(longest,current)
        return longest
        
        