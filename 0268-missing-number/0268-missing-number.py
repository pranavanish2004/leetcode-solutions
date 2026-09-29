class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        sums=0
        for i in range(n+1):
            sums+=i
        return sums-sum(nums)

            
        