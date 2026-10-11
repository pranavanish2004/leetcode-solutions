class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        arr=[]
        for val in nums:
            if val%2==0:
                arr.append(val)
        for val in nums:
            if val%2!=0:
                arr.append(val)
        return arr

        