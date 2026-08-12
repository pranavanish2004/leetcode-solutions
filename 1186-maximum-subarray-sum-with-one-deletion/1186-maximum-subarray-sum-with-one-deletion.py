class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        best_value=arr[0]
        delete=float("-inf")
        ans=arr[0]
        for i in range(1,len(arr)):
            new_delete=max(delete+arr[i],best_value)
            new_bestvalue=max(arr[i],best_value+arr[i])#normal kadanes
            best_value=new_bestvalue
            delete=new_delete
            ans=max(ans,best_value,delete)
        return ans
