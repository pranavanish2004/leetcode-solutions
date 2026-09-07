class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_water=0
        while(l<r):
            width=r-l
            ht=min(height[l],height[r])
            curr_water=width*ht
            max_water=max(max_water,curr_water)
            if(height[l]<height[r]):
                l+=1
            else:
                r-=1
        return max_water


        