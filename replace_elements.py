class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        curr_max = arr[-1]
        arr[-1] = -1
        for i in range(n-2,-1,-1):
            curr = arr[i]
            arr[i] = curr_max
            if curr>curr_max:
                curr_max = curr
        return arr
