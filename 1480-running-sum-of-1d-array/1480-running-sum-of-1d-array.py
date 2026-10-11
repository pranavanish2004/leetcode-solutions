class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans=[]
        running_sum=0
        for val in nums:
            ans.append(val+running_sum)
            running_sum=val+running_sum
        return ans

        