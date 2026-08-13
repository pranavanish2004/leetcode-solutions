class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_prefix=0
        dici={0:1}
        count=0
        sums=0
        for i in range(len(nums)):
            sums +=nums[i]
            previous_prefix=sums-k
            if previous_prefix in dici:
                count=count+dici[previous_prefix]
            if sums not in dici:
                dici[sums]=1
            else:
                dici[sums]+=1
        return count

