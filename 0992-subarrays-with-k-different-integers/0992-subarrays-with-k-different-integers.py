class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmostK(nums,k):
            l=0
            ans=0
            dici={}
            for r in range(len(nums)):
                val=nums[r]
                if val in dici:
                    dici[val]+=1
                else:
                    dici[val]=1
                while(len(dici)>k):
                    dici[nums[l]]-=1
                    if(dici[nums[l]]==0):
                        dici.pop(nums[l])
                    l+=1
                ans+=r-l+1
            return ans
        return atmostK(nums,k)-atmostK(nums,k-1)


        