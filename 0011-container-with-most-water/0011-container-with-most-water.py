class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea=0
        i=0
        j=len(height)-1
        while i<j:
          if height[i]<=height[j]:
            area=(j-i)*height[i]
            maxarea=max(maxarea,area)
            i+=1
          else:
            area=(j-i)*height[j]
            maxarea=max(maxarea,area)
            j-=1
        return maxarea 