class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n=len(arr)
        left=0
        right=n-1
        if n < 3:
            return False
        while left+1 < n-1 and arr[left] < arr[left+1]:
                left+=1
           
     
        while right-1 > 0 and arr[right] < arr[right-1]:
                right-=1
           
        return left == right
