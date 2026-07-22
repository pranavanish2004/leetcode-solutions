class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_prefix=0
        dici={0:1}
        count=0
        for num in nums:
            current_prefix+=num
            previous_prefix=current_prefix-k
            if previous_prefix in dici:
                count+=dici[previous_prefix]
            if current_prefix in dici:
                dici[current_prefix]=dici[current_prefix]+1
            else:
                dici[current_prefix]=1
        return count


