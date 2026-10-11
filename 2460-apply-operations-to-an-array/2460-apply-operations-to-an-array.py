class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        arr=[]
        for i in range(len(nums)-1):
            if (nums[i]==nums[i+1]):
                nums[i]=nums[i]*2
                nums[i+1]=0 
        for val in nums:
            if val!=0:
                arr.append(val)
        for val in nums:
            if val==0:
                arr.append(val) 
        return arr
        