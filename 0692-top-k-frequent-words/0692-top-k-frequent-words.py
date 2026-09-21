import heapq
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        dici={}
        for word in words:
            if word in dici:
                dici[word]+=1
            else:
                dici[word]=1
        heap=[]
        for word in dici:
            freq=dici[word]
            heapq.heappush(heap,(-freq,word))

        arr=[]
        while(len(heap)>0):
            freq,word=heapq.heappop(heap)
            arr.append(word)
        
        #take first k
        ans=[]
        for i in range(k):
            ans.append(arr[i])
        return ans
        
        