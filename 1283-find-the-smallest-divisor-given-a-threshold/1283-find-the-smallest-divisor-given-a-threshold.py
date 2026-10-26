class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        def smallestdiv(divisor):
            total=0
            for val in nums:
                total=total+ceil(val/divisor)
            return total<=threshold
        l=1
        r=max(nums)
        while(l<=r):
            mid=(l+r)//2
            if(smallestdiv(mid)):
                r=mid-1
            else:
                l=mid+1
        return l

        