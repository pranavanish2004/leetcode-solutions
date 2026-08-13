class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix=0
        dici={0:-1}
        for i in range(len(nums)):
            prefix+=nums[i]
            rem=prefix % k
            if rem in dici:
                if i-dici[rem]>=2:
                    return True
            else:
                dici[rem]=i
        return False
        