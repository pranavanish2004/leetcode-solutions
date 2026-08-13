class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[]
        sums=0
        for i in range(n):
            sums+=nums[i]
            prefix.append(sums)
        return prefix

        