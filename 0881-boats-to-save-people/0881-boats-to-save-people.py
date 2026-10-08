class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        l=0
        r=len(people)-1
        boat=0
        while(l<=r):
            if(people[l]+people[r]<=limit):
                boat+=1
                l+=1
                r-=1
            else:
                r-=1
                boat+=1
        return boat


        