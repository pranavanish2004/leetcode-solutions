import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap=[]
        #put all stones into heap
        for stone in stones:
            heapq.heappush(heap,-stone)
        #continue until 0 or 1 stone 
        while(len(heap)>1):
            A=heapq.heappop(heap)
            B=heapq.heappop(heap)
            if(A!=B):
                Add=A-B
                heapq.heappush(heap,Add)
        #if 1 stone remaining
        if len(heap)>0:
            return -heap[0]  
        #if no stones remaining
        else:
            return 0          
            


        