class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        list1=[]
        for i in range(1,len(nums)+1):
            list1.append(i)
        return(list(set(list1)-set(nums)))
        