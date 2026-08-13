class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix=0
        count=0
        dici={0:1}
        for num in nums:
            prefix+=num
            rem=prefix % k
            if rem in dici:
                count+=dici[rem]
            if rem not in dici:
                dici[rem]=1
            else:
                dici[rem]+=1
        return count
        
        