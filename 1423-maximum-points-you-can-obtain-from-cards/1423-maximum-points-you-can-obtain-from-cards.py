class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum=0
        rsum=0
        max_sum=0
        for i in range(k):
            lsum+=cardPoints[i]
        max_sum=lsum
        r=len(cardPoints)-1
        for i in range(k-1,-1,-1):
            lsum=lsum-cardPoints[i]
            rsum+=cardPoints[r]
            r-=1
            max_sum=max(max_sum,lsum+rsum)
        return max_sum        
        
        