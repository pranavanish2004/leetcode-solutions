class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            
            while(l<r):
                total=nums[i]+nums[l]+nums[r]

                if(abs(total-target)<abs(closest-target)):
                    closest=total
                
                #if(total==target):
                    #return total
                elif(total<target):
                    l+=1
                else:
                    r-=1
        return closest
        
        