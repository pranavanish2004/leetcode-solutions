class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        def min_days(day):
            bloom=0
            bouquet=0
            for i in bloomDay:
                if i<=day:
                    bloom+=1
                else:
                    bloom=0
                if(bloom==k):
                    bouquet+=1
                    bloom=0
            return bouquet>=m
        if(m*k>len(bloomDay)):
            return -1
        l=min(bloomDay)
        r=max(bloomDay)
        while(l<=r):
            mid=(l+r)//2
            if(min_days(mid)):
                r=mid-1
            else:
                l=mid+1
        return l




        