class Solution:
    def pancakeSort(self, arr):
        result=[]
        n=len(arr)
        for i in range(n,0,-1):
            indx=arr.index(i)
            if indx == i-1:
                continue
            if indx != 0:
                result.append(indx+1)
                arr[:indx+1]=arr[:indx+1][::-1]
        
            result.append(i)
            arr[:i]=arr[:i][::-1]
        return result
      
