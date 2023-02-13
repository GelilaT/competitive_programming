class Solution: 
    def select(self, arr, i):
       minimum=arr[i]
       min_indx=i
       while i < len(arr):
           if arr[i] < minimum:
               minimum=arr[i]
               min_indx=i
           i+=1
       return min_indx
    
    def selectionSort(self, arr,n):
        
        i = 0
        while i < len(arr):
            swaped_indx = self.select(arr, i)
            arr[i], arr[swaped_indx] = arr[swaped_indx], arr[i]
            i += 1
        return arr
