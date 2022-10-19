class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat=0
        people=sorted(people)
        left,right=0,len(people)-1
        while left<=right:
           if people[right]==limit:
              right-=1
           elif people[left]+people[right]<=limit:
              right-=1
              left+=1
           elif people[left]+people[right]>limit:
              right-=1
           boat+=1
        return boat
            
        