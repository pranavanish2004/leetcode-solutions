from collections import Counter
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count=Counter(tasks)
        #find max frequnecy
        max_freq=max(count.values())
        count_max_freq=0
        for i in count.values():
            if(i==max_freq):
                count_max_freq+=1
        #calculate minimum intervals
        ans=(max_freq-1)*(n+1) +count_max_freq
        return max(len(tasks),ans)