class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def weightcap(capacity):
            sum_weight=0
            total_day=1
            for weight in weights:
                if(sum_weight+weight<=capacity):
                    sum_weight+=weight
                else:
                    total_day+=1
                    sum_weight=weight
            return total_day<=days
        l=max(weights)
        r=sum(weights)
        while(l<=r):
            mid=(l+r)//2
            if(weightcap(mid)):
                r=mid-1
            else:
                l=mid+1
        return l



                

        