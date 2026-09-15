class Solution:
    def numSplits(self, s: str) -> int:
        left={}
        right={}
        ans=0
        for val in s:
            if val in right:
                right[val]+=1
            else:
                right[val]=1
        for val in s:
            if val in left:
                left[val]+=1
            else:
                left[val]=1
            right[val]-=1
            if right[val]==0:
                del(right[val])
            if(len(right)==len(left)):
                ans+=1
        return ans  
        