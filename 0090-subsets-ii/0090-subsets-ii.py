class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        path=[]
        nums.sort()
        def df(index):
            ans.append(path[:])
            for i in range(index,len(nums)):
                if(i>index and nums[i]==nums[i-1]):
                    continue
                #take
                path.append(nums[i])
                df(i+1)
                    #undo
                path.pop()
        df(0)
        return ans
        

        