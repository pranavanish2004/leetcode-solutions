class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def kokopiles(k):
            hours=0
            for pile in piles:
                hours=hours+math.ceil(pile/k)
            return hours<=h
        #binary search
        l=1
        r=max(piles)
        while(l<=r):
            mid=(l+r)//2
            if(kokopiles(mid)):
                r=mid-1
            else:
                l=mid+1
        return l

        