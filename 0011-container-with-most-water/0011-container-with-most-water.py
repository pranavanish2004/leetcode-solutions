class Solution:
    def maxArea(self, height: list[int]) -> int:
        l=0
        r=len(height)-1
        max_area=0
        nums=height
        while(l<r):
            length=min(nums[l],nums[r])
            width=r-l
            area=length*width
            max_area=max(max_area,area)

            if(nums[l]<nums[r]):
                l+=1
            else:
                r-=1
        return max_area
        