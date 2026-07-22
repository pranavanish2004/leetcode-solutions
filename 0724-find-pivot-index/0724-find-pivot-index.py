class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        a=sum(nums)
        left=0
        if a-left-nums[0]==0:
            return 0
        for i in range(1,len(nums)):
            left+=nums[i-1]
            right=a-nums[i]-left
            if(left==right):
                return i
        return -1
        