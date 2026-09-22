from collections import Counter
from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        #count the tasks
        dici=Counter(tasks)
        
        heap=[]
        #max heap
        for task in dici:
            heapq.heappush(heap,-dici[task])
        #queue for tasks to cooldown
        queue=deque()
        time=0
        while len(heap)>0 or len(queue)>0:
            time+=1
            if len(heap)>0:
                freq=heapq.heappop(heap)
                freq+=1
                #if task still has remaining exections
                if freq!=0:
                    queue.append((freq,time+n))
            
            #check whether a task has completed its cooldown
            if len(queue)>0:
                if queue[0][1]==time:
                    freq,available_time=queue.popleft()
                    heapq.heappush(heap,freq)
        return time
        