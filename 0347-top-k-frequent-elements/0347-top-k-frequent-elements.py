import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        heap=[]
        dici={}
        for val in nums:
            if val not in dici:
                dici[val]=1
            else:
                dici[val]+=1
        for val in dici:
            heapq.heappush(heap,(dici[val],val))
            if(len(heap)>k):
                heapq.heappop(heap)
        ans=[]
        for freq,val in heap:
            ans.append(val)
        return ans
        
        
        